"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ValidationExceptionField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string


class ValidationExceptionField(TypedDict):
    name: "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    """<p>The name of the field associated with the error.</p>"""
    message: "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    """<p>See applicable actions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ValidationExceptionField.name required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
