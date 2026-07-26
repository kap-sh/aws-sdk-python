"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#CreditCode``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.benefit_allocation_status
    import capo_partnercentral_benefits.types.monetary_value
    import capo_partnercentral_benefits.types.timestamp


class CreditCode(TypedDict, closed=True):
    aws_account_id: "str"
    """<p>The AWS account ID that the credit code is associated with or can be applied to.</p>"""
    value: "capo_partnercentral_benefits.types.monetary_value.MonetaryValue"
    """<p>The monetary value of the credit code.</p>"""
    aws_credit_code: "str"
    """<p>The actual credit code string that can be redeemed in the AWS billing console.</p>"""
    status: "capo_partnercentral_benefits.types.benefit_allocation_status.BenefitAllocationStatus"
    """<p>The current status of the credit code (e.g., active, redeemed, expired).</p>"""
    issued_at: "capo_partnercentral_benefits.types.timestamp.Timestamp"
    """<p>The timestamp when the credit code was issued.</p>"""
    expires_at: "capo_partnercentral_benefits.types.timestamp.Timestamp"
    """<p>The timestamp when the credit code expires and can no longer be redeemed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditCode) -> dict:
    out: dict = {}
    out["AwsAccountId"] = value["aws_account_id"]
    import capo_partnercentral_benefits.types.monetary_value

    out["Value"] = (
        capo_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
            value["value"]
        )
    )
    out["AwsCreditCode"] = value["aws_credit_code"]
    import capo_partnercentral_benefits.types.benefit_allocation_status

    out["Status"] = (
        capo_partnercentral_benefits.types.benefit_allocation_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_partnercentral_benefits.types.timestamp

    out["IssuedAt"] = (
        capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
            value["issued_at"]
        )
    )
    import capo_partnercentral_benefits.types.timestamp

    out["ExpiresAt"] = (
        capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
            value["expires_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreditCode:
    out: CreditCode = {}  # type: ignore[typeddict-item]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    else:
        raise DeserializationError("CreditCode.aws_account_id required")
    if "Value" in data:
        import capo_partnercentral_benefits.types.monetary_value

        out["value"] = (
            capo_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("CreditCode.value required")
    if "AwsCreditCode" in data:
        out["aws_credit_code"] = data["AwsCreditCode"]
    else:
        raise DeserializationError("CreditCode.aws_credit_code required")
    if "Status" in data:
        import capo_partnercentral_benefits.types.benefit_allocation_status

        out["status"] = (
            capo_partnercentral_benefits.types.benefit_allocation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CreditCode.status required")
    if "IssuedAt" in data:
        import capo_partnercentral_benefits.types.timestamp

        out["issued_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["IssuedAt"]
            )
        )
    else:
        raise DeserializationError("CreditCode.issued_at required")
    if "ExpiresAt" in data:
        import capo_partnercentral_benefits.types.timestamp

        out["expires_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["ExpiresAt"]
            )
        )
    else:
        raise DeserializationError("CreditCode.expires_at required")
    return out
