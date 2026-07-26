"""Generated from Smithy shape ``com.amazonaws.glue#SchemaVersionErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.error_details
    import capo_glue.types.version_long_number


class SchemaVersionErrorItem(TypedDict, closed=True):
    version_number: NotRequired["capo_glue.types.version_long_number.VersionLongNumber"]
    """<p>The version number of the schema.</p>"""
    error_details: NotRequired["capo_glue.types.error_details.ErrorDetails"]
    """<p>The details of the error for the schema version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaVersionErrorItem) -> dict:
    out: dict = {}
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "error_details" in value:
        import capo_glue.types.error_details

        out["ErrorDetails"] = capo_glue.types.error_details.serialize_aws_json_1_1(
            value["error_details"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaVersionErrorItem:
    out: SchemaVersionErrorItem = {}  # type: ignore[typeddict-item]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "ErrorDetails" in data:
        import capo_glue.types.error_details

        out["error_details"] = capo_glue.types.error_details.deserialize_aws_json_1_1(
            data["ErrorDetails"]
        )
    return out
