"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#AcceptPageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.accept_code
    import aws_sdk_ssm_contacts.types.accept_code_validation
    import aws_sdk_ssm_contacts.types.accept_type
    import aws_sdk_ssm_contacts.types.receipt_info
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class AcceptPageRequest(TypedDict):
    page_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the engagement to a contact channel.</p>"""
    contact_channel_id: NotRequired[
        "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    ]
    """<p>The ARN of the contact channel.</p>"""
    accept_type: "aws_sdk_ssm_contacts.types.accept_type.AcceptType"
    """<p>The type indicates if the page was <code>DELIVERED</code> or <code>READ</code>.</p>"""
    note: NotRequired["aws_sdk_ssm_contacts.types.receipt_info.ReceiptInfo"]
    """<p>Information provided by the user when the user acknowledges the page.</p>"""
    accept_code: "aws_sdk_ssm_contacts.types.accept_code.AcceptCode"
    """<p>A 6-digit code used to acknowledge the page.</p>"""
    accept_code_validation: NotRequired[
        "aws_sdk_ssm_contacts.types.accept_code_validation.AcceptCodeValidation"
    ]
    """<p>An optional field that Incident Manager uses to <code>ENFORCE</code> <code>AcceptCode</code> validation when acknowledging an page. Acknowledgement can occur by replying to a page, or when entering the AcceptCode in the console. Enforcing AcceptCode validation causes Incident Manager to verify that the code entered by the user matches the code sent by Incident Manager with the page.</p> <p>Incident Manager can also <code>IGNORE</code> <code>AcceptCode</code> validation. Ignoring <code>AcceptCode</code> validation causes Incident Manager to accept any value entered for the <code>AcceptCode</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptPageRequest) -> dict:
    out: dict = {}
    out["PageId"] = value["page_id"]
    if "contact_channel_id" in value:
        out["ContactChannelId"] = value["contact_channel_id"]
    import aws_sdk_ssm_contacts.types.accept_type

    out["AcceptType"] = aws_sdk_ssm_contacts.types.accept_type.serialize_aws_json_1_1(
        value["accept_type"]
    )
    if "note" in value:
        out["Note"] = value["note"]
    out["AcceptCode"] = value["accept_code"]
    if "accept_code_validation" in value:
        import aws_sdk_ssm_contacts.types.accept_code_validation

        out["AcceptCodeValidation"] = (
            aws_sdk_ssm_contacts.types.accept_code_validation.serialize_aws_json_1_1(
                value["accept_code_validation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptPageRequest:
    out: AcceptPageRequest = {}  # type: ignore[typeddict-item]
    if "PageId" in data:
        out["page_id"] = data["PageId"]
    else:
        raise DeserializationError("AcceptPageRequest.page_id required")
    if "ContactChannelId" in data:
        out["contact_channel_id"] = data["ContactChannelId"]
    if "AcceptType" in data:
        import aws_sdk_ssm_contacts.types.accept_type

        out["accept_type"] = (
            aws_sdk_ssm_contacts.types.accept_type.deserialize_aws_json_1_1(
                data["AcceptType"]
            )
        )
    else:
        raise DeserializationError("AcceptPageRequest.accept_type required")
    if "Note" in data:
        out["note"] = data["Note"]
    if "AcceptCode" in data:
        out["accept_code"] = data["AcceptCode"]
    else:
        raise DeserializationError("AcceptPageRequest.accept_code required")
    if "AcceptCodeValidation" in data:
        import aws_sdk_ssm_contacts.types.accept_code_validation

        out["accept_code_validation"] = (
            aws_sdk_ssm_contacts.types.accept_code_validation.deserialize_aws_json_1_1(
                data["AcceptCodeValidation"]
            )
        )
    return out
