"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListNetworkProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.network_profile_type
    import capo_device_farm.types.pagination_token


class ListNetworkProfilesRequest(TypedDict, closed=True):
    arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the project for which you want to list network profiles.</p>"""
    type: NotRequired["capo_device_farm.types.network_profile_type.NetworkProfileType"]
    """<p>The type of network profile to return information about. Valid values are listed here.</p>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNetworkProfilesRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "type" in value:
        import capo_device_farm.types.network_profile_type

        out["type"] = (
            capo_device_farm.types.network_profile_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNetworkProfilesRequest:
    out: ListNetworkProfilesRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListNetworkProfilesRequest.arn required")
    if "type" in data:
        import capo_device_farm.types.network_profile_type

        out["type"] = (
            capo_device_farm.types.network_profile_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
