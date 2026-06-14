from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_neptune_graph._auth._signers
import aws_sdk_neptune_graph._auth._sigv4
from aws_sdk_neptune_graph._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.create_graph_input
    import aws_sdk_neptune_graph.types.create_graph_output
    import aws_sdk_neptune_graph.types.delete_graph_input
    import aws_sdk_neptune_graph.types.delete_graph_output
    import aws_sdk_neptune_graph.types.get_graph_input
    import aws_sdk_neptune_graph.types.get_graph_output
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.graph_name
    import aws_sdk_neptune_graph.types.graph_summary
    import aws_sdk_neptune_graph.types.kms_key_arn
    import aws_sdk_neptune_graph.types.list_graphs_input
    import aws_sdk_neptune_graph.types.list_graphs_output
    import aws_sdk_neptune_graph.types.max_results
    import aws_sdk_neptune_graph.types.pagination_token
    import aws_sdk_neptune_graph.types.provisioned_memory
    import aws_sdk_neptune_graph.types.replica_count
    import aws_sdk_neptune_graph.types.reset_graph_input
    import aws_sdk_neptune_graph.types.reset_graph_output
    import aws_sdk_neptune_graph.types.restore_graph_from_snapshot_input
    import aws_sdk_neptune_graph.types.restore_graph_from_snapshot_output
    import aws_sdk_neptune_graph.types.snapshot_identifier
    import aws_sdk_neptune_graph.types.start_graph_input
    import aws_sdk_neptune_graph.types.start_graph_output
    import aws_sdk_neptune_graph.types.stop_graph_input
    import aws_sdk_neptune_graph.types.stop_graph_output
    import aws_sdk_neptune_graph.types.tag_map
    import aws_sdk_neptune_graph.types.update_graph_input
    import aws_sdk_neptune_graph.types.update_graph_output
    import aws_sdk_neptune_graph.types.vector_search_configuration
    from aws_sdk_neptune_graph._services.async_neptune_graph import (
        AsyncNeptuneGraphClient,
        AsyncNeptuneGraphClientConfig,
    )
    from aws_sdk_neptune_graph._services.neptune_graph import (
        NeptuneGraphClient,
        NeptuneGraphClientConfig,
    )


class GraphResource:
    def __init__(self, service: NeptuneGraphClient) -> None:
        self._service = service

    def create_graph(
        self,
        graph_name: "aws_sdk_neptune_graph.types.graph_name.GraphName",
        provisioned_memory: "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        tags: Optional["aws_sdk_neptune_graph.types.tag_map.TagMap"] = None,
        public_connectivity: Optional[bool] = None,
        kms_key_identifier: Optional[
            "aws_sdk_neptune_graph.types.kms_key_arn.KmsKeyArn"
        ] = None,
        vector_search_configuration: Optional[
            "aws_sdk_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"
        ] = None,
        replica_count: Optional[
            "aws_sdk_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "aws_sdk_neptune_graph.types.create_graph_output.CreateGraphOutput":
        """<p>Creates a new Neptune Analytics graph.</p>

        Args:
            graph_name: <p>A name for the new Neptune Analytics graph to be created.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>
            kms_key_identifier: <p>Specifies a KMS key to use to encrypt data in the new graph.</p>
            vector_search_configuration: <p>Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as <code>dimension=</code>value. Max = 65,535</p>
            replica_count: <p>The number of replicas in other AZs. Min =0, Max = 2, Default = 1.</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            deletion_protection: <p>Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (<code>true</code> or <code>false</code>).</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 16</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.create_graph_input.CreateGraphInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.create_graph_output.CreateGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.create_graph

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.create_graph.create_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.create_graph_input.CreateGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_name"] = graph_name
        if tags is not None:
            input_["tags"] = tags
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if vector_search_configuration is not None:
            input_["vector_search_configuration"] = vector_search_configuration
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        input_["provisioned_memory"] = provisioned_memory

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        skip_snapshot: bool,
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.delete_graph_output.DeleteGraphOutput":
        """<p>Deletes the specified graph. Graphs cannot be deleted if delete-protection is enabled.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            skip_snapshot: <p>Determines whether a final graph snapshot is created before the graph is deleted. If <code>true</code> is specified, no graph snapshot is created. If <code>false</code> is specified, a graph snapshot is created before the graph is deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.delete_graph_input.DeleteGraphInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.delete_graph_output.DeleteGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.delete_graph

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.delete_graph.delete_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.delete_graph_input.DeleteGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier
        input_["skip_snapshot"] = skip_snapshot

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.get_graph_output.GetGraphOutput":
        """<p>Gets information about a specified graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.get_graph_input.GetGraphInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.get_graph_output.GetGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_graph

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_graph.get_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.get_graph_input.GetGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_graphs(
        self,
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_neptune_graph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_neptune_graph.types.list_graphs_output.ListGraphsOutput":
        """<p>Lists available Neptune Analytics graphs.</p>

        Args:
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.list_graphs_input.ListGraphsInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.list_graphs_output.ListGraphsOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_graphs

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_graphs.list_graphs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.list_graphs_input.ListGraphsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reset_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        skip_snapshot: bool,
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.reset_graph_output.ResetGraphOutput":
        """<p>Empties the data from a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>ID of the graph to reset.</p>
            skip_snapshot: <p>Determines whether a final graph snapshot is created before the graph data is deleted. If set to <code>true</code>, no graph snapshot is created. If set to <code>false</code>, a graph snapshot is created before the data is deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.reset_graph_input.ResetGraphInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.reset_graph_output.ResetGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.reset_graph

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.reset_graph.reset_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.reset_graph_input.ResetGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier
        input_["skip_snapshot"] = skip_snapshot

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def restore_graph_from_snapshot(
        self,
        snapshot_identifier: "aws_sdk_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        graph_name: "aws_sdk_neptune_graph.types.graph_name.GraphName",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        provisioned_memory: Optional[
            "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        deletion_protection: Optional[bool] = None,
        tags: Optional["aws_sdk_neptune_graph.types.tag_map.TagMap"] = None,
        replica_count: Optional[
            "aws_sdk_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        public_connectivity: Optional[bool] = None,
    ) -> "aws_sdk_neptune_graph.types.restore_graph_from_snapshot_output.RestoreGraphFromSnapshotOutput":
        """<p>Restores a graph from a snapshot.</p>

        Args:
            snapshot_identifier: <p>The ID of the snapshot in question.</p>
            graph_name: <p>A name for the new Neptune Analytics graph to be created from the snapshot.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>
            deletion_protection: <p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>
            tags: <p>Adds metadata tags to the snapshot. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            replica_count: <p>The number of replicas in other AZs. Min =0, Max = 2, Default =1</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.restore_graph_from_snapshot_input.RestoreGraphFromSnapshotInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.restore_graph_from_snapshot_output.RestoreGraphFromSnapshotOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.restore_graph_from_snapshot

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.restore_graph_from_snapshot.restore_graph_from_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.restore_graph_from_snapshot_input.RestoreGraphFromSnapshotInput = {}  # type: ignore[typeddict-item]
        input_["snapshot_identifier"] = snapshot_identifier
        input_["graph_name"] = graph_name
        if provisioned_memory is not None:
            input_["provisioned_memory"] = provisioned_memory
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if tags is not None:
            input_["tags"] = tags
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.start_graph_output.StartGraphOutput":
        """<p>Starts the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.start_graph_input.StartGraphInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.start_graph_output.StartGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.start_graph

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.start_graph.start_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.start_graph_input.StartGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.stop_graph_output.StopGraphOutput":
        """<p>Stops the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.stop_graph_input.StopGraphInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.stop_graph_output.StopGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.stop_graph

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.stop_graph.stop_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.stop_graph_input.StopGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        public_connectivity: Optional[bool] = None,
        provisioned_memory: Optional[
            "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "aws_sdk_neptune_graph.types.update_graph_output.UpdateGraphOutput":
        """<p>Updates the configuration of a specified Neptune Analytics graph</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>
            deletion_protection: <p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.update_graph_input.UpdateGraphInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.update_graph_output.UpdateGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.update_graph

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.update_graph.update_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.update_graph_input.UpdateGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if provisioned_memory is not None:
            input_["provisioned_memory"] = provisioned_memory
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncGraphResource:
    def __init__(self, service: AsyncNeptuneGraphClient) -> None:
        self._service = service

    async def create_graph(
        self,
        graph_name: "aws_sdk_neptune_graph.types.graph_name.GraphName",
        provisioned_memory: "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        tags: Optional["aws_sdk_neptune_graph.types.tag_map.TagMap"] = None,
        public_connectivity: Optional[bool] = None,
        kms_key_identifier: Optional[
            "aws_sdk_neptune_graph.types.kms_key_arn.KmsKeyArn"
        ] = None,
        vector_search_configuration: Optional[
            "aws_sdk_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"
        ] = None,
        replica_count: Optional[
            "aws_sdk_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "aws_sdk_neptune_graph.types.create_graph_output.CreateGraphOutput":
        """<p>Creates a new Neptune Analytics graph.</p>

        Args:
            graph_name: <p>A name for the new Neptune Analytics graph to be created.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>
            kms_key_identifier: <p>Specifies a KMS key to use to encrypt data in the new graph.</p>
            vector_search_configuration: <p>Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as <code>dimension=</code>value. Max = 65,535</p>
            replica_count: <p>The number of replicas in other AZs. Min =0, Max = 2, Default = 1.</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            deletion_protection: <p>Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (<code>true</code> or <code>false</code>).</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 16</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.create_graph_input.CreateGraphInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.create_graph_output.CreateGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.create_graph

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.create_graph.async_create_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.create_graph_input.CreateGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_name"] = graph_name
        if tags is not None:
            input_["tags"] = tags
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if vector_search_configuration is not None:
            input_["vector_search_configuration"] = vector_search_configuration
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        input_["provisioned_memory"] = provisioned_memory

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        skip_snapshot: bool,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.delete_graph_output.DeleteGraphOutput":
        """<p>Deletes the specified graph. Graphs cannot be deleted if delete-protection is enabled.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            skip_snapshot: <p>Determines whether a final graph snapshot is created before the graph is deleted. If <code>true</code> is specified, no graph snapshot is created. If <code>false</code> is specified, a graph snapshot is created before the graph is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.delete_graph_input.DeleteGraphInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.delete_graph_output.DeleteGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.delete_graph

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.delete_graph.async_delete_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.delete_graph_input.DeleteGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier
        input_["skip_snapshot"] = skip_snapshot

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.get_graph_output.GetGraphOutput":
        """<p>Gets information about a specified graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.get_graph_input.GetGraphInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.get_graph_output.GetGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_graph

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_graph.async_get_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.get_graph_input.GetGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_graphs(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_neptune_graph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_neptune_graph.types.list_graphs_output.ListGraphsOutput":
        """<p>Lists available Neptune Analytics graphs.</p>

        Args:
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.list_graphs_input.ListGraphsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.list_graphs_output.ListGraphsOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_graphs

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_graphs.async_list_graphs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.list_graphs_input.ListGraphsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        skip_snapshot: bool,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.reset_graph_output.ResetGraphOutput":
        """<p>Empties the data from a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>ID of the graph to reset.</p>
            skip_snapshot: <p>Determines whether a final graph snapshot is created before the graph data is deleted. If set to <code>true</code>, no graph snapshot is created. If set to <code>false</code>, a graph snapshot is created before the data is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.reset_graph_input.ResetGraphInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.reset_graph_output.ResetGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.reset_graph

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.reset_graph.async_reset_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.reset_graph_input.ResetGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier
        input_["skip_snapshot"] = skip_snapshot

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def restore_graph_from_snapshot(
        self,
        snapshot_identifier: "aws_sdk_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        graph_name: "aws_sdk_neptune_graph.types.graph_name.GraphName",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        provisioned_memory: Optional[
            "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        deletion_protection: Optional[bool] = None,
        tags: Optional["aws_sdk_neptune_graph.types.tag_map.TagMap"] = None,
        replica_count: Optional[
            "aws_sdk_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        public_connectivity: Optional[bool] = None,
    ) -> "aws_sdk_neptune_graph.types.restore_graph_from_snapshot_output.RestoreGraphFromSnapshotOutput":
        """<p>Restores a graph from a snapshot.</p>

        Args:
            snapshot_identifier: <p>The ID of the snapshot in question.</p>
            graph_name: <p>A name for the new Neptune Analytics graph to be created from the snapshot.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>
            deletion_protection: <p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>
            tags: <p>Adds metadata tags to the snapshot. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            replica_count: <p>The number of replicas in other AZs. Min =0, Max = 2, Default =1</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.restore_graph_from_snapshot_input.RestoreGraphFromSnapshotInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.restore_graph_from_snapshot_output.RestoreGraphFromSnapshotOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.restore_graph_from_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.restore_graph_from_snapshot.async_restore_graph_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.restore_graph_from_snapshot_input.RestoreGraphFromSnapshotInput = {}  # type: ignore[typeddict-item]
        input_["snapshot_identifier"] = snapshot_identifier
        input_["graph_name"] = graph_name
        if provisioned_memory is not None:
            input_["provisioned_memory"] = provisioned_memory
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if tags is not None:
            input_["tags"] = tags
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.start_graph_output.StartGraphOutput":
        """<p>Starts the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.start_graph_input.StartGraphInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.start_graph_output.StartGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.start_graph

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.start_graph.async_start_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.start_graph_input.StartGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.stop_graph_output.StopGraphOutput":
        """<p>Stops the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.stop_graph_input.StopGraphInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.stop_graph_output.StopGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.stop_graph

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.stop_graph.async_stop_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.stop_graph_input.StopGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_graph(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        public_connectivity: Optional[bool] = None,
        provisioned_memory: Optional[
            "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "aws_sdk_neptune_graph.types.update_graph_output.UpdateGraphOutput":
        """<p>Updates the configuration of a specified Neptune Analytics graph</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>
            deletion_protection: <p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.update_graph_input.UpdateGraphInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.update_graph_output.UpdateGraphOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.update_graph

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.update_graph.async_update_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_neptune_graph.types.update_graph_input.UpdateGraphInput = {}  # type: ignore[typeddict-item]
        input_["graph_identifier"] = graph_identifier
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if provisioned_memory is not None:
            input_["provisioned_memory"] = provisioned_memory
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
