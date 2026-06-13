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
    import aws_sdk_mediaconnect.types.batch_get_router_output_request
    import aws_sdk_mediaconnect.types.batch_get_router_output_response
    import aws_sdk_mediaconnect.types.create_router_output_request
    import aws_sdk_mediaconnect.types.create_router_output_response
    import aws_sdk_mediaconnect.types.delete_router_output_request
    import aws_sdk_mediaconnect.types.delete_router_output_response
    import aws_sdk_mediaconnect.types.get_router_output_request
    import aws_sdk_mediaconnect.types.get_router_output_response
    import aws_sdk_mediaconnect.types.list_router_outputs_request
    import aws_sdk_mediaconnect.types.list_router_outputs_response
    import aws_sdk_mediaconnect.types.listed_router_output
    import aws_sdk_mediaconnect.types.maintenance_configuration
    import aws_sdk_mediaconnect.types.restart_router_output_request
    import aws_sdk_mediaconnect.types.restart_router_output_response
    import aws_sdk_mediaconnect.types.router_input_arn
    import aws_sdk_mediaconnect.types.router_output_arn
    import aws_sdk_mediaconnect.types.router_output_arn_list
    import aws_sdk_mediaconnect.types.router_output_configuration
    import aws_sdk_mediaconnect.types.router_output_filter_list
    import aws_sdk_mediaconnect.types.router_output_tier
    import aws_sdk_mediaconnect.types.routing_scope
    import aws_sdk_mediaconnect.types.start_router_output_request
    import aws_sdk_mediaconnect.types.start_router_output_response
    import aws_sdk_mediaconnect.types.stop_router_output_request
    import aws_sdk_mediaconnect.types.stop_router_output_response
    import aws_sdk_mediaconnect.types.take_router_input_request
    import aws_sdk_mediaconnect.types.take_router_input_response
    import aws_sdk_mediaconnect.types.update_router_output_request
    import aws_sdk_mediaconnect.types.update_router_output_response
    from aws_sdk_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from aws_sdk_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class RouterOutputResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        configuration: "aws_sdk_mediaconnect.types.router_output_configuration.RouterOutputConfiguration",
        maximum_bitrate: int,
        routing_scope: "aws_sdk_mediaconnect.types.routing_scope.RoutingScope",
        tier: "aws_sdk_mediaconnect.types.router_output_tier.RouterOutputTier",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        availability_zone: Optional[str] = None,
        maintenance_configuration: Optional[
            "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        tags: Optional[
            "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.create_router_output_response.CreateRouterOutputResponse":
        """<p>Creates a new router output in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router output.</p>
            configuration: <p>The configuration settings for the router output.</p>
            maximum_bitrate: <p>The maximum bitrate for the router output.</p>
            routing_scope: <p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>
            tier: <p>The tier level for the router output.</p>
            region_name: <p>The Amazon Web Services Region for the router output. Defaults to the current region if not specified.</p>
            availability_zone: <p>The Availability Zone where you want to create the router output. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>
            maintenance_configuration: <p>The maintenance configuration settings for the router output, including preferred maintenance windows and schedules.</p>
            tags: <p>Key-value pairs that can be used to tag this router output.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.create_router_output_request.CreateRouterOutputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.create_router_output_response.CreateRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.create_router_output

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.create_router_output.create_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.create_router_output_request.CreateRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["configuration"] = configuration
        input["maximum_bitrate"] = maximum_bitrate
        input["routing_scope"] = routing_scope
        input["tier"] = tier
        if region_name is not None:
            input["region_name"] = region_name
        if availability_zone is not None:
            input["availability_zone"] = availability_zone
        if maintenance_configuration is not None:
            input["maintenance_configuration"] = maintenance_configuration
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> (
        "aws_sdk_mediaconnect.types.get_router_output_response.GetRouterOutputResponse"
    ):
        """<p>Retrieves information about a specific router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to retrieve information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.get_router_output_request.GetRouterOutputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.get_router_output_response.GetRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.get_router_output

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.get_router_output.get_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.get_router_output_request.GetRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "aws_sdk_mediaconnect.types.router_output_configuration.RouterOutputConfiguration"
        ] = None,
        maximum_bitrate: Optional[int] = None,
        routing_scope: Optional[
            "aws_sdk_mediaconnect.types.routing_scope.RoutingScope"
        ] = None,
        tier: Optional[
            "aws_sdk_mediaconnect.types.router_output_tier.RouterOutputTier"
        ] = None,
        maintenance_configuration: Optional[
            "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_router_output_response.UpdateRouterOutputResponse":
        """<p>Updates the configuration of an existing router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to update.</p>
            name: <p>The updated name for the router output.</p>
            configuration: <p>The updated configuration settings for the router output. Changing the type of the configuration is not supported.</p>
            maximum_bitrate: <p>The updated maximum bitrate for the router output.</p>
            routing_scope: <p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>
            tier: <p>The updated tier level for the router output.</p>
            maintenance_configuration: <p>The updated maintenance configuration settings for the router output, including any changes to preferred maintenance windows and schedules.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.update_router_output_request.UpdateRouterOutputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.update_router_output_response.UpdateRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_router_output

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.update_router_output.update_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_router_output_request.UpdateRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        if name is not None:
            input["name"] = name
        if configuration is not None:
            input["configuration"] = configuration
        if maximum_bitrate is not None:
            input["maximum_bitrate"] = maximum_bitrate
        if routing_scope is not None:
            input["routing_scope"] = routing_scope
        if tier is not None:
            input["tier"] = tier
        if maintenance_configuration is not None:
            input["maintenance_configuration"] = maintenance_configuration

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.delete_router_output_response.DeleteRouterOutputResponse":
        """<p>Deletes a router output from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.delete_router_output_request.DeleteRouterOutputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.delete_router_output_response.DeleteRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.delete_router_output

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.delete_router_output.delete_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.delete_router_output_request.DeleteRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

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
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "aws_sdk_mediaconnect.types.router_output_filter_list.RouterOutputFilterList"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.list_router_outputs_response.ListRouterOutputsResponse":
        """<p>Retrieves a list of router outputs in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router outputs to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router outputs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.list_router_outputs_request.ListRouterOutputsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.list_router_outputs_response.ListRouterOutputsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_router_outputs

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.list_router_outputs.list_router_outputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.list_router_outputs_request.ListRouterOutputsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def restart_router_output(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.restart_router_output_response.RestartRouterOutputResponse":
        """<p>Restarts a router output. This operation can be used to recover from errors or refresh the output state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to restart.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.restart_router_output_request.RestartRouterOutputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.restart_router_output_response.RestartRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.restart_router_output

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.restart_router_output.restart_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.restart_router_output_request.RestartRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_router_output(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.start_router_output_response.StartRouterOutputResponse":
        """<p>Starts a router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to start.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.start_router_output_request.StartRouterOutputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.start_router_output_response.StartRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.start_router_output

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.start_router_output.start_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.start_router_output_request.StartRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_router_output(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.stop_router_output_response.StopRouterOutputResponse":
        """<p>Stops a router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.stop_router_output_request.StopRouterOutputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.stop_router_output_response.StopRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.stop_router_output

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.stop_router_output.stop_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.stop_router_output_request.StopRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def take_router_input(
        self,
        router_output_arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        router_input_arn: Optional[
            "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
        ] = None,
    ) -> (
        "aws_sdk_mediaconnect.types.take_router_input_response.TakeRouterInputResponse"
    ):
        """<p>Associates a router input with a router output in AWS Elemental MediaConnect.</p>

        Args:
            router_output_arn: <p>The Amazon Resource Name (ARN) of the router output that you want to associate with a router input.</p>
            router_input_arn: <p>The Amazon Resource Name (ARN) of the router input that you want to associate with a router output.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.take_router_input_request.TakeRouterInputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.take_router_input_response.TakeRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.take_router_input

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.take_router_input.take_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.take_router_input_request.TakeRouterInputRequest = {}  # type: ignore[typeddict-item]
        input["router_output_arn"] = router_output_arn
        if router_input_arn is not None:
            input["router_input_arn"] = router_input_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_router_output(
        self,
        arns: "aws_sdk_mediaconnect.types.router_output_arn_list.RouterOutputArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.batch_get_router_output_response.BatchGetRouterOutputResponse":
        """<p>Retrieves information about multiple router outputs in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router outputs you want to retrieve information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.batch_get_router_output_request.BatchGetRouterOutputRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.batch_get_router_output_response.BatchGetRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.batch_get_router_output

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.batch_get_router_output.batch_get_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.batch_get_router_output_request.BatchGetRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arns"] = arns

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRouterOutputResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        configuration: "aws_sdk_mediaconnect.types.router_output_configuration.RouterOutputConfiguration",
        maximum_bitrate: int,
        routing_scope: "aws_sdk_mediaconnect.types.routing_scope.RoutingScope",
        tier: "aws_sdk_mediaconnect.types.router_output_tier.RouterOutputTier",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        availability_zone: Optional[str] = None,
        maintenance_configuration: Optional[
            "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        tags: Optional[
            "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.create_router_output_response.CreateRouterOutputResponse":
        """<p>Creates a new router output in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router output.</p>
            configuration: <p>The configuration settings for the router output.</p>
            maximum_bitrate: <p>The maximum bitrate for the router output.</p>
            routing_scope: <p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>
            tier: <p>The tier level for the router output.</p>
            region_name: <p>The Amazon Web Services Region for the router output. Defaults to the current region if not specified.</p>
            availability_zone: <p>The Availability Zone where you want to create the router output. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>
            maintenance_configuration: <p>The maintenance configuration settings for the router output, including preferred maintenance windows and schedules.</p>
            tags: <p>Key-value pairs that can be used to tag this router output.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.create_router_output_request.CreateRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.create_router_output_response.CreateRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.create_router_output

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.create_router_output.async_create_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.create_router_output_request.CreateRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["configuration"] = configuration
        input["maximum_bitrate"] = maximum_bitrate
        input["routing_scope"] = routing_scope
        input["tier"] = tier
        if region_name is not None:
            input["region_name"] = region_name
        if availability_zone is not None:
            input["availability_zone"] = availability_zone
        if maintenance_configuration is not None:
            input["maintenance_configuration"] = maintenance_configuration
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> (
        "aws_sdk_mediaconnect.types.get_router_output_response.GetRouterOutputResponse"
    ):
        """<p>Retrieves information about a specific router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.get_router_output_request.GetRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.get_router_output_response.GetRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.get_router_output

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.get_router_output.async_get_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.get_router_output_request.GetRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "aws_sdk_mediaconnect.types.router_output_configuration.RouterOutputConfiguration"
        ] = None,
        maximum_bitrate: Optional[int] = None,
        routing_scope: Optional[
            "aws_sdk_mediaconnect.types.routing_scope.RoutingScope"
        ] = None,
        tier: Optional[
            "aws_sdk_mediaconnect.types.router_output_tier.RouterOutputTier"
        ] = None,
        maintenance_configuration: Optional[
            "aws_sdk_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.update_router_output_response.UpdateRouterOutputResponse":
        """<p>Updates the configuration of an existing router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to update.</p>
            name: <p>The updated name for the router output.</p>
            configuration: <p>The updated configuration settings for the router output. Changing the type of the configuration is not supported.</p>
            maximum_bitrate: <p>The updated maximum bitrate for the router output.</p>
            routing_scope: <p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>
            tier: <p>The updated tier level for the router output.</p>
            maintenance_configuration: <p>The updated maintenance configuration settings for the router output, including any changes to preferred maintenance windows and schedules.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.update_router_output_request.UpdateRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.update_router_output_response.UpdateRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.update_router_output

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.update_router_output.async_update_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.update_router_output_request.UpdateRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        if name is not None:
            input["name"] = name
        if configuration is not None:
            input["configuration"] = configuration
        if maximum_bitrate is not None:
            input["maximum_bitrate"] = maximum_bitrate
        if routing_scope is not None:
            input["routing_scope"] = routing_scope
        if tier is not None:
            input["tier"] = tier
        if maintenance_configuration is not None:
            input["maintenance_configuration"] = maintenance_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.delete_router_output_response.DeleteRouterOutputResponse":
        """<p>Deletes a router output from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.delete_router_output_request.DeleteRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.delete_router_output_response.DeleteRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.delete_router_output

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.delete_router_output.async_delete_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.delete_router_output_request.DeleteRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

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
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "aws_sdk_mediaconnect.types.router_output_filter_list.RouterOutputFilterList"
        ] = None,
    ) -> "aws_sdk_mediaconnect.types.list_router_outputs_response.ListRouterOutputsResponse":
        """<p>Retrieves a list of router outputs in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router outputs to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router outputs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.list_router_outputs_request.ListRouterOutputsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.list_router_outputs_response.ListRouterOutputsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_router_outputs

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.list_router_outputs.async_list_router_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.list_router_outputs_request.ListRouterOutputsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def restart_router_output(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.restart_router_output_response.RestartRouterOutputResponse":
        """<p>Restarts a router output. This operation can be used to recover from errors or refresh the output state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to restart.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.restart_router_output_request.RestartRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.restart_router_output_response.RestartRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.restart_router_output

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.restart_router_output.async_restart_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.restart_router_output_request.RestartRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_router_output(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.start_router_output_response.StartRouterOutputResponse":
        """<p>Starts a router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to start.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.start_router_output_request.StartRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.start_router_output_response.StartRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.start_router_output

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.start_router_output.async_start_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.start_router_output_request.StartRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_router_output(
        self,
        arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.stop_router_output_response.StopRouterOutputResponse":
        """<p>Stops a router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.stop_router_output_request.StopRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.stop_router_output_response.StopRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.stop_router_output

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.stop_router_output.async_stop_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.stop_router_output_request.StopRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def take_router_input(
        self,
        router_output_arn: "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        router_input_arn: Optional[
            "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
        ] = None,
    ) -> (
        "aws_sdk_mediaconnect.types.take_router_input_response.TakeRouterInputResponse"
    ):
        """<p>Associates a router input with a router output in AWS Elemental MediaConnect.</p>

        Args:
            router_output_arn: <p>The Amazon Resource Name (ARN) of the router output that you want to associate with a router input.</p>
            router_input_arn: <p>The Amazon Resource Name (ARN) of the router input that you want to associate with a router output.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.take_router_input_request.TakeRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.take_router_input_response.TakeRouterInputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.take_router_input

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.take_router_input.async_take_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.take_router_input_request.TakeRouterInputRequest = {}  # type: ignore[typeddict-item]
        input["router_output_arn"] = router_output_arn
        if router_input_arn is not None:
            input["router_input_arn"] = router_input_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_router_output(
        self,
        arns: "aws_sdk_mediaconnect.types.router_output_arn_list.RouterOutputArnList",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.batch_get_router_output_response.BatchGetRouterOutputResponse":
        """<p>Retrieves information about multiple router outputs in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router outputs you want to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.batch_get_router_output_request.BatchGetRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.batch_get_router_output_response.BatchGetRouterOutputResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.batch_get_router_output

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.batch_get_router_output.async_batch_get_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.batch_get_router_output_request.BatchGetRouterOutputRequest = {}  # type: ignore[typeddict-item]
        input["arns"] = arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
