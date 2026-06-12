from typing import TYPE_CHECKING, Optional

import aws_sdk_iot_managed_integrations._auth._signers
import aws_sdk_iot_managed_integrations._auth._sigv4
from aws_sdk_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.create_destination_request
    import aws_sdk_iot_managed_integrations.types.create_destination_response
    import aws_sdk_iot_managed_integrations.types.delete_destination_request
    import aws_sdk_iot_managed_integrations.types.delivery_destination_arn
    import aws_sdk_iot_managed_integrations.types.delivery_destination_role_arn
    import aws_sdk_iot_managed_integrations.types.delivery_destination_type
    import aws_sdk_iot_managed_integrations.types.destination_description
    import aws_sdk_iot_managed_integrations.types.destination_name
    import aws_sdk_iot_managed_integrations.types.destination_summary
    import aws_sdk_iot_managed_integrations.types.get_destination_request
    import aws_sdk_iot_managed_integrations.types.get_destination_response
    import aws_sdk_iot_managed_integrations.types.list_destinations_request
    import aws_sdk_iot_managed_integrations.types.list_destinations_response
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.tags_map
    import aws_sdk_iot_managed_integrations.types.update_destination_request
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class DestinationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create_destination(
        self,
        delivery_destination_arn: "aws_sdk_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn",
        delivery_destination_type: "aws_sdk_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType",
        name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        role_arn: "aws_sdk_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.destination_description.DestinationDescription"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_destination_response.CreateDestinationResponse":
        """<p> Create a notification destination such as Kinesis Data Streams that receive events and notifications from Managed integrations. Managed integrations uses the destination to determine where to deliver notifications.</p>

        Args:
            delivery_destination_arn: <p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>
            delivery_destination_type: <p>The destination type for the customer-managed destination.</p>
            name: <p>The name of the customer-managed destination.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the delivery destination role.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            description: <p>The description of the customer-managed destination.</p>
            tags: <p>A set of key/value pairs that are used to manage the destination.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_destination_response.CreateDestinationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_destination

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_destination.create_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest = {}  # type: ignore[typeddict-item]
        input["delivery_destination_arn"] = delivery_destination_arn
        input["delivery_destination_type"] = delivery_destination_type
        input["name"] = name
        input["role_arn"] = role_arn
        if client_token is not None:
            input["client_token"] = client_token
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

    def delete_destination(
        self,
        name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deletes a notification destination specified by name. </p>

        Args:
            name: <p>The id of the customer-managed destination.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.delete_destination_request.DeleteDestinationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_destination

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_destination.delete_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.delete_destination_request.DeleteDestinationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_destination(
        self,
        name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_destination_response.GetDestinationResponse":
        """<p>Gets a destination by name. </p>

        Args:
            name: <p>The name of the customer-managed destination.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_destination_request.GetDestinationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_destination_response.GetDestinationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_destination

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_destination.get_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.get_destination_request.GetDestinationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_destinations(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_destinations_response.ListDestinationsResponse":
        """<p> List all notification destinations.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_destinations_request.ListDestinationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_destinations_response.ListDestinationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_destinations

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_destinations.list_destinations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.list_destinations_request.ListDestinationsRequest = {}  # type: ignore[typeddict-item]
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

    def update_destination(
        self,
        name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        delivery_destination_arn: Optional[
            "aws_sdk_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn"
        ] = None,
        delivery_destination_type: Optional[
            "aws_sdk_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType"
        ] = None,
        role_arn: Optional[
            "aws_sdk_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn"
        ] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.destination_description.DestinationDescription"
        ] = None,
    ) -> None:
        """<p> Update a destination specified by name. </p>

        Args:
            name: <p>The name of the customer-managed destination.</p>
            delivery_destination_arn: <p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>
            delivery_destination_type: <p>The destination type for the customer-managed destination.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the delivery destination role.</p>
            description: <p>The description of the customer-managed destination.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.update_destination_request.UpdateDestinationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_destination

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_destination.update_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.update_destination_request.UpdateDestinationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if delivery_destination_arn is not None:
            input["delivery_destination_arn"] = delivery_destination_arn
        if delivery_destination_type is not None:
            input["delivery_destination_type"] = delivery_destination_type
        if role_arn is not None:
            input["role_arn"] = role_arn
        if description is not None:
            input["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDestinationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create_destination(
        self,
        delivery_destination_arn: "aws_sdk_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn",
        delivery_destination_type: "aws_sdk_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType",
        name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        role_arn: "aws_sdk_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.destination_description.DestinationDescription"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_destination_response.CreateDestinationResponse":
        """<p> Create a notification destination such as Kinesis Data Streams that receive events and notifications from Managed integrations. Managed integrations uses the destination to determine where to deliver notifications.</p>

        Args:
            delivery_destination_arn: <p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>
            delivery_destination_type: <p>The destination type for the customer-managed destination.</p>
            name: <p>The name of the customer-managed destination.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the delivery destination role.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            description: <p>The description of the customer-managed destination.</p>
            tags: <p>A set of key/value pairs that are used to manage the destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_destination_response.CreateDestinationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_destination.async_create_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest = {}  # type: ignore[typeddict-item]
        input["delivery_destination_arn"] = delivery_destination_arn
        input["delivery_destination_type"] = delivery_destination_type
        input["name"] = name
        input["role_arn"] = role_arn
        if client_token is not None:
            input["client_token"] = client_token
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

    async def delete_destination(
        self,
        name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deletes a notification destination specified by name. </p>

        Args:
            name: <p>The id of the customer-managed destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.delete_destination_request.DeleteDestinationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_destination.async_delete_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.delete_destination_request.DeleteDestinationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_destination(
        self,
        name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_destination_response.GetDestinationResponse":
        """<p>Gets a destination by name. </p>

        Args:
            name: <p>The name of the customer-managed destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_destination_request.GetDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_destination_response.GetDestinationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_destination.async_get_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.get_destination_request.GetDestinationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_destinations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_destinations_response.ListDestinationsResponse":
        """<p> List all notification destinations.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_destinations_request.ListDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_destinations_response.ListDestinationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_destinations

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_destinations.async_list_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.list_destinations_request.ListDestinationsRequest = {}  # type: ignore[typeddict-item]
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

    async def update_destination(
        self,
        name: "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        delivery_destination_arn: Optional[
            "aws_sdk_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn"
        ] = None,
        delivery_destination_type: Optional[
            "aws_sdk_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType"
        ] = None,
        role_arn: Optional[
            "aws_sdk_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn"
        ] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.destination_description.DestinationDescription"
        ] = None,
    ) -> None:
        """<p> Update a destination specified by name. </p>

        Args:
            name: <p>The name of the customer-managed destination.</p>
            delivery_destination_arn: <p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>
            delivery_destination_type: <p>The destination type for the customer-managed destination.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the delivery destination role.</p>
            description: <p>The description of the customer-managed destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.update_destination_request.UpdateDestinationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_destination.async_update_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.update_destination_request.UpdateDestinationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if delivery_destination_arn is not None:
            input["delivery_destination_arn"] = delivery_destination_arn
        if delivery_destination_type is not None:
            input["delivery_destination_type"] = delivery_destination_type
        if role_arn is not None:
            input["role_arn"] = role_arn
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
