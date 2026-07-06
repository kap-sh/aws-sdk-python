"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleGroupVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.timestamp
    import aws_sdk_wafv2.types.version_key_string


class ManagedRuleGroupVersion(TypedDict, closed=True):
    name: NotRequired["aws_sdk_wafv2.types.version_key_string.VersionKeyString"]
    """<p>The version name. </p>"""
    last_update_timestamp: NotRequired["aws_sdk_wafv2.types.timestamp.Timestamp"]
    """<p>The date and time that the managed rule group owner updated the rule group version information. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleGroupVersion) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "last_update_timestamp" in value:
        import aws_sdk_wafv2.types.timestamp

        out["LastUpdateTimestamp"] = (
            aws_sdk_wafv2.types.timestamp.serialize_aws_json_1_1(
                value["last_update_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedRuleGroupVersion:
    out: ManagedRuleGroupVersion = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LastUpdateTimestamp" in data:
        import aws_sdk_wafv2.types.timestamp

        out["last_update_timestamp"] = (
            aws_sdk_wafv2.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdateTimestamp"]
            )
        )
    return out
