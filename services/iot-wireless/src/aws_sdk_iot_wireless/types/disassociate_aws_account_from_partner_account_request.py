"""Generated from Smithy shape ``com.amazonaws.iotwireless#DisassociateAwsAccountFromPartnerAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.partner_account_id
    import aws_sdk_iot_wireless.types.partner_type


class DisassociateAwsAccountFromPartnerAccountRequest(TypedDict):
    partner_account_id: "aws_sdk_iot_wireless.types.partner_account_id.PartnerAccountId"
    """<p>The partner account ID to disassociate from the AWS account.</p>"""
    partner_type: "aws_sdk_iot_wireless.types.partner_type.PartnerType"
    """<p>The partner type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAwsAccountFromPartnerAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateAwsAccountFromPartnerAccountRequest:
    out: DisassociateAwsAccountFromPartnerAccountRequest = {}  # type: ignore[typeddict-item]
    return out
