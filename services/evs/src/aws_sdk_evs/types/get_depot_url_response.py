"""Generated from Smithy shape ``com.amazonaws.evs#GetDepotUrlResponse``."""

from typing_extensions import TypedDict

from aws_sdk_evs.errors import DeserializationError


class GetDepotUrlResponse(TypedDict, closed=True):
    depot_url: "str"
    """<p>The URL for accessing the Amazon EVS Custom Addon depot. This URL includes the authentication token as a path component.</p>"""
    token: "str"
    """<p>The authentication token for depot access. This token is included in the depot URL and is used to authenticate requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDepotUrlResponse) -> dict:
    out: dict = {}
    out["depotUrl"] = value["depot_url"]
    out["token"] = value["token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDepotUrlResponse:
    out: GetDepotUrlResponse = {}  # type: ignore[typeddict-item]
    if "depotUrl" in data:
        out["depot_url"] = data["depotUrl"]
    else:
        raise DeserializationError("GetDepotUrlResponse.depot_url required")
    if "token" in data:
        out["token"] = data["token"]
    else:
        raise DeserializationError("GetDepotUrlResponse.token required")
    return out
