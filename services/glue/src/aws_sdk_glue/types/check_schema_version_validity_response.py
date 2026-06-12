"""Generated from Smithy shape ``com.amazonaws.glue#CheckSchemaVersionValidityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.is_version_valid
    import aws_sdk_glue.types.schema_validation_error


class CheckSchemaVersionValidityResponse(TypedDict):
    valid: "aws_sdk_glue.types.is_version_valid.IsVersionValid"
    """<p>Return true, if the schema is valid and false otherwise.</p>"""
    error: NotRequired[
        "aws_sdk_glue.types.schema_validation_error.SchemaValidationError"
    ]
    """<p>A validation failure error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckSchemaVersionValidityResponse) -> dict:
    out: dict = {}
    out["Valid"] = value.get("valid", False)
    if "error" in value:
        out["Error"] = value["error"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckSchemaVersionValidityResponse:
    out: CheckSchemaVersionValidityResponse = {}  # type: ignore[typeddict-item]
    if "Valid" in data:
        out["valid"] = data["Valid"]
    else:
        out["valid"] = False
    if "Error" in data:
        out["error"] = data["Error"]
    return out
