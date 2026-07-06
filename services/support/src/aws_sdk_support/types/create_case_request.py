"""Generated from Smithy shape ``com.amazonaws.support#CreateCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.attachment_set_id
    import aws_sdk_support.types.category_code
    import aws_sdk_support.types.cc_email_address_list
    import aws_sdk_support.types.communication_body
    import aws_sdk_support.types.issue_type
    import aws_sdk_support.types.language
    import aws_sdk_support.types.service_code2
    import aws_sdk_support.types.severity_code
    import aws_sdk_support.types.subject


class CreateCaseRequest(TypedDict, closed=True):
    subject: "aws_sdk_support.types.subject.Subject"
    r"""<p>The title of the support case. The title appears in the <b>Subject</b> field on the Amazon Web Services Support Center <a href=\"https://console.aws.amazon.com/support/home#/case/create\">Create Case</a> page.</p>"""
    service_code: NotRequired["aws_sdk_support.types.service_code2.ServiceCode2"]
    """<p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>"""
    severity_code: NotRequired["aws_sdk_support.types.severity_code.SeverityCode"]
    r"""<p>A value that indicates the urgency of the case. This value determines the response time according to your service level agreement with Amazon Web Services Support. You can use the <a>DescribeSeverityLevels</a> operation to get the possible values for <code>severityCode</code>. </p> <p>For more information, see <a>SeverityLevel</a> and <a href=\"https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity\">Choosing a Severity</a> in the <i>Amazon Web Services Support User Guide</i>.</p> <note> <p>The availability of severity levels depends on the support plan for the Amazon Web Services account.</p> </note>"""
    category_code: NotRequired["aws_sdk_support.types.category_code.CategoryCode"]
    """<p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>"""
    communication_body: "aws_sdk_support.types.communication_body.CommunicationBody"
    r"""<p>The communication body text that describes the issue. This text appears in the <b>Description</b> field on the Amazon Web Services Support Center <a href=\"https://console.aws.amazon.com/support/home#/case/create\">Create Case</a> page.</p>"""
    cc_email_addresses: NotRequired[
        "aws_sdk_support.types.cc_email_address_list.CcEmailAddressList"
    ]
    r"""<p>A list of email addresses that Amazon Web Services Support copies on case correspondence. Amazon Web Services Support identifies the account that creates the case when you specify your Amazon Web Services credentials in an HTTP POST method or use the <a href=\"http://aws.amazon.com/tools/\">Amazon Web Services SDKs</a>. </p>"""
    language: NotRequired["aws_sdk_support.types.language.Language"]
    r"""<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""
    issue_type: NotRequired["aws_sdk_support.types.issue_type.IssueType"]
    """<p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>. If you don't specify a value, the default is <code>technical</code>.</p>"""
    attachment_set_id: NotRequired[
        "aws_sdk_support.types.attachment_set_id.AttachmentSetId"
    ]
    """<p>The ID of a set of one or more attachments for the case. Create the set by using the <a>AddAttachmentsToSet</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCaseRequest) -> dict:
    out: dict = {}
    out["subject"] = value["subject"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "severity_code" in value:
        out["severityCode"] = value["severity_code"]
    if "category_code" in value:
        out["categoryCode"] = value["category_code"]
    out["communicationBody"] = value["communication_body"]
    if "cc_email_addresses" in value:
        import aws_sdk_support.types.cc_email_address_list

        out["ccEmailAddresses"] = (
            aws_sdk_support.types.cc_email_address_list.serialize_aws_json_1_1(
                value["cc_email_addresses"]
            )
        )
    if "language" in value:
        out["language"] = value["language"]
    if "issue_type" in value:
        out["issueType"] = value["issue_type"]
    if "attachment_set_id" in value:
        out["attachmentSetId"] = value["attachment_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCaseRequest:
    out: CreateCaseRequest = {}  # type: ignore[typeddict-item]
    if "subject" in data:
        out["subject"] = data["subject"]
    else:
        raise DeserializationError("CreateCaseRequest.subject required")
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "severityCode" in data:
        out["severity_code"] = data["severityCode"]
    if "categoryCode" in data:
        out["category_code"] = data["categoryCode"]
    if "communicationBody" in data:
        out["communication_body"] = data["communicationBody"]
    else:
        raise DeserializationError("CreateCaseRequest.communication_body required")
    if "ccEmailAddresses" in data:
        import aws_sdk_support.types.cc_email_address_list

        out["cc_email_addresses"] = (
            aws_sdk_support.types.cc_email_address_list.deserialize_aws_json_1_1(
                data["ccEmailAddresses"]
            )
        )
    if "language" in data:
        out["language"] = data["language"]
    if "issueType" in data:
        out["issue_type"] = data["issueType"]
    if "attachmentSetId" in data:
        out["attachment_set_id"] = data["attachmentSetId"]
    return out
