"""Generated from Smithy shape ``com.amazonaws.support#CaseDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support.types.case_id
    import aws_sdk_support.types.category_code
    import aws_sdk_support.types.cc_email_address_list
    import aws_sdk_support.types.display_id
    import aws_sdk_support.types.language
    import aws_sdk_support.types.recent_case_communications
    import aws_sdk_support.types.service_code
    import aws_sdk_support.types.severity_code
    import aws_sdk_support.types.status
    import aws_sdk_support.types.subject
    import aws_sdk_support.types.submitted_by
    import aws_sdk_support.types.time_created


class CaseDetails(TypedDict):
    case_id: NotRequired["aws_sdk_support.types.case_id.CaseId"]
    """<p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-2013-c4c1d2bf33c5cf47</i> </p>"""
    display_id: NotRequired["aws_sdk_support.types.display_id.DisplayId"]
    """<p>The ID displayed for the case in the Amazon Web Services Support Center. This is a numeric string.</p>"""
    subject: NotRequired["aws_sdk_support.types.subject.Subject"]
    """<p>The subject line for the case in the Amazon Web Services Support Center.</p>"""
    status: NotRequired["aws_sdk_support.types.status.Status"]
    """<p>The status of the case.</p> <p>Valid values:</p> <ul> <li> <p> <code>all-open</code> </p> </li> <li> <p> <code>customer-action-completed</code> </p> </li> <li> <p> <code>opened</code> </p> </li> <li> <p> <code>pending-customer-action</code> </p> </li> <li> <p> <code>reopened</code> </p> </li> <li> <p> <code>resolved</code> </p> </li> <li> <p> <code>unassigned</code> </p> </li> <li> <p> <code>work-in-progress</code> </p> </li> </ul>"""
    service_code: NotRequired["aws_sdk_support.types.service_code.ServiceCode"]
    """<p>The code for the Amazon Web Services service. You can get a list of codes and the corresponding service names by calling <a>DescribeServices</a>.</p>"""
    category_code: NotRequired["aws_sdk_support.types.category_code.CategoryCode"]
    """<p>The category of problem for the support case.</p>"""
    severity_code: NotRequired["aws_sdk_support.types.severity_code.SeverityCode"]
    """<p>The code for the severity level returned by the call to <a>DescribeSeverityLevels</a>.</p>"""
    submitted_by: NotRequired["aws_sdk_support.types.submitted_by.SubmittedBy"]
    """<p>The email address of the account that submitted the case.</p>"""
    time_created: NotRequired["aws_sdk_support.types.time_created.TimeCreated"]
    """<p>The time that the case was created in the Amazon Web Services Support Center.</p>"""
    recent_communications: NotRequired[
        "aws_sdk_support.types.recent_case_communications.RecentCaseCommunications"
    ]
    """<p>The five most recent communications between you and Amazon Web Services Support Center, including the IDs of any attachments to the communications. Also includes a <code>nextToken</code> that you can use to retrieve earlier communications.</p>"""
    cc_email_addresses: NotRequired[
        "aws_sdk_support.types.cc_email_address_list.CcEmailAddressList"
    ]
    """<p>The email addresses that receive copies of communication about the case.</p>"""
    language: NotRequired["aws_sdk_support.types.language.Language"]
    r"""<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaseDetails) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    if "display_id" in value:
        out["displayId"] = value["display_id"]
    if "subject" in value:
        out["subject"] = value["subject"]
    if "status" in value:
        out["status"] = value["status"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "category_code" in value:
        out["categoryCode"] = value["category_code"]
    if "severity_code" in value:
        out["severityCode"] = value["severity_code"]
    if "submitted_by" in value:
        out["submittedBy"] = value["submitted_by"]
    if "time_created" in value:
        out["timeCreated"] = value["time_created"]
    if "recent_communications" in value:
        import aws_sdk_support.types.recent_case_communications

        out["recentCommunications"] = (
            aws_sdk_support.types.recent_case_communications.serialize_aws_json_1_1(
                value["recent_communications"]
            )
        )
    if "cc_email_addresses" in value:
        import aws_sdk_support.types.cc_email_address_list

        out["ccEmailAddresses"] = (
            aws_sdk_support.types.cc_email_address_list.serialize_aws_json_1_1(
                value["cc_email_addresses"]
            )
        )
    if "language" in value:
        out["language"] = value["language"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CaseDetails:
    out: CaseDetails = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    if "displayId" in data:
        out["display_id"] = data["displayId"]
    if "subject" in data:
        out["subject"] = data["subject"]
    if "status" in data:
        out["status"] = data["status"]
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    if "categoryCode" in data:
        out["category_code"] = data["categoryCode"]
    if "severityCode" in data:
        out["severity_code"] = data["severityCode"]
    if "submittedBy" in data:
        out["submitted_by"] = data["submittedBy"]
    if "timeCreated" in data:
        out["time_created"] = data["timeCreated"]
    if "recentCommunications" in data:
        import aws_sdk_support.types.recent_case_communications

        out["recent_communications"] = (
            aws_sdk_support.types.recent_case_communications.deserialize_aws_json_1_1(
                data["recentCommunications"]
            )
        )
    if "ccEmailAddresses" in data:
        import aws_sdk_support.types.cc_email_address_list

        out["cc_email_addresses"] = (
            aws_sdk_support.types.cc_email_address_list.deserialize_aws_json_1_1(
                data["ccEmailAddresses"]
            )
        )
    if "language" in data:
        out["language"] = data["language"]
    return out
