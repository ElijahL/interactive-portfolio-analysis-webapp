import MarketPriceWithMAs from './charts/MarketPriceWithMAs';
import PortfolioMarketValue from "./charts/PortfolioMarketValue";
import NumOfInsType from "./charts/NumOfInsType";
import InsTypeNetPosPerPrtf from "./charts/InsTypeNetPosPerPrtf";
import StrategyScenarios from './charts/StrategyScenarios';

import "./styles.css"; 

export default function App() {
  return (
    <div className="App">
      <h1>MEG Visualization</h1>
      <MarketPriceWithMAs/>
      <StrategyScenarios/>
      <PortfolioMarketValue/>
      <InsTypeNetPosPerPrtf/>
      <NumOfInsType/>
    </div>
  );
}