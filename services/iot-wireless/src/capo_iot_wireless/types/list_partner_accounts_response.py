"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListPartnerAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.next_token
    import capo_iot_wireless.types.sidewalk_account_list


class ListPartnerAccountsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_account_list.SidewalkAccountList"
    ]
    """<p>The Sidewalk account credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPartnerAccountsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_account_list

        out["Sidewalk"] = capo_iot_wireless.types.sidewalk_account_list.serialize_json(
            value["sidewalk"]
        )
    return out


def deserialize_json(data: dict) -> ListPartnerAccountsResponse:
    out: ListPartnerAccountsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Sidewalk" in data:
        import capo_iot_wireless.types.sidewalk_account_list

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_account_list.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
