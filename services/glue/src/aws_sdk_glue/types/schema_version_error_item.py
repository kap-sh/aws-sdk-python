"""Generated from Smithy shape ``com.amazonaws.glue#SchemaVersionErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.error_details
    import aws_sdk_glue.types.version_long_number


class SchemaVersionErrorItem(TypedDict, closed=True):
    version_number: NotRequired[
        "aws_sdk_glue.types.version_long_number.VersionLongNumber"
    ]
    """<p>The version number of the schema.</p>"""
    error_details: NotRequired["aws_sdk_glue.types.error_details.ErrorDetails"]
    """<p>The details of the error for the schema version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaVersionErrorItem) -> dict:
    out: dict = {}
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "error_details" in value:
        import aws_sdk_glue.types.error_details

        out["ErrorDetails"] = aws_sdk_glue.types.error_details.serialize_aws_json_1_1(
            value["error_details"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaVersionErrorItem:
    out: SchemaVersionErrorItem = {}  # type: ignore[typeddict-item]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "ErrorDetails" in data:
        import aws_sdk_glue.types.error_details

        out["error_details"] = (
            aws_sdk_glue.types.error_details.deserialize_aws_json_1_1(
                data["ErrorDetails"]
            )
        )
    return out
