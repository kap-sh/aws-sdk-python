"""Generated from Smithy shape ``com.amazonaws.glue#SchemaVersionNumber``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.latest_schema_version_boolean
    import capo_glue.types.version_long_number


class SchemaVersionNumber(TypedDict, closed=True):
    latest_version: (
        "capo_glue.types.latest_schema_version_boolean.LatestSchemaVersionBoolean"
    )
    """<p>The latest version available for the schema.</p>"""
    version_number: NotRequired["capo_glue.types.version_long_number.VersionLongNumber"]
    """<p>The version number of the schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaVersionNumber) -> dict:
    out: dict = {}
    out["LatestVersion"] = value.get("latest_version", False)
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaVersionNumber:
    out: SchemaVersionNumber = {}  # type: ignore[typeddict-item]
    if "LatestVersion" in data:
        out["latest_version"] = data["LatestVersion"]
    else:
        out["latest_version"] = False
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    return out
