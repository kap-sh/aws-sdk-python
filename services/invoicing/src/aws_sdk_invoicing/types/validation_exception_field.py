"""Generated from Smithy shape ``com.amazonaws.invoicing#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string


class ValidationExceptionField(TypedDict, closed=True):
    name: "aws_sdk_invoicing.types.basic_string.BasicString"
    """<p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>"""
    message: "aws_sdk_invoicing.types.basic_string.BasicString"
    """<p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>"""


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
