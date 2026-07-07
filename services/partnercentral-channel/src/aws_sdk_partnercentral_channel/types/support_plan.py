"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#SupportPlan``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_partnercentral_channel.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.partner_led_support
    import aws_sdk_partnercentral_channel.types.resold_enterprise
    import aws_sdk_partnercentral_channel.types.resold_unified_operations


class _SupportPlan_resoldEnterprise(TypedDict, closed=True):
    resoldEnterprise: (
        "aws_sdk_partnercentral_channel.types.resold_enterprise.ResoldEnterprise"
    )


class _SupportPlan_partnerLedSupport(TypedDict, closed=True):
    partnerLedSupport: (
        "aws_sdk_partnercentral_channel.types.partner_led_support.PartnerLedSupport"
    )


class _SupportPlan_resoldUnifiedOperations(TypedDict, closed=True):
    resoldUnifiedOperations: "aws_sdk_partnercentral_channel.types.resold_unified_operations.ResoldUnifiedOperations"


SupportPlan: TypeAlias = (
    _SupportPlan_resoldEnterprise
    | _SupportPlan_partnerLedSupport
    | _SupportPlan_resoldUnifiedOperations
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportPlan) -> dict:
    if "resoldEnterprise" in value:
        import aws_sdk_partnercentral_channel.types.resold_enterprise

        return {
            "resoldEnterprise": aws_sdk_partnercentral_channel.types.resold_enterprise.serialize_aws_json_1_0(
                value["resoldEnterprise"]
            )
        }
    elif "partnerLedSupport" in value:
        import aws_sdk_partnercentral_channel.types.partner_led_support

        return {
            "partnerLedSupport": aws_sdk_partnercentral_channel.types.partner_led_support.serialize_aws_json_1_0(
                value["partnerLedSupport"]
            )
        }
    elif "resoldUnifiedOperations" in value:
        import aws_sdk_partnercentral_channel.types.resold_unified_operations

        return {
            "resoldUnifiedOperations": aws_sdk_partnercentral_channel.types.resold_unified_operations.serialize_aws_json_1_0(
                value["resoldUnifiedOperations"]
            )
        }
    else:
        raise SerializationError("SupportPlan: no variant present")


def deserialize_aws_json_1_0(data: dict) -> SupportPlan:
    if "resoldEnterprise" in data:
        import aws_sdk_partnercentral_channel.types.resold_enterprise

        return {
            "resoldEnterprise": aws_sdk_partnercentral_channel.types.resold_enterprise.deserialize_aws_json_1_0(
                data["resoldEnterprise"]
            )
        }
    elif "partnerLedSupport" in data:
        import aws_sdk_partnercentral_channel.types.partner_led_support

        return {
            "partnerLedSupport": aws_sdk_partnercentral_channel.types.partner_led_support.deserialize_aws_json_1_0(
                data["partnerLedSupport"]
            )
        }
    elif "resoldUnifiedOperations" in data:
        import aws_sdk_partnercentral_channel.types.resold_unified_operations

        return {
            "resoldUnifiedOperations": aws_sdk_partnercentral_channel.types.resold_unified_operations.deserialize_aws_json_1_0(
                data["resoldUnifiedOperations"]
            )
        }
    else:
        raise DeserializationError("SupportPlan: no recognized variant key")
