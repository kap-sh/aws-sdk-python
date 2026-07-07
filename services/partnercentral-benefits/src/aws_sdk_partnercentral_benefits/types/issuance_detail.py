"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#IssuanceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.monetary_value
    import aws_sdk_partnercentral_benefits.types.timestamp


class IssuanceDetail(TypedDict, closed=True):
    issuance_id: NotRequired["str"]
    """<p>The unique identifier for this specific issuance.</p>"""
    issuance_amount: NotRequired[
        "aws_sdk_partnercentral_benefits.types.monetary_value.MonetaryValue"
    ]
    """<p>The monetary amount or value that was issued in this specific issuance.</p>"""
    issued_at: NotRequired["aws_sdk_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when this specific issuance was processed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IssuanceDetail) -> dict:
    out: dict = {}
    if "issuance_id" in value:
        out["IssuanceId"] = value["issuance_id"]
    if "issuance_amount" in value:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["IssuanceAmount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
                value["issuance_amount"]
            )
        )
    if "issued_at" in value:
        import aws_sdk_partnercentral_benefits.types.timestamp

        out["IssuedAt"] = (
            aws_sdk_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["issued_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IssuanceDetail:
    out: IssuanceDetail = {}  # type: ignore[typeddict-item]
    if "IssuanceId" in data:
        out["issuance_id"] = data["IssuanceId"]
    if "IssuanceAmount" in data:
        import aws_sdk_partnercentral_benefits.types.monetary_value

        out["issuance_amount"] = (
            aws_sdk_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["IssuanceAmount"]
            )
        )
    if "IssuedAt" in data:
        import aws_sdk_partnercentral_benefits.types.timestamp

        out["issued_at"] = (
            aws_sdk_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["IssuedAt"]
            )
        )
    return out
