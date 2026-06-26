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
    import aws_sdk_mailmanager.types.addon_instance
    import aws_sdk_mailmanager.types.addon_instance_id
    import aws_sdk_mailmanager.types.addon_subscription_id
    import aws_sdk_mailmanager.types.create_addon_instance_request
    import aws_sdk_mailmanager.types.create_addon_instance_response
    import aws_sdk_mailmanager.types.delete_addon_instance_request
    import aws_sdk_mailmanager.types.delete_addon_instance_response
    import aws_sdk_mailmanager.types.get_addon_instance_request
    import aws_sdk_mailmanager.types.get_addon_instance_response
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.list_addon_instances_request
    import aws_sdk_mailmanager.types.list_addon_instances_response
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


class AddonInstanceResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        addon_subscription_id: "aws_sdk_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_addon_instance_response.CreateAddonInstanceResponse":
        r"""<p>Creates an Add On instance for the subscription indicated in the request. The resulting Amazon Resource Name (ARN) can be used in a conditional statement for a rule set or traffic policy. </p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            addon_subscription_id: <p>The unique ID of a previously created subscription that an Add On instance is created for. You can only have one instance per subscription.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>

        Raises:
            aws_sdk_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            aws_sdk_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            aws_sdk_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.create_addon_instance_request.CreateAddonInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.create_addon_instance_response.CreateAddonInstanceResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_addon_instance

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.create_addon_instance.create_addon_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_addon_instance_request.CreateAddonInstanceRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["addon_subscription_id"] = addon_subscription_id
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
        addon_instance_id: "aws_sdk_mailmanager.types.addon_instance_id.AddonInstanceId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> (
        "aws_sdk_mailmanager.types.get_addon_instance_response.GetAddonInstanceResponse"
    ):
        """<p>Gets detailed information about an Add On instance.</p>

        Args:
            addon_instance_id: <p>The Add On instance ID to retrieve information for.</p>

        Raises:
            aws_sdk_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            aws_sdk_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_addon_instance_request.GetAddonInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_addon_instance_response.GetAddonInstanceResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_addon_instance

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_addon_instance.get_addon_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_addon_instance_request.GetAddonInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["addon_instance_id"] = addon_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        addon_instance_id: "aws_sdk_mailmanager.types.addon_instance_id.AddonInstanceId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_addon_instance_response.DeleteAddonInstanceResponse":
        """<p>Deletes an Add On instance.</p>

        Args:
            addon_instance_id: <p>The Add On instance ID to delete.</p>

        Raises:
            aws_sdk_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.delete_addon_instance_request.DeleteAddonInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.delete_addon_instance_response.DeleteAddonInstanceResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_addon_instance

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.delete_addon_instance.delete_addon_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.delete_addon_instance_request.DeleteAddonInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["addon_instance_id"] = addon_instance_id

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
    ) -> "aws_sdk_mailmanager.types.list_addon_instances_response.ListAddonInstancesResponse":
        """<p>Lists all Add On instances in your account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints. </p>

        Raises:
            aws_sdk_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_addon_instances_request.ListAddonInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_addon_instances_response.ListAddonInstancesResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_addon_instances

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_addon_instances.list_addon_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_addon_instances_request.ListAddonInstancesRequest = {}  # type: ignore[typeddict-item]
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


class AsyncAddonInstanceResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        addon_subscription_id: "aws_sdk_mailmanager.types.addon_subscription_id.AddonSubscriptionId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_addon_instance_response.CreateAddonInstanceResponse":
        r"""<p>Creates an Add On instance for the subscription indicated in the request. The resulting Amazon Resource Name (ARN) can be used in a conditional statement for a rule set or traffic policy. </p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            addon_subscription_id: <p>The unique ID of a previously created subscription that an Add On instance is created for. You can only have one instance per subscription.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>

        Raises:
            aws_sdk_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            aws_sdk_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            aws_sdk_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.create_addon_instance_request.CreateAddonInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.create_addon_instance_response.CreateAddonInstanceResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_addon_instance

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.create_addon_instance.async_create_addon_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_addon_instance_request.CreateAddonInstanceRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["addon_subscription_id"] = addon_subscription_id
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
        addon_instance_id: "aws_sdk_mailmanager.types.addon_instance_id.AddonInstanceId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> (
        "aws_sdk_mailmanager.types.get_addon_instance_response.GetAddonInstanceResponse"
    ):
        """<p>Gets detailed information about an Add On instance.</p>

        Args:
            addon_instance_id: <p>The Add On instance ID to retrieve information for.</p>

        Raises:
            aws_sdk_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            aws_sdk_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.get_addon_instance_request.GetAddonInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.get_addon_instance_response.GetAddonInstanceResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_addon_instance

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.get_addon_instance.async_get_addon_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_addon_instance_request.GetAddonInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["addon_instance_id"] = addon_instance_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        addon_instance_id: "aws_sdk_mailmanager.types.addon_instance_id.AddonInstanceId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_addon_instance_response.DeleteAddonInstanceResponse":
        """<p>Deletes an Add On instance.</p>

        Args:
            addon_instance_id: <p>The Add On instance ID to delete.</p>

        Raises:
            aws_sdk_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.delete_addon_instance_request.DeleteAddonInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.delete_addon_instance_response.DeleteAddonInstanceResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_addon_instance

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.delete_addon_instance.async_delete_addon_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.delete_addon_instance_request.DeleteAddonInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["addon_instance_id"] = addon_instance_id

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
    ) -> "aws_sdk_mailmanager.types.list_addon_instances_response.ListAddonInstancesResponse":
        """<p>Lists all Add On instances in your account.</p>

        Args:
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints. </p>

        Raises:
            aws_sdk_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            aws_sdk_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.list_addon_instances_request.ListAddonInstancesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.list_addon_instances_response.ListAddonInstancesResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_addon_instances

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.list_addon_instances.async_list_addon_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_addon_instances_request.ListAddonInstancesRequest = {}  # type: ignore[typeddict-item]
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
