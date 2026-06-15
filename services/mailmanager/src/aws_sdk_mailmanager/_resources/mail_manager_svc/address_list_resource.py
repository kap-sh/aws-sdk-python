from __future__ import annotations

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
    import aws_sdk_mailmanager.types.address_list
    import aws_sdk_mailmanager.types.address_list_id
    import aws_sdk_mailmanager.types.address_list_name
    import aws_sdk_mailmanager.types.create_address_list_request
    import aws_sdk_mailmanager.types.create_address_list_response
    import aws_sdk_mailmanager.types.delete_address_list_request
    import aws_sdk_mailmanager.types.delete_address_list_response
    import aws_sdk_mailmanager.types.get_address_list_request
    import aws_sdk_mailmanager.types.get_address_list_response
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.list_address_lists_request
    import aws_sdk_mailmanager.types.list_address_lists_response
    import aws_sdk_mailmanager.types.page_size
    import aws_sdk_mailmanager.types.pagination_token
    import aws_sdk_mailmanager.types.tag_list
    from aws_sdk_mailmanager._services.async_mail_manager import (
        AsyncMailManagerClient,
        AsyncMailManagerClientConfig,
    )
    from aws_sdk_mailmanager._services.mail_manager import (
        MailManagerClient,
        MailManagerClientConfig,
    )


class AddressListResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        address_list_name: "aws_sdk_mailmanager.types.address_list_name.AddressListName",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_address_list_response.CreateAddressListResponse":
        r"""<p>Creates a new address list.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            address_list_name: <p>A user-friendly name for the address list.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.create_address_list_request.CreateAddressListRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.create_address_list_response.CreateAddressListResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_address_list

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.create_address_list.create_address_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_address_list_request.CreateAddressListRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["address_list_name"] = address_list_name
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
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_address_list_response.GetAddressListResponse":
        """<p>Fetch attributes of an address list.</p>

        Args:
            address_list_id: <p>The identifier of an existing address list resource to be retrieved.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_address_list_request.GetAddressListRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_address_list_response.GetAddressListResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_address_list

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_address_list.get_address_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_address_list_request.GetAddressListRequest = {}  # type: ignore[typeddict-item]
        input_["address_list_id"] = address_list_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_address_list_response.DeleteAddressListResponse":
        """<p>Deletes an address list.</p>

        Args:
            address_list_id: <p>The identifier of an existing address list resource to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.delete_address_list_request.DeleteAddressListRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.delete_address_list_response.DeleteAddressListResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_address_list

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.delete_address_list.delete_address_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.delete_address_list_request.DeleteAddressListRequest = {}  # type: ignore[typeddict-item]
        input_["address_list_id"] = address_list_id

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
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
    ) -> (
        "aws_sdk_mailmanager.types.list_address_lists_response.ListAddressListsResponse"
    ):
        """<p>Lists address lists for this account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of address list resources that are returned per call. You can use NextToken to retrieve the next page of address lists.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_address_lists_request.ListAddressListsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_address_lists_response.ListAddressListsResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_address_lists

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_address_lists.list_address_lists(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_address_lists_request.ListAddressListsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAddressListResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        address_list_name: "aws_sdk_mailmanager.types.address_list_name.AddressListName",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_address_list_response.CreateAddressListResponse":
        r"""<p>Creates a new address list.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            address_list_name: <p>A user-friendly name for the address list.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.create_address_list_request.CreateAddressListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.create_address_list_response.CreateAddressListResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_address_list

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.create_address_list.async_create_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_address_list_request.CreateAddressListRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["address_list_name"] = address_list_name
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
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_address_list_response.GetAddressListResponse":
        """<p>Fetch attributes of an address list.</p>

        Args:
            address_list_id: <p>The identifier of an existing address list resource to be retrieved.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.get_address_list_request.GetAddressListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.get_address_list_response.GetAddressListResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_address_list

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.get_address_list.async_get_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_address_list_request.GetAddressListRequest = {}  # type: ignore[typeddict-item]
        input_["address_list_id"] = address_list_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_address_list_response.DeleteAddressListResponse":
        """<p>Deletes an address list.</p>

        Args:
            address_list_id: <p>The identifier of an existing address list resource to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.delete_address_list_request.DeleteAddressListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.delete_address_list_response.DeleteAddressListResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_address_list

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.delete_address_list.async_delete_address_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.delete_address_list_request.DeleteAddressListRequest = {}  # type: ignore[typeddict-item]
        input_["address_list_id"] = address_list_id

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
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
    ) -> (
        "aws_sdk_mailmanager.types.list_address_lists_response.ListAddressListsResponse"
    ):
        """<p>Lists address lists for this account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of address list resources that are returned per call. You can use NextToken to retrieve the next page of address lists.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.list_address_lists_request.ListAddressListsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.list_address_lists_response.ListAddressListsResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_address_lists

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.list_address_lists.async_list_address_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_address_lists_request.ListAddressListsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
