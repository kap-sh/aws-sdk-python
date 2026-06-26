from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_account._auth._signers
import aws_sdk_account._auth._sigv4
from aws_sdk_account._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_account.types.accept_primary_email_update_request
    import aws_sdk_account.types.accept_primary_email_update_response
    import aws_sdk_account.types.account_id
    import aws_sdk_account.types.get_primary_email_request
    import aws_sdk_account.types.get_primary_email_response
    import aws_sdk_account.types.otp
    import aws_sdk_account.types.primary_email_address
    import aws_sdk_account.types.start_primary_email_update_request
    import aws_sdk_account.types.start_primary_email_update_response
    from aws_sdk_account._services.account import AccountClient, AccountClientConfig
    from aws_sdk_account._services.async_account import (
        AsyncAccountClient,
        AsyncAccountClientConfig,
    )


class PrimaryEmailResource:
    def __init__(self, service: AccountClient) -> None:
        self._service = service

    def accept_primary_email_update(
        self,
        account_id: "aws_sdk_account.types.account_id.AccountId",
        primary_email: "aws_sdk_account.types.primary_email_address.PrimaryEmailAddress",
        otp: "aws_sdk_account.types.otp.Otp",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
    ) -> "aws_sdk_account.types.accept_primary_email_update_response.AcceptPrimaryEmailUpdateResponse":
        r"""<p>Accepts the request that originated from <a>StartPrimaryEmailUpdate</a> to update the primary email address (also known as the root user email address) for the specified account.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>
            primary_email: <p>The new primary email address for use with the specified account. This must match the <code>PrimaryEmail</code> from the <code>StartPrimaryEmailUpdate</code> API call.</p>
            otp: <p>The OTP code sent to the <code>PrimaryEmail</code> specified on the <code>StartPrimaryEmailUpdate</code> API call.</p>

        Raises:
            aws_sdk_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            aws_sdk_account.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.</p>
            aws_sdk_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            aws_sdk_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            aws_sdk_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            aws_sdk_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            aws_sdk_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_account.types.accept_primary_email_update_request.AcceptPrimaryEmailUpdateRequest]",
        ) -> OperationResponse[
            "aws_sdk_account.types.accept_primary_email_update_response.AcceptPrimaryEmailUpdateResponse"
        ]:
            import aws_sdk_account._operations.account.accept_primary_email_update

            output, http_response = (
                aws_sdk_account._operations.account.accept_primary_email_update.accept_primary_email_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_account.types.accept_primary_email_update_request.AcceptPrimaryEmailUpdateRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["primary_email"] = primary_email
        input_["otp"] = otp

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_primary_email(
        self,
        account_id: "aws_sdk_account.types.account_id.AccountId",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
    ) -> "aws_sdk_account.types.get_primary_email_response.GetPrimaryEmailResponse":
        r"""<p>Retrieves the primary email address for the specified account.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>

        Raises:
            aws_sdk_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            aws_sdk_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            aws_sdk_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            aws_sdk_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            aws_sdk_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            aws_sdk_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_account.types.get_primary_email_request.GetPrimaryEmailRequest]",
        ) -> OperationResponse[
            "aws_sdk_account.types.get_primary_email_response.GetPrimaryEmailResponse"
        ]:
            import aws_sdk_account._operations.account.get_primary_email

            output, http_response = (
                aws_sdk_account._operations.account.get_primary_email.get_primary_email(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_account.types.get_primary_email_request.GetPrimaryEmailRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_primary_email_update(
        self,
        account_id: "aws_sdk_account.types.account_id.AccountId",
        primary_email: "aws_sdk_account.types.primary_email_address.PrimaryEmailAddress",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
    ) -> "aws_sdk_account.types.start_primary_email_update_response.StartPrimaryEmailUpdateResponse":
        r"""<p>Starts the process to update the primary email address for the specified account.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>
            primary_email: <p>The new primary email address (also known as the root user email address) to use in the specified account.</p>

        Raises:
            aws_sdk_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            aws_sdk_account.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.</p>
            aws_sdk_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            aws_sdk_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            aws_sdk_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            aws_sdk_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            aws_sdk_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_account.types.start_primary_email_update_request.StartPrimaryEmailUpdateRequest]",
        ) -> OperationResponse[
            "aws_sdk_account.types.start_primary_email_update_response.StartPrimaryEmailUpdateResponse"
        ]:
            import aws_sdk_account._operations.account.start_primary_email_update

            output, http_response = (
                aws_sdk_account._operations.account.start_primary_email_update.start_primary_email_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_account.types.start_primary_email_update_request.StartPrimaryEmailUpdateRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["primary_email"] = primary_email

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncPrimaryEmailResource:
    def __init__(self, service: AsyncAccountClient) -> None:
        self._service = service

    async def accept_primary_email_update(
        self,
        account_id: "aws_sdk_account.types.account_id.AccountId",
        primary_email: "aws_sdk_account.types.primary_email_address.PrimaryEmailAddress",
        otp: "aws_sdk_account.types.otp.Otp",
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
    ) -> "aws_sdk_account.types.accept_primary_email_update_response.AcceptPrimaryEmailUpdateResponse":
        r"""<p>Accepts the request that originated from <a>StartPrimaryEmailUpdate</a> to update the primary email address (also known as the root user email address) for the specified account.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>
            primary_email: <p>The new primary email address for use with the specified account. This must match the <code>PrimaryEmail</code> from the <code>StartPrimaryEmailUpdate</code> API call.</p>
            otp: <p>The OTP code sent to the <code>PrimaryEmail</code> specified on the <code>StartPrimaryEmailUpdate</code> API call.</p>

        Raises:
            aws_sdk_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            aws_sdk_account.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.</p>
            aws_sdk_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            aws_sdk_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            aws_sdk_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            aws_sdk_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            aws_sdk_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_account.types.accept_primary_email_update_request.AcceptPrimaryEmailUpdateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_account.types.accept_primary_email_update_response.AcceptPrimaryEmailUpdateResponse"
        ]:
            import aws_sdk_account._operations.account.accept_primary_email_update

            (
                output,
                http_response,
            ) = await aws_sdk_account._operations.account.accept_primary_email_update.async_accept_primary_email_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_account.types.accept_primary_email_update_request.AcceptPrimaryEmailUpdateRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["primary_email"] = primary_email
        input_["otp"] = otp

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_primary_email(
        self,
        account_id: "aws_sdk_account.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
    ) -> "aws_sdk_account.types.get_primary_email_response.GetPrimaryEmailResponse":
        r"""<p>Retrieves the primary email address for the specified account.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>

        Raises:
            aws_sdk_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            aws_sdk_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            aws_sdk_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            aws_sdk_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            aws_sdk_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            aws_sdk_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_account.types.get_primary_email_request.GetPrimaryEmailRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_account.types.get_primary_email_response.GetPrimaryEmailResponse"
        ]:
            import aws_sdk_account._operations.account.get_primary_email

            (
                output,
                http_response,
            ) = await aws_sdk_account._operations.account.get_primary_email.async_get_primary_email(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_account.types.get_primary_email_request.GetPrimaryEmailRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_primary_email_update(
        self,
        account_id: "aws_sdk_account.types.account_id.AccountId",
        primary_email: "aws_sdk_account.types.primary_email_address.PrimaryEmailAddress",
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
    ) -> "aws_sdk_account.types.start_primary_email_update_response.StartPrimaryEmailUpdateResponse":
        r"""<p>Starts the process to update the primary email address for the specified account.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>
            primary_email: <p>The new primary email address (also known as the root user email address) to use in the specified account.</p>

        Raises:
            aws_sdk_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            aws_sdk_account.errors.conflict_exception.ConflictException: <p>The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.</p>
            aws_sdk_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            aws_sdk_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation failed because it specified a resource that can't be found.</p>
            aws_sdk_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            aws_sdk_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            aws_sdk_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_account.types.start_primary_email_update_request.StartPrimaryEmailUpdateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_account.types.start_primary_email_update_response.StartPrimaryEmailUpdateResponse"
        ]:
            import aws_sdk_account._operations.account.start_primary_email_update

            (
                output,
                http_response,
            ) = await aws_sdk_account._operations.account.start_primary_email_update.async_start_primary_email_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_account.types.start_primary_email_update_request.StartPrimaryEmailUpdateRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["primary_email"] = primary_email

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
