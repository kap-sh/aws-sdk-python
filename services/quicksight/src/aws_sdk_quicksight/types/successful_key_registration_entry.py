"""Generated from Smithy shape ``com.amazonaws.quicksight#SuccessfulKeyRegistrationEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class SuccessfulKeyRegistrationEntry(TypedDict):
    key_arn: "aws_sdk_quicksight.types.string.String"
    """<p>The ARN of the KMS key that is associated with the <code>SuccessfulKeyRegistrationEntry</code> entry.</p>"""
    status_code: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of a <code>SuccessfulKeyRegistrationEntry</code> entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulKeyRegistrationEntry) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["StatusCode"] = value.get("status_code", 0)
    return out


def deserialize_json(data: dict) -> SuccessfulKeyRegistrationEntry:
    out: SuccessfulKeyRegistrationEntry = {}  # type: ignore[typeddict-item]
    if "KeyArn" in data:
        out["key_arn"] = data["KeyArn"]
    else:
        raise DeserializationError("SuccessfulKeyRegistrationEntry.key_arn required")
    if "StatusCode" in data:
        out["status_code"] = data["StatusCode"]
    else:
        out["status_code"] = 0
    return out
