"""Generated from Smithy shape ``com.amazonaws.support#AddCommunicationToCaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.attachment_set_id
    import aws_sdk_support.types.case_id
    import aws_sdk_support.types.cc_email_address_list
    import aws_sdk_support.types.communication_body


class AddCommunicationToCaseRequest(TypedDict):
    case_id: NotRequired["aws_sdk_support.types.case_id.CaseId"]
    """<p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-2013-c4c1d2bf33c5cf47</i> </p>"""
    communication_body: "aws_sdk_support.types.communication_body.CommunicationBody"
    """<p>The body of an email communication to add to the support case.</p>"""
    cc_email_addresses: NotRequired[
        "aws_sdk_support.types.cc_email_address_list.CcEmailAddressList"
    ]
    """<p>The email addresses in the CC line of an email to be added to the support case.</p>"""
    attachment_set_id: NotRequired[
        "aws_sdk_support.types.attachment_set_id.AttachmentSetId"
    ]
    """<p>The ID of a set of one or more attachments for the communication to add to the case. Create the set by calling <a>AddAttachmentsToSet</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddCommunicationToCaseRequest) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    out["communicationBody"] = value["communication_body"]
    if "cc_email_addresses" in value:
        import aws_sdk_support.types.cc_email_address_list

        out["ccEmailAddresses"] = (
            aws_sdk_support.types.cc_email_address_list.serialize_aws_json_1_1(
                value["cc_email_addresses"]
            )
        )
    if "attachment_set_id" in value:
        out["attachmentSetId"] = value["attachment_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddCommunicationToCaseRequest:
    out: AddCommunicationToCaseRequest = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    if "communicationBody" in data:
        out["communication_body"] = data["communicationBody"]
    else:
        raise DeserializationError(
            "AddCommunicationToCaseRequest.communication_body required"
        )
    if "ccEmailAddresses" in data:
        import aws_sdk_support.types.cc_email_address_list

        out["cc_email_addresses"] = (
            aws_sdk_support.types.cc_email_address_list.deserialize_aws_json_1_1(
                data["ccEmailAddresses"]
            )
        )
    if "attachmentSetId" in data:
        out["attachment_set_id"] = data["attachmentSetId"]
    return out
