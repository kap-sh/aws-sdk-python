"""Generated from Smithy shape ``com.amazonaws.iot#MitigationActionIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.mitigation_action_arn
    import capo_iot.types.mitigation_action_name
    import capo_iot.types.timestamp


class MitigationActionIdentifier(TypedDict, closed=True):
    action_name: NotRequired[
        "capo_iot.types.mitigation_action_name.MitigationActionName"
    ]
    """<p>The friendly name of the mitigation action.</p>"""
    action_arn: NotRequired["capo_iot.types.mitigation_action_arn.MitigationActionArn"]
    """<p>The IAM role ARN used to apply this mitigation action.</p>"""
    creation_date: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>The date when this mitigation action was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MitigationActionIdentifier) -> dict:
    out: dict = {}
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "action_arn" in value:
        out["actionArn"] = value["action_arn"]
    if "creation_date" in value:
        import capo_iot.types.timestamp

        out["creationDate"] = capo_iot.types.timestamp.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> MitigationActionIdentifier:
    out: MitigationActionIdentifier = {}  # type: ignore[typeddict-item]
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    if "actionArn" in data:
        out["action_arn"] = data["actionArn"]
    if "creationDate" in data:
        import capo_iot.types.timestamp

        out["creation_date"] = capo_iot.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    return out
