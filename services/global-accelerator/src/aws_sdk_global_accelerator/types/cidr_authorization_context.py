"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CidrAuthorizationContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string


class CidrAuthorizationContext(TypedDict, closed=True):
    message: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The plain-text authorization message for the prefix and account.</p>"""
    signature: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The signed authorization message for the prefix and account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CidrAuthorizationContext) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["Signature"] = value["signature"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CidrAuthorizationContext:
    out: CidrAuthorizationContext = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("CidrAuthorizationContext.message required")
    if "Signature" in data:
        out["signature"] = data["Signature"]
    else:
        raise DeserializationError("CidrAuthorizationContext.signature required")
    return out
