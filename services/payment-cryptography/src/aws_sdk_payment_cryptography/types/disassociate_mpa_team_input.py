"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#DisassociateMpaTeamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.mpa_operation
    import aws_sdk_payment_cryptography.types.mpa_requester_comment


class DisassociateMpaTeamInput(TypedDict, closed=True):
    action: "aws_sdk_payment_cryptography.types.mpa_operation.MpaOperation"
    """<p>The protected operation to disassociate from the MPA team. Currently, the only supported value is <code>IMPORT_ROOT_PUBLIC_KEY_CERTIFICATE</code>.</p>"""
    requester_comment: NotRequired[
        "aws_sdk_payment_cryptography.types.mpa_requester_comment.MpaRequesterComment"
    ]
    """<p>The comment from the requester explaining the reason for the disassociation.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateMpaTeamInput) -> dict:
    out: dict = {}
    out["Action"] = value["action"]
    if "requester_comment" in value:
        out["RequesterComment"] = value["requester_comment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateMpaTeamInput:
    out: DisassociateMpaTeamInput = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        out["action"] = data["Action"]
    else:
        raise DeserializationError("DisassociateMpaTeamInput.action required")
    if "RequesterComment" in data:
        out["requester_comment"] = data["RequesterComment"]
    return out
