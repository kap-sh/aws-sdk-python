from __future__ import annotations

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
    import aws_sdk_partnercentral_account.types.access_type
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.get_connection_preferences_request
    import aws_sdk_partnercentral_account.types.get_connection_preferences_response
    import aws_sdk_partnercentral_account.types.participant_identifier_list
    import aws_sdk_partnercentral_account.types.revision
    import aws_sdk_partnercentral_account.types.update_connection_preferences_request
    import aws_sdk_partnercentral_account.types.update_connection_preferences_response
    from aws_sdk_partnercentral_account._services.async_partner_central_account import (
        AsyncPartnerCentralAccountClient,
        AsyncPartnerCentralAccountClientConfig,
    )
    from aws_sdk_partnercentral_account._services.partner_central_account import (
        PartnerCentralAccountClient,
        PartnerCentralAccountClientConfig,
    )


class ConnectionPreferences:
    def __init__(self, service: PartnerCentralAccountClient) -> None:
        self._service = service

    def read(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_connection_preferences_response.GetConnectionPreferencesResponse":
        """<p>Retrieves the connection preferences for a partner account, including access settings and exclusions.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.get_connection_preferences_request.GetConnectionPreferencesRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.get_connection_preferences_response.GetConnectionPreferencesResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_connection_preferences

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.get_connection_preferences.get_connection_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.get_connection_preferences_request.GetConnectionPreferencesRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_connection_preferences(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        revision: "aws_sdk_partnercentral_account.types.revision.Revision",
        access_type: "aws_sdk_partnercentral_account.types.access_type.AccessType",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        excluded_participant_identifiers: Optional[
            "aws_sdk_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.update_connection_preferences_response.UpdateConnectionPreferencesResponse":
        """<p>Updates the connection preferences for a partner account, modifying access settings and exclusions.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            revision: <p>The revision number of the connection preferences for optimistic locking.</p>
            access_type: <p>The access type setting for connections (e.g., open, restricted, invitation-only).</p>
            excluded_participant_identifiers: <p>The updated list of participant identifiers to exclude from connections.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.update_connection_preferences_request.UpdateConnectionPreferencesRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.update_connection_preferences_response.UpdateConnectionPreferencesResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.update_connection_preferences

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.update_connection_preferences.update_connection_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.update_connection_preferences_request.UpdateConnectionPreferencesRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["revision"] = revision
        input_["access_type"] = access_type
        if excluded_participant_identifiers is not None:
            input_["excluded_participant_identifiers"] = (
                excluded_participant_identifiers
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncConnectionPreferences:
    def __init__(self, service: AsyncPartnerCentralAccountClient) -> None:
        self._service = service

    async def read(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_connection_preferences_response.GetConnectionPreferencesResponse":
        """<p>Retrieves the connection preferences for a partner account, including access settings and exclusions.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.get_connection_preferences_request.GetConnectionPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.get_connection_preferences_response.GetConnectionPreferencesResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_connection_preferences

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.get_connection_preferences.async_get_connection_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.get_connection_preferences_request.GetConnectionPreferencesRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_connection_preferences(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        revision: "aws_sdk_partnercentral_account.types.revision.Revision",
        access_type: "aws_sdk_partnercentral_account.types.access_type.AccessType",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        excluded_participant_identifiers: Optional[
            "aws_sdk_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.update_connection_preferences_response.UpdateConnectionPreferencesResponse":
        """<p>Updates the connection preferences for a partner account, modifying access settings and exclusions.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            revision: <p>The revision number of the connection preferences for optimistic locking.</p>
            access_type: <p>The access type setting for connections (e.g., open, restricted, invitation-only).</p>
            excluded_participant_identifiers: <p>The updated list of participant identifiers to exclude from connections.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.update_connection_preferences_request.UpdateConnectionPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.update_connection_preferences_response.UpdateConnectionPreferencesResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.update_connection_preferences

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.update_connection_preferences.async_update_connection_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.update_connection_preferences_request.UpdateConnectionPreferencesRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["revision"] = revision
        input_["access_type"] = access_type
        if excluded_participant_identifiers is not None:
            input_["excluded_participant_identifiers"] = (
                excluded_participant_identifiers
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
