from typing import TYPE_CHECKING, Optional

from aws_sdk_mailmanager._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.create_relay_request
    import aws_sdk_mailmanager.types.create_relay_response
    import aws_sdk_mailmanager.types.delete_relay_request
    import aws_sdk_mailmanager.types.delete_relay_response
    import aws_sdk_mailmanager.types.get_relay_request
    import aws_sdk_mailmanager.types.get_relay_response
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.list_relays_request
    import aws_sdk_mailmanager.types.list_relays_response
    import aws_sdk_mailmanager.types.pagination_token
    import aws_sdk_mailmanager.types.relay
    import aws_sdk_mailmanager.types.relay_authentication
    import aws_sdk_mailmanager.types.relay_id
    import aws_sdk_mailmanager.types.relay_name
    import aws_sdk_mailmanager.types.relay_server_name
    import aws_sdk_mailmanager.types.relay_server_port
    import aws_sdk_mailmanager.types.tag_list
    import aws_sdk_mailmanager.types.update_relay_request
    import aws_sdk_mailmanager.types.update_relay_response
    from aws_sdk_mailmanager._services.async_mail_manager import (
        AsyncMailManagerClient,
        AsyncMailManagerClientConfig,
    )
    from aws_sdk_mailmanager._services.mail_manager import (
        MailManagerClient,
        MailManagerClientConfig,
    )


class RelayResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        relay_name: "aws_sdk_mailmanager.types.relay_name.RelayName",
        server_name: "aws_sdk_mailmanager.types.relay_server_name.RelayServerName",
        server_port: "aws_sdk_mailmanager.types.relay_server_port.RelayServerPort",
        authentication: "aws_sdk_mailmanager.types.relay_authentication.RelayAuthentication",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_relay_response.CreateRelayResponse":
        """<p>Creates a relay resource which can be used in rules to relay incoming emails to defined relay destinations. </p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            relay_name: <p>The unique name of the relay resource.</p>
            server_name: <p>The destination relay server address.</p>
            server_port: <p>The destination relay server port.</p>
            authentication: <p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.create_relay_request.CreateRelayRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.create_relay_response.CreateRelayResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_relay

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.create_relay.create_relay(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_relay_request.CreateRelayRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["relay_name"] = relay_name
        input_["server_name"] = server_name
        input_["server_port"] = server_port
        input_["authentication"] = authentication
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        relay_id: "aws_sdk_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_relay_response.GetRelayResponse":
        """<p>Fetch the relay resource and it's attributes.</p>

        Args:
            relay_id: <p>A unique relay identifier.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_relay_request.GetRelayRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_relay_response.GetRelayResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_relay

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_relay.get_relay(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_relay_request.GetRelayRequest = {}  # type: ignore[typeddict-item]
        input_["relay_id"] = relay_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        relay_id: "aws_sdk_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        relay_name: Optional["aws_sdk_mailmanager.types.relay_name.RelayName"] = None,
        server_name: Optional[
            "aws_sdk_mailmanager.types.relay_server_name.RelayServerName"
        ] = None,
        server_port: Optional[
            "aws_sdk_mailmanager.types.relay_server_port.RelayServerPort"
        ] = None,
        authentication: Optional[
            "aws_sdk_mailmanager.types.relay_authentication.RelayAuthentication"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.update_relay_response.UpdateRelayResponse":
        """<p>Updates the attributes of an existing relay resource.</p>

        Args:
            relay_id: <p>The unique relay identifier.</p>
            relay_name: <p>The name of the relay resource.</p>
            server_name: <p>The destination relay server address.</p>
            server_port: <p>The destination relay server port.</p>
            authentication: <p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.update_relay_request.UpdateRelayRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.update_relay_response.UpdateRelayResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.update_relay

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.update_relay.update_relay(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.update_relay_request.UpdateRelayRequest = {}  # type: ignore[typeddict-item]
        input_["relay_id"] = relay_id
        if relay_name is not None:
            input_["relay_name"] = relay_name
        if server_name is not None:
            input_["server_name"] = server_name
        if server_port is not None:
            input_["server_port"] = server_port
        if authentication is not None:
            input_["authentication"] = authentication

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        relay_id: "aws_sdk_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_relay_response.DeleteRelayResponse":
        """<p>Deletes an existing relay resource.</p>

        Args:
            relay_id: <p>The unique relay identifier.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.delete_relay_request.DeleteRelayRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.delete_relay_response.DeleteRelayResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_relay

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.delete_relay.delete_relay(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.delete_relay_request.DeleteRelayRequest = {}  # type: ignore[typeddict-item]
        input_["relay_id"] = relay_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        page_size: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.list_relays_response.ListRelaysResponse":
        """<p>Lists all the existing relay resources.</p>

        Args:
            page_size: <p>The number of relays to be returned in one request.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_relays_request.ListRelaysRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_relays_response.ListRelaysResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_relays

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_relays.list_relays(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_relays_request.ListRelaysRequest = {}  # type: ignore[typeddict-item]
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRelayResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        relay_name: "aws_sdk_mailmanager.types.relay_name.RelayName",
        server_name: "aws_sdk_mailmanager.types.relay_server_name.RelayServerName",
        server_port: "aws_sdk_mailmanager.types.relay_server_port.RelayServerPort",
        authentication: "aws_sdk_mailmanager.types.relay_authentication.RelayAuthentication",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_relay_response.CreateRelayResponse":
        """<p>Creates a relay resource which can be used in rules to relay incoming emails to defined relay destinations. </p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            relay_name: <p>The unique name of the relay resource.</p>
            server_name: <p>The destination relay server address.</p>
            server_port: <p>The destination relay server port.</p>
            authentication: <p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.create_relay_request.CreateRelayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.create_relay_response.CreateRelayResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_relay

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.create_relay.async_create_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_relay_request.CreateRelayRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["relay_name"] = relay_name
        input_["server_name"] = server_name
        input_["server_port"] = server_port
        input_["authentication"] = authentication
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        relay_id: "aws_sdk_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_relay_response.GetRelayResponse":
        """<p>Fetch the relay resource and it's attributes.</p>

        Args:
            relay_id: <p>A unique relay identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.get_relay_request.GetRelayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.get_relay_response.GetRelayResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_relay

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.get_relay.async_get_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_relay_request.GetRelayRequest = {}  # type: ignore[typeddict-item]
        input_["relay_id"] = relay_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        relay_id: "aws_sdk_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        relay_name: Optional["aws_sdk_mailmanager.types.relay_name.RelayName"] = None,
        server_name: Optional[
            "aws_sdk_mailmanager.types.relay_server_name.RelayServerName"
        ] = None,
        server_port: Optional[
            "aws_sdk_mailmanager.types.relay_server_port.RelayServerPort"
        ] = None,
        authentication: Optional[
            "aws_sdk_mailmanager.types.relay_authentication.RelayAuthentication"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.update_relay_response.UpdateRelayResponse":
        """<p>Updates the attributes of an existing relay resource.</p>

        Args:
            relay_id: <p>The unique relay identifier.</p>
            relay_name: <p>The name of the relay resource.</p>
            server_name: <p>The destination relay server address.</p>
            server_port: <p>The destination relay server port.</p>
            authentication: <p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.update_relay_request.UpdateRelayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.update_relay_response.UpdateRelayResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.update_relay

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.update_relay.async_update_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.update_relay_request.UpdateRelayRequest = {}  # type: ignore[typeddict-item]
        input_["relay_id"] = relay_id
        if relay_name is not None:
            input_["relay_name"] = relay_name
        if server_name is not None:
            input_["server_name"] = server_name
        if server_port is not None:
            input_["server_port"] = server_port
        if authentication is not None:
            input_["authentication"] = authentication

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        relay_id: "aws_sdk_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_relay_response.DeleteRelayResponse":
        """<p>Deletes an existing relay resource.</p>

        Args:
            relay_id: <p>The unique relay identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.delete_relay_request.DeleteRelayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.delete_relay_response.DeleteRelayResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_relay

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.delete_relay.async_delete_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.delete_relay_request.DeleteRelayRequest = {}  # type: ignore[typeddict-item]
        input_["relay_id"] = relay_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        page_size: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.list_relays_response.ListRelaysResponse":
        """<p>Lists all the existing relay resources.</p>

        Args:
            page_size: <p>The number of relays to be returned in one request.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.list_relays_request.ListRelaysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.list_relays_response.ListRelaysResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_relays

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.list_relays.async_list_relays(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_relays_request.ListRelaysRequest = {}  # type: ignore[typeddict-item]
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
