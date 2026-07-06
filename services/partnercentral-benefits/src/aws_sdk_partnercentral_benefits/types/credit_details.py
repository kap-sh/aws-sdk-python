"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#CreditDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.credit_codes
    import aws_sdk_partnercentral_benefits.types.monetary_value


class CreditDetails(TypedDict, closed=True):
    allocated_amount: (
        "aws_sdk_partnercentral_benefits.types.monetary_value.MonetaryValue"
    )
    """<p>The total amount of credits that have been allocated for this benefit.</p>"""
    issued_amount: "aws_sdk_partnercentral_benefits.types.monetary_value.MonetaryValue"
    """<p>The amount of credits that have actually been issued and are available for use.</p>"""
    codes: "aws_sdk_partnercentral_benefits.types.credit_codes.CreditCodes"
    """<p>A list of credit codes that have been generated for this benefit allocation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditDetails) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_benefits.types.monetary_value

    out["AllocatedAmount"] = (
        aws_sdk_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
            value["allocated_amount"]
        )
    )
    import aws_sdk_partnercentral_benefits.types.monetary_value

    out["IssuedAmount"] = (
        aws_sdk_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
            value["issued_amount"]
        )
    )
    import aws_sdk_partnercentral_benefits.types.credit_codes

    out["Codes"] = (
        aws_sdk_partnercentral_benefits.types.credit_codes.serialize_aws_json_1_0(
            value["codes"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreditDetails:
    out: CreditDetails = {}  # type: ignore[typeddict-item]
    if "AllocatedAmount" in data:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["allocated_amount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["AllocatedAmount"]
            )
        )
    else:
        raise DeserializationError("CreditDetails.allocated_amount required")
    if "IssuedAmount" in data:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["issued_amount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["IssuedAmount"]
            )
        )
    else:
        raise DeserializationError("CreditDetails.issued_amount required")
    if "Codes" in data:
        import aws_sdk_partnercentral_benefits.types.credit_codes

        out["codes"] = (
            aws_sdk_partnercentral_benefits.types.credit_codes.deserialize_aws_json_1_0(
                data["Codes"]
            )
        )
    else:
        raise DeserializationError("CreditDetails.codes required")
    return out
