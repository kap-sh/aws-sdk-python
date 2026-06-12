"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_action_status
    import aws_sdk_fis.types.experiment_action_status_reason


class ExperimentActionState(TypedDict):
    status: NotRequired[
        "aws_sdk_fis.types.experiment_action_status.ExperimentActionStatus"
    ]
    """<p>The state of the action.</p>"""
    reason: NotRequired[
        "aws_sdk_fis.types.experiment_action_status_reason.ExperimentActionStatusReason"
    ]
    """<p>The reason for the state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentActionState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_fis.types.experiment_action_status

        out["status"] = aws_sdk_fis.types.experiment_action_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ExperimentActionState:
    out: ExperimentActionState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_fis.types.experiment_action_status

        out["status"] = aws_sdk_fis.types.experiment_action_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
