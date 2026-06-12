"""Generated from Smithy shape ``com.amazonaws.securityhub#GroupByRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.group_by_field
    import aws_sdk_securityhub.types.ocsf_finding_filters


class GroupByRule(TypedDict):
    filters: NotRequired[
        "aws_sdk_securityhub.types.ocsf_finding_filters.OcsfFindingFilters"
    ]
    """<p>The criteria used to select which security findings should be included in the grouping operation.</p>"""
    group_by_field: NotRequired["aws_sdk_securityhub.types.group_by_field.GroupByField"]
    """<p>The attribute by which filtered findings should be grouped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupByRule) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_securityhub.types.ocsf_finding_filters

        out["Filters"] = aws_sdk_securityhub.types.ocsf_finding_filters.serialize_json(
            value["filters"]
        )
    if "group_by_field" in value:
        import aws_sdk_securityhub.types.group_by_field

        out["GroupByField"] = aws_sdk_securityhub.types.group_by_field.serialize_json(
            value["group_by_field"]
        )
    return out


def deserialize_json(data: dict) -> GroupByRule:
    out: GroupByRule = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_securityhub.types.ocsf_finding_filters

        out["filters"] = (
            aws_sdk_securityhub.types.ocsf_finding_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "GroupByField" in data:
        import aws_sdk_securityhub.types.group_by_field

        out["group_by_field"] = (
            aws_sdk_securityhub.types.group_by_field.deserialize_json(
                data["GroupByField"]
            )
        )
    return out
