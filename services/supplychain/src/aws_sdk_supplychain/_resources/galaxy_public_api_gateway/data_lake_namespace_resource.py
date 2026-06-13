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
    import aws_sdk_supplychain.types.create_data_lake_namespace_request
    import aws_sdk_supplychain.types.create_data_lake_namespace_response
    import aws_sdk_supplychain.types.data_lake_namespace
    import aws_sdk_supplychain.types.data_lake_namespace_description
    import aws_sdk_supplychain.types.data_lake_namespace_max_results
    import aws_sdk_supplychain.types.data_lake_namespace_name
    import aws_sdk_supplychain.types.data_lake_namespace_next_token
    import aws_sdk_supplychain.types.delete_data_lake_namespace_request
    import aws_sdk_supplychain.types.delete_data_lake_namespace_response
    import aws_sdk_supplychain.types.get_data_lake_namespace_request
    import aws_sdk_supplychain.types.get_data_lake_namespace_response
    import aws_sdk_supplychain.types.list_data_lake_namespaces_request
    import aws_sdk_supplychain.types.list_data_lake_namespaces_response
    import aws_sdk_supplychain.types.tag_map
    import aws_sdk_supplychain.types.update_data_lake_namespace_request
    import aws_sdk_supplychain.types.update_data_lake_namespace_response
    import aws_sdk_supplychain.types.uuid
    from aws_sdk_supplychain._services.async_supply_chain import (
        AsyncSupplyChainClient,
        AsyncSupplyChainClientConfig,
    )
    from aws_sdk_supplychain._services.supply_chain import (
        SupplyChainClient,
        SupplyChainClientConfig,
    )


class DataLakeNamespaceResource:
    def __init__(self, service: SupplyChainClient) -> None:
        self._service = service

    def put(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        name: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        description: Optional[
            "aws_sdk_supplychain.types.data_lake_namespace_description.DataLakeNamespaceDescription"
        ] = None,
        tags: Optional["aws_sdk_supplychain.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_supplychain.types.create_data_lake_namespace_response.CreateDataLakeNamespaceResponse":
        """<p>Enables you to programmatically create an Amazon Web Services Supply Chain data lake namespace. Developers can create the namespaces for a given instance ID.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the namespace. Noted you cannot create namespace with name starting with <b>asc</b>, <b>default</b>, <b>scn</b>, <b>aws</b>, <b>amazon</b>, <b>amzn</b> </p>
            description: <p>The description of the namespace.</p>
            tags: <p>The tags of the namespace.</p>

        Examples:
            Create a data lake namespace

            >>> client.put(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace', description='This is my AWS Supply Chain namespace', tags={'tagKey1': 'tagValue1', 'tagKey2': 'tagValue2'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.create_data_lake_namespace_request.CreateDataLakeNamespaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.create_data_lake_namespace_response.CreateDataLakeNamespaceResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_lake_namespace

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_lake_namespace.create_data_lake_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.create_data_lake_namespace_request.CreateDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["name"] = name
        if description is not None:
            input["description"] = description
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
        name: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.get_data_lake_namespace_response.GetDataLakeNamespaceResponse":
        """<p>Enables you to programmatically view an Amazon Web Services Supply Chain data lake namespace. Developers can view the data lake namespace information such as description for a given instance ID and namespace name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the namespace. Besides the namespaces user created, you can also specify the pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - Pre-defined namespace containing Amazon Web Services Supply Chain supported datasets, see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - Pre-defined namespace containing datasets with custom user-defined schemas.</p> </li> </ul>

        Examples:
            Get properties of an existing AWS Supply Chain namespace

            >>> client.read(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace')
            Get proporties of an existing pre-defined AWS Supply Chain namespace

            >>> client.read(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='asc')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.get_data_lake_namespace_request.GetDataLakeNamespaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.get_data_lake_namespace_response.GetDataLakeNamespaceResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_lake_namespace

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_lake_namespace.get_data_lake_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.get_data_lake_namespace_request.GetDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
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
        name: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        description: Optional[
            "aws_sdk_supplychain.types.data_lake_namespace_description.DataLakeNamespaceDescription"
        ] = None,
    ) -> "aws_sdk_supplychain.types.update_data_lake_namespace_response.UpdateDataLakeNamespaceResponse":
        """<p>Enables you to programmatically update an Amazon Web Services Supply Chain data lake namespace. Developers can update the description of a data lake namespace for a given instance ID and namespace name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Chain instance identifier.</p>
            name: <p>The name of the namespace. Noted you cannot update namespace with name starting with <b>asc</b>, <b>default</b>, <b>scn</b>, <b>aws</b>, <b>amazon</b>, <b>amzn</b> </p>
            description: <p>The updated description of the data lake namespace.</p>

        Examples:
            Update description of an existing AWS Supply Chain namespace

            >>> client.update(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace', description='This is an updated AWS Supply Chain namespace')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.update_data_lake_namespace_request.UpdateDataLakeNamespaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.update_data_lake_namespace_response.UpdateDataLakeNamespaceResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_lake_namespace

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_lake_namespace.update_data_lake_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.update_data_lake_namespace_request.UpdateDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
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
        name: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.delete_data_lake_namespace_response.DeleteDataLakeNamespaceResponse":
        """<p>Enables you to programmatically delete an Amazon Web Services Supply Chain data lake namespace and its underling datasets. Developers can delete the existing namespaces for a given instance ID and namespace name.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            name: <p>The name of the namespace. Noted you cannot delete pre-defined namespace like <b>asc</b>, <b>default</b> which are only deleted through instance deletion.</p>

        Examples:
            Delete an AWS Supply Chain namespace

            >>> client.delete(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.delete_data_lake_namespace_request.DeleteDataLakeNamespaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.delete_data_lake_namespace_response.DeleteDataLakeNamespaceResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_namespace

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_namespace.delete_data_lake_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.delete_data_lake_namespace_request.DeleteDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
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
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        next_token: Optional[
            "aws_sdk_supplychain.types.data_lake_namespace_next_token.DataLakeNamespaceNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_supplychain.types.data_lake_namespace_max_results.DataLakeNamespaceMaxResults"
        ] = None,
    ) -> "aws_sdk_supplychain.types.list_data_lake_namespaces_response.ListDataLakeNamespacesResponse":
        """<p>Enables you to programmatically view the list of Amazon Web Services Supply Chain data lake namespaces. Developers can view the namespaces and the corresponding information such as description for a given instance ID. Note that this API only return custom namespaces, instance pre-defined namespaces are not included.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            next_token: <p>The pagination token to fetch next page of namespaces.</p>
            max_results: <p>The max number of namespaces to fetch in this paginated request.</p>

        Examples:
            List AWS Supply Chain namespaces

            >>> client.list(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5')
            List AWS Supply Chain namespaces using pagination

            >>> client.list(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', max_results=1, next_token='next_token_returned_from_previous_list_request')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.list_data_lake_namespaces_request.ListDataLakeNamespacesRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.list_data_lake_namespaces_response.ListDataLakeNamespacesResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_lake_namespaces

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_lake_namespaces.list_data_lake_namespaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.list_data_lake_namespaces_request.ListDataLakeNamespacesRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
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


class AsyncDataLakeNamespaceResource:
    def __init__(self, service: AsyncSupplyChainClient) -> None:
        self._service = service

    async def put(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        name: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        description: Optional[
            "aws_sdk_supplychain.types.data_lake_namespace_description.DataLakeNamespaceDescription"
        ] = None,
        tags: Optional["aws_sdk_supplychain.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_supplychain.types.create_data_lake_namespace_response.CreateDataLakeNamespaceResponse":
        """<p>Enables you to programmatically create an Amazon Web Services Supply Chain data lake namespace. Developers can create the namespaces for a given instance ID.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the namespace. Noted you cannot create namespace with name starting with <b>asc</b>, <b>default</b>, <b>scn</b>, <b>aws</b>, <b>amazon</b>, <b>amzn</b> </p>
            description: <p>The description of the namespace.</p>
            tags: <p>The tags of the namespace.</p>

        Examples:
            Create a data lake namespace

            >>> await client.put(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace', description='This is my AWS Supply Chain namespace', tags={'tagKey1': 'tagValue1', 'tagKey2': 'tagValue2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.create_data_lake_namespace_request.CreateDataLakeNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.create_data_lake_namespace_response.CreateDataLakeNamespaceResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_lake_namespace

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_lake_namespace.async_create_data_lake_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.create_data_lake_namespace_request.CreateDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["name"] = name
        if description is not None:
            input["description"] = description
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
        name: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.get_data_lake_namespace_response.GetDataLakeNamespaceResponse":
        """<p>Enables you to programmatically view an Amazon Web Services Supply Chain data lake namespace. Developers can view the data lake namespace information such as description for a given instance ID and namespace name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the namespace. Besides the namespaces user created, you can also specify the pre-defined namespaces:</p> <ul> <li> <p> <b>asc</b> - Pre-defined namespace containing Amazon Web Services Supply Chain supported datasets, see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html</a>.</p> </li> <li> <p> <b>default</b> - Pre-defined namespace containing datasets with custom user-defined schemas.</p> </li> </ul>

        Examples:
            Get properties of an existing AWS Supply Chain namespace

            >>> await client.read(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace')
            Get proporties of an existing pre-defined AWS Supply Chain namespace

            >>> await client.read(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='asc')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.get_data_lake_namespace_request.GetDataLakeNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.get_data_lake_namespace_response.GetDataLakeNamespaceResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_lake_namespace

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_lake_namespace.async_get_data_lake_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.get_data_lake_namespace_request.GetDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
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
        name: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        description: Optional[
            "aws_sdk_supplychain.types.data_lake_namespace_description.DataLakeNamespaceDescription"
        ] = None,
    ) -> "aws_sdk_supplychain.types.update_data_lake_namespace_response.UpdateDataLakeNamespaceResponse":
        """<p>Enables you to programmatically update an Amazon Web Services Supply Chain data lake namespace. Developers can update the description of a data lake namespace for a given instance ID and namespace name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Chain instance identifier.</p>
            name: <p>The name of the namespace. Noted you cannot update namespace with name starting with <b>asc</b>, <b>default</b>, <b>scn</b>, <b>aws</b>, <b>amazon</b>, <b>amzn</b> </p>
            description: <p>The updated description of the data lake namespace.</p>

        Examples:
            Update description of an existing AWS Supply Chain namespace

            >>> await client.update(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace', description='This is an updated AWS Supply Chain namespace')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.update_data_lake_namespace_request.UpdateDataLakeNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.update_data_lake_namespace_response.UpdateDataLakeNamespaceResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_lake_namespace

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_lake_namespace.async_update_data_lake_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.update_data_lake_namespace_request.UpdateDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
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
        name: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.delete_data_lake_namespace_response.DeleteDataLakeNamespaceResponse":
        """<p>Enables you to programmatically delete an Amazon Web Services Supply Chain data lake namespace and its underling datasets. Developers can delete the existing namespaces for a given instance ID and namespace name.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            name: <p>The name of the namespace. Noted you cannot delete pre-defined namespace like <b>asc</b>, <b>default</b> which are only deleted through instance deletion.</p>

        Examples:
            Delete an AWS Supply Chain namespace

            >>> await client.delete(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', name='my_namespace')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.delete_data_lake_namespace_request.DeleteDataLakeNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.delete_data_lake_namespace_response.DeleteDataLakeNamespaceResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_namespace

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_lake_namespace.async_delete_data_lake_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.delete_data_lake_namespace_request.DeleteDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
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
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "aws_sdk_supplychain.types.data_lake_namespace_next_token.DataLakeNamespaceNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_supplychain.types.data_lake_namespace_max_results.DataLakeNamespaceMaxResults"
        ] = None,
    ) -> "aws_sdk_supplychain.types.list_data_lake_namespaces_response.ListDataLakeNamespacesResponse":
        """<p>Enables you to programmatically view the list of Amazon Web Services Supply Chain data lake namespaces. Developers can view the namespaces and the corresponding information such as description for a given instance ID. Note that this API only return custom namespaces, instance pre-defined namespaces are not included.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            next_token: <p>The pagination token to fetch next page of namespaces.</p>
            max_results: <p>The max number of namespaces to fetch in this paginated request.</p>

        Examples:
            List AWS Supply Chain namespaces

            >>> await client.list(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5')
            List AWS Supply Chain namespaces using pagination

            >>> await client.list(instance_id='1877dd20-dee9-4639-8e99-cb67acf21fe5', max_results=1, next_token='next_token_returned_from_previous_list_request')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.list_data_lake_namespaces_request.ListDataLakeNamespacesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.list_data_lake_namespaces_response.ListDataLakeNamespacesResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_lake_namespaces

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_lake_namespaces.async_list_data_lake_namespaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.list_data_lake_namespaces_request.ListDataLakeNamespacesRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
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
