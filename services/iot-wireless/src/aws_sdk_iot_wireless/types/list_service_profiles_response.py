"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListServiceProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.next_token
    import aws_sdk_iot_wireless.types.service_profile_list


class ListServiceProfilesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""
    service_profile_list: NotRequired[
        "aws_sdk_iot_wireless.types.service_profile_list.ServiceProfileList"
    ]
    """<p>The list of service profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceProfilesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "service_profile_list" in value:
        import aws_sdk_iot_wireless.types.service_profile_list

        out["ServiceProfileList"] = (
            aws_sdk_iot_wireless.types.service_profile_list.serialize_json(
                value["service_profile_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListServiceProfilesResponse:
    out: ListServiceProfilesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ServiceProfileList" in data:
        import aws_sdk_iot_wireless.types.service_profile_list

        out["service_profile_list"] = (
            aws_sdk_iot_wireless.types.service_profile_list.deserialize_json(
                data["ServiceProfileList"]
            )
        )
    return out
