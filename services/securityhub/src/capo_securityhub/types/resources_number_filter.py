"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesNumberFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.number_filter
    import capo_securityhub.types.resources_number_field


class ResourcesNumberFilter(TypedDict, closed=True):
    field_name: NotRequired[
        "capo_securityhub.types.resources_number_field.ResourcesNumberField"
    ]
    """<p>The name of the field.</p>"""
    filter: NotRequired["capo_securityhub.types.number_filter.NumberFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesNumberFilter) -> dict:
    out: dict = {}
    if "field_name" in value:
        import capo_securityhub.types.resources_number_field

        out["FieldName"] = capo_securityhub.types.resources_number_field.serialize_json(
            value["field_name"]
        )
    if "filter" in value:
        import capo_securityhub.types.number_filter

        out["Filter"] = capo_securityhub.types.number_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ResourcesNumberFilter:
    out: ResourcesNumberFilter = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import capo_securityhub.types.resources_number_field

        out["field_name"] = (
            capo_securityhub.types.resources_number_field.deserialize_json(
                data["FieldName"]
            )
        )
    if "Filter" in data:
        import capo_securityhub.types.number_filter

        out["filter"] = capo_securityhub.types.number_filter.deserialize_json(
            data["Filter"]
        )
    return out
