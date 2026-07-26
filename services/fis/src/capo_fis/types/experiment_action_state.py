"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_action_status
    import capo_fis.types.experiment_action_status_reason


class ExperimentActionState(TypedDict, closed=True):
    status: NotRequired[
        "capo_fis.types.experiment_action_status.ExperimentActionStatus"
    ]
    """<p>The state of the action.</p>"""
    reason: NotRequired[
        "capo_fis.types.experiment_action_status_reason.ExperimentActionStatusReason"
    ]
    """<p>The reason for the state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentActionState) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_fis.types.experiment_action_status

        out["status"] = capo_fis.types.experiment_action_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ExperimentActionState:
    out: ExperimentActionState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_fis.types.experiment_action_status

        out["status"] = capo_fis.types.experiment_action_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
