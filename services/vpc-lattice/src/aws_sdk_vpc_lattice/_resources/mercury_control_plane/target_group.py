from typing import TYPE_CHECKING, Optional

import aws_sdk_vpc_lattice._auth._signers
import aws_sdk_vpc_lattice._auth._sigv4
from aws_sdk_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.create_target_group_request
    import aws_sdk_vpc_lattice.types.create_target_group_response
    import aws_sdk_vpc_lattice.types.delete_target_group_request
    import aws_sdk_vpc_lattice.types.delete_target_group_response
    import aws_sdk_vpc_lattice.types.deregister_targets_request
    import aws_sdk_vpc_lattice.types.deregister_targets_response
    import aws_sdk_vpc_lattice.types.get_target_group_request
    import aws_sdk_vpc_lattice.types.get_target_group_response
    import aws_sdk_vpc_lattice.types.health_check_config
    import aws_sdk_vpc_lattice.types.list_target_groups_request
    import aws_sdk_vpc_lattice.types.list_target_groups_response
    import aws_sdk_vpc_lattice.types.list_targets_request
    import aws_sdk_vpc_lattice.types.list_targets_response
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.register_targets_request
    import aws_sdk_vpc_lattice.types.register_targets_response
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.target_group_config
    import aws_sdk_vpc_lattice.types.target_group_identifier
    import aws_sdk_vpc_lattice.types.target_group_name
    import aws_sdk_vpc_lattice.types.target_group_summary
    import aws_sdk_vpc_lattice.types.target_group_type
    import aws_sdk_vpc_lattice.types.target_list
    import aws_sdk_vpc_lattice.types.target_summary
    import aws_sdk_vpc_lattice.types.update_target_group_request
    import aws_sdk_vpc_lattice.types.update_target_group_response
    import aws_sdk_vpc_lattice.types.vpc_id
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class TargetGroup:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_vpc_lattice.types.target_group_name.TargetGroupName",
        type: "aws_sdk_vpc_lattice.types.target_group_type.TargetGroupType",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        config: Optional[
            "aws_sdk_vpc_lattice.types.target_group_config.TargetGroupConfig"
        ] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_target_group_response.CreateTargetGroupResponse":
        """<p>Creates a target group. A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html\">Target groups</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            name: <p>The name of the target group. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            type: <p>The type of target group.</p>
            config: <p>The target group configuration.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the target group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.create_target_group_request.CreateTargetGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.create_target_group_response.CreateTargetGroupResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_target_group

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.create_target_group.create_target_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_target_group_request.CreateTargetGroupRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["type"] = type
        if config is not None:
            input_["config"] = config
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_target_group_response.GetTargetGroupResponse":
        """<p>Retrieves information about the specified target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_target_group_request.GetTargetGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_target_group_response.GetTargetGroupResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_target_group

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_target_group.get_target_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_target_group_request.GetTargetGroupRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        health_check: "aws_sdk_vpc_lattice.types.health_check_config.HealthCheckConfig",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_target_group_response.UpdateTargetGroupResponse":
        """<p>Updates the specified target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            health_check: <p>The health check configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.update_target_group_request.UpdateTargetGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.update_target_group_response.UpdateTargetGroupResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_target_group

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.update_target_group.update_target_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_target_group_request.UpdateTargetGroupRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier
        input_["health_check"] = health_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_target_group_response.DeleteTargetGroupResponse":
        """<p>Deletes a target group. You can't delete a target group if it is used in a listener rule or if the target group creation is in progress.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_target_group_request.DeleteTargetGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_target_group_response.DeleteTargetGroupResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_target_group

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_target_group.delete_target_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_target_group_request.DeleteTargetGroupRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
        vpc_identifier: Optional["aws_sdk_vpc_lattice.types.vpc_id.VpcId"] = None,
        target_group_type: Optional[
            "aws_sdk_vpc_lattice.types.target_group_type.TargetGroupType"
        ] = None,
    ) -> (
        "aws_sdk_vpc_lattice.types.list_target_groups_response.ListTargetGroupsResponse"
    ):
        """<p>Lists your target groups. You can narrow your search by using the filters below in your request.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
            vpc_identifier: <p>The ID or ARN of the VPC.</p>
            target_group_type: <p>The target group type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_target_groups_request.ListTargetGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_target_groups_response.ListTargetGroupsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_target_groups

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_target_groups.list_target_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_target_groups_request.ListTargetGroupsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if vpc_identifier is not None:
            input_["vpc_identifier"] = vpc_identifier
        if target_group_type is not None:
            input_["target_group_type"] = target_group_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_targets(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        targets: "aws_sdk_vpc_lattice.types.target_list.TargetList",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.deregister_targets_response.DeregisterTargetsResponse":
        """<p>Deregisters the specified targets from the specified target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            targets: <p>The targets to deregister.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.deregister_targets_request.DeregisterTargetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.deregister_targets_response.DeregisterTargetsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.deregister_targets

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.deregister_targets.deregister_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.deregister_targets_request.DeregisterTargetsRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier
        input_["targets"] = targets

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_targets(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
        targets: Optional["aws_sdk_vpc_lattice.types.target_list.TargetList"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_targets_response.ListTargetsResponse":
        """<p>Lists the targets for the target group. By default, all targets are included. You can use this API to check the health status of targets. You can also ﬁlter the results by target.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
            targets: <p>The targets.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_targets_request.ListTargetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_targets_response.ListTargetsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_targets

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_targets.list_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_targets_request.ListTargetsRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if targets is not None:
            input_["targets"] = targets

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_targets(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        targets: "aws_sdk_vpc_lattice.types.target_list.TargetList",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.register_targets_response.RegisterTargetsResponse":
        """<p>Registers the targets with the target group. If it's a Lambda target, you can only have one target in a target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            targets: <p>The targets.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.register_targets_request.RegisterTargetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.register_targets_response.RegisterTargetsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.register_targets

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.register_targets.register_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.register_targets_request.RegisterTargetsRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier
        input_["targets"] = targets

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTargetGroup:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_vpc_lattice.types.target_group_name.TargetGroupName",
        type: "aws_sdk_vpc_lattice.types.target_group_type.TargetGroupType",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        config: Optional[
            "aws_sdk_vpc_lattice.types.target_group_config.TargetGroupConfig"
        ] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_target_group_response.CreateTargetGroupResponse":
        """<p>Creates a target group. A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html\">Target groups</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            name: <p>The name of the target group. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            type: <p>The type of target group.</p>
            config: <p>The target group configuration.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the target group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.create_target_group_request.CreateTargetGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.create_target_group_response.CreateTargetGroupResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_target_group

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.create_target_group.async_create_target_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_target_group_request.CreateTargetGroupRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["type"] = type
        if config is not None:
            input_["config"] = config
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_target_group_response.GetTargetGroupResponse":
        """<p>Retrieves information about the specified target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_target_group_request.GetTargetGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_target_group_response.GetTargetGroupResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_target_group

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_target_group.async_get_target_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_target_group_request.GetTargetGroupRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        health_check: "aws_sdk_vpc_lattice.types.health_check_config.HealthCheckConfig",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_target_group_response.UpdateTargetGroupResponse":
        """<p>Updates the specified target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            health_check: <p>The health check configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.update_target_group_request.UpdateTargetGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.update_target_group_response.UpdateTargetGroupResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_target_group

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.update_target_group.async_update_target_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_target_group_request.UpdateTargetGroupRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier
        input_["health_check"] = health_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_target_group_response.DeleteTargetGroupResponse":
        """<p>Deletes a target group. You can't delete a target group if it is used in a listener rule or if the target group creation is in progress.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_target_group_request.DeleteTargetGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_target_group_response.DeleteTargetGroupResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_target_group

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_target_group.async_delete_target_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_target_group_request.DeleteTargetGroupRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
        vpc_identifier: Optional["aws_sdk_vpc_lattice.types.vpc_id.VpcId"] = None,
        target_group_type: Optional[
            "aws_sdk_vpc_lattice.types.target_group_type.TargetGroupType"
        ] = None,
    ) -> (
        "aws_sdk_vpc_lattice.types.list_target_groups_response.ListTargetGroupsResponse"
    ):
        """<p>Lists your target groups. You can narrow your search by using the filters below in your request.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
            vpc_identifier: <p>The ID or ARN of the VPC.</p>
            target_group_type: <p>The target group type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_target_groups_request.ListTargetGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_target_groups_response.ListTargetGroupsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_target_groups

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_target_groups.async_list_target_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_target_groups_request.ListTargetGroupsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if vpc_identifier is not None:
            input_["vpc_identifier"] = vpc_identifier
        if target_group_type is not None:
            input_["target_group_type"] = target_group_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def deregister_targets(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        targets: "aws_sdk_vpc_lattice.types.target_list.TargetList",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.deregister_targets_response.DeregisterTargetsResponse":
        """<p>Deregisters the specified targets from the specified target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            targets: <p>The targets to deregister.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.deregister_targets_request.DeregisterTargetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.deregister_targets_response.DeregisterTargetsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.deregister_targets

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.deregister_targets.async_deregister_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.deregister_targets_request.DeregisterTargetsRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier
        input_["targets"] = targets

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_targets(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
        targets: Optional["aws_sdk_vpc_lattice.types.target_list.TargetList"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_targets_response.ListTargetsResponse":
        """<p>Lists the targets for the target group. By default, all targets are included. You can use this API to check the health status of targets. You can also ﬁlter the results by target.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
            targets: <p>The targets.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_targets_request.ListTargetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_targets_response.ListTargetsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_targets

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_targets.async_list_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_targets_request.ListTargetsRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if targets is not None:
            input_["targets"] = targets

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def register_targets(
        self,
        target_group_identifier: "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier",
        targets: "aws_sdk_vpc_lattice.types.target_list.TargetList",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.register_targets_response.RegisterTargetsResponse":
        """<p>Registers the targets with the target group. If it's a Lambda target, you can only have one target in a target group.</p>

        Args:
            target_group_identifier: <p>The ID or ARN of the target group.</p>
            targets: <p>The targets.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.register_targets_request.RegisterTargetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.register_targets_response.RegisterTargetsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.register_targets

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.register_targets.async_register_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.register_targets_request.RegisterTargetsRequest = {}  # type: ignore[typeddict-item]
        input_["target_group_identifier"] = target_group_identifier
        input_["targets"] = targets

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
