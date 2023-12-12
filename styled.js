import styled from 'styled-components';
import { Select, Button, Form  } from 'antd';

export const StyledSelect = styled(Select)`
  flex: 1;

  .ant-select-selector {
    border-top-left-radius: 0 !important;
    border-bottom-left-radius: 0 !important;
  }
`;

export const SelectWrapper = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 5px;
`;

export const SelectLabel = styled.p`
  width: 150px;
  padding: 0 12px;
  background: #fafafa;
  height: 32px;
  line-height: 32px;
  border: 1px solid #d9d9d9;
  border-radius: 2px 0 0 2px;
  border-right: 0;
  color: rgba(0, 0, 0, 0.65);
`;

export const StyledForm = styled(Form)`
  .ant-form-item {
    margin-bottom: 8px;
  }

  .ant-form-item:last-child {
    margin-bottom: 24px;
  }

  .ant-form-item-explain {
    text-align: left;
    margin-bottom: 5px;
  }
`;

export const StyledButton = styled(Button)`
  width: 100%;
`;