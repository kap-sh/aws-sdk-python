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
    import aws_sdk_mailmanager.types.addon_name
    import aws_sdk_mailmanager.types.addon_subscription
    import aws_sdk_mailmanager.types.addon_subscription_id
    import aws_sdk_mailmanager.types.create_addon_subscription_request
    import aws_sdk_mailmanager.types.create_addon_subscription_response
    import aws_sdk_mailmanager.types.delete_addon_subscription_request
    import aws_sdk_mailmanager.types.delete_addon_subscription_response
    import aws_sdk_mailmanager.types.get_addon_subscription_request
    import aws_sdk_mailmanager.types.get_addon_subscription_response
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.list_addon_subscriptions_request
    import aws_sdk_mailmanager.types.list_addon_subscriptions_response
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


class AddonSubscriptionResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        addon_name: "aws_sdk_mailmanager.types.addon_name.AddonName",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_addon_subscription_response.CreateAddonSubscriptionResponse":
        """<p>Creates a subscription for an Add On representing the acceptance of its terms of use and additional pricing. The subscription can then be used to create an instance for use in rule sets or traffic policies.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            addon_name: <p>The name of the Add On to subscribe to. You can only have one subscription for each Add On name.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.create_addon_subscription_request.CreateAddonSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.create_addon_subscription_response.CreateAddonSubscriptionResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_addon_subscription

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.create_addon_subscription.create_addon_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_addon_subscription_request.CreateAddonSubscriptionRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["addon_name"] = addon_name
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
        addon_subscription_id: "aws_sdk_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_addon_subscription_response.GetAddonSubscriptionResponse":
        """<p>Gets detailed information about an Add On subscription.</p>

        Args:
            addon_subscription_id: <p>The Add On subscription ID to retrieve information for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_addon_subscription_request.GetAddonSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_addon_subscription_response.GetAddonSubscriptionResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_addon_subscription

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_addon_subscription.get_addon_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_addon_subscription_request.GetAddonSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["addon_subscription_id"] = addon_subscription_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        addon_subscription_id: "aws_sdk_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_addon_subscription_response.DeleteAddonSubscriptionResponse":
        """<p>Deletes an Add On subscription.</p>

        Args:
            addon_subscription_id: <p>The Add On subscription ID to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.delete_addon_subscription_request.DeleteAddonSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.delete_addon_subscription_response.DeleteAddonSubscriptionResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_addon_subscription

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.delete_addon_subscription.delete_addon_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.delete_addon_subscription_request.DeleteAddonSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["addon_subscription_id"] = addon_subscription_id

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
    ) -> "aws_sdk_mailmanager.types.list_addon_subscriptions_response.ListAddonSubscriptionsResponse":
        """<p>Lists all Add On subscriptions in your account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_addon_subscriptions_request.ListAddonSubscriptionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_addon_subscriptions_response.ListAddonSubscriptionsResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_addon_subscriptions

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_addon_subscriptions.list_addon_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_addon_subscriptions_request.ListAddonSubscriptionsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncAddonSubscriptionResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        addon_name: "aws_sdk_mailmanager.types.addon_name.AddonName",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_addon_subscription_response.CreateAddonSubscriptionResponse":
        """<p>Creates a subscription for an Add On representing the acceptance of its terms of use and additional pricing. The subscription can then be used to create an instance for use in rule sets or traffic policies.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            addon_name: <p>The name of the Add On to subscribe to. You can only have one subscription for each Add On name.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.create_addon_subscription_request.CreateAddonSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.create_addon_subscription_response.CreateAddonSubscriptionResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_addon_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.create_addon_subscription.async_create_addon_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_addon_subscription_request.CreateAddonSubscriptionRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["addon_name"] = addon_name
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
        addon_subscription_id: "aws_sdk_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_addon_subscription_response.GetAddonSubscriptionResponse":
        """<p>Gets detailed information about an Add On subscription.</p>

        Args:
            addon_subscription_id: <p>The Add On subscription ID to retrieve information for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.get_addon_subscription_request.GetAddonSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.get_addon_subscription_response.GetAddonSubscriptionResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_addon_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.get_addon_subscription.async_get_addon_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_addon_subscription_request.GetAddonSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["addon_subscription_id"] = addon_subscription_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        addon_subscription_id: "aws_sdk_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_addon_subscription_response.DeleteAddonSubscriptionResponse":
        """<p>Deletes an Add On subscription.</p>

        Args:
            addon_subscription_id: <p>The Add On subscription ID to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.delete_addon_subscription_request.DeleteAddonSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.delete_addon_subscription_response.DeleteAddonSubscriptionResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_addon_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.delete_addon_subscription.async_delete_addon_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.delete_addon_subscription_request.DeleteAddonSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["addon_subscription_id"] = addon_subscription_id

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
    ) -> "aws_sdk_mailmanager.types.list_addon_subscriptions_response.ListAddonSubscriptionsResponse":
        """<p>Lists all Add On subscriptions in your account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.list_addon_subscriptions_request.ListAddonSubscriptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.list_addon_subscriptions_response.ListAddonSubscriptionsResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_addon_subscriptions

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.list_addon_subscriptions.async_list_addon_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_addon_subscriptions_request.ListAddonSubscriptionsRequest = {}  # type: ignore[typeddict-item]
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
