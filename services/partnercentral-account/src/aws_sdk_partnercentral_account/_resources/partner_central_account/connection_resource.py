from typing import TYPE_CHECKING, Optional

from aws_sdk_partnercentral_account._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.cancel_connection_request
    import aws_sdk_partnercentral_account.types.cancel_connection_response
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.connection_id
    import aws_sdk_partnercentral_account.types.connection_summary
    import aws_sdk_partnercentral_account.types.connection_type
    import aws_sdk_partnercentral_account.types.connection_type_filter
    import aws_sdk_partnercentral_account.types.get_connection_request
    import aws_sdk_partnercentral_account.types.get_connection_response
    import aws_sdk_partnercentral_account.types.list_connections_request
    import aws_sdk_partnercentral_account.types.list_connections_response
    import aws_sdk_partnercentral_account.types.max_results
    import aws_sdk_partnercentral_account.types.next_token
    import aws_sdk_partnercentral_account.types.participant_identifier_list
    from aws_sdk_partnercentral_account._services.async_partner_central_account import (
        AsyncPartnerCentralAccountClient,
        AsyncPartnerCentralAccountClientConfig,
    )
    from aws_sdk_partnercentral_account._services.partner_central_account import (
        PartnerCentralAccountClient,
        PartnerCentralAccountClientConfig,
    )


class ConnectionResource:
    def __init__(self, service: PartnerCentralAccountClient) -> None:
        self._service = service

    def read(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_connection_response.GetConnectionResponse":
        """<p>Retrieves detailed information about a specific connection between partners.</p>

        Args:
            catalog: <p>The catalog identifier where the connection exists.</p>
            identifier: <p>The unique identifier of the connection to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.get_connection_request.GetConnectionRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.get_connection_response.GetConnectionResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_connection

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.get_connection.get_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.get_connection_request.GetConnectionRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "aws_sdk_partnercentral_account.types.next_token.NextToken"
        ] = None,
        connection_type: Optional[
            "aws_sdk_partnercentral_account.types.connection_type_filter.ConnectionTypeFilter"
        ] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_account.types.max_results.MaxResults"
        ] = None,
        other_participant_identifiers: Optional[
            "aws_sdk_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.list_connections_response.ListConnectionsResponse":
        """<p>Lists active connections for the partner account, with optional filtering by connection type and participant.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>
            connection_type: <p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>
            max_results: <p>The maximum number of connections to return in a single response.</p>
            other_participant_identifiers: <p>Filter results by specific participant identifiers.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.list_connections_request.ListConnectionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.list_connections_response.ListConnectionsResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.list_connections

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.list_connections.list_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.list_connections_request.ListConnectionsRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if next_token is not None:
            input["next_token"] = next_token
        if connection_type is not None:
            input["connection_type"] = connection_type
        if max_results is not None:
            input["max_results"] = max_results
        if other_participant_identifiers is not None:
            input["other_participant_identifiers"] = other_participant_identifiers

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_connection(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_id.ConnectionId",
        connection_type: "aws_sdk_partnercentral_account.types.connection_type.ConnectionType",
        reason: str,
        client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.cancel_connection_response.CancelConnectionResponse":
        """<p>Cancels an existing connection between partners, terminating the partnership relationship.</p>

        Args:
            catalog: <p>The catalog identifier where the connection exists.</p>
            identifier: <p>The unique identifier of the connection to cancel.</p>
            connection_type: <p>The type of connection to cancel (e.g., reseller, distributor, technology partner).</p>
            reason: <p>The reason for canceling the connection, providing context for the termination.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.cancel_connection_request.CancelConnectionRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.cancel_connection_response.CancelConnectionResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.cancel_connection

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.cancel_connection.cancel_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.cancel_connection_request.CancelConnectionRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        input["connection_type"] = connection_type
        input["reason"] = reason
        input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncConnectionResource:
    def __init__(self, service: AsyncPartnerCentralAccountClient) -> None:
        self._service = service

    async def read(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_connection_response.GetConnectionResponse":
        """<p>Retrieves detailed information about a specific connection between partners.</p>

        Args:
            catalog: <p>The catalog identifier where the connection exists.</p>
            identifier: <p>The unique identifier of the connection to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.get_connection_request.GetConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.get_connection_response.GetConnectionResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_connection

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.get_connection.async_get_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.get_connection_request.GetConnectionRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "aws_sdk_partnercentral_account.types.next_token.NextToken"
        ] = None,
        connection_type: Optional[
            "aws_sdk_partnercentral_account.types.connection_type_filter.ConnectionTypeFilter"
        ] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_account.types.max_results.MaxResults"
        ] = None,
        other_participant_identifiers: Optional[
            "aws_sdk_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.list_connections_response.ListConnectionsResponse":
        """<p>Lists active connections for the partner account, with optional filtering by connection type and participant.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>
            connection_type: <p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>
            max_results: <p>The maximum number of connections to return in a single response.</p>
            other_participant_identifiers: <p>Filter results by specific participant identifiers.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.list_connections_request.ListConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.list_connections_response.ListConnectionsResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.list_connections

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.list_connections.async_list_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.list_connections_request.ListConnectionsRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if next_token is not None:
            input["next_token"] = next_token
        if connection_type is not None:
            input["connection_type"] = connection_type
        if max_results is not None:
            input["max_results"] = max_results
        if other_participant_identifiers is not None:
            input["other_participant_identifiers"] = other_participant_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_connection(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_id.ConnectionId",
        connection_type: "aws_sdk_partnercentral_account.types.connection_type.ConnectionType",
        reason: str,
        client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.cancel_connection_response.CancelConnectionResponse":
        """<p>Cancels an existing connection between partners, terminating the partnership relationship.</p>

        Args:
            catalog: <p>The catalog identifier where the connection exists.</p>
            identifier: <p>The unique identifier of the connection to cancel.</p>
            connection_type: <p>The type of connection to cancel (e.g., reseller, distributor, technology partner).</p>
            reason: <p>The reason for canceling the connection, providing context for the termination.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.cancel_connection_request.CancelConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.cancel_connection_response.CancelConnectionResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.cancel_connection

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.cancel_connection.async_cancel_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.cancel_connection_request.CancelConnectionRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        input["connection_type"] = connection_type
        input["reason"] = reason
        input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
