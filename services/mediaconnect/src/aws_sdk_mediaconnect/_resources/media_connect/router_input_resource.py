from __future__ import annotations

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
    import aws_sdk_mediaconnect.types.__map_of_string
    import aws_sdk_mediaconnect.types.batch_get_router_input_request
    import aws_sdk_mediaconnect.types.batch_get_router_input_response
    import aws_sdk_mediaconnect.types.create_router_input_request
    import aws_sdk_mediaconnect.types.create_router_input_response
    import aws_sdk_mediaconnect.types.delete_router_input_request
    import aws_sdk_mediaconnect.types.delete_router_input_response
    import aws_sdk_mediaconnect.types.get_router_input_request
    import aws_sdk_mediaconnect.types.get_router_input_response
    import aws_sdk_mediaconnect.types.get_router_input_source_metadata_request
    import aws_sdk_mediaconnect.types.get_router_input_source_metadata_response
    import aws_sdk_mediaconnect.types.get_router_input_thumbnail_request
    import aws_sdk_mediaconnect.types.get_router_input_thumbnail_response
    import aws_sdk_mediaconnect.types.list_router_inputs_request
    import aws_sdk_mediaconnect.types.list_router_inputs_response
    import aws_sdk_mediaconnect.types.listed_router_input
    import aws_sdk_mediaconnect.types.maintenance_configuration
    import aws_sdk_mediaconnect.types.restart_router_input_request
    import aws_sdk_mediaconnect.types.restart_router_input_response
    import aws_sdk_mediaconnect.types.router_input_arn
    import aws_sdk_mediaconnect.types.router_input_arn_list
    import aws_sdk_mediaconnect.types.router_input_configuration
    import aws_sdk_mediaconnect.types.router_input_filter_list
    import aws_sdk_mediaconnect.types.router_input_tier
    import aws_sdk_mediaconnect.types.router_input_transit_encryption
    import aws_sdk_mediaconnect.types.routing_scope
    import aws_sdk_mediaconnect.types.start_router_input_request
    import aws_sdk_mediaconnect.types.start_router_input_response
    import aws_sdk_mediaconnect.types.stop_router_input_request
    import aws_sdk_mediaconnect.types.stop_router_input_response
    import aws_sdk_mediaconnect.types.update_router_input_request
    import aws_sdk_mediaconnect.types.update_router_input_response
    from aws_sdk_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from aws_sdk_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class RouterInputResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        configuration: "aws_sdk_mediaconnect.types.router_input_configuration.RouterInputConfiguration",
        maximum_bitrate: int,
        routing_scope: "aws_sdk_mediaconnect.types.routing_scope.RoutingScope",
        tier: "aws_sdk_mediaconnect.types.router_input_tier.RouterInputTier",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        availability_zone: Optional[str] = None,
        transit_encryption: Optional[
            "aws_sdk_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
        ] = None,
        maintenance_configuration: Optional[
            "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        tags: Optional[
            "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.create_router_input_response.CreateRouterInputResponse":
        """<p>Creates a new router input in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router input.</p>
            configuration: <p>The configuration settings for the router input, which can include the protocol, network interface, and other details.</p>
            maximum_bitrate: <p>The maximum bitrate for the router input.</p>
            routing_scope: <p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - connects only to outputs in same Region. GLOBAL - connects to outputs in any Region.</p>
            tier: <p>The tier level for the router input.</p>
            region_name: <p>The Amazon Web Services Region for the router input. Defaults to the current region if not specified.</p>
            availability_zone: <p>The Availability Zone where you want to create the router input. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>
            transit_encryption: <p>The transit encryption settings for the router input.</p>
            maintenance_configuration: <p>The maintenance configuration settings for the router input, including preferred maintenance windows and schedules.</p>
            tags: <p>Key-value pairs that can be used to tag and organize this router input.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.create_router_input_request.CreateRouterInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.create_router_input_response.CreateRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.create_router_input

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.create_router_input.create_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.create_router_input_request.CreateRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["configuration"] = configuration
        input_["maximum_bitrate"] = maximum_bitrate
        input_["routing_scope"] = routing_scope
        input_["tier"] = tier
        if region_name is not None:
            input_["region_name"] = region_name
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if transit_encryption is not None:
            input_["transit_encryption"] = transit_encryption
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.get_router_input_response.GetRouterInputResponse":
        """<p>Retrieves information about a specific router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input to retrieve information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.get_router_input_request.GetRouterInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.get_router_input_response.GetRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.get_router_input

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.get_router_input.get_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.get_router_input_request.GetRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "aws_sdk_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
        ] = None,
        maximum_bitrate: Optional[int] = None,
        routing_scope: Optional[
            "aws_sdk_mediaconnect.types.routing_scope.RoutingScope"
        ] = None,
        tier: Optional[
            "aws_sdk_mediaconnect.types.router_input_tier.RouterInputTier"
        ] = None,
        transit_encryption: Optional[
            "aws_sdk_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
        ] = None,
        maintenance_configuration: Optional[
            "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_router_input_response.UpdateRouterInputResponse":
        """<p>Updates the configuration of an existing router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to update.</p>
            name: <p>The updated name for the router input.</p>
            configuration: <p>The updated configuration settings for the router input. Changing the type of the configuration is not supported.</p>
            maximum_bitrate: <p>The updated maximum bitrate for the router input.</p>
            routing_scope: <p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - can be assigned only to outputs in the same Region. GLOBAL - can be assigned to outputs in any Region.</p>
            tier: <p>The updated tier level for the router input.</p>
            transit_encryption: <p>The updated transit encryption settings for the router input.</p>
            maintenance_configuration: <p>The updated maintenance configuration settings for the router input, including any changes to preferred maintenance windows and schedules.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.update_router_input_request.UpdateRouterInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.update_router_input_response.UpdateRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_router_input

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.update_router_input.update_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.update_router_input_request.UpdateRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if maximum_bitrate is not None:
            input_["maximum_bitrate"] = maximum_bitrate
        if routing_scope is not None:
            input_["routing_scope"] = routing_scope
        if tier is not None:
            input_["tier"] = tier
        if transit_encryption is not None:
            input_["transit_encryption"] = transit_encryption
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.delete_router_input_response.DeleteRouterInputResponse":
        """<p>Deletes a router input from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.delete_router_input_request.DeleteRouterInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.delete_router_input_response.DeleteRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.delete_router_input

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.delete_router_input.delete_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.delete_router_input_request.DeleteRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "aws_sdk_mediaconnect.types.router_input_filter_list.RouterInputFilterList"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.list_router_inputs_response.ListRouterInputsResponse":
        """<p>Retrieves a list of router inputs in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router inputs to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router inputs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.list_router_inputs_request.ListRouterInputsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.list_router_inputs_response.ListRouterInputsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_router_inputs

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.list_router_inputs.list_router_inputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.list_router_inputs_request.ListRouterInputsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_router_input_source_metadata(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.get_router_input_source_metadata_response.GetRouterInputSourceMetadataResponse":
        """<p>Retrieves detailed metadata information about a specific router input source, including stream details and connection state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input to retrieve metadata for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.get_router_input_source_metadata_request.GetRouterInputSourceMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.get_router_input_source_metadata_response.GetRouterInputSourceMetadataResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.get_router_input_source_metadata

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.get_router_input_source_metadata.get_router_input_source_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.get_router_input_source_metadata_request.GetRouterInputSourceMetadataRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_router_input_thumbnail(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.get_router_input_thumbnail_response.GetRouterInputThumbnailResponse":
        """<p>Retrieves the thumbnail for a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to see a thumbnail of.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.get_router_input_thumbnail_request.GetRouterInputThumbnailRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.get_router_input_thumbnail_response.GetRouterInputThumbnailResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.get_router_input_thumbnail

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.get_router_input_thumbnail.get_router_input_thumbnail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.get_router_input_thumbnail_request.GetRouterInputThumbnailRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def restart_router_input(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.restart_router_input_response.RestartRouterInputResponse":
        """<p>Restarts a router input. This operation can be used to recover from errors or refresh the input state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to restart.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.restart_router_input_request.RestartRouterInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.restart_router_input_response.RestartRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.restart_router_input

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.restart_router_input.restart_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.restart_router_input_request.RestartRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_router_input(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.start_router_input_response.StartRouterInputResponse":
        """<p>Starts a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to start.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.start_router_input_request.StartRouterInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.start_router_input_response.StartRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.start_router_input

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.start_router_input.start_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.start_router_input_request.StartRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_router_input(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> (
        "aws_sdk_mediaconnect.types.stop_router_input_response.StopRouterInputResponse"
    ):
        """<p>Stops a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.stop_router_input_request.StopRouterInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.stop_router_input_response.StopRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.stop_router_input

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.stop_router_input.stop_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.stop_router_input_request.StopRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_router_input(
        self,
        arns: "aws_sdk_mediaconnect.types.router_input_arn_list.RouterInputArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.batch_get_router_input_response.BatchGetRouterInputResponse":
        """<p>Retrieves information about multiple router inputs in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router inputs you want to retrieve information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.batch_get_router_input_request.BatchGetRouterInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.batch_get_router_input_response.BatchGetRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.batch_get_router_input

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.batch_get_router_input.batch_get_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.batch_get_router_input_request.BatchGetRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arns"] = arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRouterInputResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        configuration: "aws_sdk_mediaconnect.types.router_input_configuration.RouterInputConfiguration",
        maximum_bitrate: int,
        routing_scope: "aws_sdk_mediaconnect.types.routing_scope.RoutingScope",
        tier: "aws_sdk_mediaconnect.types.router_input_tier.RouterInputTier",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        availability_zone: Optional[str] = None,
        transit_encryption: Optional[
            "aws_sdk_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
        ] = None,
        maintenance_configuration: Optional[
            "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        tags: Optional[
            "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.create_router_input_response.CreateRouterInputResponse":
        """<p>Creates a new router input in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router input.</p>
            configuration: <p>The configuration settings for the router input, which can include the protocol, network interface, and other details.</p>
            maximum_bitrate: <p>The maximum bitrate for the router input.</p>
            routing_scope: <p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - connects only to outputs in same Region. GLOBAL - connects to outputs in any Region.</p>
            tier: <p>The tier level for the router input.</p>
            region_name: <p>The Amazon Web Services Region for the router input. Defaults to the current region if not specified.</p>
            availability_zone: <p>The Availability Zone where you want to create the router input. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>
            transit_encryption: <p>The transit encryption settings for the router input.</p>
            maintenance_configuration: <p>The maintenance configuration settings for the router input, including preferred maintenance windows and schedules.</p>
            tags: <p>Key-value pairs that can be used to tag and organize this router input.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.create_router_input_request.CreateRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.create_router_input_response.CreateRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.create_router_input

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.create_router_input.async_create_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.create_router_input_request.CreateRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["configuration"] = configuration
        input_["maximum_bitrate"] = maximum_bitrate
        input_["routing_scope"] = routing_scope
        input_["tier"] = tier
        if region_name is not None:
            input_["region_name"] = region_name
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if transit_encryption is not None:
            input_["transit_encryption"] = transit_encryption
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.get_router_input_response.GetRouterInputResponse":
        """<p>Retrieves information about a specific router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.get_router_input_request.GetRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.get_router_input_response.GetRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.get_router_input

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.get_router_input.async_get_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.get_router_input_request.GetRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "aws_sdk_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
        ] = None,
        maximum_bitrate: Optional[int] = None,
        routing_scope: Optional[
            "aws_sdk_mediaconnect.types.routing_scope.RoutingScope"
        ] = None,
        tier: Optional[
            "aws_sdk_mediaconnect.types.router_input_tier.RouterInputTier"
        ] = None,
        transit_encryption: Optional[
            "aws_sdk_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
        ] = None,
        maintenance_configuration: Optional[
            "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_router_input_response.UpdateRouterInputResponse":
        """<p>Updates the configuration of an existing router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to update.</p>
            name: <p>The updated name for the router input.</p>
            configuration: <p>The updated configuration settings for the router input. Changing the type of the configuration is not supported.</p>
            maximum_bitrate: <p>The updated maximum bitrate for the router input.</p>
            routing_scope: <p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - can be assigned only to outputs in the same Region. GLOBAL - can be assigned to outputs in any Region.</p>
            tier: <p>The updated tier level for the router input.</p>
            transit_encryption: <p>The updated transit encryption settings for the router input.</p>
            maintenance_configuration: <p>The updated maintenance configuration settings for the router input, including any changes to preferred maintenance windows and schedules.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.update_router_input_request.UpdateRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.update_router_input_response.UpdateRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_router_input

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.update_router_input.async_update_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.update_router_input_request.UpdateRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if maximum_bitrate is not None:
            input_["maximum_bitrate"] = maximum_bitrate
        if routing_scope is not None:
            input_["routing_scope"] = routing_scope
        if tier is not None:
            input_["tier"] = tier
        if transit_encryption is not None:
            input_["transit_encryption"] = transit_encryption
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.delete_router_input_response.DeleteRouterInputResponse":
        """<p>Deletes a router input from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.delete_router_input_request.DeleteRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.delete_router_input_response.DeleteRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.delete_router_input

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.delete_router_input.async_delete_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.delete_router_input_request.DeleteRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "aws_sdk_mediaconnect.types.router_input_filter_list.RouterInputFilterList"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.list_router_inputs_response.ListRouterInputsResponse":
        """<p>Retrieves a list of router inputs in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router inputs to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router inputs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.list_router_inputs_request.ListRouterInputsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.list_router_inputs_response.ListRouterInputsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_router_inputs

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.list_router_inputs.async_list_router_inputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.list_router_inputs_request.ListRouterInputsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_router_input_source_metadata(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.get_router_input_source_metadata_response.GetRouterInputSourceMetadataResponse":
        """<p>Retrieves detailed metadata information about a specific router input source, including stream details and connection state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input to retrieve metadata for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.get_router_input_source_metadata_request.GetRouterInputSourceMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.get_router_input_source_metadata_response.GetRouterInputSourceMetadataResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.get_router_input_source_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.get_router_input_source_metadata.async_get_router_input_source_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.get_router_input_source_metadata_request.GetRouterInputSourceMetadataRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_router_input_thumbnail(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.get_router_input_thumbnail_response.GetRouterInputThumbnailResponse":
        """<p>Retrieves the thumbnail for a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to see a thumbnail of.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.get_router_input_thumbnail_request.GetRouterInputThumbnailRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.get_router_input_thumbnail_response.GetRouterInputThumbnailResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.get_router_input_thumbnail

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.get_router_input_thumbnail.async_get_router_input_thumbnail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.get_router_input_thumbnail_request.GetRouterInputThumbnailRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def restart_router_input(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.restart_router_input_response.RestartRouterInputResponse":
        """<p>Restarts a router input. This operation can be used to recover from errors or refresh the input state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to restart.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.restart_router_input_request.RestartRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.restart_router_input_response.RestartRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.restart_router_input

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.restart_router_input.async_restart_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.restart_router_input_request.RestartRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_router_input(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.start_router_input_response.StartRouterInputResponse":
        """<p>Starts a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to start.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.start_router_input_request.StartRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.start_router_input_response.StartRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.start_router_input

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.start_router_input.async_start_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.start_router_input_request.StartRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_router_input(
        self,
        arn: "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> (
        "aws_sdk_mediaconnect.types.stop_router_input_response.StopRouterInputResponse"
    ):
        """<p>Stops a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.stop_router_input_request.StopRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.stop_router_input_response.StopRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.stop_router_input

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.stop_router_input.async_stop_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.stop_router_input_request.StopRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_router_input(
        self,
        arns: "aws_sdk_mediaconnect.types.router_input_arn_list.RouterInputArnList",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.batch_get_router_input_response.BatchGetRouterInputResponse":
        """<p>Retrieves information about multiple router inputs in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router inputs you want to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.batch_get_router_input_request.BatchGetRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.batch_get_router_input_response.BatchGetRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.batch_get_router_input

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.batch_get_router_input.async_batch_get_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.batch_get_router_input_request.BatchGetRouterInputRequest = {}  # type: ignore[typeddict-item]
        input_["arns"] = arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
