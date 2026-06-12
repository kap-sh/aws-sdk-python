"""Generated from Smithy shape ``com.amazonaws.fms#GetAppsListRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.boolean
    import aws_sdk_fms.types.list_id


class GetAppsListRequest(TypedDict):
    list_id: "aws_sdk_fms.types.list_id.ListId"
    """<p>The ID of the Firewall Manager applications list that you want the details for.</p>"""
    default_list: "aws_sdk_fms.types.boolean.Boolean"
    """<p>Specifies whether the list to retrieve is a default list owned by Firewall Manager.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAppsListRequest) -> dict:
    out: dict = {}
    out["ListId"] = value["list_id"]
    out["DefaultList"] = value.get("default_list", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAppsListRequest:
    out: GetAppsListRequest = {}  # type: ignore[typeddict-item]
    if "ListId" in data:
        out["list_id"] = data["ListId"]
    else:
        raise DeserializationError("GetAppsListRequest.list_id required")
    if "DefaultList" in data:
        out["default_list"] = data["DefaultList"]
    else:
        out["default_list"] = False
    return out
