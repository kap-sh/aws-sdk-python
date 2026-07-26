"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceGroupByRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.resource_group_by_field
    import capo_securityhub.types.resources_filters


class ResourceGroupByRule(TypedDict, closed=True):
    group_by_field: NotRequired[
        "capo_securityhub.types.resource_group_by_field.ResourceGroupByField"
    ]
    """<p>Specifies the attribute that resources should be grouped by.</p>"""
    filters: NotRequired["capo_securityhub.types.resources_filters.ResourcesFilters"]
    """<p>The criteria used to select resources and associated security findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceGroupByRule) -> dict:
    out: dict = {}
    if "group_by_field" in value:
        import capo_securityhub.types.resource_group_by_field

        out["GroupByField"] = (
            capo_securityhub.types.resource_group_by_field.serialize_json(
                value["group_by_field"]
            )
        )
    if "filters" in value:
        import capo_securityhub.types.resources_filters

        out["Filters"] = capo_securityhub.types.resources_filters.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ResourceGroupByRule:
    out: ResourceGroupByRule = {}  # type: ignore[typeddict-item]
    if "GroupByField" in data:
        import capo_securityhub.types.resource_group_by_field

        out["group_by_field"] = (
            capo_securityhub.types.resource_group_by_field.deserialize_json(
                data["GroupByField"]
            )
        )
    if "Filters" in data:
        import capo_securityhub.types.resources_filters

        out["filters"] = capo_securityhub.types.resources_filters.deserialize_json(
            data["Filters"]
        )
    return out
