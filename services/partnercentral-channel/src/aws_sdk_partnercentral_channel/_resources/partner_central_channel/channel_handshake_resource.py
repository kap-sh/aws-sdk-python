from typing import TYPE_CHECKING, Optional

from aws_sdk_partnercentral_channel._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.accept_channel_handshake_request
    import aws_sdk_partnercentral_channel.types.accept_channel_handshake_response
    import aws_sdk_partnercentral_channel.types.associated_resource_identifier
    import aws_sdk_partnercentral_channel.types.associated_resource_identifier_list
    import aws_sdk_partnercentral_channel.types.cancel_channel_handshake_request
    import aws_sdk_partnercentral_channel.types.cancel_channel_handshake_response
    import aws_sdk_partnercentral_channel.types.catalog
    import aws_sdk_partnercentral_channel.types.channel_handshake_identifier
    import aws_sdk_partnercentral_channel.types.channel_handshake_payload
    import aws_sdk_partnercentral_channel.types.channel_handshake_summary
    import aws_sdk_partnercentral_channel.types.client_token
    import aws_sdk_partnercentral_channel.types.create_channel_handshake_request
    import aws_sdk_partnercentral_channel.types.create_channel_handshake_response
    import aws_sdk_partnercentral_channel.types.handshake_status_list
    import aws_sdk_partnercentral_channel.types.handshake_type
    import aws_sdk_partnercentral_channel.types.list_channel_handshakes_request
    import aws_sdk_partnercentral_channel.types.list_channel_handshakes_response
    import aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_filters
    import aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_sort
    import aws_sdk_partnercentral_channel.types.next_token
    import aws_sdk_partnercentral_channel.types.participant_type
    import aws_sdk_partnercentral_channel.types.reject_channel_handshake_request
    import aws_sdk_partnercentral_channel.types.reject_channel_handshake_response
    import aws_sdk_partnercentral_channel.types.tag_list
    from aws_sdk_partnercentral_channel._services.async_partner_central_channel import (
        AsyncPartnerCentralChannelClient,
        AsyncPartnerCentralChannelClientConfig,
    )
    from aws_sdk_partnercentral_channel._services.partner_central_channel import (
        PartnerCentralChannelClient,
        PartnerCentralChannelClientConfig,
    )


class ChannelHandshakeResource:
    def __init__(self, service: PartnerCentralChannelClient) -> None:
        self._service = service

    def create(
        self,
        handshake_type: "aws_sdk_partnercentral_channel.types.handshake_type.HandshakeType",
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        associated_resource_identifier: "aws_sdk_partnercentral_channel.types.associated_resource_identifier.AssociatedResourceIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        payload: Optional[
            "aws_sdk_partnercentral_channel.types.channel_handshake_payload.ChannelHandshakePayload"
        ] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_partnercentral_channel.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_channel.types.create_channel_handshake_response.CreateChannelHandshakeResponse":
        """<p>Creates a new channel handshake request to establish a partnership with another AWS account.</p>

        Args:
            handshake_type: <p>The type of handshake to create (e.g., start service period, revoke service period).</p>
            catalog: <p>The catalog identifier for the handshake request.</p>
            associated_resource_identifier: <p>The identifier of the resource associated with this handshake.</p>
            payload: <p>The payload containing specific details for the handshake type.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the channel handshake.</p>

        Examples:
            Example for CreateChannelHandshake - START_SERVICE_PERIOD with Minimum Notice Period

            >>> client.create(handshake_type='START_SERVICE_PERIOD', catalog='AWS', associated_resource_identifier='rs-abc123def456g', payload={'startServicePeriodPayload': {'programManagementAccountIdentifier': 'pma-abcdef123456g', 'servicePeriodType': 'MINIMUM_NOTICE_PERIOD', 'minimumNoticeDays': '14', 'note': 'Optional Note'}}, client_token='clientToken')
            Example for CreateChannelHandshake - START_SERVICE_PERIOD with Fixed Commitment Period

            >>> client.create(handshake_type='START_SERVICE_PERIOD', catalog='AWS', associated_resource_identifier='rs-abc123def456g', payload={'startServicePeriodPayload': {'programManagementAccountIdentifier': 'pma-abcdef123456g', 'servicePeriodType': 'FIXED_COMMITMENT_PERIOD', 'endDate': '2026-07-01T00:00:00Z', 'note': 'Optional Note'}}, client_token='clientToken')
            Example for CreateChannelHandshake - REVOKE_SERVICE_PERIOD

            >>> client.create(handshake_type='REVOKE_SERVICE_PERIOD', catalog='AWS', associated_resource_identifier='rs-abc123def456g', payload={'revokeServicePeriodPayload': {'programManagementAccountIdentifier': 'pma-abcdef123456g', 'note': 'Optional Note'}}, client_token='clientToken')
            Example for CreateChannelHandshake - PROGRAM_MANAGEMENT_ACCOUNT

            >>> client.create(handshake_type='PROGRAM_MANAGEMENT_ACCOUNT', catalog='AWS', associated_resource_identifier='pma-123abc456def7', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.create_channel_handshake_request.CreateChannelHandshakeRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.create_channel_handshake_response.CreateChannelHandshakeResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.create_channel_handshake

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.create_channel_handshake.create_channel_handshake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.create_channel_handshake_request.CreateChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
        input_["handshake_type"] = handshake_type
        input_["catalog"] = catalog
        input_["associated_resource_identifier"] = associated_resource_identifier
        if payload is not None:
            input_["payload"] = payload
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

    def list(
        self,
        handshake_type: "aws_sdk_partnercentral_channel.types.handshake_type.HandshakeType",
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        participant_type: "aws_sdk_partnercentral_channel.types.participant_type.ParticipantType",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        statuses: Optional[
            "aws_sdk_partnercentral_channel.types.handshake_status_list.HandshakeStatusList"
        ] = None,
        associated_resource_identifiers: Optional[
            "aws_sdk_partnercentral_channel.types.associated_resource_identifier_list.AssociatedResourceIdentifierList"
        ] = None,
        handshake_type_filters: Optional[
            "aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_filters.ListChannelHandshakesTypeFilters"
        ] = None,
        handshake_type_sort: Optional[
            "aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_sort.ListChannelHandshakesTypeSort"
        ] = None,
        next_token: Optional[
            "aws_sdk_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_channel.types.list_channel_handshakes_response.ListChannelHandshakesResponse":
        """<p>Lists channel handshakes based on specified criteria.</p>

        Args:
            handshake_type: <p>Filter results by handshake type.</p>
            catalog: <p>The catalog identifier to filter handshakes.</p>
            participant_type: <p>Filter by participant type (sender or receiver).</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            statuses: <p>Filter results by handshake status.</p>
            associated_resource_identifiers: <p>Filter by associated resource identifiers.</p>
            handshake_type_filters: <p>Type-specific filters for handshakes.</p>
            handshake_type_sort: <p>Type-specific sorting options for handshakes.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Examples:
            Example for ListChannelHandshakes - START_SERVICE_PERIOD

            >>> client.list(handshake_type='START_SERVICE_PERIOD', catalog='AWS', participant_type='SENDER', statuses=['ACCEPTED'], associated_resource_identifiers=['rs-123abc456def7'], handshake_type_filters={'startServicePeriodTypeFilters': {'servicePeriodTypes': ['FIXED_COMMITMENT_PERIOD']}}, handshake_type_sort={'startServicePeriodTypeSort': {'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}})
            Example for ListChannelHandshakes - REVOKE_SERVICE_PERIOD

            >>> client.list(handshake_type='REVOKE_SERVICE_PERIOD', catalog='AWS', participant_type='SENDER', statuses=['ACCEPTED'], associated_resource_identifiers=['rs-123abc456def7'], handshake_type_filters={'revokeServicePeriodTypeFilters': {'servicePeriodTypes': ['MINIMUM_NOTICE_PERIOD']}}, handshake_type_sort={'revokeServicePeriodTypeSort': {'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}})
            Example for ListChannelHandshakes - PROGRAM_MANAGEMENT_ACCOUNT

            >>> client.list(handshake_type='PROGRAM_MANAGEMENT_ACCOUNT', catalog='AWS', participant_type='SENDER', statuses=['ACCEPTED'], associated_resource_identifiers=['pma-123abc456def7'], handshake_type_filters={'programManagementAccountTypeFilters': {'programs': ['SOLUTION_PROVIDER']}}, handshake_type_sort={'programManagementAccountTypeSort': {'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}}, max_results=20, next_token='nextToken')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.list_channel_handshakes_request.ListChannelHandshakesRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.list_channel_handshakes_response.ListChannelHandshakesResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.list_channel_handshakes

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.list_channel_handshakes.list_channel_handshakes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.list_channel_handshakes_request.ListChannelHandshakesRequest = {}  # type: ignore[typeddict-item]
        input_["handshake_type"] = handshake_type
        input_["catalog"] = catalog
        input_["participant_type"] = participant_type
        if max_results is not None:
            input_["max_results"] = max_results
        if statuses is not None:
            input_["statuses"] = statuses
        if associated_resource_identifiers is not None:
            input_["associated_resource_identifiers"] = associated_resource_identifiers
        if handshake_type_filters is not None:
            input_["handshake_type_filters"] = handshake_type_filters
        if handshake_type_sort is not None:
            input_["handshake_type_sort"] = handshake_type_sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def accept_channel_handshake(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "aws_sdk_partnercentral_channel.types.accept_channel_handshake_response.AcceptChannelHandshakeResponse":
        """<p>Accepts a pending channel handshake request from another AWS account.</p>

        Args:
            catalog: <p>The catalog identifier for the handshake request.</p>
            identifier: <p>The unique identifier of the channel handshake to accept.</p>

        Examples:
            Example for AcceptChannelHandshake

            >>> client.accept_channel_handshake(catalog='AWS', identifier='ch-4fj3bd2o3vb91')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.accept_channel_handshake_request.AcceptChannelHandshakeRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.accept_channel_handshake_response.AcceptChannelHandshakeResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.accept_channel_handshake

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.accept_channel_handshake.accept_channel_handshake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.accept_channel_handshake_request.AcceptChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_channel_handshake(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "aws_sdk_partnercentral_channel.types.cancel_channel_handshake_response.CancelChannelHandshakeResponse":
        """<p>Cancels a pending channel handshake request.</p>

        Args:
            catalog: <p>The catalog identifier for the handshake request.</p>
            identifier: <p>The unique identifier of the channel handshake to cancel.</p>

        Examples:
            Example for CancelChannelHandshake

            >>> client.cancel_channel_handshake(catalog='AWS', identifier='ch-4fj3bd2o3vb91')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.cancel_channel_handshake_request.CancelChannelHandshakeRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.cancel_channel_handshake_response.CancelChannelHandshakeResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.cancel_channel_handshake

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.cancel_channel_handshake.cancel_channel_handshake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.cancel_channel_handshake_request.CancelChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reject_channel_handshake(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
    ) -> "aws_sdk_partnercentral_channel.types.reject_channel_handshake_response.RejectChannelHandshakeResponse":
        """<p>Rejects a pending channel handshake request.</p>

        Args:
            catalog: <p>The catalog identifier for the handshake request.</p>
            identifier: <p>The unique identifier of the channel handshake to reject.</p>

        Examples:
            Example for RejectChannelHandshake

            >>> client.reject_channel_handshake(catalog='AWS', identifier='ch-4fj3bd2o3vb91')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.reject_channel_handshake_request.RejectChannelHandshakeRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.reject_channel_handshake_response.RejectChannelHandshakeResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.reject_channel_handshake

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.reject_channel_handshake.reject_channel_handshake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.reject_channel_handshake_request.RejectChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncChannelHandshakeResource:
    def __init__(self, service: AsyncPartnerCentralChannelClient) -> None:
        self._service = service

    async def create(
        self,
        handshake_type: "aws_sdk_partnercentral_channel.types.handshake_type.HandshakeType",
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        associated_resource_identifier: "aws_sdk_partnercentral_channel.types.associated_resource_identifier.AssociatedResourceIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        payload: Optional[
            "aws_sdk_partnercentral_channel.types.channel_handshake_payload.ChannelHandshakePayload"
        ] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_partnercentral_channel.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_channel.types.create_channel_handshake_response.CreateChannelHandshakeResponse":
        """<p>Creates a new channel handshake request to establish a partnership with another AWS account.</p>

        Args:
            handshake_type: <p>The type of handshake to create (e.g., start service period, revoke service period).</p>
            catalog: <p>The catalog identifier for the handshake request.</p>
            associated_resource_identifier: <p>The identifier of the resource associated with this handshake.</p>
            payload: <p>The payload containing specific details for the handshake type.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the channel handshake.</p>

        Examples:
            Example for CreateChannelHandshake - START_SERVICE_PERIOD with Minimum Notice Period

            >>> await client.create(handshake_type='START_SERVICE_PERIOD', catalog='AWS', associated_resource_identifier='rs-abc123def456g', payload={'startServicePeriodPayload': {'programManagementAccountIdentifier': 'pma-abcdef123456g', 'servicePeriodType': 'MINIMUM_NOTICE_PERIOD', 'minimumNoticeDays': '14', 'note': 'Optional Note'}}, client_token='clientToken')
            Example for CreateChannelHandshake - START_SERVICE_PERIOD with Fixed Commitment Period

            >>> await client.create(handshake_type='START_SERVICE_PERIOD', catalog='AWS', associated_resource_identifier='rs-abc123def456g', payload={'startServicePeriodPayload': {'programManagementAccountIdentifier': 'pma-abcdef123456g', 'servicePeriodType': 'FIXED_COMMITMENT_PERIOD', 'endDate': '2026-07-01T00:00:00Z', 'note': 'Optional Note'}}, client_token='clientToken')
            Example for CreateChannelHandshake - REVOKE_SERVICE_PERIOD

            >>> await client.create(handshake_type='REVOKE_SERVICE_PERIOD', catalog='AWS', associated_resource_identifier='rs-abc123def456g', payload={'revokeServicePeriodPayload': {'programManagementAccountIdentifier': 'pma-abcdef123456g', 'note': 'Optional Note'}}, client_token='clientToken')
            Example for CreateChannelHandshake - PROGRAM_MANAGEMENT_ACCOUNT

            >>> await client.create(handshake_type='PROGRAM_MANAGEMENT_ACCOUNT', catalog='AWS', associated_resource_identifier='pma-123abc456def7', client_token='clientToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.create_channel_handshake_request.CreateChannelHandshakeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.create_channel_handshake_response.CreateChannelHandshakeResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.create_channel_handshake

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.create_channel_handshake.async_create_channel_handshake(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.create_channel_handshake_request.CreateChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
        input_["handshake_type"] = handshake_type
        input_["catalog"] = catalog
        input_["associated_resource_identifier"] = associated_resource_identifier
        if payload is not None:
            input_["payload"] = payload
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

    async def list(
        self,
        handshake_type: "aws_sdk_partnercentral_channel.types.handshake_type.HandshakeType",
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        participant_type: "aws_sdk_partnercentral_channel.types.participant_type.ParticipantType",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        statuses: Optional[
            "aws_sdk_partnercentral_channel.types.handshake_status_list.HandshakeStatusList"
        ] = None,
        associated_resource_identifiers: Optional[
            "aws_sdk_partnercentral_channel.types.associated_resource_identifier_list.AssociatedResourceIdentifierList"
        ] = None,
        handshake_type_filters: Optional[
            "aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_filters.ListChannelHandshakesTypeFilters"
        ] = None,
        handshake_type_sort: Optional[
            "aws_sdk_partnercentral_channel.types.list_channel_handshakes_type_sort.ListChannelHandshakesTypeSort"
        ] = None,
        next_token: Optional[
            "aws_sdk_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_channel.types.list_channel_handshakes_response.ListChannelHandshakesResponse":
        """<p>Lists channel handshakes based on specified criteria.</p>

        Args:
            handshake_type: <p>Filter results by handshake type.</p>
            catalog: <p>The catalog identifier to filter handshakes.</p>
            participant_type: <p>Filter by participant type (sender or receiver).</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            statuses: <p>Filter results by handshake status.</p>
            associated_resource_identifiers: <p>Filter by associated resource identifiers.</p>
            handshake_type_filters: <p>Type-specific filters for handshakes.</p>
            handshake_type_sort: <p>Type-specific sorting options for handshakes.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Examples:
            Example for ListChannelHandshakes - START_SERVICE_PERIOD

            >>> await client.list(handshake_type='START_SERVICE_PERIOD', catalog='AWS', participant_type='SENDER', statuses=['ACCEPTED'], associated_resource_identifiers=['rs-123abc456def7'], handshake_type_filters={'startServicePeriodTypeFilters': {'servicePeriodTypes': ['FIXED_COMMITMENT_PERIOD']}}, handshake_type_sort={'startServicePeriodTypeSort': {'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}})
            Example for ListChannelHandshakes - REVOKE_SERVICE_PERIOD

            >>> await client.list(handshake_type='REVOKE_SERVICE_PERIOD', catalog='AWS', participant_type='SENDER', statuses=['ACCEPTED'], associated_resource_identifiers=['rs-123abc456def7'], handshake_type_filters={'revokeServicePeriodTypeFilters': {'servicePeriodTypes': ['MINIMUM_NOTICE_PERIOD']}}, handshake_type_sort={'revokeServicePeriodTypeSort': {'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}})
            Example for ListChannelHandshakes - PROGRAM_MANAGEMENT_ACCOUNT

            >>> await client.list(handshake_type='PROGRAM_MANAGEMENT_ACCOUNT', catalog='AWS', participant_type='SENDER', statuses=['ACCEPTED'], associated_resource_identifiers=['pma-123abc456def7'], handshake_type_filters={'programManagementAccountTypeFilters': {'programs': ['SOLUTION_PROVIDER']}}, handshake_type_sort={'programManagementAccountTypeSort': {'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'}}, max_results=20, next_token='nextToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.list_channel_handshakes_request.ListChannelHandshakesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.list_channel_handshakes_response.ListChannelHandshakesResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.list_channel_handshakes

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.list_channel_handshakes.async_list_channel_handshakes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.list_channel_handshakes_request.ListChannelHandshakesRequest = {}  # type: ignore[typeddict-item]
        input_["handshake_type"] = handshake_type
        input_["catalog"] = catalog
        input_["participant_type"] = participant_type
        if max_results is not None:
            input_["max_results"] = max_results
        if statuses is not None:
            input_["statuses"] = statuses
        if associated_resource_identifiers is not None:
            input_["associated_resource_identifiers"] = associated_resource_identifiers
        if handshake_type_filters is not None:
            input_["handshake_type_filters"] = handshake_type_filters
        if handshake_type_sort is not None:
            input_["handshake_type_sort"] = handshake_type_sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_channel_handshake(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
    ) -> "aws_sdk_partnercentral_channel.types.accept_channel_handshake_response.AcceptChannelHandshakeResponse":
        """<p>Accepts a pending channel handshake request from another AWS account.</p>

        Args:
            catalog: <p>The catalog identifier for the handshake request.</p>
            identifier: <p>The unique identifier of the channel handshake to accept.</p>

        Examples:
            Example for AcceptChannelHandshake

            >>> await client.accept_channel_handshake(catalog='AWS', identifier='ch-4fj3bd2o3vb91')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.accept_channel_handshake_request.AcceptChannelHandshakeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.accept_channel_handshake_response.AcceptChannelHandshakeResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.accept_channel_handshake

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.accept_channel_handshake.async_accept_channel_handshake(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.accept_channel_handshake_request.AcceptChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_channel_handshake(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
    ) -> "aws_sdk_partnercentral_channel.types.cancel_channel_handshake_response.CancelChannelHandshakeResponse":
        """<p>Cancels a pending channel handshake request.</p>

        Args:
            catalog: <p>The catalog identifier for the handshake request.</p>
            identifier: <p>The unique identifier of the channel handshake to cancel.</p>

        Examples:
            Example for CancelChannelHandshake

            >>> await client.cancel_channel_handshake(catalog='AWS', identifier='ch-4fj3bd2o3vb91')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.cancel_channel_handshake_request.CancelChannelHandshakeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.cancel_channel_handshake_response.CancelChannelHandshakeResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.cancel_channel_handshake

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.cancel_channel_handshake.async_cancel_channel_handshake(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.cancel_channel_handshake_request.CancelChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reject_channel_handshake(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
    ) -> "aws_sdk_partnercentral_channel.types.reject_channel_handshake_response.RejectChannelHandshakeResponse":
        """<p>Rejects a pending channel handshake request.</p>

        Args:
            catalog: <p>The catalog identifier for the handshake request.</p>
            identifier: <p>The unique identifier of the channel handshake to reject.</p>

        Examples:
            Example for RejectChannelHandshake

            >>> await client.reject_channel_handshake(catalog='AWS', identifier='ch-4fj3bd2o3vb91')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.reject_channel_handshake_request.RejectChannelHandshakeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.reject_channel_handshake_response.RejectChannelHandshakeResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.reject_channel_handshake

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.reject_channel_handshake.async_reject_channel_handshake(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.reject_channel_handshake_request.RejectChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
