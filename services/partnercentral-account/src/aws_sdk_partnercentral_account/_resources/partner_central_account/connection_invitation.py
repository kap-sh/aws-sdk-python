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
    import aws_sdk_partnercentral_account.types.accept_connection_invitation_request
    import aws_sdk_partnercentral_account.types.accept_connection_invitation_response
    import aws_sdk_partnercentral_account.types.cancel_connection_invitation_request
    import aws_sdk_partnercentral_account.types.cancel_connection_invitation_response
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.connection_invitation_id
    import aws_sdk_partnercentral_account.types.connection_invitation_summary
    import aws_sdk_partnercentral_account.types.connection_type
    import aws_sdk_partnercentral_account.types.create_connection_invitation_request
    import aws_sdk_partnercentral_account.types.create_connection_invitation_response
    import aws_sdk_partnercentral_account.types.email
    import aws_sdk_partnercentral_account.types.get_connection_invitation_request
    import aws_sdk_partnercentral_account.types.get_connection_invitation_response
    import aws_sdk_partnercentral_account.types.invitation_status
    import aws_sdk_partnercentral_account.types.list_connection_invitations_request
    import aws_sdk_partnercentral_account.types.list_connection_invitations_response
    import aws_sdk_partnercentral_account.types.max_results
    import aws_sdk_partnercentral_account.types.next_token
    import aws_sdk_partnercentral_account.types.participant_identifier
    import aws_sdk_partnercentral_account.types.participant_identifier_list
    import aws_sdk_partnercentral_account.types.participant_type
    import aws_sdk_partnercentral_account.types.reject_connection_invitation_request
    import aws_sdk_partnercentral_account.types.reject_connection_invitation_response
    import aws_sdk_partnercentral_account.types.sensitive_unicode_string
    import aws_sdk_partnercentral_account.types.unicode_string_including_new_line
    from aws_sdk_partnercentral_account._services.async_partner_central_account import (
        AsyncPartnerCentralAccountClient,
        AsyncPartnerCentralAccountClientConfig,
    )
    from aws_sdk_partnercentral_account._services.partner_central_account import (
        PartnerCentralAccountClient,
        PartnerCentralAccountClientConfig,
    )


class ConnectionInvitation:
    def __init__(self, service: PartnerCentralAccountClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken",
        connection_type: "aws_sdk_partnercentral_account.types.connection_type.ConnectionType",
        email: "aws_sdk_partnercentral_account.types.email.Email",
        message: "aws_sdk_partnercentral_account.types.unicode_string_including_new_line.UnicodeStringIncludingNewLine",
        name: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString",
        receiver_identifier: "aws_sdk_partnercentral_account.types.participant_identifier.ParticipantIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse":
        """<p>Creates a new connection invitation to establish a partnership with another organization.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation will be created.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            connection_type: <p>The type of connection being requested (e.g., reseller, distributor, technology partner).</p>
            email: <p>The email address of the person to send the connection invitation to.</p>
            message: <p>A custom message to include with the connection invitation.</p>
            name: <p>The name of the person sending the connection invitation.</p>
            receiver_identifier: <p>The identifier of the organization or partner to invite for connection.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.create_connection_invitation

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.create_connection_invitation.create_connection_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["client_token"] = client_token
        input_["connection_type"] = connection_type
        input_["email"] = email
        input_["message"] = message
        input_["name"] = name
        input_["receiver_identifier"] = receiver_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse":
        """<p>Retrieves detailed information about a specific connection invitation.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.get_connection_invitation_request.GetConnectionInvitationRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_connection_invitation

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.get_connection_invitation.get_connection_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.get_connection_invitation_request.GetConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
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
            "aws_sdk_partnercentral_account.types.connection_type.ConnectionType"
        ] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_account.types.max_results.MaxResults"
        ] = None,
        other_participant_identifiers: Optional[
            "aws_sdk_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
        participant_type: Optional[
            "aws_sdk_partnercentral_account.types.participant_type.ParticipantType"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_account.types.invitation_status.InvitationStatus"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.list_connection_invitations_response.ListConnectionInvitationsResponse":
        """<p>Lists connection invitations for the partner account, with optional filtering by status, type, and other criteria.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>
            connection_type: <p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>
            max_results: <p>The maximum number of connection invitations to return in a single response.</p>
            other_participant_identifiers: <p>Filter results by specific participant identifiers.</p>
            participant_type: <p>Filter results by participant type (inviter or invitee).</p>
            status: <p>Filter results by invitation status (pending, accepted, rejected, canceled, expired).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.list_connection_invitations_request.ListConnectionInvitationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.list_connection_invitations_response.ListConnectionInvitationsResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.list_connection_invitations

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.list_connection_invitations.list_connection_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.list_connection_invitations_request.ListConnectionInvitationsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if next_token is not None:
            input_["next_token"] = next_token
        if connection_type is not None:
            input_["connection_type"] = connection_type
        if max_results is not None:
            input_["max_results"] = max_results
        if other_participant_identifiers is not None:
            input_["other_participant_identifiers"] = other_participant_identifiers
        if participant_type is not None:
            input_["participant_type"] = participant_type
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def accept_connection_invitation(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse":
        """<p>Accepts a connection invitation from another partner, establishing a formal partnership connection between the two parties.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to accept.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.accept_connection_invitation_request.AcceptConnectionInvitationRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.accept_connection_invitation

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.accept_connection_invitation.accept_connection_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.accept_connection_invitation_request.AcceptConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_connection_invitation(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse":
        """<p>Cancels a pending connection invitation before it has been accepted or rejected.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to cancel.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.cancel_connection_invitation_request.CancelConnectionInvitationRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.cancel_connection_invitation

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.cancel_connection_invitation.cancel_connection_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.cancel_connection_invitation_request.CancelConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reject_connection_invitation(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        reason: Optional[str] = None,
    ) -> "aws_sdk_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse":
        """<p>Rejects a connection invitation from another partner, declining the partnership request.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to reject.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            reason: <p>The reason for rejecting the connection invitation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.reject_connection_invitation_request.RejectConnectionInvitationRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.reject_connection_invitation

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.reject_connection_invitation.reject_connection_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.reject_connection_invitation_request.RejectConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
        input_["client_token"] = client_token
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncConnectionInvitation:
    def __init__(self, service: AsyncPartnerCentralAccountClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken",
        connection_type: "aws_sdk_partnercentral_account.types.connection_type.ConnectionType",
        email: "aws_sdk_partnercentral_account.types.email.Email",
        message: "aws_sdk_partnercentral_account.types.unicode_string_including_new_line.UnicodeStringIncludingNewLine",
        name: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString",
        receiver_identifier: "aws_sdk_partnercentral_account.types.participant_identifier.ParticipantIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse":
        """<p>Creates a new connection invitation to establish a partnership with another organization.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation will be created.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            connection_type: <p>The type of connection being requested (e.g., reseller, distributor, technology partner).</p>
            email: <p>The email address of the person to send the connection invitation to.</p>
            message: <p>A custom message to include with the connection invitation.</p>
            name: <p>The name of the person sending the connection invitation.</p>
            receiver_identifier: <p>The identifier of the organization or partner to invite for connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.create_connection_invitation

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.create_connection_invitation.async_create_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["client_token"] = client_token
        input_["connection_type"] = connection_type
        input_["email"] = email
        input_["message"] = message
        input_["name"] = name
        input_["receiver_identifier"] = receiver_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse":
        """<p>Retrieves detailed information about a specific connection invitation.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.get_connection_invitation_request.GetConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_connection_invitation

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.get_connection_invitation.async_get_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.get_connection_invitation_request.GetConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
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
            "aws_sdk_partnercentral_account.types.connection_type.ConnectionType"
        ] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_account.types.max_results.MaxResults"
        ] = None,
        other_participant_identifiers: Optional[
            "aws_sdk_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
        participant_type: Optional[
            "aws_sdk_partnercentral_account.types.participant_type.ParticipantType"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_account.types.invitation_status.InvitationStatus"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.list_connection_invitations_response.ListConnectionInvitationsResponse":
        """<p>Lists connection invitations for the partner account, with optional filtering by status, type, and other criteria.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>
            connection_type: <p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>
            max_results: <p>The maximum number of connection invitations to return in a single response.</p>
            other_participant_identifiers: <p>Filter results by specific participant identifiers.</p>
            participant_type: <p>Filter results by participant type (inviter or invitee).</p>
            status: <p>Filter results by invitation status (pending, accepted, rejected, canceled, expired).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.list_connection_invitations_request.ListConnectionInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.list_connection_invitations_response.ListConnectionInvitationsResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.list_connection_invitations

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.list_connection_invitations.async_list_connection_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.list_connection_invitations_request.ListConnectionInvitationsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if next_token is not None:
            input_["next_token"] = next_token
        if connection_type is not None:
            input_["connection_type"] = connection_type
        if max_results is not None:
            input_["max_results"] = max_results
        if other_participant_identifiers is not None:
            input_["other_participant_identifiers"] = other_participant_identifiers
        if participant_type is not None:
            input_["participant_type"] = participant_type
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_connection_invitation(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse":
        """<p>Accepts a connection invitation from another partner, establishing a formal partnership connection between the two parties.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to accept.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.accept_connection_invitation_request.AcceptConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.accept_connection_invitation

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.accept_connection_invitation.async_accept_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.accept_connection_invitation_request.AcceptConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_connection_invitation(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse":
        """<p>Cancels a pending connection invitation before it has been accepted or rejected.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to cancel.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.cancel_connection_invitation_request.CancelConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.cancel_connection_invitation

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.cancel_connection_invitation.async_cancel_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.cancel_connection_invitation_request.CancelConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reject_connection_invitation(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "aws_sdk_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        reason: Optional[str] = None,
    ) -> "aws_sdk_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse":
        """<p>Rejects a connection invitation from another partner, declining the partnership request.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to reject.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            reason: <p>The reason for rejecting the connection invitation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.reject_connection_invitation_request.RejectConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.reject_connection_invitation

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.reject_connection_invitation.async_reject_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.reject_connection_invitation_request.RejectConnectionInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
        input_["client_token"] = client_token
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
