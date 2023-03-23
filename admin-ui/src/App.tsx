import { Admin, ListGuesser, Resource } from "react-admin";
import jsonServerProvider from "ra-data-json-server";

const dataProvider = jsonServerProvider('http://localhost:8080');

const App = () => (
  <Admin dataProvider={dataProvider}>
      <Resource name="users" list={ListGuesser} />
  </Admin>
);

export default App;