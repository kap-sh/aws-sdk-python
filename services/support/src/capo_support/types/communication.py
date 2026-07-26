"""Generated from Smithy shape ``com.amazonaws.support#Communication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.attachment_set
    import capo_support.types.case_id
    import capo_support.types.submitted_by
    import capo_support.types.time_created
    import capo_support.types.validated_communication_body


class Communication(TypedDict, closed=True):
    case_id: NotRequired["capo_support.types.case_id.CaseId"]
    """<p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-2013-c4c1d2bf33c5cf47</i> </p>"""
    body: NotRequired[
        "capo_support.types.validated_communication_body.ValidatedCommunicationBody"
    ]
    """<p>The text of the communication between the customer and Amazon Web Services Support.</p>"""
    submitted_by: NotRequired["capo_support.types.submitted_by.SubmittedBy"]
    r"""<p>The identity of the account that submitted, or responded to, the support case. Customer entries include the IAM role as well as the email address (for example, \"AdminRole (Role) <janedoe@example.com>). Entries from the Amazon Web Services Support team display \"Amazon Web Services,\" and don't show an email address. </p>"""
    time_created: NotRequired["capo_support.types.time_created.TimeCreated"]
    """<p>The time the communication was created.</p>"""
    attachment_set: NotRequired["capo_support.types.attachment_set.AttachmentSet"]
    """<p>Information about the attachments to the case communication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Communication) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    if "body" in value:
        out["body"] = value["body"]
    if "submitted_by" in value:
        out["submittedBy"] = value["submitted_by"]
    if "time_created" in value:
        out["timeCreated"] = value["time_created"]
    if "attachment_set" in value:
        import capo_support.types.attachment_set

        out["attachmentSet"] = capo_support.types.attachment_set.serialize_aws_json_1_1(
            value["attachment_set"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Communication:
    out: Communication = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    if "body" in data:
        out["body"] = data["body"]
    if "submittedBy" in data:
        out["submitted_by"] = data["submittedBy"]
    if "timeCreated" in data:
        out["time_created"] = data["timeCreated"]
    if "attachmentSet" in data:
        import capo_support.types.attachment_set

        out["attachment_set"] = (
            capo_support.types.attachment_set.deserialize_aws_json_1_1(
                data["attachmentSet"]
            )
        )
    return out
