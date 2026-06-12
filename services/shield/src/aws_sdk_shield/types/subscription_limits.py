"""Generated from Smithy shape ``com.amazonaws.shield#SubscriptionLimits``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.protection_group_limits
    import aws_sdk_shield.types.protection_limits


class SubscriptionLimits(TypedDict):
    protection_limits: "aws_sdk_shield.types.protection_limits.ProtectionLimits"
    """<p>Limits settings on protections for your subscription. </p>"""
    protection_group_limits: (
        "aws_sdk_shield.types.protection_group_limits.ProtectionGroupLimits"
    )
    """<p>Limits settings on protection groups for your subscription. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriptionLimits) -> dict:
    out: dict = {}
    import aws_sdk_shield.types.protection_limits

    out["ProtectionLimits"] = (
        aws_sdk_shield.types.protection_limits.serialize_aws_json_1_1(
            value["protection_limits"]
        )
    )
    import aws_sdk_shield.types.protection_group_limits

    out["ProtectionGroupLimits"] = (
        aws_sdk_shield.types.protection_group_limits.serialize_aws_json_1_1(
            value["protection_group_limits"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscriptionLimits:
    out: SubscriptionLimits = {}  # type: ignore[typeddict-item]
    if "ProtectionLimits" in data:
        import aws_sdk_shield.types.protection_limits

        out["protection_limits"] = (
            aws_sdk_shield.types.protection_limits.deserialize_aws_json_1_1(
                data["ProtectionLimits"]
            )
        )
    else:
        raise DeserializationError("SubscriptionLimits.protection_limits required")
    if "ProtectionGroupLimits" in data:
        import aws_sdk_shield.types.protection_group_limits

        out["protection_group_limits"] = (
            aws_sdk_shield.types.protection_group_limits.deserialize_aws_json_1_1(
                data["ProtectionGroupLimits"]
            )
        )
    else:
        raise DeserializationError(
            "SubscriptionLimits.protection_group_limits required"
        )
    return out
