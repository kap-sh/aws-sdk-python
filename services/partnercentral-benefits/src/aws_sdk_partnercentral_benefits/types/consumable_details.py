"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ConsumableDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.issuance_detail
    import aws_sdk_partnercentral_benefits.types.monetary_value


class ConsumableDetails(TypedDict):
    allocated_amount: NotRequired[
        "aws_sdk_partnercentral_benefits.types.monetary_value.MonetaryValue"
    ]
    """<p>The total amount of the consumable benefit that has been allocated.</p>"""
    remaining_amount: NotRequired[
        "aws_sdk_partnercentral_benefits.types.monetary_value.MonetaryValue"
    ]
    """<p>The remaining amount of the consumable benefit that is still available for use.</p>"""
    utilized_amount: NotRequired[
        "aws_sdk_partnercentral_benefits.types.monetary_value.MonetaryValue"
    ]
    """<p>The amount of the consumable benefit that has already been used.</p>"""
    issuance_details: NotRequired[
        "aws_sdk_partnercentral_benefits.types.issuance_detail.IssuanceDetail"
    ]
    """<p>Detailed information about how the consumable benefit was issued and distributed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConsumableDetails) -> dict:
    out: dict = {}
    if "allocated_amount" in value:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["AllocatedAmount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
                value["allocated_amount"]
            )
        )
    if "remaining_amount" in value:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["RemainingAmount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
                value["remaining_amount"]
            )
        )
    if "utilized_amount" in value:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["UtilizedAmount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
                value["utilized_amount"]
            )
        )
    if "issuance_details" in value:
        import aws_sdk_partnercentral_benefits.types.issuance_detail

        out["IssuanceDetails"] = (
            aws_sdk_partnercentral_benefits.types.issuance_detail.serialize_aws_json_1_0(
                value["issuance_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConsumableDetails:
    out: ConsumableDetails = {}  # type: ignore[typeddict-item]
    if "AllocatedAmount" in data:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["allocated_amount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["AllocatedAmount"]
            )
        )
    if "RemainingAmount" in data:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["remaining_amount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["RemainingAmount"]
            )
        )
    if "UtilizedAmount" in data:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["utilized_amount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["UtilizedAmount"]
            )
        )
    if "IssuanceDetails" in data:
        import aws_sdk_partnercentral_benefits.types.issuance_detail

        out["issuance_details"] = (
            aws_sdk_partnercentral_benefits.types.issuance_detail.deserialize_aws_json_1_0(
                data["IssuanceDetails"]
            )
        )
    return out
