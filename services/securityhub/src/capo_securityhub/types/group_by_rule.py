"""Generated from Smithy shape ``com.amazonaws.securityhub#GroupByRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.group_by_field
    import capo_securityhub.types.ocsf_finding_filters


class GroupByRule(TypedDict, closed=True):
    filters: NotRequired[
        "capo_securityhub.types.ocsf_finding_filters.OcsfFindingFilters"
    ]
    """<p>The criteria used to select which security findings should be included in the grouping operation.</p>"""
    group_by_field: NotRequired["capo_securityhub.types.group_by_field.GroupByField"]
    """<p>The attribute by which filtered findings should be grouped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupByRule) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_securityhub.types.ocsf_finding_filters

        out["Filters"] = capo_securityhub.types.ocsf_finding_filters.serialize_json(
            value["filters"]
        )
    if "group_by_field" in value:
        import capo_securityhub.types.group_by_field

        out["GroupByField"] = capo_securityhub.types.group_by_field.serialize_json(
            value["group_by_field"]
        )
    return out


def deserialize_json(data: dict) -> GroupByRule:
    out: GroupByRule = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_securityhub.types.ocsf_finding_filters

        out["filters"] = capo_securityhub.types.ocsf_finding_filters.deserialize_json(
            data["Filters"]
        )
    if "GroupByField" in data:
        import capo_securityhub.types.group_by_field

        out["group_by_field"] = capo_securityhub.types.group_by_field.deserialize_json(
            data["GroupByField"]
        )
    return out
