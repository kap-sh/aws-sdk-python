"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53_recovery_cluster.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_cluster.types.string


class ValidationExceptionField(TypedDict, closed=True):
    name: "aws_sdk_route53_recovery_cluster.types.string.String"
    """<p>The field that had the validation exception.</p>"""
    message: "aws_sdk_route53_recovery_cluster.types.string.String"
    """<p>Information about the validation exception.</p>"""


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
