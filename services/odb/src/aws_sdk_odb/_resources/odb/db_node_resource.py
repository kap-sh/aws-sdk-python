from typing import TYPE_CHECKING, Optional

from aws_sdk_odb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_node_summary
    import aws_sdk_odb.types.get_db_node_input
    import aws_sdk_odb.types.get_db_node_output
    import aws_sdk_odb.types.list_db_nodes_input
    import aws_sdk_odb.types.list_db_nodes_output
    import aws_sdk_odb.types.reboot_db_node_input
    import aws_sdk_odb.types.reboot_db_node_output
    import aws_sdk_odb.types.resource_id
    import aws_sdk_odb.types.start_db_node_input
    import aws_sdk_odb.types.start_db_node_output
    import aws_sdk_odb.types.stop_db_node_input
    import aws_sdk_odb.types.stop_db_node_output
    from aws_sdk_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from aws_sdk_odb._services.odb import odbClient, odbClientConfig


class DbNodeResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def read(
        self,
        cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId",
        db_node_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.get_db_node_output.GetDbNodeOutput":
        """<p>Returns information about the specified DB node.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node.</p>
            db_node_id: <p>The unique identifier of the DB node to retrieve information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.get_db_node_input.GetDbNodeInput]",
        ) -> OperationResponse["aws_sdk_odb.types.get_db_node_output.GetDbNodeOutput"]:
            import aws_sdk_odb._operations.odb.get_db_node

            output, http_response = aws_sdk_odb._operations.odb.get_db_node.get_db_node(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_odb.types.get_db_node_input.GetDbNodeInput = {}  # type: ignore[typeddict-item]
        input["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        input["db_node_id"] = db_node_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_odb.types.list_db_nodes_output.ListDbNodesOutput":
        """<p>Returns information about the DB nodes for the specified VM cluster.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_db_nodes_input.ListDbNodesInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_db_nodes_output.ListDbNodesOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_db_nodes

            output, http_response = (
                aws_sdk_odb._operations.odb.list_db_nodes.list_db_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_odb.types.list_db_nodes_input.ListDbNodesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["cloud_vm_cluster_id"] = cloud_vm_cluster_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reboot_db_node(
        self,
        cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId",
        db_node_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.reboot_db_node_output.RebootDbNodeOutput":
        """<p>Reboots the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to reboot.</p>
            db_node_id: <p>The unique identifier of the DB node to reboot.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.reboot_db_node_input.RebootDbNodeInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.reboot_db_node_output.RebootDbNodeOutput"
        ]:
            import aws_sdk_odb._operations.odb.reboot_db_node

            output, http_response = (
                aws_sdk_odb._operations.odb.reboot_db_node.reboot_db_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_odb.types.reboot_db_node_input.RebootDbNodeInput = {}  # type: ignore[typeddict-item]
        input["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        input["db_node_id"] = db_node_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_db_node(
        self,
        cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId",
        db_node_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.start_db_node_output.StartDbNodeOutput":
        """<p>Starts the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to start.</p>
            db_node_id: <p>The unique identifier of the DB node to start.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.start_db_node_input.StartDbNodeInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.start_db_node_output.StartDbNodeOutput"
        ]:
            import aws_sdk_odb._operations.odb.start_db_node

            output, http_response = (
                aws_sdk_odb._operations.odb.start_db_node.start_db_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_odb.types.start_db_node_input.StartDbNodeInput = {}  # type: ignore[typeddict-item]
        input["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        input["db_node_id"] = db_node_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_db_node(
        self,
        cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId",
        db_node_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.stop_db_node_output.StopDbNodeOutput":
        """<p>Stops the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to stop.</p>
            db_node_id: <p>The unique identifier of the DB node to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.stop_db_node_input.StopDbNodeInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.stop_db_node_output.StopDbNodeOutput"
        ]:
            import aws_sdk_odb._operations.odb.stop_db_node

            output, http_response = (
                aws_sdk_odb._operations.odb.stop_db_node.stop_db_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_odb.types.stop_db_node_input.StopDbNodeInput = {}  # type: ignore[typeddict-item]
        input["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        input["db_node_id"] = db_node_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDbNodeResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def read(
        self,
        cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId",
        db_node_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.get_db_node_output.GetDbNodeOutput":
        """<p>Returns information about the specified DB node.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node.</p>
            db_node_id: <p>The unique identifier of the DB node to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.get_db_node_input.GetDbNodeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.get_db_node_output.GetDbNodeOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_db_node

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.get_db_node.async_get_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_odb.types.get_db_node_input.GetDbNodeInput = {}  # type: ignore[typeddict-item]
        input["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        input["db_node_id"] = db_node_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_odb.types.list_db_nodes_output.ListDbNodesOutput":
        """<p>Returns information about the DB nodes for the specified VM cluster.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.list_db_nodes_input.ListDbNodesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.list_db_nodes_output.ListDbNodesOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_db_nodes

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.list_db_nodes.async_list_db_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_odb.types.list_db_nodes_input.ListDbNodesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["cloud_vm_cluster_id"] = cloud_vm_cluster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reboot_db_node(
        self,
        cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId",
        db_node_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.reboot_db_node_output.RebootDbNodeOutput":
        """<p>Reboots the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to reboot.</p>
            db_node_id: <p>The unique identifier of the DB node to reboot.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.reboot_db_node_input.RebootDbNodeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.reboot_db_node_output.RebootDbNodeOutput"
        ]:
            import aws_sdk_odb._operations.odb.reboot_db_node

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.reboot_db_node.async_reboot_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_odb.types.reboot_db_node_input.RebootDbNodeInput = {}  # type: ignore[typeddict-item]
        input["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        input["db_node_id"] = db_node_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_db_node(
        self,
        cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId",
        db_node_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.start_db_node_output.StartDbNodeOutput":
        """<p>Starts the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to start.</p>
            db_node_id: <p>The unique identifier of the DB node to start.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.start_db_node_input.StartDbNodeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.start_db_node_output.StartDbNodeOutput"
        ]:
            import aws_sdk_odb._operations.odb.start_db_node

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.start_db_node.async_start_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_odb.types.start_db_node_input.StartDbNodeInput = {}  # type: ignore[typeddict-item]
        input["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        input["db_node_id"] = db_node_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_db_node(
        self,
        cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId",
        db_node_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.stop_db_node_output.StopDbNodeOutput":
        """<p>Stops the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to stop.</p>
            db_node_id: <p>The unique identifier of the DB node to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.stop_db_node_input.StopDbNodeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.stop_db_node_output.StopDbNodeOutput"
        ]:
            import aws_sdk_odb._operations.odb.stop_db_node

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.stop_db_node.async_stop_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_odb.types.stop_db_node_input.StopDbNodeInput = {}  # type: ignore[typeddict-item]
        input["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        input["db_node_id"] = db_node_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
