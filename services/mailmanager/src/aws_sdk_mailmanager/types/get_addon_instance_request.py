"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetAddonInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.addon_instance_id


class GetAddonInstanceRequest(TypedDict, closed=True):
    addon_instance_id: "aws_sdk_mailmanager.types.addon_instance_id.AddonInstanceId"
    """<p>The Add On instance ID to retrieve information for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAddonInstanceRequest) -> dict:
    out: dict = {}
    out["AddonInstanceId"] = value["addon_instance_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAddonInstanceRequest:
    out: GetAddonInstanceRequest = {}  # type: ignore[typeddict-item]
    if "AddonInstanceId" in data:
        out["addon_instance_id"] = data["AddonInstanceId"]
    else:
        raise DeserializationError("GetAddonInstanceRequest.addon_instance_id required")
    return out
