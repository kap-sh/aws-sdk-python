"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetPartnerAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.partner_account_id
    import aws_sdk_iot_wireless.types.partner_type


class GetPartnerAccountRequest(TypedDict, closed=True):
    partner_account_id: "aws_sdk_iot_wireless.types.partner_account_id.PartnerAccountId"
    """<p>The partner account ID to disassociate from the AWS account.</p>"""
    partner_type: "aws_sdk_iot_wireless.types.partner_type.PartnerType"
    """<p>The partner type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPartnerAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPartnerAccountRequest:
    out: GetPartnerAccountRequest = {}  # type: ignore[typeddict-item]
    return out
