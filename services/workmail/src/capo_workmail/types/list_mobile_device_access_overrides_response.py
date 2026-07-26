"""Generated from Smithy shape ``com.amazonaws.workmail#ListMobileDeviceAccessOverridesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.mobile_device_access_overrides_list
    import capo_workmail.types.next_token


class ListMobileDeviceAccessOverridesResponse(TypedDict, closed=True):
    overrides: NotRequired[
        "capo_workmail.types.mobile_device_access_overrides_list.MobileDeviceAccessOverridesList"
    ]
    """<p>The list of mobile device access overrides that exist for the specified WorkMail organization and user.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The value is “null” when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMobileDeviceAccessOverridesResponse) -> dict:
    out: dict = {}
    if "overrides" in value:
        import capo_workmail.types.mobile_device_access_overrides_list

        out["Overrides"] = (
            capo_workmail.types.mobile_device_access_overrides_list.serialize_aws_json_1_1(
                value["overrides"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMobileDeviceAccessOverridesResponse:
    out: ListMobileDeviceAccessOverridesResponse = {}  # type: ignore[typeddict-item]
    if "Overrides" in data:
        import capo_workmail.types.mobile_device_access_overrides_list

        out["overrides"] = (
            capo_workmail.types.mobile_device_access_overrides_list.deserialize_aws_json_1_1(
                data["Overrides"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
