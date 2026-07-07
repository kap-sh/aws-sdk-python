"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteAddonInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.addon_instance_id


class DeleteAddonInstanceRequest(TypedDict, closed=True):
    addon_instance_id: "aws_sdk_mailmanager.types.addon_instance_id.AddonInstanceId"
    """<p>The Add On instance ID to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAddonInstanceRequest) -> dict:
    out: dict = {}
    out["AddonInstanceId"] = value["addon_instance_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAddonInstanceRequest:
    out: DeleteAddonInstanceRequest = {}  # type: ignore[typeddict-item]
    if "AddonInstanceId" in data:
        out["addon_instance_id"] = data["AddonInstanceId"]
    else:
        raise DeserializationError(
            "DeleteAddonInstanceRequest.addon_instance_id required"
        )
    return out
