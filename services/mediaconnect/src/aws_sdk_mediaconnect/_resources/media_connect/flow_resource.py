from typing import TYPE_CHECKING, Optional

import aws_sdk_mediaconnect._auth._signers
import aws_sdk_mediaconnect._auth._sigv4
from aws_sdk_mediaconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_add_media_stream_request
    import aws_sdk_mediaconnect.types.__list_of_add_output_request
    import aws_sdk_mediaconnect.types.__list_of_grant_entitlement_request
    import aws_sdk_mediaconnect.types.__list_of_media_stream_output_configuration_request
    import aws_sdk_mediaconnect.types.__list_of_media_stream_source_configuration_request
    import aws_sdk_mediaconnect.types.__list_of_set_source_request
    import aws_sdk_mediaconnect.types.__list_of_string
    import aws_sdk_mediaconnect.types.__list_of_vpc_interface_request
    import aws_sdk_mediaconnect.types.__map_of_string
    import aws_sdk_mediaconnect.types.add_flow_media_streams_request
    import aws_sdk_mediaconnect.types.add_flow_media_streams_response
    import aws_sdk_mediaconnect.types.add_flow_outputs_request
    import aws_sdk_mediaconnect.types.add_flow_outputs_response
    import aws_sdk_mediaconnect.types.add_flow_sources_request
    import aws_sdk_mediaconnect.types.add_flow_sources_response
    import aws_sdk_mediaconnect.types.add_flow_vpc_interfaces_request
    import aws_sdk_mediaconnect.types.add_flow_vpc_interfaces_response
    import aws_sdk_mediaconnect.types.add_maintenance
    import aws_sdk_mediaconnect.types.create_flow_request
    import aws_sdk_mediaconnect.types.create_flow_response
    import aws_sdk_mediaconnect.types.delete_flow_request
    import aws_sdk_mediaconnect.types.delete_flow_response
    import aws_sdk_mediaconnect.types.describe_flow_request
    import aws_sdk_mediaconnect.types.describe_flow_response
    import aws_sdk_mediaconnect.types.describe_flow_source_metadata_request
    import aws_sdk_mediaconnect.types.describe_flow_source_metadata_response
    import aws_sdk_mediaconnect.types.describe_flow_source_thumbnail_request
    import aws_sdk_mediaconnect.types.describe_flow_source_thumbnail_response
    import aws_sdk_mediaconnect.types.encoding_config
    import aws_sdk_mediaconnect.types.entitlement_status
    import aws_sdk_mediaconnect.types.failover_config
    import aws_sdk_mediaconnect.types.flow_arn
    import aws_sdk_mediaconnect.types.flow_size
    import aws_sdk_mediaconnect.types.flow_transit_encryption
    import aws_sdk_mediaconnect.types.grant_flow_entitlements_request
    import aws_sdk_mediaconnect.types.grant_flow_entitlements_response
    import aws_sdk_mediaconnect.types.list_flows_request
    import aws_sdk_mediaconnect.types.list_flows_response
    import aws_sdk_mediaconnect.types.listed_flow
    import aws_sdk_mediaconnect.types.max_results
    import aws_sdk_mediaconnect.types.media_stream_attributes_request
    import aws_sdk_mediaconnect.types.media_stream_type
    import aws_sdk_mediaconnect.types.monitoring_config
    import aws_sdk_mediaconnect.types.ndi_config
    import aws_sdk_mediaconnect.types.ndi_output_timecode_source
    import aws_sdk_mediaconnect.types.ndi_source_settings
    import aws_sdk_mediaconnect.types.output_status
    import aws_sdk_mediaconnect.types.protocol
    import aws_sdk_mediaconnect.types.remove_flow_media_stream_request
    import aws_sdk_mediaconnect.types.remove_flow_media_stream_response
    import aws_sdk_mediaconnect.types.remove_flow_output_request
    import aws_sdk_mediaconnect.types.remove_flow_output_response
    import aws_sdk_mediaconnect.types.remove_flow_source_request
    import aws_sdk_mediaconnect.types.remove_flow_source_response
    import aws_sdk_mediaconnect.types.remove_flow_vpc_interface_request
    import aws_sdk_mediaconnect.types.remove_flow_vpc_interface_response
    import aws_sdk_mediaconnect.types.revoke_flow_entitlement_request
    import aws_sdk_mediaconnect.types.revoke_flow_entitlement_response
    import aws_sdk_mediaconnect.types.set_source_request
    import aws_sdk_mediaconnect.types.start_flow_request
    import aws_sdk_mediaconnect.types.start_flow_response
    import aws_sdk_mediaconnect.types.state
    import aws_sdk_mediaconnect.types.stop_flow_request
    import aws_sdk_mediaconnect.types.stop_flow_response
    import aws_sdk_mediaconnect.types.update_encryption
    import aws_sdk_mediaconnect.types.update_failover_config
    import aws_sdk_mediaconnect.types.update_flow_entitlement_request
    import aws_sdk_mediaconnect.types.update_flow_entitlement_response
    import aws_sdk_mediaconnect.types.update_flow_media_stream_request
    import aws_sdk_mediaconnect.types.update_flow_media_stream_response
    import aws_sdk_mediaconnect.types.update_flow_output_request
    import aws_sdk_mediaconnect.types.update_flow_output_response
    import aws_sdk_mediaconnect.types.update_flow_request
    import aws_sdk_mediaconnect.types.update_flow_response
    import aws_sdk_mediaconnect.types.update_flow_source_request
    import aws_sdk_mediaconnect.types.update_flow_source_response
    import aws_sdk_mediaconnect.types.update_gateway_bridge_source_request
    import aws_sdk_mediaconnect.types.update_maintenance
    import aws_sdk_mediaconnect.types.vpc_interface_attachment
    from aws_sdk_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from aws_sdk_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class FlowResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        availability_zone: Optional[str] = None,
        entitlements: Optional[
            "aws_sdk_mediaconnect.types.__list_of_grant_entitlement_request.__listOfGrantEntitlementRequest"
        ] = None,
        media_streams: Optional[
            "aws_sdk_mediaconnect.types.__list_of_add_media_stream_request.__listOfAddMediaStreamRequest"
        ] = None,
        outputs: Optional[
            "aws_sdk_mediaconnect.types.__list_of_add_output_request.__listOfAddOutputRequest"
        ] = None,
        source: Optional[
            "aws_sdk_mediaconnect.types.set_source_request.SetSourceRequest"
        ] = None,
        source_failover_config: Optional[
            "aws_sdk_mediaconnect.types.failover_config.FailoverConfig"
        ] = None,
        sources: Optional[
            "aws_sdk_mediaconnect.types.__list_of_set_source_request.__listOfSetSourceRequest"
        ] = None,
        vpc_interfaces: Optional[
            "aws_sdk_mediaconnect.types.__list_of_vpc_interface_request.__listOfVpcInterfaceRequest"
        ] = None,
        maintenance: Optional[
            "aws_sdk_mediaconnect.types.add_maintenance.AddMaintenance"
        ] = None,
        source_monitoring_config: Optional[
            "aws_sdk_mediaconnect.types.monitoring_config.MonitoringConfig"
        ] = None,
        flow_size: Optional["aws_sdk_mediaconnect.types.flow_size.FlowSize"] = None,
        ndi_config: Optional["aws_sdk_mediaconnect.types.ndi_config.NdiConfig"] = None,
        encoding_config: Optional[
            "aws_sdk_mediaconnect.types.encoding_config.EncodingConfig"
        ] = None,
        flow_tags: Optional[
            "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.create_flow_response.CreateFlowResponse":
        """<p> Creates a new flow. The request must include one source. The request optionally can include outputs (up to 50) and entitlements (up to 50).</p>

        Args:
            availability_zone: <p> The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current Amazon Web Services Region.</p>
            entitlements: <p> The entitlements that you want to grant on a flow.</p>
            media_streams: <p> The media streams that you want to add to the flow. You can associate these media streams with sources and outputs on the flow.</p>
            name: <p> The name of the flow.</p>
            outputs: <p> The outputs that you want to add to this flow.</p>
            source: <p> The settings for the source that you want to use for the new flow. </p>
            source_failover_config: <p> The settings for source failover. </p>
            sources: <p>The sources that are assigned to the flow. </p>
            vpc_interfaces: <p> The VPC interfaces you want on the flow.</p>
            maintenance: <p> The maintenance settings you want to use for the flow. </p>
            source_monitoring_config: <p> The settings for source monitoring. </p>
            flow_size: <p> Determines the processing capacity and feature set of the flow. Set this optional parameter to <code>LARGE</code> if you want to enable NDI sources or outputs on the flow. </p>
            ndi_config: <p> Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output. </p>
            flow_tags: <p> The key-value pairs that can be used to tag and organize the flow. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.create_flow_request.CreateFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.create_flow_response.CreateFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.create_flow

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.create_flow.create_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.create_flow_request.CreateFlowRequest = {}  # type: ignore[typeddict-item]
        if availability_zone is not None:
            input["availability_zone"] = availability_zone
        if entitlements is not None:
            input["entitlements"] = entitlements
        if media_streams is not None:
            input["media_streams"] = media_streams
        input["name"] = name
        if outputs is not None:
            input["outputs"] = outputs
        if source is not None:
            input["source"] = source
        if source_failover_config is not None:
            input["source_failover_config"] = source_failover_config
        if sources is not None:
            input["sources"] = sources
        if vpc_interfaces is not None:
            input["vpc_interfaces"] = vpc_interfaces
        if maintenance is not None:
            input["maintenance"] = maintenance
        if source_monitoring_config is not None:
            input["source_monitoring_config"] = source_monitoring_config
        if flow_size is not None:
            input["flow_size"] = flow_size
        if ndi_config is not None:
            input["ndi_config"] = ndi_config
        if encoding_config is not None:
            input["encoding_config"] = encoding_config
        if flow_tags is not None:
            input["flow_tags"] = flow_tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.describe_flow_response.DescribeFlowResponse":
        """<p> Displays the details of a flow. The response includes the flow Amazon Resource Name (ARN), name, and Availability Zone, as well as details about the source, outputs, and entitlements.</p>

        Args:
            flow_arn: <p> The ARN of the flow that you want to describe.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.describe_flow_request.DescribeFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.describe_flow_response.DescribeFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_flow

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.describe_flow.describe_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.describe_flow_request.DescribeFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        source_failover_config: Optional[
            "aws_sdk_mediaconnect.types.update_failover_config.UpdateFailoverConfig"
        ] = None,
        maintenance: Optional[
            "aws_sdk_mediaconnect.types.update_maintenance.UpdateMaintenance"
        ] = None,
        source_monitoring_config: Optional[
            "aws_sdk_mediaconnect.types.monitoring_config.MonitoringConfig"
        ] = None,
        ndi_config: Optional["aws_sdk_mediaconnect.types.ndi_config.NdiConfig"] = None,
        flow_size: Optional["aws_sdk_mediaconnect.types.flow_size.FlowSize"] = None,
        encoding_config: Optional[
            "aws_sdk_mediaconnect.types.encoding_config.EncodingConfig"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_flow_response.UpdateFlowResponse":
        """<p> Updates an existing flow.</p> <note> <p> Because <code>UpdateFlowSources</code> and <code>UpdateFlow</code> are separate operations, you can't change both the source type AND the flow size in a single request. </p> <ul> <li> <p>If you have a <code>MEDIUM</code> flow and you want to change the flow source to NDI®:</p> <ul> <li> <p>First, use the <code>UpdateFlow</code> operation to upgrade the flow size to <code>LARGE</code>. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlowSource</code> operation to configure the NDI source. </p> </li> </ul> </li> <li> <p>If you're switching from an NDI source to a transport stream (TS) source and want to downgrade the flow size: </p> <ul> <li> <p>First, use the <code>UpdateFlowSource</code> operation to change the flow source type. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlow</code> operation to downgrade the flow size to <code>MEDIUM</code>.</p> </li> </ul> </li> </ul> </note>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            source_failover_config: <p> The settings for source failover. </p>
            maintenance: <p> The maintenance setting of the flow. </p>
            source_monitoring_config: <p> The settings for source monitoring. </p>
            ndi_config: <p> Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output. </p>
            flow_size: <p> Determines the processing capacity and feature set of the flow. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.update_flow_request.UpdateFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.update_flow_response.UpdateFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_flow

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.update_flow.update_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_flow_request.UpdateFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        if source_failover_config is not None:
            input["source_failover_config"] = source_failover_config
        if maintenance is not None:
            input["maintenance"] = maintenance
        if source_monitoring_config is not None:
            input["source_monitoring_config"] = source_monitoring_config
        if ndi_config is not None:
            input["ndi_config"] = ndi_config
        if flow_size is not None:
            input["flow_size"] = flow_size
        if encoding_config is not None:
            input["encoding_config"] = encoding_config

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.delete_flow_response.DeleteFlowResponse":
        """<p> Deletes a flow. Before you can delete a flow, you must stop the flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.delete_flow_request.DeleteFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.delete_flow_response.DeleteFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.delete_flow

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.delete_flow.delete_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.delete_flow_request.DeleteFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediaconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.list_flows_response.ListFlowsResponse":
        """<p> Displays a list of flows that are associated with this account. This request returns a paginated result.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListFlows</code> request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListFlows</code> request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListFlows</code> request a second time and specify the <code>NextToken</code> value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.list_flows_request.ListFlowsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.list_flows_response.ListFlowsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_flows

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.list_flows.list_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.list_flows_request.ListFlowsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def add_flow_media_streams(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        media_streams: "aws_sdk_mediaconnect.types.__list_of_add_media_stream_request.__listOfAddMediaStreamRequest",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.add_flow_media_streams_response.AddFlowMediaStreamsResponse":
        """<p> Adds media streams to an existing flow. After you add a media stream to a flow, you can associate it with a source and/or an output that uses the ST 2110 JPEG XS or CDI protocol.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow.</p>
            media_streams: <p> The media streams that you want to add to the flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.add_flow_media_streams_request.AddFlowMediaStreamsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.add_flow_media_streams_response.AddFlowMediaStreamsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.add_flow_media_streams

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.add_flow_media_streams.add_flow_media_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.add_flow_media_streams_request.AddFlowMediaStreamsRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["media_streams"] = media_streams

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def add_flow_outputs(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        outputs: "aws_sdk_mediaconnect.types.__list_of_add_output_request.__listOfAddOutputRequest",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.add_flow_outputs_response.AddFlowOutputsResponse":
        """<p> Adds outputs to an existing flow. You can create up to 50 outputs per flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to add outputs to.</p>
            outputs: <p> A list of outputs that you want to add to the flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.add_flow_outputs_request.AddFlowOutputsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.add_flow_outputs_response.AddFlowOutputsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.add_flow_outputs

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.add_flow_outputs.add_flow_outputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.add_flow_outputs_request.AddFlowOutputsRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["outputs"] = outputs

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def add_flow_sources(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        sources: "aws_sdk_mediaconnect.types.__list_of_set_source_request.__listOfSetSourceRequest",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.add_flow_sources_response.AddFlowSourcesResponse":
        """<p> Adds sources to a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            sources: <p> A list of sources that you want to add to the flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.add_flow_sources_request.AddFlowSourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.add_flow_sources_response.AddFlowSourcesResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.add_flow_sources

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.add_flow_sources.add_flow_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.add_flow_sources_request.AddFlowSourcesRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def add_flow_vpc_interfaces(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        vpc_interfaces: "aws_sdk_mediaconnect.types.__list_of_vpc_interface_request.__listOfVpcInterfaceRequest",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.add_flow_vpc_interfaces_response.AddFlowVpcInterfacesResponse":
        """<p> Adds VPC interfaces to a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            vpc_interfaces: <p> A list of VPC interfaces that you want to add to the flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.add_flow_vpc_interfaces_request.AddFlowVpcInterfacesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.add_flow_vpc_interfaces_response.AddFlowVpcInterfacesResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.add_flow_vpc_interfaces

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.add_flow_vpc_interfaces.add_flow_vpc_interfaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.add_flow_vpc_interfaces_request.AddFlowVpcInterfacesRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["vpc_interfaces"] = vpc_interfaces

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_flow_source_metadata(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.describe_flow_source_metadata_response.DescribeFlowSourceMetadataResponse":
        """<p> The <code>DescribeFlowSourceMetadata</code> API is used to view information about the flow's source transport stream and programs. This API displays status messages about the flow's source as well as details about the program's video, audio, and other data. </p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.describe_flow_source_metadata_request.DescribeFlowSourceMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.describe_flow_source_metadata_response.DescribeFlowSourceMetadataResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_flow_source_metadata

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.describe_flow_source_metadata.describe_flow_source_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.describe_flow_source_metadata_request.DescribeFlowSourceMetadataRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_flow_source_thumbnail(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.describe_flow_source_thumbnail_response.DescribeFlowSourceThumbnailResponse":
        """<p> Describes the thumbnail for the flow source. </p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.describe_flow_source_thumbnail_request.DescribeFlowSourceThumbnailRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.describe_flow_source_thumbnail_response.DescribeFlowSourceThumbnailResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_flow_source_thumbnail

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.describe_flow_source_thumbnail.describe_flow_source_thumbnail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.describe_flow_source_thumbnail_request.DescribeFlowSourceThumbnailRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def grant_flow_entitlements(
        self,
        entitlements: "aws_sdk_mediaconnect.types.__list_of_grant_entitlement_request.__listOfGrantEntitlementRequest",
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.grant_flow_entitlements_response.GrantFlowEntitlementsResponse":
        """<p> Grants entitlements to an existing flow.</p>

        Args:
            entitlements: <p> The list of entitlements that you want to grant.</p>
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to grant entitlements on.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.grant_flow_entitlements_request.GrantFlowEntitlementsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.grant_flow_entitlements_response.GrantFlowEntitlementsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.grant_flow_entitlements

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.grant_flow_entitlements.grant_flow_entitlements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.grant_flow_entitlements_request.GrantFlowEntitlementsRequest = {}  # type: ignore[typeddict-item]
        input["entitlements"] = entitlements
        input["flow_arn"] = flow_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_flow_media_stream(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        media_stream_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.remove_flow_media_stream_response.RemoveFlowMediaStreamResponse":
        """<p> Removes a media stream from a flow. This action is only available if the media stream is not associated with a source or output.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            media_stream_name: <p> The name of the media stream that you want to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.remove_flow_media_stream_request.RemoveFlowMediaStreamRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.remove_flow_media_stream_response.RemoveFlowMediaStreamResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.remove_flow_media_stream

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.remove_flow_media_stream.remove_flow_media_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.remove_flow_media_stream_request.RemoveFlowMediaStreamRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["media_stream_name"] = media_stream_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_flow_output(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        output_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.remove_flow_output_response.RemoveFlowOutputResponse":
        """<p> Removes an output from an existing flow. This request can be made only on an output that does not have an entitlement associated with it. If the output has an entitlement, you must revoke the entitlement instead. When an entitlement is revoked from a flow, the service automatically removes the associated output.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to remove an output from.</p>
            output_arn: <p> The ARN of the output that you want to remove. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.remove_flow_output_request.RemoveFlowOutputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.remove_flow_output_response.RemoveFlowOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.remove_flow_output

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.remove_flow_output.remove_flow_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.remove_flow_output_request.RemoveFlowOutputRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["output_arn"] = output_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_flow_source(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        source_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.remove_flow_source_response.RemoveFlowSourceResponse":
        """<p> Removes a source from an existing flow. This request can be made only if there is more than one source on the flow. </p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to remove a source from.</p>
            source_arn: <p> The ARN of the source that you want to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.remove_flow_source_request.RemoveFlowSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.remove_flow_source_response.RemoveFlowSourceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.remove_flow_source

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.remove_flow_source.remove_flow_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.remove_flow_source_request.RemoveFlowSourceRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["source_arn"] = source_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_flow_vpc_interface(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        vpc_interface_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.remove_flow_vpc_interface_response.RemoveFlowVpcInterfaceResponse":
        """<p> Removes a VPC Interface from an existing flow. This request can be made only on a VPC interface that does not have a Source or Output associated with it. If the VPC interface is referenced by a Source or Output, you must first delete or update the Source or Output to no longer reference the VPC interface.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to remove a VPC interface from.</p>
            vpc_interface_name: <p> The name of the VPC interface that you want to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.remove_flow_vpc_interface_request.RemoveFlowVpcInterfaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.remove_flow_vpc_interface_response.RemoveFlowVpcInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.remove_flow_vpc_interface

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.remove_flow_vpc_interface.remove_flow_vpc_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.remove_flow_vpc_interface_request.RemoveFlowVpcInterfaceRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["vpc_interface_name"] = vpc_interface_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def revoke_flow_entitlement(
        self,
        entitlement_arn: str,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.revoke_flow_entitlement_response.RevokeFlowEntitlementResponse":
        """<p> Revokes an entitlement from a flow. Once an entitlement is revoked, the content becomes unavailable to the subscriber and the associated output is removed.</p>

        Args:
            entitlement_arn: <p> The Amazon Resource Name (ARN) of the entitlement that you want to revoke.</p>
            flow_arn: <p> The flow that you want to revoke an entitlement from.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.revoke_flow_entitlement_request.RevokeFlowEntitlementRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.revoke_flow_entitlement_response.RevokeFlowEntitlementResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.revoke_flow_entitlement

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.revoke_flow_entitlement.revoke_flow_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.revoke_flow_entitlement_request.RevokeFlowEntitlementRequest = {}  # type: ignore[typeddict-item]
        input["entitlement_arn"] = entitlement_arn
        input["flow_arn"] = flow_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_flow(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.start_flow_response.StartFlowResponse":
        """<p> Starts a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to start.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.start_flow_request.StartFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.start_flow_response.StartFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.start_flow

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.start_flow.start_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.start_flow_request.StartFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_flow(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.stop_flow_response.StopFlowResponse":
        """<p> Stops a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.stop_flow_request.StopFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.stop_flow_response.StopFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.stop_flow

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.stop_flow.stop_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.stop_flow_request.StopFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_flow_entitlement(
        self,
        entitlement_arn: str,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        description: Optional[str] = None,
        encryption: Optional[
            "aws_sdk_mediaconnect.types.update_encryption.UpdateEncryption"
        ] = None,
        entitlement_status: Optional[
            "aws_sdk_mediaconnect.types.entitlement_status.EntitlementStatus"
        ] = None,
        subscribers: Optional[
            "aws_sdk_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_flow_entitlement_response.UpdateFlowEntitlementResponse":
        """<p> Updates an entitlement. You can change an entitlement's description, subscribers, and encryption. If you change the subscribers, the service will remove the outputs that are are used by the subscribers that are removed.</p>

        Args:
            description: <p> A description of the entitlement. This description appears only on the MediaConnect console and will not be seen by the subscriber or end user.</p>
            encryption: <p> The type of encryption that will be used on the output associated with this entitlement. Allowable encryption types: static-key, speke.</p>
            entitlement_arn: <p> The Amazon Resource Name (ARN) of the entitlement that you want to update.</p>
            entitlement_status: <p> An indication of whether you want to enable the entitlement to allow access, or disable it to stop streaming content to the subscriber’s flow temporarily. If you don’t specify the <code>entitlementStatus</code> field in your request, MediaConnect leaves the value unchanged.</p>
            flow_arn: <p> The ARN of the flow that is associated with the entitlement that you want to update.</p>
            subscribers: <p> The Amazon Web Services account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.update_flow_entitlement_request.UpdateFlowEntitlementRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.update_flow_entitlement_response.UpdateFlowEntitlementResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_flow_entitlement

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.update_flow_entitlement.update_flow_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_flow_entitlement_request.UpdateFlowEntitlementRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input["description"] = description
        if encryption is not None:
            input["encryption"] = encryption
        input["entitlement_arn"] = entitlement_arn
        if entitlement_status is not None:
            input["entitlement_status"] = entitlement_status
        input["flow_arn"] = flow_arn
        if subscribers is not None:
            input["subscribers"] = subscribers

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_flow_media_stream(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        media_stream_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        attributes: Optional[
            "aws_sdk_mediaconnect.types.media_stream_attributes_request.MediaStreamAttributesRequest"
        ] = None,
        clock_rate: Optional[int] = None,
        description: Optional[str] = None,
        media_stream_type: Optional[
            "aws_sdk_mediaconnect.types.media_stream_type.MediaStreamType"
        ] = None,
        video_format: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.update_flow_media_stream_response.UpdateFlowMediaStreamResponse":
        """<p> Updates an existing media stream.</p>

        Args:
            attributes: <p> The attributes that you want to assign to the media stream.</p>
            clock_rate: <p>The sample rate for the stream. This value in measured in kHz. </p>
            description: <p>A description that can help you quickly identify what your media stream is used for. </p>
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that is associated with the media stream that you updated.</p>
            media_stream_name: <p> The media stream that you updated.</p>
            media_stream_type: <p>The type of media stream. </p>
            video_format: <p>The resolution of the video. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.update_flow_media_stream_request.UpdateFlowMediaStreamRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.update_flow_media_stream_response.UpdateFlowMediaStreamResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_flow_media_stream

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.update_flow_media_stream.update_flow_media_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_flow_media_stream_request.UpdateFlowMediaStreamRequest = {}  # type: ignore[typeddict-item]
        if attributes is not None:
            input["attributes"] = attributes
        if clock_rate is not None:
            input["clock_rate"] = clock_rate
        if description is not None:
            input["description"] = description
        input["flow_arn"] = flow_arn
        input["media_stream_name"] = media_stream_name
        if media_stream_type is not None:
            input["media_stream_type"] = media_stream_type
        if video_format is not None:
            input["video_format"] = video_format

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_flow_output(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        output_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        cidr_allow_list: Optional[
            "aws_sdk_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
        description: Optional[str] = None,
        destination: Optional[str] = None,
        encryption: Optional[
            "aws_sdk_mediaconnect.types.update_encryption.UpdateEncryption"
        ] = None,
        max_latency: Optional[int] = None,
        media_stream_output_configurations: Optional[
            "aws_sdk_mediaconnect.types.__list_of_media_stream_output_configuration_request.__listOfMediaStreamOutputConfigurationRequest"
        ] = None,
        min_latency: Optional[int] = None,
        port: Optional[int] = None,
        protocol: Optional["aws_sdk_mediaconnect.types.protocol.Protocol"] = None,
        remote_id: Optional[str] = None,
        sender_control_port: Optional[int] = None,
        sender_ip_address: Optional[str] = None,
        smoothing_latency: Optional[int] = None,
        stream_id: Optional[str] = None,
        vpc_interface_attachment: Optional[
            "aws_sdk_mediaconnect.types.vpc_interface_attachment.VpcInterfaceAttachment"
        ] = None,
        output_status: Optional[
            "aws_sdk_mediaconnect.types.output_status.OutputStatus"
        ] = None,
        ndi_program_name: Optional[str] = None,
        ndi_speed_hq_quality: Optional[int] = None,
        router_integration_state: Optional[
            "aws_sdk_mediaconnect.types.state.State"
        ] = None,
        router_integration_transit_encryption: Optional[
            "aws_sdk_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
        ] = None,
        ndi_output_timecode_source: Optional[
            "aws_sdk_mediaconnect.types.ndi_output_timecode_source.NdiOutputTimecodeSource"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_flow_output_response.UpdateFlowOutputResponse":
        """<p> Updates an existing flow output.</p>

        Args:
            cidr_allow_list: <p> The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>
            description: <p> A description of the output. This description appears only on the MediaConnect console and will not be seen by the end user.</p>
            destination: <p> The IP address where you want to send the output.</p>
            encryption: <p> The type of key used for the encryption. If no <code>keyType</code> is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.</p>
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that is associated with the output that you want to update.</p>
            max_latency: <p> The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.</p>
            media_stream_output_configurations: <p> The media streams that are associated with the output, and the parameters for those associations.</p>
            min_latency: <p> The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.</p>
            output_arn: <p> The ARN of the output that you want to update.</p>
            port: <p> The port to use when content is distributed to this output.</p>
            protocol: <p> The protocol to use for the output.</p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>
            remote_id: <p> The remote ID for the Zixi-pull stream.</p>
            sender_control_port: <p> The port that the flow uses to send outbound requests to initiate connection with the sender.</p>
            sender_ip_address: <p> The IP address that the flow communicates with to initiate connection with the sender.</p>
            smoothing_latency: <p> The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.</p>
            stream_id: <p> The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.</p>
            vpc_interface_attachment: <p> The name of the VPC interface attachment to use for this output.</p>
            output_status: <p> An indication of whether the output should transmit data or not. If you don't specify the <code>outputStatus</code> field in your request, MediaConnect leaves the value unchanged.</p>
            ndi_program_name: <p> A suffix for the name of the NDI® sender that the flow creates. If a custom name isn't specified, MediaConnect uses the output name. </p>
            ndi_speed_hq_quality: <p>A quality setting for the NDI Speed HQ encoder. </p>
            router_integration_state: <p>Indicates whether to enable or disable router integration for this flow output.</p>
            ndi_output_timecode_source: <p>Controls how MediaConnect generates timecodes for NDI output frames. If you don't specify this field, MediaConnect leaves the value unchanged.</p> <ul> <li> <p> <code>EMBEDDED_TIMECODE</code> - Preserves timecodes from the input transport stream. The timecodes must be embedded in the video stream as SEI timing messages. If no embedded timecode is detected, MediaConnect uses the UTC system time instead.</p> </li> <li> <p> <code>UTC_SYSTEM_TIME</code> - Generates timecodes based on the system clock time when each frame is sent.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.update_flow_output_request.UpdateFlowOutputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.update_flow_output_response.UpdateFlowOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_flow_output

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.update_flow_output.update_flow_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_flow_output_request.UpdateFlowOutputRequest = {}  # type: ignore[typeddict-item]
        if cidr_allow_list is not None:
            input["cidr_allow_list"] = cidr_allow_list
        if description is not None:
            input["description"] = description
        if destination is not None:
            input["destination"] = destination
        if encryption is not None:
            input["encryption"] = encryption
        input["flow_arn"] = flow_arn
        if max_latency is not None:
            input["max_latency"] = max_latency
        if media_stream_output_configurations is not None:
            input["media_stream_output_configurations"] = (
                media_stream_output_configurations
            )
        if min_latency is not None:
            input["min_latency"] = min_latency
        input["output_arn"] = output_arn
        if port is not None:
            input["port"] = port
        if protocol is not None:
            input["protocol"] = protocol
        if remote_id is not None:
            input["remote_id"] = remote_id
        if sender_control_port is not None:
            input["sender_control_port"] = sender_control_port
        if sender_ip_address is not None:
            input["sender_ip_address"] = sender_ip_address
        if smoothing_latency is not None:
            input["smoothing_latency"] = smoothing_latency
        if stream_id is not None:
            input["stream_id"] = stream_id
        if vpc_interface_attachment is not None:
            input["vpc_interface_attachment"] = vpc_interface_attachment
        if output_status is not None:
            input["output_status"] = output_status
        if ndi_program_name is not None:
            input["ndi_program_name"] = ndi_program_name
        if ndi_speed_hq_quality is not None:
            input["ndi_speed_hq_quality"] = ndi_speed_hq_quality
        if router_integration_state is not None:
            input["router_integration_state"] = router_integration_state
        if router_integration_transit_encryption is not None:
            input["router_integration_transit_encryption"] = (
                router_integration_transit_encryption
            )
        if ndi_output_timecode_source is not None:
            input["ndi_output_timecode_source"] = ndi_output_timecode_source

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_flow_source(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        source_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        decryption: Optional[
            "aws_sdk_mediaconnect.types.update_encryption.UpdateEncryption"
        ] = None,
        description: Optional[str] = None,
        entitlement_arn: Optional[str] = None,
        ingest_port: Optional[int] = None,
        max_bitrate: Optional[int] = None,
        max_latency: Optional[int] = None,
        max_sync_buffer: Optional[int] = None,
        media_stream_source_configurations: Optional[
            "aws_sdk_mediaconnect.types.__list_of_media_stream_source_configuration_request.__listOfMediaStreamSourceConfigurationRequest"
        ] = None,
        min_latency: Optional[int] = None,
        protocol: Optional["aws_sdk_mediaconnect.types.protocol.Protocol"] = None,
        sender_control_port: Optional[int] = None,
        sender_ip_address: Optional[str] = None,
        source_listener_address: Optional[str] = None,
        source_listener_port: Optional[int] = None,
        stream_id: Optional[str] = None,
        vpc_interface_name: Optional[str] = None,
        whitelist_cidr: Optional[str] = None,
        gateway_bridge_source: Optional[
            "aws_sdk_mediaconnect.types.update_gateway_bridge_source_request.UpdateGatewayBridgeSourceRequest"
        ] = None,
        ndi_source_settings: Optional[
            "aws_sdk_mediaconnect.types.ndi_source_settings.NdiSourceSettings"
        ] = None,
        router_integration_state: Optional[
            "aws_sdk_mediaconnect.types.state.State"
        ] = None,
        router_integration_transit_decryption: Optional[
            "aws_sdk_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_flow_source_response.UpdateFlowSourceResponse":
        """<p> Updates the source of a flow.</p> <note> <p> Because <code>UpdateFlowSources</code> and <code>UpdateFlow</code> are separate operations, you can't change both the source type AND the flow size in a single request. </p> <ul> <li> <p>If you have a <code>MEDIUM</code> flow and you want to change the flow source to NDI®:</p> <ul> <li> <p>First, use the <code>UpdateFlow</code> operation to upgrade the flow size to <code>LARGE</code>. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlowSource</code> operation to configure the NDI source. </p> </li> </ul> </li> <li> <p>If you're switching from an NDI source to a transport stream (TS) source and want to downgrade the flow size: </p> <ul> <li> <p>First, use the <code>UpdateFlowSource</code> operation to change the flow source type. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlow</code> operation to downgrade the flow size to <code>MEDIUM</code>.</p> </li> </ul> </li> </ul> </note>

        Args:
            decryption: <p>The type of encryption that is used on the content ingested from the source. </p>
            description: <p>A description of the source. This description is not visible outside of the current Amazon Web Services account. </p>
            entitlement_arn: <p>The Amazon Resource Name (ARN) of the entitlement that allows you to subscribe to the flow. The entitlement is set by the content originator, and the ARN is generated as part of the originator's flow. </p>
            flow_arn: <p> The ARN of the flow that you want to update. </p>
            ingest_port: <p>The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088. </p>
            max_bitrate: <p>The maximum bitrate for RIST, RTP, and RTP-FEC streams. </p>
            max_latency: <p>The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams. </p>
            max_sync_buffer: <p>The size of the buffer (in milliseconds) to use to sync incoming source data. </p>
            media_stream_source_configurations: <p>The media stream that is associated with the source, and the parameters for that association. </p>
            min_latency: <p>The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency. </p>
            protocol: <p>The protocol that the source uses to deliver the content to MediaConnect. </p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>
            sender_control_port: <p>The port that the flow uses to send outbound requests to initiate connection with the sender. </p>
            sender_ip_address: <p>The IP address that the flow communicates with to initiate connection with the sender. </p>
            source_arn: <p>The ARN of the source that you want to update. </p>
            source_listener_address: <p>The source IP or domain name for SRT-caller protocol. </p>
            source_listener_port: <p>Source port for SRT-caller protocol. </p>
            stream_id: <p>The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams. </p>
            vpc_interface_name: <p>The name of the VPC interface that you want to send your output to.</p>
            whitelist_cidr: <p>The range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. </p>
            gateway_bridge_source: <p>The source configuration for cloud flows receiving a stream from a bridge. </p>
            ndi_source_settings: <p> The settings for the NDI source. This includes the exact name of the upstream NDI sender that you want to connect to your source. </p>
            router_integration_state: <p>Indicates whether to enable or disable router integration for this flow source.</p>
            router_integration_transit_decryption: <p>The encryption configuration for the flow source when router integration is enabled.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.update_flow_source_request.UpdateFlowSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.update_flow_source_response.UpdateFlowSourceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_flow_source

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.update_flow_source.update_flow_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_flow_source_request.UpdateFlowSourceRequest = {}  # type: ignore[typeddict-item]
        if decryption is not None:
            input["decryption"] = decryption
        if description is not None:
            input["description"] = description
        if entitlement_arn is not None:
            input["entitlement_arn"] = entitlement_arn
        input["flow_arn"] = flow_arn
        if ingest_port is not None:
            input["ingest_port"] = ingest_port
        if max_bitrate is not None:
            input["max_bitrate"] = max_bitrate
        if max_latency is not None:
            input["max_latency"] = max_latency
        if max_sync_buffer is not None:
            input["max_sync_buffer"] = max_sync_buffer
        if media_stream_source_configurations is not None:
            input["media_stream_source_configurations"] = (
                media_stream_source_configurations
            )
        if min_latency is not None:
            input["min_latency"] = min_latency
        if protocol is not None:
            input["protocol"] = protocol
        if sender_control_port is not None:
            input["sender_control_port"] = sender_control_port
        if sender_ip_address is not None:
            input["sender_ip_address"] = sender_ip_address
        input["source_arn"] = source_arn
        if source_listener_address is not None:
            input["source_listener_address"] = source_listener_address
        if source_listener_port is not None:
            input["source_listener_port"] = source_listener_port
        if stream_id is not None:
            input["stream_id"] = stream_id
        if vpc_interface_name is not None:
            input["vpc_interface_name"] = vpc_interface_name
        if whitelist_cidr is not None:
            input["whitelist_cidr"] = whitelist_cidr
        if gateway_bridge_source is not None:
            input["gateway_bridge_source"] = gateway_bridge_source
        if ndi_source_settings is not None:
            input["ndi_source_settings"] = ndi_source_settings
        if router_integration_state is not None:
            input["router_integration_state"] = router_integration_state
        if router_integration_transit_decryption is not None:
            input["router_integration_transit_decryption"] = (
                router_integration_transit_decryption
            )

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncFlowResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        availability_zone: Optional[str] = None,
        entitlements: Optional[
            "aws_sdk_mediaconnect.types.__list_of_grant_entitlement_request.__listOfGrantEntitlementRequest"
        ] = None,
        media_streams: Optional[
            "aws_sdk_mediaconnect.types.__list_of_add_media_stream_request.__listOfAddMediaStreamRequest"
        ] = None,
        outputs: Optional[
            "aws_sdk_mediaconnect.types.__list_of_add_output_request.__listOfAddOutputRequest"
        ] = None,
        source: Optional[
            "aws_sdk_mediaconnect.types.set_source_request.SetSourceRequest"
        ] = None,
        source_failover_config: Optional[
            "aws_sdk_mediaconnect.types.failover_config.FailoverConfig"
        ] = None,
        sources: Optional[
            "aws_sdk_mediaconnect.types.__list_of_set_source_request.__listOfSetSourceRequest"
        ] = None,
        vpc_interfaces: Optional[
            "aws_sdk_mediaconnect.types.__list_of_vpc_interface_request.__listOfVpcInterfaceRequest"
        ] = None,
        maintenance: Optional[
            "aws_sdk_mediaconnect.types.add_maintenance.AddMaintenance"
        ] = None,
        source_monitoring_config: Optional[
            "aws_sdk_mediaconnect.types.monitoring_config.MonitoringConfig"
        ] = None,
        flow_size: Optional["aws_sdk_mediaconnect.types.flow_size.FlowSize"] = None,
        ndi_config: Optional["aws_sdk_mediaconnect.types.ndi_config.NdiConfig"] = None,
        encoding_config: Optional[
            "aws_sdk_mediaconnect.types.encoding_config.EncodingConfig"
        ] = None,
        flow_tags: Optional[
            "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.create_flow_response.CreateFlowResponse":
        """<p> Creates a new flow. The request must include one source. The request optionally can include outputs (up to 50) and entitlements (up to 50).</p>

        Args:
            availability_zone: <p> The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current Amazon Web Services Region.</p>
            entitlements: <p> The entitlements that you want to grant on a flow.</p>
            media_streams: <p> The media streams that you want to add to the flow. You can associate these media streams with sources and outputs on the flow.</p>
            name: <p> The name of the flow.</p>
            outputs: <p> The outputs that you want to add to this flow.</p>
            source: <p> The settings for the source that you want to use for the new flow. </p>
            source_failover_config: <p> The settings for source failover. </p>
            sources: <p>The sources that are assigned to the flow. </p>
            vpc_interfaces: <p> The VPC interfaces you want on the flow.</p>
            maintenance: <p> The maintenance settings you want to use for the flow. </p>
            source_monitoring_config: <p> The settings for source monitoring. </p>
            flow_size: <p> Determines the processing capacity and feature set of the flow. Set this optional parameter to <code>LARGE</code> if you want to enable NDI sources or outputs on the flow. </p>
            ndi_config: <p> Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output. </p>
            flow_tags: <p> The key-value pairs that can be used to tag and organize the flow. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.create_flow_request.CreateFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.create_flow_response.CreateFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.create_flow

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.create_flow.async_create_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.create_flow_request.CreateFlowRequest = {}  # type: ignore[typeddict-item]
        if availability_zone is not None:
            input["availability_zone"] = availability_zone
        if entitlements is not None:
            input["entitlements"] = entitlements
        if media_streams is not None:
            input["media_streams"] = media_streams
        input["name"] = name
        if outputs is not None:
            input["outputs"] = outputs
        if source is not None:
            input["source"] = source
        if source_failover_config is not None:
            input["source_failover_config"] = source_failover_config
        if sources is not None:
            input["sources"] = sources
        if vpc_interfaces is not None:
            input["vpc_interfaces"] = vpc_interfaces
        if maintenance is not None:
            input["maintenance"] = maintenance
        if source_monitoring_config is not None:
            input["source_monitoring_config"] = source_monitoring_config
        if flow_size is not None:
            input["flow_size"] = flow_size
        if ndi_config is not None:
            input["ndi_config"] = ndi_config
        if encoding_config is not None:
            input["encoding_config"] = encoding_config
        if flow_tags is not None:
            input["flow_tags"] = flow_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.describe_flow_response.DescribeFlowResponse":
        """<p> Displays the details of a flow. The response includes the flow Amazon Resource Name (ARN), name, and Availability Zone, as well as details about the source, outputs, and entitlements.</p>

        Args:
            flow_arn: <p> The ARN of the flow that you want to describe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.describe_flow_request.DescribeFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.describe_flow_response.DescribeFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_flow

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.describe_flow.async_describe_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.describe_flow_request.DescribeFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        source_failover_config: Optional[
            "aws_sdk_mediaconnect.types.update_failover_config.UpdateFailoverConfig"
        ] = None,
        maintenance: Optional[
            "aws_sdk_mediaconnect.types.update_maintenance.UpdateMaintenance"
        ] = None,
        source_monitoring_config: Optional[
            "aws_sdk_mediaconnect.types.monitoring_config.MonitoringConfig"
        ] = None,
        ndi_config: Optional["aws_sdk_mediaconnect.types.ndi_config.NdiConfig"] = None,
        flow_size: Optional["aws_sdk_mediaconnect.types.flow_size.FlowSize"] = None,
        encoding_config: Optional[
            "aws_sdk_mediaconnect.types.encoding_config.EncodingConfig"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_flow_response.UpdateFlowResponse":
        """<p> Updates an existing flow.</p> <note> <p> Because <code>UpdateFlowSources</code> and <code>UpdateFlow</code> are separate operations, you can't change both the source type AND the flow size in a single request. </p> <ul> <li> <p>If you have a <code>MEDIUM</code> flow and you want to change the flow source to NDI®:</p> <ul> <li> <p>First, use the <code>UpdateFlow</code> operation to upgrade the flow size to <code>LARGE</code>. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlowSource</code> operation to configure the NDI source. </p> </li> </ul> </li> <li> <p>If you're switching from an NDI source to a transport stream (TS) source and want to downgrade the flow size: </p> <ul> <li> <p>First, use the <code>UpdateFlowSource</code> operation to change the flow source type. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlow</code> operation to downgrade the flow size to <code>MEDIUM</code>.</p> </li> </ul> </li> </ul> </note>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            source_failover_config: <p> The settings for source failover. </p>
            maintenance: <p> The maintenance setting of the flow. </p>
            source_monitoring_config: <p> The settings for source monitoring. </p>
            ndi_config: <p> Specifies the configuration settings for a flow's NDI source or output. Required when the flow includes an NDI source or output. </p>
            flow_size: <p> Determines the processing capacity and feature set of the flow. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.update_flow_request.UpdateFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.update_flow_response.UpdateFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_flow

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.update_flow.async_update_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_flow_request.UpdateFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        if source_failover_config is not None:
            input["source_failover_config"] = source_failover_config
        if maintenance is not None:
            input["maintenance"] = maintenance
        if source_monitoring_config is not None:
            input["source_monitoring_config"] = source_monitoring_config
        if ndi_config is not None:
            input["ndi_config"] = ndi_config
        if flow_size is not None:
            input["flow_size"] = flow_size
        if encoding_config is not None:
            input["encoding_config"] = encoding_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.delete_flow_response.DeleteFlowResponse":
        """<p> Deletes a flow. Before you can delete a flow, you must stop the flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.delete_flow_request.DeleteFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.delete_flow_response.DeleteFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.delete_flow

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.delete_flow.async_delete_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.delete_flow_request.DeleteFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediaconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.list_flows_response.ListFlowsResponse":
        """<p> Displays a list of flows that are associated with this account. This request returns a paginated result.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListFlows</code> request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListFlows</code> request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListFlows</code> request a second time and specify the <code>NextToken</code> value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.list_flows_request.ListFlowsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.list_flows_response.ListFlowsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_flows

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.list_flows.async_list_flows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.list_flows_request.ListFlowsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_flow_media_streams(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        media_streams: "aws_sdk_mediaconnect.types.__list_of_add_media_stream_request.__listOfAddMediaStreamRequest",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.add_flow_media_streams_response.AddFlowMediaStreamsResponse":
        """<p> Adds media streams to an existing flow. After you add a media stream to a flow, you can associate it with a source and/or an output that uses the ST 2110 JPEG XS or CDI protocol.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow.</p>
            media_streams: <p> The media streams that you want to add to the flow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.add_flow_media_streams_request.AddFlowMediaStreamsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.add_flow_media_streams_response.AddFlowMediaStreamsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.add_flow_media_streams

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.add_flow_media_streams.async_add_flow_media_streams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.add_flow_media_streams_request.AddFlowMediaStreamsRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["media_streams"] = media_streams

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_flow_outputs(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        outputs: "aws_sdk_mediaconnect.types.__list_of_add_output_request.__listOfAddOutputRequest",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.add_flow_outputs_response.AddFlowOutputsResponse":
        """<p> Adds outputs to an existing flow. You can create up to 50 outputs per flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to add outputs to.</p>
            outputs: <p> A list of outputs that you want to add to the flow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.add_flow_outputs_request.AddFlowOutputsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.add_flow_outputs_response.AddFlowOutputsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.add_flow_outputs

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.add_flow_outputs.async_add_flow_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.add_flow_outputs_request.AddFlowOutputsRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["outputs"] = outputs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_flow_sources(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        sources: "aws_sdk_mediaconnect.types.__list_of_set_source_request.__listOfSetSourceRequest",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.add_flow_sources_response.AddFlowSourcesResponse":
        """<p> Adds sources to a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            sources: <p> A list of sources that you want to add to the flow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.add_flow_sources_request.AddFlowSourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.add_flow_sources_response.AddFlowSourcesResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.add_flow_sources

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.add_flow_sources.async_add_flow_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.add_flow_sources_request.AddFlowSourcesRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["sources"] = sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_flow_vpc_interfaces(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        vpc_interfaces: "aws_sdk_mediaconnect.types.__list_of_vpc_interface_request.__listOfVpcInterfaceRequest",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.add_flow_vpc_interfaces_response.AddFlowVpcInterfacesResponse":
        """<p> Adds VPC interfaces to a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            vpc_interfaces: <p> A list of VPC interfaces that you want to add to the flow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.add_flow_vpc_interfaces_request.AddFlowVpcInterfacesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.add_flow_vpc_interfaces_response.AddFlowVpcInterfacesResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.add_flow_vpc_interfaces

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.add_flow_vpc_interfaces.async_add_flow_vpc_interfaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.add_flow_vpc_interfaces_request.AddFlowVpcInterfacesRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["vpc_interfaces"] = vpc_interfaces

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_flow_source_metadata(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.describe_flow_source_metadata_response.DescribeFlowSourceMetadataResponse":
        """<p> The <code>DescribeFlowSourceMetadata</code> API is used to view information about the flow's source transport stream and programs. This API displays status messages about the flow's source as well as details about the program's video, audio, and other data. </p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.describe_flow_source_metadata_request.DescribeFlowSourceMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.describe_flow_source_metadata_response.DescribeFlowSourceMetadataResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_flow_source_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.describe_flow_source_metadata.async_describe_flow_source_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.describe_flow_source_metadata_request.DescribeFlowSourceMetadataRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_flow_source_thumbnail(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.describe_flow_source_thumbnail_response.DescribeFlowSourceThumbnailResponse":
        """<p> Describes the thumbnail for the flow source. </p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.describe_flow_source_thumbnail_request.DescribeFlowSourceThumbnailRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.describe_flow_source_thumbnail_response.DescribeFlowSourceThumbnailResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_flow_source_thumbnail

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.describe_flow_source_thumbnail.async_describe_flow_source_thumbnail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.describe_flow_source_thumbnail_request.DescribeFlowSourceThumbnailRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def grant_flow_entitlements(
        self,
        entitlements: "aws_sdk_mediaconnect.types.__list_of_grant_entitlement_request.__listOfGrantEntitlementRequest",
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.grant_flow_entitlements_response.GrantFlowEntitlementsResponse":
        """<p> Grants entitlements to an existing flow.</p>

        Args:
            entitlements: <p> The list of entitlements that you want to grant.</p>
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to grant entitlements on.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.grant_flow_entitlements_request.GrantFlowEntitlementsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.grant_flow_entitlements_response.GrantFlowEntitlementsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.grant_flow_entitlements

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.grant_flow_entitlements.async_grant_flow_entitlements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.grant_flow_entitlements_request.GrantFlowEntitlementsRequest = {}  # type: ignore[typeddict-item]
        input["entitlements"] = entitlements
        input["flow_arn"] = flow_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_flow_media_stream(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        media_stream_name: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.remove_flow_media_stream_response.RemoveFlowMediaStreamResponse":
        """<p> Removes a media stream from a flow. This action is only available if the media stream is not associated with a source or output.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to update.</p>
            media_stream_name: <p> The name of the media stream that you want to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.remove_flow_media_stream_request.RemoveFlowMediaStreamRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.remove_flow_media_stream_response.RemoveFlowMediaStreamResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.remove_flow_media_stream

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.remove_flow_media_stream.async_remove_flow_media_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.remove_flow_media_stream_request.RemoveFlowMediaStreamRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["media_stream_name"] = media_stream_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_flow_output(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        output_arn: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.remove_flow_output_response.RemoveFlowOutputResponse":
        """<p> Removes an output from an existing flow. This request can be made only on an output that does not have an entitlement associated with it. If the output has an entitlement, you must revoke the entitlement instead. When an entitlement is revoked from a flow, the service automatically removes the associated output.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to remove an output from.</p>
            output_arn: <p> The ARN of the output that you want to remove. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.remove_flow_output_request.RemoveFlowOutputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.remove_flow_output_response.RemoveFlowOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.remove_flow_output

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.remove_flow_output.async_remove_flow_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.remove_flow_output_request.RemoveFlowOutputRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["output_arn"] = output_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_flow_source(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        source_arn: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.remove_flow_source_response.RemoveFlowSourceResponse":
        """<p> Removes a source from an existing flow. This request can be made only if there is more than one source on the flow. </p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to remove a source from.</p>
            source_arn: <p> The ARN of the source that you want to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.remove_flow_source_request.RemoveFlowSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.remove_flow_source_response.RemoveFlowSourceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.remove_flow_source

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.remove_flow_source.async_remove_flow_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.remove_flow_source_request.RemoveFlowSourceRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["source_arn"] = source_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_flow_vpc_interface(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        vpc_interface_name: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.remove_flow_vpc_interface_response.RemoveFlowVpcInterfaceResponse":
        """<p> Removes a VPC Interface from an existing flow. This request can be made only on a VPC interface that does not have a Source or Output associated with it. If the VPC interface is referenced by a Source or Output, you must first delete or update the Source or Output to no longer reference the VPC interface.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to remove a VPC interface from.</p>
            vpc_interface_name: <p> The name of the VPC interface that you want to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.remove_flow_vpc_interface_request.RemoveFlowVpcInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.remove_flow_vpc_interface_response.RemoveFlowVpcInterfaceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.remove_flow_vpc_interface

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.remove_flow_vpc_interface.async_remove_flow_vpc_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.remove_flow_vpc_interface_request.RemoveFlowVpcInterfaceRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn
        input["vpc_interface_name"] = vpc_interface_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def revoke_flow_entitlement(
        self,
        entitlement_arn: str,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.revoke_flow_entitlement_response.RevokeFlowEntitlementResponse":
        """<p> Revokes an entitlement from a flow. Once an entitlement is revoked, the content becomes unavailable to the subscriber and the associated output is removed.</p>

        Args:
            entitlement_arn: <p> The Amazon Resource Name (ARN) of the entitlement that you want to revoke.</p>
            flow_arn: <p> The flow that you want to revoke an entitlement from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.revoke_flow_entitlement_request.RevokeFlowEntitlementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.revoke_flow_entitlement_response.RevokeFlowEntitlementResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.revoke_flow_entitlement

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.revoke_flow_entitlement.async_revoke_flow_entitlement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.revoke_flow_entitlement_request.RevokeFlowEntitlementRequest = {}  # type: ignore[typeddict-item]
        input["entitlement_arn"] = entitlement_arn
        input["flow_arn"] = flow_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_flow(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.start_flow_response.StartFlowResponse":
        """<p> Starts a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to start.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.start_flow_request.StartFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.start_flow_response.StartFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.start_flow

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.start_flow.async_start_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.start_flow_request.StartFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_flow(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.stop_flow_response.StopFlowResponse":
        """<p> Stops a flow.</p>

        Args:
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that you want to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.stop_flow_request.StopFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.stop_flow_response.StopFlowResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.stop_flow

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.stop_flow.async_stop_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.stop_flow_request.StopFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_arn"] = flow_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_flow_entitlement(
        self,
        entitlement_arn: str,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        description: Optional[str] = None,
        encryption: Optional[
            "aws_sdk_mediaconnect.types.update_encryption.UpdateEncryption"
        ] = None,
        entitlement_status: Optional[
            "aws_sdk_mediaconnect.types.entitlement_status.EntitlementStatus"
        ] = None,
        subscribers: Optional[
            "aws_sdk_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_flow_entitlement_response.UpdateFlowEntitlementResponse":
        """<p> Updates an entitlement. You can change an entitlement's description, subscribers, and encryption. If you change the subscribers, the service will remove the outputs that are are used by the subscribers that are removed.</p>

        Args:
            description: <p> A description of the entitlement. This description appears only on the MediaConnect console and will not be seen by the subscriber or end user.</p>
            encryption: <p> The type of encryption that will be used on the output associated with this entitlement. Allowable encryption types: static-key, speke.</p>
            entitlement_arn: <p> The Amazon Resource Name (ARN) of the entitlement that you want to update.</p>
            entitlement_status: <p> An indication of whether you want to enable the entitlement to allow access, or disable it to stop streaming content to the subscriber’s flow temporarily. If you don’t specify the <code>entitlementStatus</code> field in your request, MediaConnect leaves the value unchanged.</p>
            flow_arn: <p> The ARN of the flow that is associated with the entitlement that you want to update.</p>
            subscribers: <p> The Amazon Web Services account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.update_flow_entitlement_request.UpdateFlowEntitlementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.update_flow_entitlement_response.UpdateFlowEntitlementResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_flow_entitlement

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.update_flow_entitlement.async_update_flow_entitlement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_flow_entitlement_request.UpdateFlowEntitlementRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input["description"] = description
        if encryption is not None:
            input["encryption"] = encryption
        input["entitlement_arn"] = entitlement_arn
        if entitlement_status is not None:
            input["entitlement_status"] = entitlement_status
        input["flow_arn"] = flow_arn
        if subscribers is not None:
            input["subscribers"] = subscribers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_flow_media_stream(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        media_stream_name: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        attributes: Optional[
            "aws_sdk_mediaconnect.types.media_stream_attributes_request.MediaStreamAttributesRequest"
        ] = None,
        clock_rate: Optional[int] = None,
        description: Optional[str] = None,
        media_stream_type: Optional[
            "aws_sdk_mediaconnect.types.media_stream_type.MediaStreamType"
        ] = None,
        video_format: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.update_flow_media_stream_response.UpdateFlowMediaStreamResponse":
        """<p> Updates an existing media stream.</p>

        Args:
            attributes: <p> The attributes that you want to assign to the media stream.</p>
            clock_rate: <p>The sample rate for the stream. This value in measured in kHz. </p>
            description: <p>A description that can help you quickly identify what your media stream is used for. </p>
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that is associated with the media stream that you updated.</p>
            media_stream_name: <p> The media stream that you updated.</p>
            media_stream_type: <p>The type of media stream. </p>
            video_format: <p>The resolution of the video. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.update_flow_media_stream_request.UpdateFlowMediaStreamRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.update_flow_media_stream_response.UpdateFlowMediaStreamResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_flow_media_stream

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.update_flow_media_stream.async_update_flow_media_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_flow_media_stream_request.UpdateFlowMediaStreamRequest = {}  # type: ignore[typeddict-item]
        if attributes is not None:
            input["attributes"] = attributes
        if clock_rate is not None:
            input["clock_rate"] = clock_rate
        if description is not None:
            input["description"] = description
        input["flow_arn"] = flow_arn
        input["media_stream_name"] = media_stream_name
        if media_stream_type is not None:
            input["media_stream_type"] = media_stream_type
        if video_format is not None:
            input["video_format"] = video_format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_flow_output(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        output_arn: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        cidr_allow_list: Optional[
            "aws_sdk_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
        description: Optional[str] = None,
        destination: Optional[str] = None,
        encryption: Optional[
            "aws_sdk_mediaconnect.types.update_encryption.UpdateEncryption"
        ] = None,
        max_latency: Optional[int] = None,
        media_stream_output_configurations: Optional[
            "aws_sdk_mediaconnect.types.__list_of_media_stream_output_configuration_request.__listOfMediaStreamOutputConfigurationRequest"
        ] = None,
        min_latency: Optional[int] = None,
        port: Optional[int] = None,
        protocol: Optional["aws_sdk_mediaconnect.types.protocol.Protocol"] = None,
        remote_id: Optional[str] = None,
        sender_control_port: Optional[int] = None,
        sender_ip_address: Optional[str] = None,
        smoothing_latency: Optional[int] = None,
        stream_id: Optional[str] = None,
        vpc_interface_attachment: Optional[
            "aws_sdk_mediaconnect.types.vpc_interface_attachment.VpcInterfaceAttachment"
        ] = None,
        output_status: Optional[
            "aws_sdk_mediaconnect.types.output_status.OutputStatus"
        ] = None,
        ndi_program_name: Optional[str] = None,
        ndi_speed_hq_quality: Optional[int] = None,
        router_integration_state: Optional[
            "aws_sdk_mediaconnect.types.state.State"
        ] = None,
        router_integration_transit_encryption: Optional[
            "aws_sdk_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
        ] = None,
        ndi_output_timecode_source: Optional[
            "aws_sdk_mediaconnect.types.ndi_output_timecode_source.NdiOutputTimecodeSource"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_flow_output_response.UpdateFlowOutputResponse":
        """<p> Updates an existing flow output.</p>

        Args:
            cidr_allow_list: <p> The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>
            description: <p> A description of the output. This description appears only on the MediaConnect console and will not be seen by the end user.</p>
            destination: <p> The IP address where you want to send the output.</p>
            encryption: <p> The type of key used for the encryption. If no <code>keyType</code> is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.</p>
            flow_arn: <p> The Amazon Resource Name (ARN) of the flow that is associated with the output that you want to update.</p>
            max_latency: <p> The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.</p>
            media_stream_output_configurations: <p> The media streams that are associated with the output, and the parameters for those associations.</p>
            min_latency: <p> The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.</p>
            output_arn: <p> The ARN of the output that you want to update.</p>
            port: <p> The port to use when content is distributed to this output.</p>
            protocol: <p> The protocol to use for the output.</p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>
            remote_id: <p> The remote ID for the Zixi-pull stream.</p>
            sender_control_port: <p> The port that the flow uses to send outbound requests to initiate connection with the sender.</p>
            sender_ip_address: <p> The IP address that the flow communicates with to initiate connection with the sender.</p>
            smoothing_latency: <p> The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.</p>
            stream_id: <p> The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.</p>
            vpc_interface_attachment: <p> The name of the VPC interface attachment to use for this output.</p>
            output_status: <p> An indication of whether the output should transmit data or not. If you don't specify the <code>outputStatus</code> field in your request, MediaConnect leaves the value unchanged.</p>
            ndi_program_name: <p> A suffix for the name of the NDI® sender that the flow creates. If a custom name isn't specified, MediaConnect uses the output name. </p>
            ndi_speed_hq_quality: <p>A quality setting for the NDI Speed HQ encoder. </p>
            router_integration_state: <p>Indicates whether to enable or disable router integration for this flow output.</p>
            ndi_output_timecode_source: <p>Controls how MediaConnect generates timecodes for NDI output frames. If you don't specify this field, MediaConnect leaves the value unchanged.</p> <ul> <li> <p> <code>EMBEDDED_TIMECODE</code> - Preserves timecodes from the input transport stream. The timecodes must be embedded in the video stream as SEI timing messages. If no embedded timecode is detected, MediaConnect uses the UTC system time instead.</p> </li> <li> <p> <code>UTC_SYSTEM_TIME</code> - Generates timecodes based on the system clock time when each frame is sent.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.update_flow_output_request.UpdateFlowOutputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.update_flow_output_response.UpdateFlowOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_flow_output

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.update_flow_output.async_update_flow_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_flow_output_request.UpdateFlowOutputRequest = {}  # type: ignore[typeddict-item]
        if cidr_allow_list is not None:
            input["cidr_allow_list"] = cidr_allow_list
        if description is not None:
            input["description"] = description
        if destination is not None:
            input["destination"] = destination
        if encryption is not None:
            input["encryption"] = encryption
        input["flow_arn"] = flow_arn
        if max_latency is not None:
            input["max_latency"] = max_latency
        if media_stream_output_configurations is not None:
            input["media_stream_output_configurations"] = (
                media_stream_output_configurations
            )
        if min_latency is not None:
            input["min_latency"] = min_latency
        input["output_arn"] = output_arn
        if port is not None:
            input["port"] = port
        if protocol is not None:
            input["protocol"] = protocol
        if remote_id is not None:
            input["remote_id"] = remote_id
        if sender_control_port is not None:
            input["sender_control_port"] = sender_control_port
        if sender_ip_address is not None:
            input["sender_ip_address"] = sender_ip_address
        if smoothing_latency is not None:
            input["smoothing_latency"] = smoothing_latency
        if stream_id is not None:
            input["stream_id"] = stream_id
        if vpc_interface_attachment is not None:
            input["vpc_interface_attachment"] = vpc_interface_attachment
        if output_status is not None:
            input["output_status"] = output_status
        if ndi_program_name is not None:
            input["ndi_program_name"] = ndi_program_name
        if ndi_speed_hq_quality is not None:
            input["ndi_speed_hq_quality"] = ndi_speed_hq_quality
        if router_integration_state is not None:
            input["router_integration_state"] = router_integration_state
        if router_integration_transit_encryption is not None:
            input["router_integration_transit_encryption"] = (
                router_integration_transit_encryption
            )
        if ndi_output_timecode_source is not None:
            input["ndi_output_timecode_source"] = ndi_output_timecode_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_flow_source(
        self,
        flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn",
        source_arn: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        decryption: Optional[
            "aws_sdk_mediaconnect.types.update_encryption.UpdateEncryption"
        ] = None,
        description: Optional[str] = None,
        entitlement_arn: Optional[str] = None,
        ingest_port: Optional[int] = None,
        max_bitrate: Optional[int] = None,
        max_latency: Optional[int] = None,
        max_sync_buffer: Optional[int] = None,
        media_stream_source_configurations: Optional[
            "aws_sdk_mediaconnect.types.__list_of_media_stream_source_configuration_request.__listOfMediaStreamSourceConfigurationRequest"
        ] = None,
        min_latency: Optional[int] = None,
        protocol: Optional["aws_sdk_mediaconnect.types.protocol.Protocol"] = None,
        sender_control_port: Optional[int] = None,
        sender_ip_address: Optional[str] = None,
        source_listener_address: Optional[str] = None,
        source_listener_port: Optional[int] = None,
        stream_id: Optional[str] = None,
        vpc_interface_name: Optional[str] = None,
        whitelist_cidr: Optional[str] = None,
        gateway_bridge_source: Optional[
            "aws_sdk_mediaconnect.types.update_gateway_bridge_source_request.UpdateGatewayBridgeSourceRequest"
        ] = None,
        ndi_source_settings: Optional[
            "aws_sdk_mediaconnect.types.ndi_source_settings.NdiSourceSettings"
        ] = None,
        router_integration_state: Optional[
            "aws_sdk_mediaconnect.types.state.State"
        ] = None,
        router_integration_transit_decryption: Optional[
            "aws_sdk_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_flow_source_response.UpdateFlowSourceResponse":
        """<p> Updates the source of a flow.</p> <note> <p> Because <code>UpdateFlowSources</code> and <code>UpdateFlow</code> are separate operations, you can't change both the source type AND the flow size in a single request. </p> <ul> <li> <p>If you have a <code>MEDIUM</code> flow and you want to change the flow source to NDI®:</p> <ul> <li> <p>First, use the <code>UpdateFlow</code> operation to upgrade the flow size to <code>LARGE</code>. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlowSource</code> operation to configure the NDI source. </p> </li> </ul> </li> <li> <p>If you're switching from an NDI source to a transport stream (TS) source and want to downgrade the flow size: </p> <ul> <li> <p>First, use the <code>UpdateFlowSource</code> operation to change the flow source type. </p> </li> <li> <p>After that, you can then use the <code>UpdateFlow</code> operation to downgrade the flow size to <code>MEDIUM</code>.</p> </li> </ul> </li> </ul> </note>

        Args:
            decryption: <p>The type of encryption that is used on the content ingested from the source. </p>
            description: <p>A description of the source. This description is not visible outside of the current Amazon Web Services account. </p>
            entitlement_arn: <p>The Amazon Resource Name (ARN) of the entitlement that allows you to subscribe to the flow. The entitlement is set by the content originator, and the ARN is generated as part of the originator's flow. </p>
            flow_arn: <p> The ARN of the flow that you want to update. </p>
            ingest_port: <p>The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088. </p>
            max_bitrate: <p>The maximum bitrate for RIST, RTP, and RTP-FEC streams. </p>
            max_latency: <p>The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams. </p>
            max_sync_buffer: <p>The size of the buffer (in milliseconds) to use to sync incoming source data. </p>
            media_stream_source_configurations: <p>The media stream that is associated with the source, and the parameters for that association. </p>
            min_latency: <p>The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency. </p>
            protocol: <p>The protocol that the source uses to deliver the content to MediaConnect. </p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>
            sender_control_port: <p>The port that the flow uses to send outbound requests to initiate connection with the sender. </p>
            sender_ip_address: <p>The IP address that the flow communicates with to initiate connection with the sender. </p>
            source_arn: <p>The ARN of the source that you want to update. </p>
            source_listener_address: <p>The source IP or domain name for SRT-caller protocol. </p>
            source_listener_port: <p>Source port for SRT-caller protocol. </p>
            stream_id: <p>The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams. </p>
            vpc_interface_name: <p>The name of the VPC interface that you want to send your output to.</p>
            whitelist_cidr: <p>The range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. </p>
            gateway_bridge_source: <p>The source configuration for cloud flows receiving a stream from a bridge. </p>
            ndi_source_settings: <p> The settings for the NDI source. This includes the exact name of the upstream NDI sender that you want to connect to your source. </p>
            router_integration_state: <p>Indicates whether to enable or disable router integration for this flow source.</p>
            router_integration_transit_decryption: <p>The encryption configuration for the flow source when router integration is enabled.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.update_flow_source_request.UpdateFlowSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.update_flow_source_response.UpdateFlowSourceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_flow_source

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.update_flow_source.async_update_flow_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_flow_source_request.UpdateFlowSourceRequest = {}  # type: ignore[typeddict-item]
        if decryption is not None:
            input["decryption"] = decryption
        if description is not None:
            input["description"] = description
        if entitlement_arn is not None:
            input["entitlement_arn"] = entitlement_arn
        input["flow_arn"] = flow_arn
        if ingest_port is not None:
            input["ingest_port"] = ingest_port
        if max_bitrate is not None:
            input["max_bitrate"] = max_bitrate
        if max_latency is not None:
            input["max_latency"] = max_latency
        if max_sync_buffer is not None:
            input["max_sync_buffer"] = max_sync_buffer
        if media_stream_source_configurations is not None:
            input["media_stream_source_configurations"] = (
                media_stream_source_configurations
            )
        if min_latency is not None:
            input["min_latency"] = min_latency
        if protocol is not None:
            input["protocol"] = protocol
        if sender_control_port is not None:
            input["sender_control_port"] = sender_control_port
        if sender_ip_address is not None:
            input["sender_ip_address"] = sender_ip_address
        input["source_arn"] = source_arn
        if source_listener_address is not None:
            input["source_listener_address"] = source_listener_address
        if source_listener_port is not None:
            input["source_listener_port"] = source_listener_port
        if stream_id is not None:
            input["stream_id"] = stream_id
        if vpc_interface_name is not None:
            input["vpc_interface_name"] = vpc_interface_name
        if whitelist_cidr is not None:
            input["whitelist_cidr"] = whitelist_cidr
        if gateway_bridge_source is not None:
            input["gateway_bridge_source"] = gateway_bridge_source
        if ndi_source_settings is not None:
            input["ndi_source_settings"] = ndi_source_settings
        if router_integration_state is not None:
            input["router_integration_state"] = router_integration_state
        if router_integration_transit_decryption is not None:
            input["router_integration_transit_decryption"] = (
                router_integration_transit_decryption
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
