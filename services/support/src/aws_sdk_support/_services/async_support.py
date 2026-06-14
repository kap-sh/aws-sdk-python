"""Generated from Smithy shape ``com.amazonaws.support#AWSSupport_20130415``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_support._auth._signers
import aws_sdk_support._auth._sigv4
from aws_sdk_support._auth._identity import Credentials
from aws_sdk_support._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_support._auth._zapros_handler import AuthMiddleware
from aws_sdk_support._pagination import resolve_path as _resolve_path
from aws_sdk_support._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_support.types.add_attachments_to_set_request
    import aws_sdk_support.types.add_attachments_to_set_response
    import aws_sdk_support.types.add_communication_to_case_request
    import aws_sdk_support.types.add_communication_to_case_response
    import aws_sdk_support.types.after_time
    import aws_sdk_support.types.attachment_id
    import aws_sdk_support.types.attachment_set_id
    import aws_sdk_support.types.attachments
    import aws_sdk_support.types.before_time
    import aws_sdk_support.types.case_details
    import aws_sdk_support.types.case_id
    import aws_sdk_support.types.case_id_list
    import aws_sdk_support.types.category_code
    import aws_sdk_support.types.cc_email_address_list
    import aws_sdk_support.types.communication
    import aws_sdk_support.types.communication_body
    import aws_sdk_support.types.create_case_request
    import aws_sdk_support.types.create_case_response
    import aws_sdk_support.types.describe_attachment_request
    import aws_sdk_support.types.describe_attachment_response
    import aws_sdk_support.types.describe_cases_request
    import aws_sdk_support.types.describe_cases_response
    import aws_sdk_support.types.describe_communications_request
    import aws_sdk_support.types.describe_communications_response
    import aws_sdk_support.types.describe_create_case_options_request
    import aws_sdk_support.types.describe_create_case_options_response
    import aws_sdk_support.types.describe_services_request
    import aws_sdk_support.types.describe_services_response
    import aws_sdk_support.types.describe_severity_levels_request
    import aws_sdk_support.types.describe_severity_levels_response
    import aws_sdk_support.types.describe_supported_languages_request
    import aws_sdk_support.types.describe_supported_languages_response
    import aws_sdk_support.types.describe_trusted_advisor_check_refresh_statuses_request
    import aws_sdk_support.types.describe_trusted_advisor_check_refresh_statuses_response
    import aws_sdk_support.types.describe_trusted_advisor_check_result_request
    import aws_sdk_support.types.describe_trusted_advisor_check_result_response
    import aws_sdk_support.types.describe_trusted_advisor_check_summaries_request
    import aws_sdk_support.types.describe_trusted_advisor_check_summaries_response
    import aws_sdk_support.types.describe_trusted_advisor_checks_request
    import aws_sdk_support.types.describe_trusted_advisor_checks_response
    import aws_sdk_support.types.display_id
    import aws_sdk_support.types.include_communications
    import aws_sdk_support.types.include_resolved_cases
    import aws_sdk_support.types.issue_type
    import aws_sdk_support.types.language
    import aws_sdk_support.types.max_results
    import aws_sdk_support.types.next_token
    import aws_sdk_support.types.refresh_trusted_advisor_check_request
    import aws_sdk_support.types.refresh_trusted_advisor_check_response
    import aws_sdk_support.types.resolve_case_request
    import aws_sdk_support.types.resolve_case_response
    import aws_sdk_support.types.service_code2
    import aws_sdk_support.types.service_code_list
    import aws_sdk_support.types.severity_code
    import aws_sdk_support.types.string
    import aws_sdk_support.types.string_list
    import aws_sdk_support.types.subject
    import aws_sdk_support.types.validated_category_code
    import aws_sdk_support.types.validated_issue_type_string
    import aws_sdk_support.types.validated_service_code


class AsyncSupportClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncSupportClient:
    """A client for the ``Support`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncSupportClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSupportClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSupportClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def add_attachments_to_set(
        self,
        attachments: "aws_sdk_support.types.attachments.Attachments",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        attachment_set_id: Optional[
            "aws_sdk_support.types.attachment_set_id.AttachmentSetId"
        ] = None,
    ) -> "aws_sdk_support.types.add_attachments_to_set_response.AddAttachmentsToSetResponse":
        r"""<p>Adds one or more attachments to an attachment set. </p> <p>An attachment set is a temporary container for attachments that you add to a case or case communication. The set is available for 1 hour after it's created. The <code>expiryTime</code> returned in the response is when the set expires. </p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            attachment_set_id: <p>The ID of the attachment set. If an <code>attachmentSetId</code> is not specified, a new attachment set is created, and the ID of the set is returned in the response. If an <code>attachmentSetId</code> is specified, the attachments are added to the specified set, if it exists.</p>
            attachments: <p>One or more attachments to add to the set. You can add up to three attachments per set. The size limit is 5 MB per attachment.</p> <p>In the <code>Attachment</code> object, use the <code>data</code> parameter to specify the contents of the attachment file. In the previous request syntax, the value for <code>data</code> appear as <code>blob</code>, which is represented as a base64-encoded string. The value for <code>fileName</code> is the name of the attachment, such as <code>troubleshoot-screenshot.png</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.add_attachments_to_set_request.AddAttachmentsToSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.add_attachments_to_set_response.AddAttachmentsToSetResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.add_attachments_to_set

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.add_attachments_to_set.async_add_attachments_to_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.add_attachments_to_set_request.AddAttachmentsToSetRequest = {}  # type: ignore[typeddict-item]
        if attachment_set_id is not None:
            input_["attachment_set_id"] = attachment_set_id
        input_["attachments"] = attachments

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_communication_to_case(
        self,
        communication_body: "aws_sdk_support.types.communication_body.CommunicationBody",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        case_id: Optional["aws_sdk_support.types.case_id.CaseId"] = None,
        cc_email_addresses: Optional[
            "aws_sdk_support.types.cc_email_address_list.CcEmailAddressList"
        ] = None,
        attachment_set_id: Optional[
            "aws_sdk_support.types.attachment_set_id.AttachmentSetId"
        ] = None,
    ) -> "aws_sdk_support.types.add_communication_to_case_response.AddCommunicationToCaseResponse":
        r"""<p>Adds additional customer communication to an Amazon Web Services Support case. Use the <code>caseId</code> parameter to identify the case to which to add communication. You can list a set of email addresses to copy on the communication by using the <code>ccEmailAddresses</code> parameter. The <code>communicationBody</code> value contains the text of the communication.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            case_id: <p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-2013-c4c1d2bf33c5cf47</i> </p>
            communication_body: <p>The body of an email communication to add to the support case.</p>
            cc_email_addresses: <p>The email addresses in the CC line of an email to be added to the support case.</p>
            attachment_set_id: <p>The ID of a set of one or more attachments for the communication to add to the case. Create the set by calling <a>AddAttachmentsToSet</a> </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.add_communication_to_case_request.AddCommunicationToCaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.add_communication_to_case_response.AddCommunicationToCaseResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.add_communication_to_case

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.add_communication_to_case.async_add_communication_to_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.add_communication_to_case_request.AddCommunicationToCaseRequest = {}  # type: ignore[typeddict-item]
        if case_id is not None:
            input_["case_id"] = case_id
        input_["communication_body"] = communication_body
        if cc_email_addresses is not None:
            input_["cc_email_addresses"] = cc_email_addresses
        if attachment_set_id is not None:
            input_["attachment_set_id"] = attachment_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_case(
        self,
        subject: "aws_sdk_support.types.subject.Subject",
        communication_body: "aws_sdk_support.types.communication_body.CommunicationBody",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        service_code: Optional[
            "aws_sdk_support.types.service_code2.ServiceCode2"
        ] = None,
        severity_code: Optional[
            "aws_sdk_support.types.severity_code.SeverityCode"
        ] = None,
        category_code: Optional[
            "aws_sdk_support.types.category_code.CategoryCode"
        ] = None,
        cc_email_addresses: Optional[
            "aws_sdk_support.types.cc_email_address_list.CcEmailAddressList"
        ] = None,
        language: Optional["aws_sdk_support.types.language.Language"] = None,
        issue_type: Optional["aws_sdk_support.types.issue_type.IssueType"] = None,
        attachment_set_id: Optional[
            "aws_sdk_support.types.attachment_set_id.AttachmentSetId"
        ] = None,
    ) -> "aws_sdk_support.types.create_case_response.CreateCaseResponse":
        r"""<p>Creates a case in the Amazon Web Services Support Center. This operation is similar to how you create a case in the Amazon Web Services Support Center <a href=\"https://console.aws.amazon.com/support/home#/case/create\">Create Case</a> page.</p> <p>The Amazon Web Services Support API doesn't support requesting service limit increases. You can submit a service limit increase in the following ways: </p> <ul> <li> <p>Submit a request from the Amazon Web Services Support Center <a href=\"https://console.aws.amazon.com/support/home#/case/create\">Create Case</a> page.</p> </li> <li> <p>Use the Service Quotas <a href=\"https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html\">RequestServiceQuotaIncrease</a> operation.</p> </li> </ul> <p>A successful <code>CreateCase</code> request returns an Amazon Web Services Support case number. You can use the <a>DescribeCases</a> operation and specify the case number to get existing Amazon Web Services Support cases. After you create a case, use the <a>AddCommunicationToCase</a> operation to add additional communication or attachments to an existing case.</p> <p>The <code>caseId</code> is separate from the <code>displayId</code> that appears in the <a href=\"https://console.aws.amazon.com/support\">Amazon Web Services Support Center</a>. Use the <a>DescribeCases</a> operation to get the <code>displayId</code>.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            subject: <p>The title of the support case. The title appears in the <b>Subject</b> field on the Amazon Web Services Support Center <a href=\"https://console.aws.amazon.com/support/home#/case/create\">Create Case</a> page.</p>
            service_code: <p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>
            severity_code: <p>A value that indicates the urgency of the case. This value determines the response time according to your service level agreement with Amazon Web Services Support. You can use the <a>DescribeSeverityLevels</a> operation to get the possible values for <code>severityCode</code>. </p> <p>For more information, see <a>SeverityLevel</a> and <a href=\"https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity\">Choosing a Severity</a> in the <i>Amazon Web Services Support User Guide</i>.</p> <note> <p>The availability of severity levels depends on the support plan for the Amazon Web Services account.</p> </note>
            category_code: <p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>
            communication_body: <p>The communication body text that describes the issue. This text appears in the <b>Description</b> field on the Amazon Web Services Support Center <a href=\"https://console.aws.amazon.com/support/home#/case/create\">Create Case</a> page.</p>
            cc_email_addresses: <p>A list of email addresses that Amazon Web Services Support copies on case correspondence. Amazon Web Services Support identifies the account that creates the case when you specify your Amazon Web Services credentials in an HTTP POST method or use the <a href=\"http://aws.amazon.com/tools/\">Amazon Web Services SDKs</a>. </p>
            language: <p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>
            issue_type: <p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>. If you don't specify a value, the default is <code>technical</code>.</p>
            attachment_set_id: <p>The ID of a set of one or more attachments for the case. Create the set by using the <a>AddAttachmentsToSet</a> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.create_case_request.CreateCaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.create_case_response.CreateCaseResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.create_case

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.create_case.async_create_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.create_case_request.CreateCaseRequest = {}  # type: ignore[typeddict-item]
        input_["subject"] = subject
        if service_code is not None:
            input_["service_code"] = service_code
        if severity_code is not None:
            input_["severity_code"] = severity_code
        if category_code is not None:
            input_["category_code"] = category_code
        input_["communication_body"] = communication_body
        if cc_email_addresses is not None:
            input_["cc_email_addresses"] = cc_email_addresses
        if language is not None:
            input_["language"] = language
        if issue_type is not None:
            input_["issue_type"] = issue_type
        if attachment_set_id is not None:
            input_["attachment_set_id"] = attachment_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_attachment(
        self,
        attachment_id: "aws_sdk_support.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> (
        "aws_sdk_support.types.describe_attachment_response.DescribeAttachmentResponse"
    ):
        r"""<p>Returns the attachment that has the specified ID. Attachments can include screenshots, error logs, or other files that describe your issue. Attachment IDs are generated by the case management system when you add an attachment to a case or case communication. Attachment IDs are returned in the <a>AttachmentDetails</a> objects that are returned by the <a>DescribeCommunications</a> operation.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            attachment_id: <p>The ID of the attachment to return. Attachment IDs are returned by the <a>DescribeCommunications</a> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_attachment_request.DescribeAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_attachment_response.DescribeAttachmentResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_attachment

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_attachment.async_describe_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_attachment_request.DescribeAttachmentRequest = {}  # type: ignore[typeddict-item]
        input_["attachment_id"] = attachment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_cases(
        self,
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        case_id_list: Optional["aws_sdk_support.types.case_id_list.CaseIdList"] = None,
        display_id: Optional["aws_sdk_support.types.display_id.DisplayId"] = None,
        after_time: Optional["aws_sdk_support.types.after_time.AfterTime"] = None,
        before_time: Optional["aws_sdk_support.types.before_time.BeforeTime"] = None,
        include_resolved_cases: Optional[
            "aws_sdk_support.types.include_resolved_cases.IncludeResolvedCases"
        ] = None,
        next_token: Optional["aws_sdk_support.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_support.types.max_results.MaxResults"] = None,
        language: Optional["aws_sdk_support.types.language.Language"] = None,
        include_communications: Optional[
            "aws_sdk_support.types.include_communications.IncludeCommunications"
        ] = None,
    ) -> "aws_sdk_support.types.describe_cases_response.DescribeCasesResponse":
        r"""<p>Returns a list of cases that you specify by passing one or more case IDs. You can use the <code>afterTime</code> and <code>beforeTime</code> parameters to filter the cases by date. You can set values for the <code>includeResolvedCases</code> and <code>includeCommunications</code> parameters to specify how much information to return.</p> <p>The response returns the following in JSON format:</p> <ul> <li> <p>One or more <a href=\"https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CaseDetails.html\">CaseDetails</a> data types.</p> </li> <li> <p>One or more <code>nextToken</code> values, which specify where to paginate the returned records represented by the <code>CaseDetails</code> objects.</p> </li> </ul> <p>Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request might return an error.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            case_id_list: <p>A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.</p>
            display_id: <p>The ID displayed for a case in the Amazon Web Services Support Center user interface.</p>
            after_time: <p>The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.</p>
            before_time: <p>The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.</p>
            include_resolved_cases: <p>Specifies whether to include resolved support cases in the <code>DescribeCases</code> response. By default, resolved cases aren't included.</p>
            next_token: <p>A resumption point for pagination.</p>
            max_results: <p>The maximum number of results to return before paginating.</p>
            language: <p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>
            include_communications: <p>Specifies whether to include communications in the <code>DescribeCases</code> response. By default, communications are included.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_cases_request.DescribeCasesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_cases_response.DescribeCasesResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_cases

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_cases.async_describe_cases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_cases_request.DescribeCasesRequest = {}  # type: ignore[typeddict-item]
        if case_id_list is not None:
            input_["case_id_list"] = case_id_list
        if display_id is not None:
            input_["display_id"] = display_id
        if after_time is not None:
            input_["after_time"] = after_time
        if before_time is not None:
            input_["before_time"] = before_time
        if include_resolved_cases is not None:
            input_["include_resolved_cases"] = include_resolved_cases
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if include_communications is not None:
            input_["include_communications"] = include_communications

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_cases(
        self,
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        case_id_list: Optional["aws_sdk_support.types.case_id_list.CaseIdList"] = None,
        display_id: Optional["aws_sdk_support.types.display_id.DisplayId"] = None,
        after_time: Optional["aws_sdk_support.types.after_time.AfterTime"] = None,
        before_time: Optional["aws_sdk_support.types.before_time.BeforeTime"] = None,
        include_resolved_cases: Optional[
            "aws_sdk_support.types.include_resolved_cases.IncludeResolvedCases"
        ] = None,
        next_token: Optional["aws_sdk_support.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_support.types.max_results.MaxResults"] = None,
        language: Optional["aws_sdk_support.types.language.Language"] = None,
        include_communications: Optional[
            "aws_sdk_support.types.include_communications.IncludeCommunications"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_support.types.case_details.CaseDetails]":
        _token = next_token
        while True:
            _response = await self.describe_cases(
                config_overrides=config_overrides,
                case_id_list=case_id_list,
                display_id=display_id,
                after_time=after_time,
                before_time=before_time,
                include_resolved_cases=include_resolved_cases,
                next_token=_token,
                max_results=max_results,
                language=language,
                include_communications=include_communications,
            )
            _page = _resolve_path(_response, ("cases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_communications(
        self,
        case_id: "aws_sdk_support.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        before_time: Optional["aws_sdk_support.types.before_time.BeforeTime"] = None,
        after_time: Optional["aws_sdk_support.types.after_time.AfterTime"] = None,
        next_token: Optional["aws_sdk_support.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_support.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_support.types.describe_communications_response.DescribeCommunicationsResponse":
        r"""<p>Returns communications and attachments for one or more support cases. Use the <code>afterTime</code> and <code>beforeTime</code> parameters to filter by date. You can use the <code>caseId</code> parameter to restrict the results to a specific case.</p> <p>Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request for data might cause an error.</p> <p>You can use the <code>maxResults</code> and <code>nextToken</code> parameters to control the pagination of the results. Set <code>maxResults</code> to the number of cases that you want to display on each page, and use <code>nextToken</code> to specify the resumption of pagination.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            case_id: <p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-2013-c4c1d2bf33c5cf47</i> </p>
            before_time: <p>The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.</p>
            after_time: <p>The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.</p>
            next_token: <p>A resumption point for pagination.</p>
            max_results: <p>The maximum number of results to return before paginating.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_communications_request.DescribeCommunicationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_communications_response.DescribeCommunicationsResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_communications

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_communications.async_describe_communications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_communications_request.DescribeCommunicationsRequest = {}  # type: ignore[typeddict-item]
        input_["case_id"] = case_id
        if before_time is not None:
            input_["before_time"] = before_time
        if after_time is not None:
            input_["after_time"] = after_time
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_communications(
        self,
        case_id: "aws_sdk_support.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        before_time: Optional["aws_sdk_support.types.before_time.BeforeTime"] = None,
        after_time: Optional["aws_sdk_support.types.after_time.AfterTime"] = None,
        next_token: Optional["aws_sdk_support.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_support.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_support.types.communication.Communication]":
        _token = next_token
        while True:
            _response = await self.describe_communications(
                case_id,
                config_overrides=config_overrides,
                before_time=before_time,
                after_time=after_time,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("communications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_create_case_options(
        self,
        issue_type: "aws_sdk_support.types.issue_type.IssueType",
        service_code: "aws_sdk_support.types.service_code2.ServiceCode2",
        language: "aws_sdk_support.types.language.Language",
        category_code: "aws_sdk_support.types.category_code.CategoryCode",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> "aws_sdk_support.types.describe_create_case_options_response.DescribeCreateCaseOptionsResponse":
        r"""<p>Returns a list of CreateCaseOption types along with the corresponding supported hours and language availability. You can specify the <code>language</code> <code>categoryCode</code>, <code>issueType</code> and <code>serviceCode</code> used to retrieve the CreateCaseOptions.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            issue_type: <p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>. If you don't specify a value, the default is <code>technical</code>.</p>
            service_code: <p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>
            language: <p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>
            category_code: <p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_create_case_options_request.DescribeCreateCaseOptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_create_case_options_response.DescribeCreateCaseOptionsResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_create_case_options

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_create_case_options.async_describe_create_case_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_create_case_options_request.DescribeCreateCaseOptionsRequest = {}  # type: ignore[typeddict-item]
        input_["issue_type"] = issue_type
        input_["service_code"] = service_code
        input_["language"] = language
        input_["category_code"] = category_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_services(
        self,
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        service_code_list: Optional[
            "aws_sdk_support.types.service_code_list.ServiceCodeList"
        ] = None,
        language: Optional["aws_sdk_support.types.language.Language"] = None,
    ) -> "aws_sdk_support.types.describe_services_response.DescribeServicesResponse":
        r"""<p>Returns the current list of Amazon Web Services services and a list of service categories for each service. You then use service names and categories in your <a>CreateCase</a> requests. Each Amazon Web Services service has its own set of categories.</p> <p>The service codes and category codes correspond to the values that appear in the <b>Service</b> and <b>Category</b> lists on the Amazon Web Services Support Center <a href=\"https://console.aws.amazon.com/support/home#/case/create\">Create Case</a> page. The values in those fields don't necessarily match the service codes and categories returned by the <code>DescribeServices</code> operation. Always use the service codes and categories that the <code>DescribeServices</code> operation returns, so that you have the most recent set of service and category codes.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            service_code_list: <p>A JSON-formatted list of service codes available for Amazon Web Services services.</p>
            language: <p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_services_request.DescribeServicesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_services_response.DescribeServicesResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_services

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_services.async_describe_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_services_request.DescribeServicesRequest = {}  # type: ignore[typeddict-item]
        if service_code_list is not None:
            input_["service_code_list"] = service_code_list
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_severity_levels(
        self,
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        language: Optional["aws_sdk_support.types.language.Language"] = None,
    ) -> "aws_sdk_support.types.describe_severity_levels_response.DescribeSeverityLevelsResponse":
        r"""<p>Returns the list of severity levels that you can assign to a support case. The severity level for a case is also a field in the <a>CaseDetails</a> data type that you include for a <a>CreateCase</a> request.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            language: <p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_severity_levels_request.DescribeSeverityLevelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_severity_levels_response.DescribeSeverityLevelsResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_severity_levels

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_severity_levels.async_describe_severity_levels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_severity_levels_request.DescribeSeverityLevelsRequest = {}  # type: ignore[typeddict-item]
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_supported_languages(
        self,
        issue_type: "aws_sdk_support.types.validated_issue_type_string.ValidatedIssueTypeString",
        service_code: "aws_sdk_support.types.validated_service_code.ValidatedServiceCode",
        category_code: "aws_sdk_support.types.validated_category_code.ValidatedCategoryCode",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> "aws_sdk_support.types.describe_supported_languages_response.DescribeSupportedLanguagesResponse":
        r"""<p>Returns a list of supported languages for a specified <code>categoryCode</code>, <code>issueType</code> and <code>serviceCode</code>. The returned supported languages will include a ISO 639-1 code for the <code>language</code>, and the language display name.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            issue_type: <p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>.</p>
            service_code: <p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>
            category_code: <p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_supported_languages_request.DescribeSupportedLanguagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_supported_languages_response.DescribeSupportedLanguagesResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_supported_languages

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_supported_languages.async_describe_supported_languages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_supported_languages_request.DescribeSupportedLanguagesRequest = {}  # type: ignore[typeddict-item]
        input_["issue_type"] = issue_type
        input_["service_code"] = service_code
        input_["category_code"] = category_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_trusted_advisor_check_refresh_statuses(
        self,
        check_ids: "aws_sdk_support.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> "aws_sdk_support.types.describe_trusted_advisor_check_refresh_statuses_response.DescribeTrustedAdvisorCheckRefreshStatusesResponse":
        r"""<p>Returns the refresh status of the Trusted Advisor checks that have the specified check IDs. You can get the check IDs by calling the <a>DescribeTrustedAdvisorChecks</a> operation.</p> <p>Some checks are refreshed automatically, and you can't return their refresh statuses by using the <code>DescribeTrustedAdvisorCheckRefreshStatuses</code> operation. If you call this operation for these checks, you might see an <code>InvalidParameterValue</code> error.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note> <p>To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see <a href=\"https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\">About the Amazon Web Services Support API</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Args:
            check_ids: <p>The IDs of the Trusted Advisor checks to get the status.</p> <note> <p>If you specify the check ID of a check that is automatically refreshed, you might see an <code>InvalidParameterValue</code> error.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_trusted_advisor_check_refresh_statuses_request.DescribeTrustedAdvisorCheckRefreshStatusesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_trusted_advisor_check_refresh_statuses_response.DescribeTrustedAdvisorCheckRefreshStatusesResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_trusted_advisor_check_refresh_statuses

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_trusted_advisor_check_refresh_statuses.async_describe_trusted_advisor_check_refresh_statuses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_trusted_advisor_check_refresh_statuses_request.DescribeTrustedAdvisorCheckRefreshStatusesRequest = {}  # type: ignore[typeddict-item]
        input_["check_ids"] = check_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_trusted_advisor_check_result(
        self,
        check_id: "aws_sdk_support.types.string.String",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        language: Optional["aws_sdk_support.types.string.String"] = None,
    ) -> "aws_sdk_support.types.describe_trusted_advisor_check_result_response.DescribeTrustedAdvisorCheckResultResponse":
        r"""<p>Returns the results of the Trusted Advisor check that has the specified check ID. You can get the check IDs by calling the <a>DescribeTrustedAdvisorChecks</a> operation.</p> <p>The response contains a <a>TrustedAdvisorCheckResult</a> object, which contains these three objects:</p> <ul> <li> <p> <a>TrustedAdvisorCategorySpecificSummary</a> </p> </li> <li> <p> <a>TrustedAdvisorResourceDetail</a> </p> </li> <li> <p> <a>TrustedAdvisorResourcesSummary</a> </p> </li> </ul> <p>In addition, the response contains these fields:</p> <ul> <li> <p> <b>status</b> - The alert status of the check can be <code>ok</code> (green), <code>warning</code> (yellow), <code>error</code> (red), or <code>not_available</code>.</p> </li> <li> <p> <b>timestamp</b> - The time of the last refresh of the check.</p> </li> <li> <p> <b>checkId</b> - The unique identifier for the check.</p> </li> </ul> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note> <p>To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see <a href=\"https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\">About the Amazon Web Services Support API</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Args:
            check_id: <p>The unique identifier for the Trusted Advisor check.</p>
            language: <p>The ISO 639-1 code for the language that you want your check results to appear in.</p> <p>The Amazon Web Services Support API currently supports the following languages for Trusted Advisor:</p> <ul> <li> <p>Chinese, Simplified - <code>zh</code> </p> </li> <li> <p>Chinese, Traditional - <code>zh_TW</code> </p> </li> <li> <p>English - <code>en</code> </p> </li> <li> <p>French - <code>fr</code> </p> </li> <li> <p>German - <code>de</code> </p> </li> <li> <p>Indonesian - <code>id</code> </p> </li> <li> <p>Italian - <code>it</code> </p> </li> <li> <p>Japanese - <code>ja</code> </p> </li> <li> <p>Korean - <code>ko</code> </p> </li> <li> <p>Portuguese, Brazilian - <code>pt_BR</code> </p> </li> <li> <p>Spanish - <code>es</code> </p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_trusted_advisor_check_result_request.DescribeTrustedAdvisorCheckResultRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_trusted_advisor_check_result_response.DescribeTrustedAdvisorCheckResultResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_trusted_advisor_check_result

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_trusted_advisor_check_result.async_describe_trusted_advisor_check_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_trusted_advisor_check_result_request.DescribeTrustedAdvisorCheckResultRequest = {}  # type: ignore[typeddict-item]
        input_["check_id"] = check_id
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_trusted_advisor_checks(
        self,
        language: "aws_sdk_support.types.string.String",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> "aws_sdk_support.types.describe_trusted_advisor_checks_response.DescribeTrustedAdvisorChecksResponse":
        r"""<p>Returns information about all available Trusted Advisor checks, including the name, ID, category, description, and metadata. You must specify a language code.</p> <p>The response contains a <a>TrustedAdvisorCheckDescription</a> object for each check. You must set the Amazon Web Services Region to us-east-1.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> <li> <p>The names and descriptions for Trusted Advisor checks are subject to change. We recommend that you specify the check ID in your code to uniquely identify a check.</p> </li> </ul> </note> <p>To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see <a href=\"https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\">About the Amazon Web Services Support API</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Args:
            language: <p>The ISO 639-1 code for the language that you want your checks to appear in.</p> <p>The Amazon Web Services Support API currently supports the following languages for Trusted Advisor:</p> <ul> <li> <p>Chinese, Simplified - <code>zh</code> </p> </li> <li> <p>Chinese, Traditional - <code>zh_TW</code> </p> </li> <li> <p>English - <code>en</code> </p> </li> <li> <p>French - <code>fr</code> </p> </li> <li> <p>German - <code>de</code> </p> </li> <li> <p>Indonesian - <code>id</code> </p> </li> <li> <p>Italian - <code>it</code> </p> </li> <li> <p>Japanese - <code>ja</code> </p> </li> <li> <p>Korean - <code>ko</code> </p> </li> <li> <p>Portuguese, Brazilian - <code>pt_BR</code> </p> </li> <li> <p>Spanish - <code>es</code> </p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_trusted_advisor_checks_request.DescribeTrustedAdvisorChecksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_trusted_advisor_checks_response.DescribeTrustedAdvisorChecksResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_trusted_advisor_checks

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_trusted_advisor_checks.async_describe_trusted_advisor_checks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_trusted_advisor_checks_request.DescribeTrustedAdvisorChecksRequest = {}  # type: ignore[typeddict-item]
        input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_trusted_advisor_check_summaries(
        self,
        check_ids: "aws_sdk_support.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> "aws_sdk_support.types.describe_trusted_advisor_check_summaries_response.DescribeTrustedAdvisorCheckSummariesResponse":
        r"""<p>Returns the results for the Trusted Advisor check summaries for the check IDs that you specified. You can get the check IDs by calling the <a>DescribeTrustedAdvisorChecks</a> operation.</p> <p>The response contains an array of <a>TrustedAdvisorCheckSummary</a> objects.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note> <p>To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see <a href=\"https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\">About the Amazon Web Services Support API</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Args:
            check_ids: <p>The IDs of the Trusted Advisor checks.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.describe_trusted_advisor_check_summaries_request.DescribeTrustedAdvisorCheckSummariesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.describe_trusted_advisor_check_summaries_response.DescribeTrustedAdvisorCheckSummariesResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.describe_trusted_advisor_check_summaries

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.describe_trusted_advisor_check_summaries.async_describe_trusted_advisor_check_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.describe_trusted_advisor_check_summaries_request.DescribeTrustedAdvisorCheckSummariesRequest = {}  # type: ignore[typeddict-item]
        input_["check_ids"] = check_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def refresh_trusted_advisor_check(
        self,
        check_id: "aws_sdk_support.types.string.String",
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
    ) -> "aws_sdk_support.types.refresh_trusted_advisor_check_response.RefreshTrustedAdvisorCheckResponse":
        r"""<p>Refreshes the Trusted Advisor check that you specify using the check ID. You can get the check IDs by calling the <a>DescribeTrustedAdvisorChecks</a> operation.</p> <p>Some checks are refreshed automatically. If you call the <code>RefreshTrustedAdvisorCheck</code> operation to refresh them, you might see the <code>InvalidParameterValue</code> error.</p> <p>The response contains a <a>TrustedAdvisorCheckRefreshStatus</a> object.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note> <p>To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don't support the Trusted Advisor operations. For more information, see <a href=\"https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\">About the Amazon Web Services Support API</a> in the <i>Amazon Web Services Support User Guide</i>.</p>

        Args:
            check_id: <p>The unique identifier for the Trusted Advisor check to refresh.</p> <note> <p>Specifying the check ID of a check that is automatically refreshed causes an <code>InvalidParameterValue</code> error.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.refresh_trusted_advisor_check_request.RefreshTrustedAdvisorCheckRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.refresh_trusted_advisor_check_response.RefreshTrustedAdvisorCheckResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.refresh_trusted_advisor_check

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.refresh_trusted_advisor_check.async_refresh_trusted_advisor_check(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.refresh_trusted_advisor_check_request.RefreshTrustedAdvisorCheckRequest = {}  # type: ignore[typeddict-item]
        input_["check_id"] = check_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def resolve_case(
        self,
        *,
        config_overrides: Optional[AsyncSupportClientConfig] = None,
        case_id: Optional["aws_sdk_support.types.case_id.CaseId"] = None,
    ) -> "aws_sdk_support.types.resolve_case_response.ResolveCaseResponse":
        r"""<p>Resolves a support case. This operation takes a <code>caseId</code> and returns the initial and final state of the case.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href=\"http://aws.amazon.com/premiumsupport/\">Amazon Web Services Support</a>.</p> </li> </ul> </note>

        Args:
            case_id: <p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-2013-c4c1d2bf33c5cf47</i> </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_support.types.resolve_case_request.ResolveCaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_support.types.resolve_case_response.ResolveCaseResponse"
        ]:
            import aws_sdk_support._operations.aws_support_20130415.resolve_case

            (
                output,
                http_response,
            ) = await aws_sdk_support._operations.aws_support_20130415.resolve_case.async_resolve_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_support.types.resolve_case_request.ResolveCaseRequest = {}  # type: ignore[typeddict-item]
        if case_id is not None:
            input_["case_id"] = case_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
