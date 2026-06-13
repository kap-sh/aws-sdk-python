from typing import TYPE_CHECKING, Optional

import aws_sdk_supplychain._auth._signers
import aws_sdk_supplychain._auth._sigv4
from aws_sdk_supplychain._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.create_data_lake_dataset_request
    import aws_sdk_supplychain.types.create_data_lake_dataset_response
    import aws_sdk_supplychain.types.data_lake_dataset
    import aws_sdk_supplychain.types.data_lake_dataset_description
    import aws_sdk_supplychain.types.data_lake_dataset_max_results
    import aws_sdk_supplychain.types.data_lake_dataset_name
    import aws_sdk_supplychain.types.data_lake_dataset_next_token
    import aws_sdk_supplychain.types.data_lake_dataset_partition_spec
    import aws_sdk_supplychain.types.data_lake_dataset_schema
    import aws_sdk_supplychain.types.data_lake_namespace_name
    import aws_sdk_supplychain.types.delete_data_lake_dataset_request
    import aws_sdk_supplychain.types.delete_data_lake_dataset_response
    import aws_sdk_supplychain.types.get_data_lake_dataset_request
    import aws_sdk_supplychain.types.get_data_lake_dataset_response
    import aws_sdk_supplychain.types.list_data_lake_datasets_request
    import aws_sdk_supplychain.types.list_data_lake_datasets_response
    import aws_sdk_supplychain.types.tag_map
    import aws_sdk_supplychain.types.update_data_lake_dataset_request
    import aws_sdk_supplychain.types.update_data_lake_dataset_response
    import aws_sdk_supplychain.types.uuid
    from aws_sdk_supplychain._services.async_supply_chain import (
        AsyncSupplyChainClient,
        AsyncSupplyChainClientConfig,
    )
    from aws_sdk_supplychain._services.supply_chain import (
        SupplyChainClient,
        SupplyChainClientConfig,
    )


class DataLakeDatasetResource:
    def __init__(self, service: SupplyChainClient) -> None:
        self._service = service

    def put(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        schema: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_schema.DataLakeDatasetSchema"
        ] = None,
        description: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_description.DataLakeDatasetDescription"
        ] = None,
        partition_spec: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_partition_spec.DataLakeDatasetPartitionSpec"
        ] = None,
        tags: Optional["aws_sdk_supplychain.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_supplychain.types.create_data_lake_dataset_response.CreateDataLakeDatasetResponse":
        """<p>Enables you to programmatically create an Amazon Web Services Supply Chain data lake dataset. Developers can create the datasets using their pre-defined or custom schema for a given instance ID, namespace, and dataset name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> name space, the name must be one of the supported data entities under <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>
            schema: <p>The custom schema of the data lake dataset and required for dataset in <b>default</b> and custom namespaces.</p>
            description: <p>The description of the dataset.</p>
            partition_spec: <p>The partition specification of the dataset. Partitioning can effectively improve the dataset query performance by reducing the amount of data scanned during query execution. But partitioning or not will affect how data get ingested by data ingestion methods, such as SendDataIntegrationEvent's dataset UPSERT will upsert records within partition (instead of within whole dataset). For more details, refer to those data ingestion documentations.</p>
            tags: <p>The tags of the dataset.</p>

        Examples:
            Create an AWS Supply Chain inbound order dataset

            >>> client.put(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order', description='This is an AWS Supply Chain inbound order dataset', tags={'tagKey1': 'tagValue1', 'tagKey2': 'tagValue2'})
            Create a custom dataset

            >>> client.put(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset', description='This is a custom dataset', schema={'name': 'MyDataset', 'fields': [{'name': 'id', 'type': 'INT', 'isRequired': True}, {'name': 'description', 'type': 'STRING', 'isRequired': True}, {'name': 'price', 'type': 'DOUBLE', 'isRequired': False}, {'name': 'creation_time', 'type': 'TIMESTAMP', 'isRequired': False}, {'name': 'quantity', 'type': 'LONG', 'isRequired': False}], 'primaryKeys': [{'name': 'id'}]}, partition_spec={'fields': [{'name': 'creation_time', 'transform': {'type': 'DAY'}}, {'name': 'description', 'transform': {'type': 'IDENTITY'}}]}, tags={'tagKey1': 'tagValue1', 'tagKey2': 'tagValue2'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.create_data_lake_dataset_request.CreateDataLakeDatasetRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.create_data_lake_dataset_response.CreateDataLakeDatasetResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_lake_dataset

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_lake_dataset.create_data_lake_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.create_data_lake_dataset_request.CreateDataLakeDatasetRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["namespace"] = namespace
        input["name"] = name
        if schema is not None:
            input["schema"] = schema
        if description is not None:
            input["description"] = description
        if partition_spec is not None:
            input["partition_spec"] = partition_spec
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.get_data_lake_dataset_response.GetDataLakeDatasetResponse":
        """<p>Enables you to programmatically view an Amazon Web Services Supply Chain data lake dataset. Developers can view the data lake dataset information such as namespace, schema, and so on for a given instance ID, namespace, and dataset name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>

        Examples:
            Get properties of an existing AWS Supply Chain inbound order dataset

            >>> client.read(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order')
            Get proporties of an existing custom dataset

            >>> client.read(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.get_data_lake_dataset_request.GetDataLakeDatasetRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.get_data_lake_dataset_response.GetDataLakeDatasetResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_lake_dataset

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_lake_dataset.get_data_lake_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.get_data_lake_dataset_request.GetDataLakeDatasetRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["namespace"] = namespace
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        description: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_description.DataLakeDatasetDescription"
        ] = None,
    ) -> "aws_sdk_supplychain.types.update_data_lake_dataset_response.UpdateDataLakeDatasetResponse":
        """<p>Enables you to programmatically update an Amazon Web Services Supply Chain data lake dataset. Developers can update the description of a data lake dataset for a given instance ID, namespace, and dataset name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>
            description: <p>The updated description of the data lake dataset.</p>

        Examples:
            Update description of an existing AWS Supply Chain inbound order dataset

            >>> client.update(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order', description='This is an updated AWS Supply Chain inbound order dataset')
            Update description of an existing custom dataset

            >>> client.update(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset', description='This is an updated custom dataset')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.update_data_lake_dataset_request.UpdateDataLakeDatasetRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.update_data_lake_dataset_response.UpdateDataLakeDatasetResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_lake_dataset

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_lake_dataset.update_data_lake_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.update_data_lake_dataset_request.UpdateDataLakeDatasetRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["namespace"] = namespace
        input["name"] = name
        if description is not None:
            input["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.delete_data_lake_dataset_response.DeleteDataLakeDatasetResponse":
        """<p>Enables you to programmatically delete an Amazon Web Services Supply Chain data lake dataset. Developers can delete the existing datasets for a given instance ID, namespace, and instance name.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>

        Examples:
            Delete an AWS Supply Chain inbound_order dataset

            >>> client.delete(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order')
            Delete a custom dataset

            >>> client.delete(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.delete_data_lake_dataset_request.DeleteDataLakeDatasetRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.delete_data_lake_dataset_response.DeleteDataLakeDatasetResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_dataset

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_dataset.delete_data_lake_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.delete_data_lake_dataset_request.DeleteDataLakeDatasetRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["namespace"] = namespace
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        next_token: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_next_token.DataLakeDatasetNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_max_results.DataLakeDatasetMaxResults"
        ] = None,
    ) -> "aws_sdk_supplychain.types.list_data_lake_datasets_response.ListDataLakeDatasetsResponse":
        """<p>Enables you to programmatically view the list of Amazon Web Services Supply Chain data lake datasets. Developers can view the datasets and the corresponding information such as namespace, schema, and so on for a given instance ID and namespace.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            next_token: <p>The pagination token to fetch next page of datasets.</p>
            max_results: <p>The max number of datasets to fetch in this paginated request.</p>

        Examples:
            List AWS Supply Chain datasets

            >>> client.list(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc')
            List custom datasets using pagination

            >>> client.list(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', max_results=2, next_token='next_token_returned_from_previous_list_request')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.list_data_lake_datasets_request.ListDataLakeDatasetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.list_data_lake_datasets_response.ListDataLakeDatasetsResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_lake_datasets

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_lake_datasets.list_data_lake_datasets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.list_data_lake_datasets_request.ListDataLakeDatasetsRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["namespace"] = namespace
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDataLakeDatasetResource:
    def __init__(self, service: AsyncSupplyChainClient) -> None:
        self._service = service

    async def put(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        schema: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_schema.DataLakeDatasetSchema"
        ] = None,
        description: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_description.DataLakeDatasetDescription"
        ] = None,
        partition_spec: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_partition_spec.DataLakeDatasetPartitionSpec"
        ] = None,
        tags: Optional["aws_sdk_supplychain.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_supplychain.types.create_data_lake_dataset_response.CreateDataLakeDatasetResponse":
        """<p>Enables you to programmatically create an Amazon Web Services Supply Chain data lake dataset. Developers can create the datasets using their pre-defined or custom schema for a given instance ID, namespace, and dataset name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> name space, the name must be one of the supported data entities under <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>
            schema: <p>The custom schema of the data lake dataset and required for dataset in <b>default</b> and custom namespaces.</p>
            description: <p>The description of the dataset.</p>
            partition_spec: <p>The partition specification of the dataset. Partitioning can effectively improve the dataset query performance by reducing the amount of data scanned during query execution. But partitioning or not will affect how data get ingested by data ingestion methods, such as SendDataIntegrationEvent's dataset UPSERT will upsert records within partition (instead of within whole dataset). For more details, refer to those data ingestion documentations.</p>
            tags: <p>The tags of the dataset.</p>

        Examples:
            Create an AWS Supply Chain inbound order dataset

            >>> await client.put(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order', description='This is an AWS Supply Chain inbound order dataset', tags={'tagKey1': 'tagValue1', 'tagKey2': 'tagValue2'})
            Create a custom dataset

            >>> await client.put(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset', description='This is a custom dataset', schema={'name': 'MyDataset', 'fields': [{'name': 'id', 'type': 'INT', 'isRequired': True}, {'name': 'description', 'type': 'STRING', 'isRequired': True}, {'name': 'price', 'type': 'DOUBLE', 'isRequired': False}, {'name': 'creation_time', 'type': 'TIMESTAMP', 'isRequired': False}, {'name': 'quantity', 'type': 'LONG', 'isRequired': False}], 'primaryKeys': [{'name': 'id'}]}, partition_spec={'fields': [{'name': 'creation_time', 'transform': {'type': 'DAY'}}, {'name': 'description', 'transform': {'type': 'IDENTITY'}}]}, tags={'tagKey1': 'tagValue1', 'tagKey2': 'tagValue2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.create_data_lake_dataset_request.CreateDataLakeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.create_data_lake_dataset_response.CreateDataLakeDatasetResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_lake_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_lake_dataset.async_create_data_lake_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.create_data_lake_dataset_request.CreateDataLakeDatasetRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["namespace"] = namespace
        input["name"] = name
        if schema is not None:
            input["schema"] = schema
        if description is not None:
            input["description"] = description
        if partition_spec is not None:
            input["partition_spec"] = partition_spec
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.get_data_lake_dataset_response.GetDataLakeDatasetResponse":
        """<p>Enables you to programmatically view an Amazon Web Services Supply Chain data lake dataset. Developers can view the data lake dataset information such as namespace, schema, and so on for a given instance ID, namespace, and dataset name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>

        Examples:
            Get properties of an existing AWS Supply Chain inbound order dataset

            >>> await client.read(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order')
            Get proporties of an existing custom dataset

            >>> await client.read(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.get_data_lake_dataset_request.GetDataLakeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.get_data_lake_dataset_response.GetDataLakeDatasetResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_lake_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_lake_dataset.async_get_data_lake_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.get_data_lake_dataset_request.GetDataLakeDatasetRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["namespace"] = namespace
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        description: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_description.DataLakeDatasetDescription"
        ] = None,
    ) -> "aws_sdk_supplychain.types.update_data_lake_dataset_response.UpdateDataLakeDatasetResponse":
        """<p>Enables you to programmatically update an Amazon Web Services Supply Chain data lake dataset. Developers can update the description of a data lake dataset for a given instance ID, namespace, and dataset name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>
            description: <p>The updated description of the data lake dataset.</p>

        Examples:
            Update description of an existing AWS Supply Chain inbound order dataset

            >>> await client.update(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order', description='This is an updated AWS Supply Chain inbound order dataset')
            Update description of an existing custom dataset

            >>> await client.update(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset', description='This is an updated custom dataset')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.update_data_lake_dataset_request.UpdateDataLakeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.update_data_lake_dataset_response.UpdateDataLakeDatasetResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_lake_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_lake_dataset.async_update_data_lake_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.update_data_lake_dataset_request.UpdateDataLakeDatasetRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["namespace"] = namespace
        input["name"] = name
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        name: "aws_sdk_supplychain.types.data_lake_dataset_name.DataLakeDatasetName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.delete_data_lake_dataset_response.DeleteDataLakeDatasetResponse":
        """<p>Enables you to programmatically delete an Amazon Web Services Supply Chain data lake dataset. Developers can delete the existing datasets for a given instance ID, namespace, and instance name.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            name: <p>The name of the dataset. For <b>asc</b> namespace, the name must be one of the supported data entities under <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p>

        Examples:
            Delete an AWS Supply Chain inbound_order dataset

            >>> await client.delete(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc', name='inbound_order')
            Delete a custom dataset

            >>> await client.delete(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', name='my_dataset')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.delete_data_lake_dataset_request.DeleteDataLakeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.delete_data_lake_dataset_response.DeleteDataLakeDatasetResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_dataset.async_delete_data_lake_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.delete_data_lake_dataset_request.DeleteDataLakeDatasetRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["namespace"] = namespace
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        namespace: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_next_token.DataLakeDatasetNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_supplychain.types.data_lake_dataset_max_results.DataLakeDatasetMaxResults"
        ] = None,
    ) -> "aws_sdk_supplychain.types.list_data_lake_datasets_response.ListDataLakeDatasetsResponse":
        """<p>Enables you to programmatically view the list of Amazon Web Services Supply Chain data lake datasets. Developers can view the datasets and the corresponding information such as namespace, schema, and so on for a given instance ID and namespace.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            namespace: <p>The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - For information on the Amazon Web Services Supply Chain supported datasets see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - For datasets with custom user-defined schemas.</p> </li> </ul>
            next_token: <p>The pagination token to fetch next page of datasets.</p>
            max_results: <p>The max number of datasets to fetch in this paginated request.</p>

        Examples:
            List AWS Supply Chain datasets

            >>> await client.list(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='asc')
            List custom datasets using pagination

            >>> await client.list(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', namespace='default', max_results=2, next_token='next_token_returned_from_previous_list_request')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.list_data_lake_datasets_request.ListDataLakeDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.list_data_lake_datasets_response.ListDataLakeDatasetsResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_lake_datasets

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_lake_datasets.async_list_data_lake_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.list_data_lake_datasets_request.ListDataLakeDatasetsRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["namespace"] = namespace
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
