"""Generated from Smithy shape ``com.amazonaws.shield#InclusionProtectionGroupFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_shield.types.protected_resource_type_filters
    import aws_sdk_shield.types.protection_group_aggregation_filters
    import aws_sdk_shield.types.protection_group_id_filters
    import aws_sdk_shield.types.protection_group_pattern_filters


class InclusionProtectionGroupFilters(TypedDict, closed=True):
    protection_group_ids: NotRequired[
        "aws_sdk_shield.types.protection_group_id_filters.ProtectionGroupIdFilters"
    ]
    """<p>The ID of the protection group that you want to retrieve. </p>"""
    patterns: NotRequired[
        "aws_sdk_shield.types.protection_group_pattern_filters.ProtectionGroupPatternFilters"
    ]
    """<p>The pattern specification of the protection groups that you want to retrieve. </p>"""
    resource_types: NotRequired[
        "aws_sdk_shield.types.protected_resource_type_filters.ProtectedResourceTypeFilters"
    ]
    """<p>The resource type configuration of the protection groups that you want to retrieve. In the protection group configuration, you specify the resource type when you set the group's <code>Pattern</code> to <code>BY_RESOURCE_TYPE</code>. </p>"""
    aggregations: NotRequired[
        "aws_sdk_shield.types.protection_group_aggregation_filters.ProtectionGroupAggregationFilters"
    ]
    """<p>The aggregation setting of the protection groups that you want to retrieve. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InclusionProtectionGroupFilters) -> dict:
    out: dict = {}
    if "protection_group_ids" in value:
        import aws_sdk_shield.types.protection_group_id_filters

        out["ProtectionGroupIds"] = (
            aws_sdk_shield.types.protection_group_id_filters.serialize_aws_json_1_1(
                value["protection_group_ids"]
            )
        )
    if "patterns" in value:
        import aws_sdk_shield.types.protection_group_pattern_filters

        out["Patterns"] = (
            aws_sdk_shield.types.protection_group_pattern_filters.serialize_aws_json_1_1(
                value["patterns"]
            )
        )
    if "resource_types" in value:
        import aws_sdk_shield.types.protected_resource_type_filters

        out["ResourceTypes"] = (
            aws_sdk_shield.types.protected_resource_type_filters.serialize_aws_json_1_1(
                value["resource_types"]
            )
        )
    if "aggregations" in value:
        import aws_sdk_shield.types.protection_group_aggregation_filters

        out["Aggregations"] = (
            aws_sdk_shield.types.protection_group_aggregation_filters.serialize_aws_json_1_1(
                value["aggregations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InclusionProtectionGroupFilters:
    out: InclusionProtectionGroupFilters = {}  # type: ignore[typeddict-item]
    if "ProtectionGroupIds" in data:
        import aws_sdk_shield.types.protection_group_id_filters

        out["protection_group_ids"] = (
            aws_sdk_shield.types.protection_group_id_filters.deserialize_aws_json_1_1(
                data["ProtectionGroupIds"]
            )
        )
    if "Patterns" in data:
        import aws_sdk_shield.types.protection_group_pattern_filters

        out["patterns"] = (
            aws_sdk_shield.types.protection_group_pattern_filters.deserialize_aws_json_1_1(
                data["Patterns"]
            )
        )
    if "ResourceTypes" in data:
        import aws_sdk_shield.types.protected_resource_type_filters

        out["resource_types"] = (
            aws_sdk_shield.types.protected_resource_type_filters.deserialize_aws_json_1_1(
                data["ResourceTypes"]
            )
        )
    if "Aggregations" in data:
        import aws_sdk_shield.types.protection_group_aggregation_filters

        out["aggregations"] = (
            aws_sdk_shield.types.protection_group_aggregation_filters.deserialize_aws_json_1_1(
                data["Aggregations"]
            )
        )
    return out
