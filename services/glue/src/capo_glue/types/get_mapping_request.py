"""Generated from Smithy shape ``com.amazonaws.glue#GetMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_entries
    import capo_glue.types.catalog_entry
    import capo_glue.types.location


class GetMappingRequest(TypedDict, closed=True):
    source: "capo_glue.types.catalog_entry.CatalogEntry"
    """<p>Specifies the source table.</p>"""
    sinks: NotRequired["capo_glue.types.catalog_entries.CatalogEntries"]
    """<p>A list of target tables.</p>"""
    location: NotRequired["capo_glue.types.location.Location"]
    """<p>Parameters for the mapping.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMappingRequest) -> dict:
    out: dict = {}
    import capo_glue.types.catalog_entry

    out["Source"] = capo_glue.types.catalog_entry.serialize_aws_json_1_1(
        value["source"]
    )
    if "sinks" in value:
        import capo_glue.types.catalog_entries

        out["Sinks"] = capo_glue.types.catalog_entries.serialize_aws_json_1_1(
            value["sinks"]
        )
    if "location" in value:
        import capo_glue.types.location

        out["Location"] = capo_glue.types.location.serialize_aws_json_1_1(
            value["location"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMappingRequest:
    out: GetMappingRequest = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import capo_glue.types.catalog_entry

        out["source"] = capo_glue.types.catalog_entry.deserialize_aws_json_1_1(
            data["Source"]
        )
    else:
        raise DeserializationError("GetMappingRequest.source required")
    if "Sinks" in data:
        import capo_glue.types.catalog_entries

        out["sinks"] = capo_glue.types.catalog_entries.deserialize_aws_json_1_1(
            data["Sinks"]
        )
    if "Location" in data:
        import capo_glue.types.location

        out["location"] = capo_glue.types.location.deserialize_aws_json_1_1(
            data["Location"]
        )
    return out
