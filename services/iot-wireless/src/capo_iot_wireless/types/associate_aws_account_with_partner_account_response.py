"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateAwsAccountWithPartnerAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.partner_account_arn
    import capo_iot_wireless.types.sidewalk_account_info


class AssociateAwsAccountWithPartnerAccountResponse(TypedDict, closed=True):
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_account_info.SidewalkAccountInfo"
    ]
    """<p>The Sidewalk account credentials.</p>"""
    arn: NotRequired["capo_iot_wireless.types.partner_account_arn.PartnerAccountArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAwsAccountWithPartnerAccountResponse) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_account_info

        out["Sidewalk"] = capo_iot_wireless.types.sidewalk_account_info.serialize_json(
            value["sidewalk"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AssociateAwsAccountWithPartnerAccountResponse:
    out: AssociateAwsAccountWithPartnerAccountResponse = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import capo_iot_wireless.types.sidewalk_account_info

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_account_info.deserialize_json(
                data["Sidewalk"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
