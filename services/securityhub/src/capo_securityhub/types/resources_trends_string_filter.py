"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.resources_trends_string_field
    import capo_securityhub.types.string_filter


class ResourcesTrendsStringFilter(TypedDict, closed=True):
    field_name: NotRequired[
        "capo_securityhub.types.resources_trends_string_field.ResourcesTrendsStringField"
    ]
    """<p>The name of the resources field to filter on, such as resourceType, accountId, or region.</p>"""
    filter: NotRequired["capo_securityhub.types.string_filter.StringFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsStringFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import capo_securityhub.types.resources_trends_string_field

        out["FieldName"] = (
            capo_securityhub.types.resources_trends_string_field.serialize_json(
                value["field_name"]
            )
        )
    if "filter" in value:
        import capo_securityhub.types.string_filter

        out["Filter"] = capo_securityhub.types.string_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesTrendsStringFilter:
    out: ResourcesTrendsStringFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import capo_securityhub.types.resources_trends_string_field

        out["field_name"] = (
            capo_securityhub.types.resources_trends_string_field.deserialize_json(
                data["FieldName"]
            )
        )
    if "Filter" in data:
        import capo_securityhub.types.string_filter

        out["filter"] = capo_securityhub.types.string_filter.deserialize_json(
            data["Filter"]
        )
    return out
