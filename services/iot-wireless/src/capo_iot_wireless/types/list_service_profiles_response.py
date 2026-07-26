"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListServiceProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.next_token
    import capo_iot_wireless.types.service_profile_list


class ListServiceProfilesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""
    service_profile_list: NotRequired[
        "capo_iot_wireless.types.service_profile_list.ServiceProfileList"
    ]
    """<p>The list of service profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceProfilesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "service_profile_list" in value:
        import capo_iot_wireless.types.service_profile_list

        out["ServiceProfileList"] = (
            capo_iot_wireless.types.service_profile_list.serialize_json(
                value["service_profile_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListServiceProfilesResponse:
    out: ListServiceProfilesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServiceProfileList" in data:
        import capo_iot_wireless.types.service_profile_list

        out["service_profile_list"] = (
            capo_iot_wireless.types.service_profile_list.deserialize_json(
                data["ServiceProfileList"]
            )
        )
    return out
