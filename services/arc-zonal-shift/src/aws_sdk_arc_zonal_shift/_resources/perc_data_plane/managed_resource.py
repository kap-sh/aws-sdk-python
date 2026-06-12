from typing import TYPE_CHECKING, Optional

import aws_sdk_arc_zonal_shift._auth._signers
import aws_sdk_arc_zonal_shift._auth._sigv4
from aws_sdk_arc_zonal_shift._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.get_managed_resource_request
    import aws_sdk_arc_zonal_shift.types.get_managed_resource_response
    import aws_sdk_arc_zonal_shift.types.list_managed_resources_request
    import aws_sdk_arc_zonal_shift.types.list_managed_resources_response
    import aws_sdk_arc_zonal_shift.types.managed_resource_summary
    import aws_sdk_arc_zonal_shift.types.max_results
    import aws_sdk_arc_zonal_shift.types.resource_identifier
    import aws_sdk_arc_zonal_shift.types.update_zonal_autoshift_configuration_request
    import aws_sdk_arc_zonal_shift.types.update_zonal_autoshift_configuration_response
    import aws_sdk_arc_zonal_shift.types.zonal_autoshift_status
    from aws_sdk_arc_zonal_shift._services.arc_zonal_shift import (
        ARCZonalShiftClient,
        ARCZonalShiftClientConfig,
    )
    from aws_sdk_arc_zonal_shift._services.async_arc_zonal_shift import (
        AsyncARCZonalShiftClient,
        AsyncARCZonalShiftClientConfig,
    )


class ManagedResource:
    def __init__(self, service: ARCZonalShiftClient) -> None:
        self._service = service

    def read(
        self,
        resource_identifier: "aws_sdk_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.get_managed_resource_response.GetManagedResourceResponse":
        """<p>Get information about a resource that's been registered for zonal shifts with Amazon Application Recovery Controller in this Amazon Web Services Region. Resources that are registered for zonal shifts are managed resources in ARC. You can start zonal shifts and configure zonal autoshift for managed resources.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that Amazon Web Services shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html\">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html\">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html\">Application Load Balancer</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html\">Network Load Balancer</a> </p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_arc_zonal_shift.types.get_managed_resource_request.GetManagedResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_arc_zonal_shift.types.get_managed_resource_response.GetManagedResourceResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.get_managed_resource

            output, http_response = (
                aws_sdk_arc_zonal_shift._operations.perc_data_plane.get_managed_resource.get_managed_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_arc_zonal_shift.types.get_managed_resource_request.GetManagedResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_arc_zonal_shift.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.list_managed_resources_response.ListManagedResourcesResponse":
        """<p>Lists all the resources in your Amazon Web Services account in this Amazon Web Services Region that are managed for zonal shifts in Amazon Application Recovery Controller, and information about them. The information includes the zonal autoshift status for the resource, as well as the Amazon Resource Name (ARN), the Availability Zones that each resource is deployed in, and the resource name.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_arc_zonal_shift.types.list_managed_resources_request.ListManagedResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_arc_zonal_shift.types.list_managed_resources_response.ListManagedResourcesResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.list_managed_resources

            output, http_response = (
                aws_sdk_arc_zonal_shift._operations.perc_data_plane.list_managed_resources.list_managed_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_arc_zonal_shift.types.list_managed_resources_request.ListManagedResourcesRequest = {}  # type: ignore[typeddict-item]
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

    def update_zonal_autoshift_configuration(
        self,
        resource_identifier: "aws_sdk_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        zonal_autoshift_status: "aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.update_zonal_autoshift_configuration_response.UpdateZonalAutoshiftConfigurationResponse":
        """<p>The zonal autoshift configuration for a resource includes the practice run configuration and the status for running autoshifts, zonal autoshift status. When a resource has a practice run configuration, ARC starts weekly zonal shifts for the resource, to shift traffic away from an Availability Zone. Weekly practice runs help you to make sure that your application can continue to operate normally with the loss of one Availability Zone.</p> <p>You can update the zonal autoshift status to enable or disable zonal autoshift. When zonal autoshift is <code>ENABLED</code>, you authorize Amazon Web Services to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that you want to update the zonal autoshift configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>
            zonal_autoshift_status: <p>The zonal autoshift status for the resource that you want to update the zonal autoshift configuration for. Choose <code>ENABLED</code> to authorize Amazon Web Services to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_arc_zonal_shift.types.update_zonal_autoshift_configuration_request.UpdateZonalAutoshiftConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_arc_zonal_shift.types.update_zonal_autoshift_configuration_response.UpdateZonalAutoshiftConfigurationResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_zonal_autoshift_configuration

            output, http_response = (
                aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_zonal_autoshift_configuration.update_zonal_autoshift_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_arc_zonal_shift.types.update_zonal_autoshift_configuration_request.UpdateZonalAutoshiftConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["zonal_autoshift_status"] = zonal_autoshift_status

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncManagedResource:
    def __init__(self, service: AsyncARCZonalShiftClient) -> None:
        self._service = service

    async def read(
        self,
        resource_identifier: "aws_sdk_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.get_managed_resource_response.GetManagedResourceResponse":
        """<p>Get information about a resource that's been registered for zonal shifts with Amazon Application Recovery Controller in this Amazon Web Services Region. Resources that are registered for zonal shifts are managed resources in ARC. You can start zonal shifts and configure zonal autoshift for managed resources.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that Amazon Web Services shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html\">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html\">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html\">Application Load Balancer</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html\">Network Load Balancer</a> </p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_arc_zonal_shift.types.get_managed_resource_request.GetManagedResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_arc_zonal_shift.types.get_managed_resource_response.GetManagedResourceResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.get_managed_resource

            (
                output,
                http_response,
            ) = await aws_sdk_arc_zonal_shift._operations.perc_data_plane.get_managed_resource.async_get_managed_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_arc_zonal_shift.types.get_managed_resource_request.GetManagedResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_arc_zonal_shift.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.list_managed_resources_response.ListManagedResourcesResponse":
        """<p>Lists all the resources in your Amazon Web Services account in this Amazon Web Services Region that are managed for zonal shifts in Amazon Application Recovery Controller, and information about them. The information includes the zonal autoshift status for the resource, as well as the Amazon Resource Name (ARN), the Availability Zones that each resource is deployed in, and the resource name.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_arc_zonal_shift.types.list_managed_resources_request.ListManagedResourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_arc_zonal_shift.types.list_managed_resources_response.ListManagedResourcesResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.list_managed_resources

            (
                output,
                http_response,
            ) = await aws_sdk_arc_zonal_shift._operations.perc_data_plane.list_managed_resources.async_list_managed_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_arc_zonal_shift.types.list_managed_resources_request.ListManagedResourcesRequest = {}  # type: ignore[typeddict-item]
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

    async def update_zonal_autoshift_configuration(
        self,
        resource_identifier: "aws_sdk_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        zonal_autoshift_status: "aws_sdk_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.update_zonal_autoshift_configuration_response.UpdateZonalAutoshiftConfigurationResponse":
        """<p>The zonal autoshift configuration for a resource includes the practice run configuration and the status for running autoshifts, zonal autoshift status. When a resource has a practice run configuration, ARC starts weekly zonal shifts for the resource, to shift traffic away from an Availability Zone. Weekly practice runs help you to make sure that your application can continue to operate normally with the loss of one Availability Zone.</p> <p>You can update the zonal autoshift status to enable or disable zonal autoshift. When zonal autoshift is <code>ENABLED</code>, you authorize Amazon Web Services to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that you want to update the zonal autoshift configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>
            zonal_autoshift_status: <p>The zonal autoshift status for the resource that you want to update the zonal autoshift configuration for. Choose <code>ENABLED</code> to authorize Amazon Web Services to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_arc_zonal_shift.types.update_zonal_autoshift_configuration_request.UpdateZonalAutoshiftConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_arc_zonal_shift.types.update_zonal_autoshift_configuration_response.UpdateZonalAutoshiftConfigurationResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_zonal_autoshift_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_zonal_autoshift_configuration.async_update_zonal_autoshift_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_arc_zonal_shift.types.update_zonal_autoshift_configuration_request.UpdateZonalAutoshiftConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["resource_identifier"] = resource_identifier
        input["zonal_autoshift_status"] = zonal_autoshift_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
