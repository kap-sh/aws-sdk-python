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
    import aws_sdk_account.types.contact_information
    import aws_sdk_account.types.get_contact_information_request
    import aws_sdk_account.types.get_contact_information_response
    import aws_sdk_account.types.put_contact_information_request
    from aws_sdk_account._services.account import AccountClient, AccountClientConfig
    from aws_sdk_account._services.async_account import (
        AsyncAccountClient,
        AsyncAccountClientConfig,
    )


class ContactInformationResource:
    def __init__(self, service: AccountClient) -> None:
        self._service = service

    def put(
        self,
        contact_information: "aws_sdk_account.types.contact_information.ContactInformation",
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["aws_sdk_account.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Updates the primary contact information of an Amazon Web Services account.</p> <p>For complete details about how to use the primary contact operations, see <a href=\"https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html\">Update the primary contact for your Amazon Web Services account</a>.</p>

        Args:
            contact_information: <p>Contains the details of the primary contact information associated with an Amazon Web Services account.</p>
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_account.types.put_contact_information_request.PutContactInformationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_account._operations.account.put_contact_information

            output, http_response = (
                aws_sdk_account._operations.account.put_contact_information.put_contact_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_account.types.put_contact_information_request.PutContactInformationRequest = {}  # type: ignore[typeddict-item]
        input["contact_information"] = contact_information
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        *,
        config_overrides: Optional[AccountClientConfig] = None,
        account_id: Optional["aws_sdk_account.types.account_id.AccountId"] = None,
    ) -> "aws_sdk_account.types.get_contact_information_response.GetContactInformationResponse":
        """<p>Retrieves the primary contact information of an Amazon Web Services account.</p> <p>For complete details about how to use the primary contact operations, see <a href=\"https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html\">Update the primary contact for your Amazon Web Services account</a>.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated admin</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_account.types.get_contact_information_request.GetContactInformationRequest]",
        ) -> OperationResponse[
            "aws_sdk_account.types.get_contact_information_response.GetContactInformationResponse"
        ]:
            import aws_sdk_account._operations.account.get_contact_information

            output, http_response = (
                aws_sdk_account._operations.account.get_contact_information.get_contact_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_account.types.get_contact_information_request.GetContactInformationRequest = {}  # type: ignore[typeddict-item]
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncContactInformationResource:
    def __init__(self, service: AsyncAccountClient) -> None:
        self._service = service

    async def put(
        self,
        contact_information: "aws_sdk_account.types.contact_information.ContactInformation",
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
        account_id: Optional["aws_sdk_account.types.account_id.AccountId"] = None,
    ) -> None:
        """<p>Updates the primary contact information of an Amazon Web Services account.</p> <p>For complete details about how to use the primary contact operations, see <a href=\"https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html\">Update the primary contact for your Amazon Web Services account</a>.</p>

        Args:
            contact_information: <p>Contains the details of the primary contact information associated with an Amazon Web Services account.</p>
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_account.types.put_contact_information_request.PutContactInformationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_account._operations.account.put_contact_information

            (
                output,
                http_response,
            ) = await aws_sdk_account._operations.account.put_contact_information.async_put_contact_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_account.types.put_contact_information_request.PutContactInformationRequest = {}  # type: ignore[typeddict-item]
        input["contact_information"] = contact_information
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        *,
        config_overrides: Optional[AsyncAccountClientConfig] = None,
        account_id: Optional["aws_sdk_account.types.account_id.AccountId"] = None,
    ) -> "aws_sdk_account.types.get_contact_information_response.GetContactInformationResponse":
        """<p>Retrieves the primary contact information of an Amazon Web Services account.</p> <p>For complete details about how to use the primary contact operations, see <a href=\"https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html\">Update the primary contact for your Amazon Web Services account</a>.</p>

        Args:
            account_id: <p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account\">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html\">all features enabled</a>, and the organization must have <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html\">trusted access</a> enabled for the Account Management service, and optionally a <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin\">delegated admin</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_account.types.get_contact_information_request.GetContactInformationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_account.types.get_contact_information_response.GetContactInformationResponse"
        ]:
            import aws_sdk_account._operations.account.get_contact_information

            (
                output,
                http_response,
            ) = await aws_sdk_account._operations.account.get_contact_information.async_get_contact_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_account.types.get_contact_information_request.GetContactInformationRequest = {}  # type: ignore[typeddict-item]
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
