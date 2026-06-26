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
    import aws_sdk_account.types.account_id
    import aws_sdk_account.types.account_name
    import aws_sdk_account.types.get_account_information_request
    import aws_sdk_account.types.get_account_information_response
    import aws_sdk_account.types.put_account_name_request
    from aws_sdk_account._services.account import AccountClient, AccountClientConfig
    from aws_sdk_account._services.async_account import (
        AsyncAccountClient,
        AsyncAccountClientConfig,
    )


class AccountNameResource:
    def __init__(self, service: AccountClient) -> None:
        self._service = service

    def put(
        self,
        account_name: "aws_sdk_account.types.account_name.AccountName",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["aws_sdk_account.types.account_id.AccountId"] = None,
    ) -> None:
        r"""<p>Updates the account name of the specified account. To use this API, IAM principals must have the <code>account:PutAccountName</code> IAM permission. </p>

        Args:
            account_name: <p>The name of the account.</p>
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            aws_sdk_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            aws_sdk_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            aws_sdk_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            aws_sdk_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            aws_sdk_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_account.types.put_account_name_request.PutAccountNameRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_account._operations.account.put_account_name

            output, http_response = (
                aws_sdk_account._operations.account.put_account_name.put_account_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_account.types.put_account_name_request.PutAccountNameRequest = {}  # type: ignore[typeddict-item]
        input_["account_name"] = account_name
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["aws_sdk_account.types.account_id.AccountId"] = None,
    ) -> "aws_sdk_account.types.get_account_information_response.GetAccountInformationResponse":
        r"""<p>Retrieves information about the specified account including its account name, account ID, account creation date and time, and account state. To use this API, an IAM user or role must have the <code>account:GetAccountInformation</code> IAM permission. </p>

        Args:
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            aws_sdk_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            aws_sdk_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            aws_sdk_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            aws_sdk_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            aws_sdk_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_account.types.get_account_information_request.GetAccountInformationRequest]",
        ) -> OperationResponse[
            "aws_sdk_account.types.get_account_information_response.GetAccountInformationResponse"
        ]:
            import aws_sdk_account._operations.account.get_account_information

            output, http_response = (
                aws_sdk_account._operations.account.get_account_information.get_account_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_account.types.get_account_information_request.GetAccountInformationRequest = {}  # type: ignore[typeddict-item]
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAccountNameResource:
    def __init__(self, service: AsyncAccountClient) -> None:
        self._service = service

    async def put(
        self,
        account_name: "aws_sdk_account.types.account_name.AccountName",
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
        account_id: Optional["aws_sdk_account.types.account_id.AccountId"] = None,
    ) -> None:
        r"""<p>Updates the account name of the specified account. To use this API, IAM principals must have the <code>account:PutAccountName</code> IAM permission. </p>

        Args:
            account_name: <p>The name of the account.</p>
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            aws_sdk_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            aws_sdk_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            aws_sdk_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            aws_sdk_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            aws_sdk_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_account.types.put_account_name_request.PutAccountNameRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_account._operations.account.put_account_name

            (
                output,
                http_response,
            ) = await aws_sdk_account._operations.account.put_account_name.async_put_account_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_account.types.put_account_name_request.PutAccountNameRequest = {}  # type: ignore[typeddict-item]
        input_["account_name"] = account_name
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
        account_id: Optional["aws_sdk_account.types.account_id.AccountId"] = None,
    ) -> "aws_sdk_account.types.get_account_information_response.GetAccountInformationResponse":
        r"""<p>Retrieves information about the specified account including its account name, account ID, account creation date and time, and account state. To use this API, an IAM user or role must have the <code>account:GetAccountInformation</code> IAM permission. </p>

        Args:
            account_id: <p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>

        Raises:
            aws_sdk_account.errors.access_denied_exception.AccessDeniedException: <p>The operation failed because the calling identity doesn't have the minimum required permissions.</p>
            aws_sdk_account.errors.internal_server_exception.InternalServerException: <p>The operation failed because of an error internal to Amazon Web Services. Try your operation again later.</p>
            aws_sdk_account.errors.too_many_requests_exception.TooManyRequestsException: <p>The operation failed because it was called too frequently and exceeded a throttle limit.</p>
            aws_sdk_account.errors.validation_exception.ValidationException: <p>The operation failed because one of the input parameters was invalid.</p>
            aws_sdk_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_account.types.get_account_information_request.GetAccountInformationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_account.types.get_account_information_response.GetAccountInformationResponse"
        ]:
            import aws_sdk_account._operations.account.get_account_information

            (
                output,
                http_response,
            ) = await aws_sdk_account._operations.account.get_account_information.async_get_account_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_account.types.get_account_information_request.GetAccountInformationRequest = {}  # type: ignore[typeddict-item]
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
