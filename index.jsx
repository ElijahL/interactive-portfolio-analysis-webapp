import axios from 'axios';
import { notification } from 'antd';

const baseURL = `https://dc-fa-meg-01:5000`;

const api = {
  base: axios.create({
    baseURL,
  }),
  git: axios.create({
    baseURL,
  }),
};

api.base.interceptors.response.use(
  response => response,
  err => {
    const errorResponse = err.response;
    if (errorResponse && errorResponse.data && errorResponse.data.detail && errorResponse.data.detail.error) {
      notification.error({
        message: errorResponse.data.detail.error,
        placement: 'topRight',
      });
    } else {
      notification.error({
        message: 'Something went wrong',
        placement: 'topRight',
      });
      console.log('err status', err.status);
    }

    return Promise.reject(err);
  }
);

api.git.interceptors.response.use(
  response => response,
  err => Promise.reject(err)
);

export default api;
