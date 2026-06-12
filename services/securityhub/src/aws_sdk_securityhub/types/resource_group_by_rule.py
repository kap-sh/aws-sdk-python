"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceGroupByRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resource_group_by_field
    import aws_sdk_securityhub.types.resources_filters


class ResourceGroupByRule(TypedDict):
    group_by_field: NotRequired[
        "aws_sdk_securityhub.types.resource_group_by_field.ResourceGroupByField"
    ]
    """<p>Specifies the attribute that resources should be grouped by.</p>"""
    filters: NotRequired["aws_sdk_securityhub.types.resources_filters.ResourcesFilters"]
    """<p>The criteria used to select resources and associated security findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceGroupByRule) -> dict:
    out: dict = {}
    if "group_by_field" in value:
        import aws_sdk_securityhub.types.resource_group_by_field

        out["GroupByField"] = (
            aws_sdk_securityhub.types.resource_group_by_field.serialize_json(
                value["group_by_field"]
            )
        )
    if "filters" in value:
        import aws_sdk_securityhub.types.resources_filters

        out["Filters"] = aws_sdk_securityhub.types.resources_filters.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ResourceGroupByRule:
    out: ResourceGroupByRule = {}  # type: ignore[typeddict-item]
    if "GroupByField" in data:
        import aws_sdk_securityhub.types.resource_group_by_field

        out["group_by_field"] = (
            aws_sdk_securityhub.types.resource_group_by_field.deserialize_json(
                data["GroupByField"]
            )
        )
    if "Filters" in data:
        import aws_sdk_securityhub.types.resources_filters

        out["filters"] = aws_sdk_securityhub.types.resources_filters.deserialize_json(
            data["Filters"]
        )
    return out
