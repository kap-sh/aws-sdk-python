"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesMapFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.map_filter
    import capo_securityhub.types.resources_map_field


class ResourcesMapFilter(TypedDict, closed=True):
    field_name: NotRequired[
        "capo_securityhub.types.resources_map_field.ResourcesMapField"
    ]
    """<p>The name of the field.</p>"""
    filter: NotRequired["capo_securityhub.types.map_filter.MapFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesMapFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import capo_securityhub.types.resources_map_field

        out["FieldName"] = capo_securityhub.types.resources_map_field.serialize_json(
            value["field_name"]
        )
    if "filter" in value:
        import capo_securityhub.types.map_filter

        out["Filter"] = capo_securityhub.types.map_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesMapFilter:
    out: ResourcesMapFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import capo_securityhub.types.resources_map_field

        out["field_name"] = capo_securityhub.types.resources_map_field.deserialize_json(
            data["FieldName"]
        )
    if "Filter" in data:
        import capo_securityhub.types.map_filter

        out["filter"] = capo_securityhub.types.map_filter.deserialize_json(
            data["Filter"]
        )
    return out
