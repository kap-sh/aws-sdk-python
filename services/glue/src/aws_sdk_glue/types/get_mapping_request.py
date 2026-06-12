"""Generated from Smithy shape ``com.amazonaws.glue#GetMappingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_entries
    import aws_sdk_glue.types.catalog_entry
    import aws_sdk_glue.types.location


class GetMappingRequest(TypedDict):
    source: "aws_sdk_glue.types.catalog_entry.CatalogEntry"
    """<p>Specifies the source table.</p>"""
    sinks: NotRequired["aws_sdk_glue.types.catalog_entries.CatalogEntries"]
    """<p>A list of target tables.</p>"""
    location: NotRequired["aws_sdk_glue.types.location.Location"]
    """<p>Parameters for the mapping.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMappingRequest) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.catalog_entry

    out["Source"] = aws_sdk_glue.types.catalog_entry.serialize_aws_json_1_1(
        value["source"]
    )
    if "sinks" in value:
        import aws_sdk_glue.types.catalog_entries

        out["Sinks"] = aws_sdk_glue.types.catalog_entries.serialize_aws_json_1_1(
            value["sinks"]
        )
    if "location" in value:
        import aws_sdk_glue.types.location

        out["Location"] = aws_sdk_glue.types.location.serialize_aws_json_1_1(
            value["location"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMappingRequest:
    out: GetMappingRequest = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import aws_sdk_glue.types.catalog_entry

        out["source"] = aws_sdk_glue.types.catalog_entry.deserialize_aws_json_1_1(
            data["Source"]
        )
    else:
        raise DeserializationError("GetMappingRequest.source required")
    if "Sinks" in data:
        import aws_sdk_glue.types.catalog_entries

        out["sinks"] = aws_sdk_glue.types.catalog_entries.deserialize_aws_json_1_1(
            data["Sinks"]
        )
    if "Location" in data:
        import aws_sdk_glue.types.location

        out["location"] = aws_sdk_glue.types.location.deserialize_aws_json_1_1(
            data["Location"]
        )
    return out
