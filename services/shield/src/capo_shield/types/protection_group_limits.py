"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_shield.errors import DeserializationError

if TYPE_CHECKING:
    import capo_shield.types.long
    import capo_shield.types.protection_group_pattern_type_limits


class ProtectionGroupLimits(TypedDict, closed=True):
    max_protection_groups: "capo_shield.types.long.Long"
    """<p>The maximum number of protection groups that you can have at one time. </p>"""
    pattern_type_limits: "capo_shield.types.protection_group_pattern_type_limits.ProtectionGroupPatternTypeLimits"
    """<p>Limits settings by pattern type in the protection groups for your subscription. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupLimits) -> dict:
    out: dict = {}
    out["MaxProtectionGroups"] = value.get("max_protection_groups", 0)
    import capo_shield.types.protection_group_pattern_type_limits

    out["PatternTypeLimits"] = (
        capo_shield.types.protection_group_pattern_type_limits.serialize_aws_json_1_1(
            value["pattern_type_limits"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectionGroupLimits:
    out: ProtectionGroupLimits = {}  # type: ignore[typeddict-item]
    if "MaxProtectionGroups" in data:
        out["max_protection_groups"] = data["MaxProtectionGroups"]
    else:
        out["max_protection_groups"] = 0
    if "PatternTypeLimits" in data:
        import capo_shield.types.protection_group_pattern_type_limits

        out["pattern_type_limits"] = (
            capo_shield.types.protection_group_pattern_type_limits.deserialize_aws_json_1_1(
                data["PatternTypeLimits"]
            )
        )
    else:
        raise DeserializationError("ProtectionGroupLimits.pattern_type_limits required")
    return out
