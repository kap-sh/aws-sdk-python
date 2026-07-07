"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#DeleteTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.force_unsubscribe_all
    import aws_sdk_codestar_notifications.types.target_address


class DeleteTargetRequest(TypedDict, closed=True):
    target_address: "aws_sdk_codestar_notifications.types.target_address.TargetAddress"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client to delete.</p>"""
    force_unsubscribe_all: (
        "aws_sdk_codestar_notifications.types.force_unsubscribe_all.ForceUnsubscribeAll"
    )
    """<p>A Boolean value that can be used to delete all associations with this Amazon Q Developer in chat applications topic. The default value is FALSE. If set to TRUE, all associations between that target and every notification rule in your Amazon Web Services account are deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTargetRequest) -> dict:
    out: dict = {}
    out["TargetAddress"] = value["target_address"]
    out["ForceUnsubscribeAll"] = value.get("force_unsubscribe_all", False)
    return out


def deserialize_json(data: dict) -> DeleteTargetRequest:
    out: DeleteTargetRequest = {}  # type: ignore[typeddict-item]
    if "TargetAddress" in data:
        out["target_address"] = data["TargetAddress"]
    else:
        raise DeserializationError("DeleteTargetRequest.target_address required")
    if "ForceUnsubscribeAll" in data:
        out["force_unsubscribe_all"] = data["ForceUnsubscribeAll"]
    else:
        out["force_unsubscribe_all"] = False
    return out
