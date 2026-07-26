"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddonInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.addon_instance_id


class CreateAddonInstanceResponse(TypedDict, closed=True):
    addon_instance_id: "capo_mailmanager.types.addon_instance_id.AddonInstanceId"
    """<p>The unique ID of the Add On instance created by this API.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddonInstanceResponse) -> dict:
    out: dict = {}
    out["AddonInstanceId"] = value["addon_instance_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddonInstanceResponse:
    out: CreateAddonInstanceResponse = {}  # type: ignore[typeddict-item]
    if "AddonInstanceId" in data:
        out["addon_instance_id"] = data["AddonInstanceId"]
    else:
        raise DeserializationError(
            "CreateAddonInstanceResponse.addon_instance_id required"
        )
    return out
