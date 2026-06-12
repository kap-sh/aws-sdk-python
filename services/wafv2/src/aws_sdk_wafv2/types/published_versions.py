"""Generated from Smithy shape ``com.amazonaws.wafv2#PublishedVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.managed_rule_set_version
    import aws_sdk_wafv2.types.version_key_string

PublishedVersions: TypeAlias = dict[
    "aws_sdk_wafv2.types.version_key_string.VersionKeyString",
    "aws_sdk_wafv2.types.managed_rule_set_version.ManagedRuleSetVersion",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PublishedVersions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_wafv2.types.managed_rule_set_version

        out[key] = aws_sdk_wafv2.types.managed_rule_set_version.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PublishedVersions:
    out: PublishedVersions = {}
    for key, value in data.items():
        import aws_sdk_wafv2.types.managed_rule_set_version

        out[key] = (
            aws_sdk_wafv2.types.managed_rule_set_version.deserialize_aws_json_1_1(value)
        )
    return out
