"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleGroupVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.managed_rule_group_version

ManagedRuleGroupVersions: TypeAlias = list[
    "aws_sdk_wafv2.types.managed_rule_group_version.ManagedRuleGroupVersion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleGroupVersions) -> list:
    import aws_sdk_wafv2.types.managed_rule_group_version

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wafv2.types.managed_rule_group_version.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedRuleGroupVersions:
    import aws_sdk_wafv2.types.managed_rule_group_version

    out: ManagedRuleGroupVersions = []
    for item in data:
        out.append(
            aws_sdk_wafv2.types.managed_rule_group_version.deserialize_aws_json_1_1(
                item
            )
        )
    return out
