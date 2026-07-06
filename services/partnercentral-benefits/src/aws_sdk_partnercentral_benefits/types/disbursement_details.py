"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#DisbursementDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.issuance_detail
    import aws_sdk_partnercentral_benefits.types.monetary_value


class DisbursementDetails(TypedDict, closed=True):
    disbursed_amount: NotRequired[
        "aws_sdk_partnercentral_benefits.types.monetary_value.MonetaryValue"
    ]
    """<p>The total amount that has been disbursed for this benefit allocation.</p>"""
    issuance_details: NotRequired[
        "aws_sdk_partnercentral_benefits.types.issuance_detail.IssuanceDetail"
    ]
    """<p>Detailed information about how the disbursement was issued and processed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisbursementDetails) -> dict:
    out: dict = {}
    if "disbursed_amount" in value:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["DisbursedAmount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
                value["disbursed_amount"]
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


def deserialize_aws_json_1_0(data: dict) -> DisbursementDetails:
    out: DisbursementDetails = {}  # type: ignore[typeddict-item]
    if "DisbursedAmount" in data:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["disbursed_amount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["DisbursedAmount"]
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
