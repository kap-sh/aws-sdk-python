"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdatePartnerAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.partner_account_id
    import aws_sdk_iot_wireless.types.partner_type
    import aws_sdk_iot_wireless.types.sidewalk_update_account


class UpdatePartnerAccountRequest(TypedDict):
    sidewalk: "aws_sdk_iot_wireless.types.sidewalk_update_account.SidewalkUpdateAccount"
    """<p>The Sidewalk account credentials.</p>"""
    partner_account_id: "aws_sdk_iot_wireless.types.partner_account_id.PartnerAccountId"
    """<p>The ID of the partner account to update.</p>"""
    partner_type: "aws_sdk_iot_wireless.types.partner_type.PartnerType"
    """<p>The partner type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePartnerAccountRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.sidewalk_update_account

    out["Sidewalk"] = aws_sdk_iot_wireless.types.sidewalk_update_account.serialize_json(
        value["sidewalk"]
    )
    return out


def deserialize_json(data: dict) -> UpdatePartnerAccountRequest:
    out: UpdatePartnerAccountRequest = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_update_account

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_update_account.deserialize_json(
                data["Sidewalk"]
            )
        )
    else:
        raise DeserializationError("UpdatePartnerAccountRequest.sidewalk required")
    return out
