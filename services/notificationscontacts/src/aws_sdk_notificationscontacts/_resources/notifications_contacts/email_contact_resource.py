from typing import TYPE_CHECKING, Optional

import aws_sdk_notificationscontacts._auth._signers
import aws_sdk_notificationscontacts._auth._sigv4
from aws_sdk_notificationscontacts._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_notificationscontacts.types.activate_email_contact_request
    import aws_sdk_notificationscontacts.types.activate_email_contact_response
    import aws_sdk_notificationscontacts.types.create_email_contact_request
    import aws_sdk_notificationscontacts.types.create_email_contact_response
    import aws_sdk_notificationscontacts.types.delete_email_contact_request
    import aws_sdk_notificationscontacts.types.delete_email_contact_response
    import aws_sdk_notificationscontacts.types.email_contact
    import aws_sdk_notificationscontacts.types.email_contact_address
    import aws_sdk_notificationscontacts.types.email_contact_arn
    import aws_sdk_notificationscontacts.types.email_contact_name
    import aws_sdk_notificationscontacts.types.get_email_contact_request
    import aws_sdk_notificationscontacts.types.get_email_contact_response
    import aws_sdk_notificationscontacts.types.list_email_contacts_request
    import aws_sdk_notificationscontacts.types.list_email_contacts_response
    import aws_sdk_notificationscontacts.types.send_activation_code_request
    import aws_sdk_notificationscontacts.types.send_activation_code_response
    import aws_sdk_notificationscontacts.types.tag_map
    import aws_sdk_notificationscontacts.types.token
    from aws_sdk_notificationscontacts._services.async_notifications_contacts import (
        AsyncNotificationsContactsClient,
        AsyncNotificationsContactsClientConfig,
    )
    from aws_sdk_notificationscontacts._services.notifications_contacts import (
        NotificationsContactsClient,
        NotificationsContactsClientConfig,
    )


class EmailContactResource:
    def __init__(self, service: NotificationsContactsClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_notificationscontacts.types.email_contact_name.EmailContactName",
        email_address: "aws_sdk_notificationscontacts.types.email_contact_address.EmailContactAddress",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
        tags: Optional["aws_sdk_notificationscontacts.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_notificationscontacts.types.create_email_contact_response.CreateEmailContactResponse":
        """<p>Creates an email contact for the provided email address.</p>

        Args:
            name: <p>The name of the email contact.</p>
            email_address: <p>The email address this email contact points to. The activation email and any subscribed emails are sent here.</p> <note> <p>This email address can't receive emails until it's activated.</p> </note>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notificationscontacts.types.create_email_contact_request.CreateEmailContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_notificationscontacts.types.create_email_contact_response.CreateEmailContactResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.create_email_contact

            output, http_response = (
                aws_sdk_notificationscontacts._operations.notifications_contacts.create_email_contact.create_email_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.create_email_contact_request.CreateEmailContactRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["email_address"] = email_address
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
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
    ) -> "aws_sdk_notificationscontacts.types.get_email_contact_response.GetEmailContactResponse":
        """<p>Returns an email contact.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the email contact to get.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notificationscontacts.types.get_email_contact_request.GetEmailContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_notificationscontacts.types.get_email_contact_response.GetEmailContactResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.get_email_contact

            output, http_response = (
                aws_sdk_notificationscontacts._operations.notifications_contacts.get_email_contact.get_email_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.get_email_contact_request.GetEmailContactRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
    ) -> "aws_sdk_notificationscontacts.types.delete_email_contact_response.DeleteEmailContactResponse":
        """<p>Deletes an email contact.</p> <note> <p>Deleting an email contact removes it from all associated notification configurations.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notificationscontacts.types.delete_email_contact_request.DeleteEmailContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_notificationscontacts.types.delete_email_contact_response.DeleteEmailContactResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.delete_email_contact

            output, http_response = (
                aws_sdk_notificationscontacts._operations.notifications_contacts.delete_email_contact.delete_email_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.delete_email_contact_request.DeleteEmailContactRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_notificationscontacts.types.list_email_contacts_response.ListEmailContactsResponse":
        """<p>Lists all email contacts created under the Account.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notificationscontacts.types.list_email_contacts_request.ListEmailContactsRequest]",
        ) -> OperationResponse[
            "aws_sdk_notificationscontacts.types.list_email_contacts_response.ListEmailContactsResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.list_email_contacts

            output, http_response = (
                aws_sdk_notificationscontacts._operations.notifications_contacts.list_email_contacts.list_email_contacts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.list_email_contacts_request.ListEmailContactsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def activate_email_contact(
        self,
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        code: "aws_sdk_notificationscontacts.types.token.Token",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
    ) -> "aws_sdk_notificationscontacts.types.activate_email_contact_response.ActivateEmailContactResponse":
        """<p>Activates an email contact using an activation code. This code is in the activation email sent to the email address associated with this email contact.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            code: <p>The activation code for this email contact.</p> <p>An email contact has a maximum of five activation attempts. Activation codes expire after 12 hours and are generated by the <a href=\"https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/API_SendActivationCode.html\">SendActivationCode</a> API action.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notificationscontacts.types.activate_email_contact_request.ActivateEmailContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_notificationscontacts.types.activate_email_contact_response.ActivateEmailContactResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.activate_email_contact

            output, http_response = (
                aws_sdk_notificationscontacts._operations.notifications_contacts.activate_email_contact.activate_email_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.activate_email_contact_request.ActivateEmailContactRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["code"] = code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_activation_code(
        self,
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
    ) -> "aws_sdk_notificationscontacts.types.send_activation_code_response.SendActivationCodeResponse":
        """<p>Sends an activation email to the email address associated with the specified email contact.</p> <note> <p>It might take a few minutes for the activation email to arrive. If it doesn't arrive, check in your spam folder or try sending another activation email.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notificationscontacts.types.send_activation_code_request.SendActivationCodeRequest]",
        ) -> OperationResponse[
            "aws_sdk_notificationscontacts.types.send_activation_code_response.SendActivationCodeResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.send_activation_code

            output, http_response = (
                aws_sdk_notificationscontacts._operations.notifications_contacts.send_activation_code.send_activation_code(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.send_activation_code_request.SendActivationCodeRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEmailContactResource:
    def __init__(self, service: AsyncNotificationsContactsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_notificationscontacts.types.email_contact_name.EmailContactName",
        email_address: "aws_sdk_notificationscontacts.types.email_contact_address.EmailContactAddress",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
        tags: Optional["aws_sdk_notificationscontacts.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_notificationscontacts.types.create_email_contact_response.CreateEmailContactResponse":
        """<p>Creates an email contact for the provided email address.</p>

        Args:
            name: <p>The name of the email contact.</p>
            email_address: <p>The email address this email contact points to. The activation email and any subscribed emails are sent here.</p> <note> <p>This email address can't receive emails until it's activated.</p> </note>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notificationscontacts.types.create_email_contact_request.CreateEmailContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notificationscontacts.types.create_email_contact_response.CreateEmailContactResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.create_email_contact

            (
                output,
                http_response,
            ) = await aws_sdk_notificationscontacts._operations.notifications_contacts.create_email_contact.async_create_email_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.create_email_contact_request.CreateEmailContactRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["email_address"] = email_address
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
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> "aws_sdk_notificationscontacts.types.get_email_contact_response.GetEmailContactResponse":
        """<p>Returns an email contact.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the email contact to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notificationscontacts.types.get_email_contact_request.GetEmailContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notificationscontacts.types.get_email_contact_response.GetEmailContactResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.get_email_contact

            (
                output,
                http_response,
            ) = await aws_sdk_notificationscontacts._operations.notifications_contacts.get_email_contact.async_get_email_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.get_email_contact_request.GetEmailContactRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> "aws_sdk_notificationscontacts.types.delete_email_contact_response.DeleteEmailContactResponse":
        """<p>Deletes an email contact.</p> <note> <p>Deleting an email contact removes it from all associated notification configurations.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notificationscontacts.types.delete_email_contact_request.DeleteEmailContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notificationscontacts.types.delete_email_contact_response.DeleteEmailContactResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.delete_email_contact

            (
                output,
                http_response,
            ) = await aws_sdk_notificationscontacts._operations.notifications_contacts.delete_email_contact.async_delete_email_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.delete_email_contact_request.DeleteEmailContactRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_notificationscontacts.types.list_email_contacts_response.ListEmailContactsResponse":
        """<p>Lists all email contacts created under the Account.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notificationscontacts.types.list_email_contacts_request.ListEmailContactsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notificationscontacts.types.list_email_contacts_response.ListEmailContactsResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.list_email_contacts

            (
                output,
                http_response,
            ) = await aws_sdk_notificationscontacts._operations.notifications_contacts.list_email_contacts.async_list_email_contacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.list_email_contacts_request.ListEmailContactsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def activate_email_contact(
        self,
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        code: "aws_sdk_notificationscontacts.types.token.Token",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> "aws_sdk_notificationscontacts.types.activate_email_contact_response.ActivateEmailContactResponse":
        """<p>Activates an email contact using an activation code. This code is in the activation email sent to the email address associated with this email contact.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            code: <p>The activation code for this email contact.</p> <p>An email contact has a maximum of five activation attempts. Activation codes expire after 12 hours and are generated by the <a href=\"https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/API_SendActivationCode.html\">SendActivationCode</a> API action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notificationscontacts.types.activate_email_contact_request.ActivateEmailContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notificationscontacts.types.activate_email_contact_response.ActivateEmailContactResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.activate_email_contact

            (
                output,
                http_response,
            ) = await aws_sdk_notificationscontacts._operations.notifications_contacts.activate_email_contact.async_activate_email_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.activate_email_contact_request.ActivateEmailContactRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["code"] = code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_activation_code(
        self,
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[AsyncNotificationsContactsClientConfig] = None,
    ) -> "aws_sdk_notificationscontacts.types.send_activation_code_response.SendActivationCodeResponse":
        """<p>Sends an activation email to the email address associated with the specified email contact.</p> <note> <p>It might take a few minutes for the activation email to arrive. If it doesn't arrive, check in your spam folder or try sending another activation email.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notificationscontacts.types.send_activation_code_request.SendActivationCodeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notificationscontacts.types.send_activation_code_response.SendActivationCodeResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.send_activation_code

            (
                output,
                http_response,
            ) = await aws_sdk_notificationscontacts._operations.notifications_contacts.send_activation_code.async_send_activation_code(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.send_activation_code_request.SendActivationCodeRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
