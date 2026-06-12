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
    import aws_sdk_iot_managed_integrations.types.account_association_description
    import aws_sdk_iot_managed_integrations.types.account_association_id
    import aws_sdk_iot_managed_integrations.types.account_association_item
    import aws_sdk_iot_managed_integrations.types.account_association_name
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.connector_destination_id
    import aws_sdk_iot_managed_integrations.types.create_account_association_request
    import aws_sdk_iot_managed_integrations.types.create_account_association_response
    import aws_sdk_iot_managed_integrations.types.delete_account_association_request
    import aws_sdk_iot_managed_integrations.types.general_authorization_name
    import aws_sdk_iot_managed_integrations.types.get_account_association_request
    import aws_sdk_iot_managed_integrations.types.get_account_association_response
    import aws_sdk_iot_managed_integrations.types.list_account_associations_request
    import aws_sdk_iot_managed_integrations.types.list_account_associations_response
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.start_account_association_refresh_request
    import aws_sdk_iot_managed_integrations.types.start_account_association_refresh_response
    import aws_sdk_iot_managed_integrations.types.tags_map
    import aws_sdk_iot_managed_integrations.types.update_account_association_request
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class AccountAssociationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        connector_destination_id: "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_name.AccountAssociationName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
        general_authorization: Optional[
            "aws_sdk_iot_managed_integrations.types.general_authorization_name.GeneralAuthorizationName"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse":
        """<p>Creates a new account association via the destination id.</p>

        Args:
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            connector_destination_id: <p>The identifier of the connector destination.</p>
            name: <p>The name of the destination for the new account association.</p>
            description: <p>A description of the account association request.</p>
            tags: <p>A set of key/value pairs that are used to manage the account association.</p>
            general_authorization: <p>The General Authorization reference by authorization material name.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_account_association

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_account_association.create_account_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["connector_destination_id"] = connector_destination_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        if general_authorization is not None:
            input["general_authorization"] = general_authorization

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse":
        """<p>Get an account association for an Amazon Web Services account linked to a customer-managed destination.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_account_association_request.GetAccountAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_account_association

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_account_association.get_account_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.get_account_association_request.GetAccountAssociationRequest = {}  # type: ignore[typeddict-item]
        input["account_association_id"] = account_association_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_name.AccountAssociationName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
        ] = None,
    ) -> None:
        """<p>Updates the properties of an existing account association.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to update.</p>
            name: <p>The new name to assign to the account association.</p>
            description: <p>The new description to assign to the account association.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.update_account_association_request.UpdateAccountAssociationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_account_association

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_account_association.update_account_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.update_account_association_request.UpdateAccountAssociationRequest = {}  # type: ignore[typeddict-item]
        input["account_association_id"] = account_association_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Remove a third-party account association for an end user.</p> <note> <p>You must first call the <code>DeregisterAccountAssociation</code> to remove the connection between the managed thing and the third-party account before calling the <code>DeleteAccountAssociation</code> API.</p> </note>

        Args:
            account_association_id: <p>The unique identifier of the account association to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.delete_account_association_request.DeleteAccountAssociationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_account_association

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_account_association.delete_account_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.delete_account_association_request.DeleteAccountAssociationRequest = {}  # type: ignore[typeddict-item]
        input["account_association_id"] = account_association_id

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
        connector_destination_id: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_account_associations_response.ListAccountAssociationsResponse":
        """<p>Lists all account associations, with optional filtering by connector destination ID.</p>

        Args:
            connector_destination_id: <p>The identifier of the connector destination to filter account associations by.</p>
            max_results: <p>The maximum number of account associations to return in a single response.</p>
            next_token: <p>A token used for pagination of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_account_associations_request.ListAccountAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_account_associations_response.ListAccountAssociationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_account_associations

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_account_associations.list_account_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.list_account_associations_request.ListAccountAssociationsRequest = {}  # type: ignore[typeddict-item]
        if connector_destination_id is not None:
            input["connector_destination_id"] = connector_destination_id
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

    def start_account_association_refresh(
        self,
        account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse":
        """<p>Initiates a refresh of an existing account association to update its authorization and connection status.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to refresh.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.start_account_association_refresh_request.StartAccountAssociationRefreshRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.start_account_association_refresh

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.start_account_association_refresh.start_account_association_refresh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.start_account_association_refresh_request.StartAccountAssociationRefreshRequest = {}  # type: ignore[typeddict-item]
        input["account_association_id"] = account_association_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAccountAssociationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        connector_destination_id: "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_name.AccountAssociationName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
        general_authorization: Optional[
            "aws_sdk_iot_managed_integrations.types.general_authorization_name.GeneralAuthorizationName"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse":
        """<p>Creates a new account association via the destination id.</p>

        Args:
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            connector_destination_id: <p>The identifier of the connector destination.</p>
            name: <p>The name of the destination for the new account association.</p>
            description: <p>A description of the account association request.</p>
            tags: <p>A set of key/value pairs that are used to manage the account association.</p>
            general_authorization: <p>The General Authorization reference by authorization material name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_account_association

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_account_association.async_create_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["connector_destination_id"] = connector_destination_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        if general_authorization is not None:
            input["general_authorization"] = general_authorization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse":
        """<p>Get an account association for an Amazon Web Services account linked to a customer-managed destination.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_account_association_request.GetAccountAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_account_association

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_account_association.async_get_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.get_account_association_request.GetAccountAssociationRequest = {}  # type: ignore[typeddict-item]
        input["account_association_id"] = account_association_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_name.AccountAssociationName"
        ] = None,
        description: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
        ] = None,
    ) -> None:
        """<p>Updates the properties of an existing account association.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to update.</p>
            name: <p>The new name to assign to the account association.</p>
            description: <p>The new description to assign to the account association.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.update_account_association_request.UpdateAccountAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_account_association

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.update_account_association.async_update_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.update_account_association_request.UpdateAccountAssociationRequest = {}  # type: ignore[typeddict-item]
        input["account_association_id"] = account_association_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Remove a third-party account association for an end user.</p> <note> <p>You must first call the <code>DeregisterAccountAssociation</code> to remove the connection between the managed thing and the third-party account before calling the <code>DeleteAccountAssociation</code> API.</p> </note>

        Args:
            account_association_id: <p>The unique identifier of the account association to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.delete_account_association_request.DeleteAccountAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_account_association

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_account_association.async_delete_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.delete_account_association_request.DeleteAccountAssociationRequest = {}  # type: ignore[typeddict-item]
        input["account_association_id"] = account_association_id

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
        connector_destination_id: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_account_associations_response.ListAccountAssociationsResponse":
        """<p>Lists all account associations, with optional filtering by connector destination ID.</p>

        Args:
            connector_destination_id: <p>The identifier of the connector destination to filter account associations by.</p>
            max_results: <p>The maximum number of account associations to return in a single response.</p>
            next_token: <p>A token used for pagination of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_account_associations_request.ListAccountAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_account_associations_response.ListAccountAssociationsResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_account_associations

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_account_associations.async_list_account_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.list_account_associations_request.ListAccountAssociationsRequest = {}  # type: ignore[typeddict-item]
        if connector_destination_id is not None:
            input["connector_destination_id"] = connector_destination_id
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

    async def start_account_association_refresh(
        self,
        account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse":
        """<p>Initiates a refresh of an existing account association to update its authorization and connection status.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to refresh.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.start_account_association_refresh_request.StartAccountAssociationRefreshRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.start_account_association_refresh

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.start_account_association_refresh.async_start_account_association_refresh(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iot_managed_integrations.types.start_account_association_refresh_request.StartAccountAssociationRefreshRequest = {}  # type: ignore[typeddict-item]
        input["account_association_id"] = account_association_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
