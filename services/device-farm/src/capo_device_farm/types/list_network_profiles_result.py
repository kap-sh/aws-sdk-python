"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListNetworkProfilesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.network_profiles
    import capo_device_farm.types.pagination_token


class ListNetworkProfilesResult(TypedDict, closed=True):
    network_profiles: NotRequired[
        "capo_device_farm.types.network_profiles.NetworkProfiles"
    ]
    """<p>A list of the available network profiles.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNetworkProfilesResult) -> dict:
    out: dict = {}
    if "network_profiles" in value:
        import capo_device_farm.types.network_profiles

        out["networkProfiles"] = (
            capo_device_farm.types.network_profiles.serialize_aws_json_1_1(
                value["network_profiles"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNetworkProfilesResult:
    out: ListNetworkProfilesResult = {}  # type: ignore[typeddict-item]
    if "networkProfiles" in data:
        import capo_device_farm.types.network_profiles

        out["network_profiles"] = (
            capo_device_farm.types.network_profiles.deserialize_aws_json_1_1(
                data["networkProfiles"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
