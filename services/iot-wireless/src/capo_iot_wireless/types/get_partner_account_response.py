"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetPartnerAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.account_linked
    import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint


class GetPartnerAccountResponse(TypedDict, closed=True):
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.SidewalkAccountInfoWithFingerprint"
    ]
    """<p>The Sidewalk account credentials.</p>"""
    account_linked: "capo_iot_wireless.types.account_linked.AccountLinked"
    """<p>Whether the partner account is linked to the AWS account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPartnerAccountResponse) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.serialize_json(
                value["sidewalk"]
            )
        )
    out["AccountLinked"] = value.get("account_linked", False)
    return out


def deserialize_json(data: dict) -> GetPartnerAccountResponse:
    out: GetPartnerAccountResponse = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.deserialize_json(
                data["Sidewalk"]
            )
        )
    if "AccountLinked" in data:
        out["account_linked"] = data["AccountLinked"]
    else:
        out["account_linked"] = False
    return out
