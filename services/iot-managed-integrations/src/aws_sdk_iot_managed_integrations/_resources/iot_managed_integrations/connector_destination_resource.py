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
    import aws_sdk_iot_managed_integrations.types.auth_config
    import aws_sdk_iot_managed_integrations.types.auth_config_update
    import aws_sdk_iot_managed_integrations.types.auth_type
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.cloud_connector_id
    import aws_sdk_iot_managed_integrations.types.connector_destination_description
    import aws_sdk_iot_managed_integrations.types.connector_destination_id
    import aws_sdk_iot_managed_integrations.types.connector_destination_name
    import aws_sdk_iot_managed_integrations.types.connector_destination_summary
    import aws_sdk_iot_managed_integrations.types.create_connector_destination_request
    import aws_sdk_iot_managed_integrations.types.create_connector_destination_response
    import aws_sdk_iot_managed_integrations.types.delete_connector_destination_request
    import aws_sdk_iot_managed_integrations.types.get_connector_destination_request
    import aws_sdk_iot_managed_integrations.types.get_connector_destination_response
    import aws_sdk_iot_managed_integrations.types.list_connector_destinations_request
    import aws_sdk_iot_managed_integrations.types.list_connector_destinations_response
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.secrets_manager
    import aws_sdk_iot_managed_integrations.types.update_connector_destination_request
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class ConnectorDestinationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        cloud_connector_id: "aws_sdk_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        auth_config: "aws_sdk_iot_managed_integrations.types.auth_config.AuthConfig",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_destination_name.ConnectorDestinationName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_destination_description.ConnectorDestinationDescription"
        ] = None,
        auth_type: Optional[
            "aws_sdk_iot_managed_integrations.types.auth_type.AuthType"
        ] = None,
        secrets_manager: Optional[
            "aws_sdk_iot_managed_integrations.types.secrets_manager.SecretsManager"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_connector_destination_response.CreateConnectorDestinationResponse":
        """<p>Create a connector destination for connecting a cloud-to-cloud (C2C) connector to the customer's Amazon Web Services account.</p>

        Args:
            name: <p>The display name of the connector destination.</p>
            description: <p>A description of the connector destination.</p>
            cloud_connector_id: <p>The identifier of the C2C connector.</p>
            auth_type: <p>The authentication type used for the connector destination, which determines how credentials and access are managed.</p>
            auth_config: <p>The authentication configuration details for the connector destination, including OAuth settings and other authentication parameters.</p>
            secrets_manager: <p>The AWS Secrets Manager configuration used to securely store and manage sensitive information for the connector destination.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.create_connector_destination_request.CreateConnectorDestinationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_connector_destination_response.CreateConnectorDestinationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_connector_destination

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_connector_destination.create_connector_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.create_connector_destination_request.CreateConnectorDestinationRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        input["cloud_connector_id"] = cloud_connector_id
        if auth_type is not None:
            input["auth_type"] = auth_type
        input["auth_config"] = auth_config
        if secrets_manager is not None:
            input["secrets_manager"] = secrets_manager
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
        identifier: "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_connector_destination_response.GetConnectorDestinationResponse":
        """<p>Get connector destination details linked to a cloud-to-cloud (C2C) connector.</p>

        Args:
            identifier: <p>The identifier of the C2C connector destination.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_connector_destination_request.GetConnectorDestinationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_connector_destination_response.GetConnectorDestinationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_connector_destination

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_connector_destination.get_connector_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.get_connector_destination_request.GetConnectorDestinationRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_destination_description.ConnectorDestinationDescription"
        ] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_destination_name.ConnectorDestinationName"
        ] = None,
        auth_type: Optional[
            "aws_sdk_iot_managed_integrations.types.auth_type.AuthType"
        ] = None,
        auth_config: Optional[
            "aws_sdk_iot_managed_integrations.types.auth_config_update.AuthConfigUpdate"
        ] = None,
        secrets_manager: Optional[
            "aws_sdk_iot_managed_integrations.types.secrets_manager.SecretsManager"
        ] = None,
    ) -> None:
        """<p>Updates the properties of an existing connector destination.</p>

        Args:
            identifier: <p>The unique identifier of the connector destination to update.</p>
            description: <p>The new description to assign to the connector destination.</p>
            name: <p>The new display name to assign to the connector destination.</p>
            auth_type: <p>The new authentication type to use for the connector destination.</p>
            auth_config: <p>The updated authentication configuration details for the connector destination.</p>
            secrets_manager: <p>The updated AWS Secrets Manager configuration for the connector destination.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.update_connector_destination_request.UpdateConnectorDestinationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_connector_destination

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_connector_destination.update_connector_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.update_connector_destination_request.UpdateConnectorDestinationRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if description is not None:
            input["description"] = description
        if name is not None:
            input["name"] = name
        if auth_type is not None:
            input["auth_type"] = auth_type
        if auth_config is not None:
            input["auth_config"] = auth_config
        if secrets_manager is not None:
            input["secrets_manager"] = secrets_manager

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a connector destination linked to a cloud-to-cloud (C2C) connector.</p> <note> <p>Deletion can't be done if the account association has used this connector destination.</p> </note>

        Args:
            identifier: <p>The identifier of the connector destination.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.delete_connector_destination_request.DeleteConnectorDestinationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_connector_destination

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_connector_destination.delete_connector_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.delete_connector_destination_request.DeleteConnectorDestinationRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        cloud_connector_id: Optional[
            "aws_sdk_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
        ] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_connector_destinations_response.ListConnectorDestinationsResponse":
        """<p>Lists all connector destinations, with optional filtering by cloud connector ID.</p>

        Args:
            cloud_connector_id: <p>The identifier of the cloud connector to filter connector destinations by.</p>
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of connector destinations to return in a single response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_connector_destinations_request.ListConnectorDestinationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_connector_destinations_response.ListConnectorDestinationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_connector_destinations

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_connector_destinations.list_connector_destinations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.list_connector_destinations_request.ListConnectorDestinationsRequest = {}  # type: ignore[typeddict-item]
        if cloud_connector_id is not None:
            input["cloud_connector_id"] = cloud_connector_id
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


class AsyncConnectorDestinationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        cloud_connector_id: "aws_sdk_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        auth_config: "aws_sdk_iot_managed_integrations.types.auth_config.AuthConfig",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_destination_name.ConnectorDestinationName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_destination_description.ConnectorDestinationDescription"
        ] = None,
        auth_type: Optional[
            "aws_sdk_iot_managed_integrations.types.auth_type.AuthType"
        ] = None,
        secrets_manager: Optional[
            "aws_sdk_iot_managed_integrations.types.secrets_manager.SecretsManager"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_connector_destination_response.CreateConnectorDestinationResponse":
        """<p>Create a connector destination for connecting a cloud-to-cloud (C2C) connector to the customer's Amazon Web Services account.</p>

        Args:
            name: <p>The display name of the connector destination.</p>
            description: <p>A description of the connector destination.</p>
            cloud_connector_id: <p>The identifier of the C2C connector.</p>
            auth_type: <p>The authentication type used for the connector destination, which determines how credentials and access are managed.</p>
            auth_config: <p>The authentication configuration details for the connector destination, including OAuth settings and other authentication parameters.</p>
            secrets_manager: <p>The AWS Secrets Manager configuration used to securely store and manage sensitive information for the connector destination.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.create_connector_destination_request.CreateConnectorDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_connector_destination_response.CreateConnectorDestinationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_connector_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_connector_destination.async_create_connector_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.create_connector_destination_request.CreateConnectorDestinationRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        input["cloud_connector_id"] = cloud_connector_id
        if auth_type is not None:
            input["auth_type"] = auth_type
        input["auth_config"] = auth_config
        if secrets_manager is not None:
            input["secrets_manager"] = secrets_manager
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
        identifier: "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_connector_destination_response.GetConnectorDestinationResponse":
        """<p>Get connector destination details linked to a cloud-to-cloud (C2C) connector.</p>

        Args:
            identifier: <p>The identifier of the C2C connector destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_connector_destination_request.GetConnectorDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_connector_destination_response.GetConnectorDestinationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_connector_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_connector_destination.async_get_connector_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.get_connector_destination_request.GetConnectorDestinationRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_destination_description.ConnectorDestinationDescription"
        ] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_destination_name.ConnectorDestinationName"
        ] = None,
        auth_type: Optional[
            "aws_sdk_iot_managed_integrations.types.auth_type.AuthType"
        ] = None,
        auth_config: Optional[
            "aws_sdk_iot_managed_integrations.types.auth_config_update.AuthConfigUpdate"
        ] = None,
        secrets_manager: Optional[
            "aws_sdk_iot_managed_integrations.types.secrets_manager.SecretsManager"
        ] = None,
    ) -> None:
        """<p>Updates the properties of an existing connector destination.</p>

        Args:
            identifier: <p>The unique identifier of the connector destination to update.</p>
            description: <p>The new description to assign to the connector destination.</p>
            name: <p>The new display name to assign to the connector destination.</p>
            auth_type: <p>The new authentication type to use for the connector destination.</p>
            auth_config: <p>The updated authentication configuration details for the connector destination.</p>
            secrets_manager: <p>The updated AWS Secrets Manager configuration for the connector destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.update_connector_destination_request.UpdateConnectorDestinationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_connector_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_connector_destination.async_update_connector_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.update_connector_destination_request.UpdateConnectorDestinationRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if description is not None:
            input["description"] = description
        if name is not None:
            input["name"] = name
        if auth_type is not None:
            input["auth_type"] = auth_type
        if auth_config is not None:
            input["auth_config"] = auth_config
        if secrets_manager is not None:
            input["secrets_manager"] = secrets_manager

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a connector destination linked to a cloud-to-cloud (C2C) connector.</p> <note> <p>Deletion can't be done if the account association has used this connector destination.</p> </note>

        Args:
            identifier: <p>The identifier of the connector destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.delete_connector_destination_request.DeleteConnectorDestinationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_connector_destination

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_connector_destination.async_delete_connector_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.delete_connector_destination_request.DeleteConnectorDestinationRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        cloud_connector_id: Optional[
            "aws_sdk_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
        ] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_connector_destinations_response.ListConnectorDestinationsResponse":
        """<p>Lists all connector destinations, with optional filtering by cloud connector ID.</p>

        Args:
            cloud_connector_id: <p>The identifier of the cloud connector to filter connector destinations by.</p>
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of connector destinations to return in a single response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_connector_destinations_request.ListConnectorDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_connector_destinations_response.ListConnectorDestinationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_connector_destinations

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_connector_destinations.async_list_connector_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.list_connector_destinations_request.ListConnectorDestinationsRequest = {}  # type: ignore[typeddict-item]
        if cloud_connector_id is not None:
            input["cloud_connector_id"] = cloud_connector_id
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
