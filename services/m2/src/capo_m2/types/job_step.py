"""Generated from Smithy shape ``com.amazonaws.m2#JobStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.boolean
    import capo_m2.types.integer
    import capo_m2.types.timestamp


class JobStep(TypedDict, closed=True):
    step_number: "capo_m2.types.integer.Integer"
    """<p>The number of a step.</p>"""
    step_name: NotRequired["str"]
    """<p>The name of a step.</p>"""
    proc_step_number: "capo_m2.types.integer.Integer"
    """<p>The number of a procedure step.</p>"""
    proc_step_name: NotRequired["str"]
    """<p>The name of a procedure step.</p>"""
    step_cond_code: NotRequired["str"]
    """<p>The condition code of a step.</p>"""
    step_restartable: "capo_m2.types.boolean.Boolean"
    """<p>Specifies if a step can be restarted or not.</p>"""
    step_checkpoint: NotRequired["capo_m2.types.integer.Integer"]
    """<p>A registered step-level checkpoint identifier that can be used for restarting an Amazon Web Services Blu Age application batch job.</p>"""
    step_checkpoint_status: NotRequired["str"]
    """<p>The step-level checkpoint status for an Amazon Web Services Blu Age application batch job.</p>"""
    step_checkpoint_time: NotRequired["capo_m2.types.timestamp.Timestamp"]
    """<p>The step-level checkpoint status for an Amazon Web Services Blu Age application batch job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobStep) -> dict:
    out: dict = {}
    out["stepNumber"] = value.get("step_number", 0)
    if "step_name" in value:
        out["stepName"] = value["step_name"]
    out["procStepNumber"] = value.get("proc_step_number", 0)
    if "proc_step_name" in value:
        out["procStepName"] = value["proc_step_name"]
    if "step_cond_code" in value:
        out["stepCondCode"] = value["step_cond_code"]
    out["stepRestartable"] = value.get("step_restartable", False)
    if "step_checkpoint" in value:
        out["stepCheckpoint"] = value["step_checkpoint"]
    if "step_checkpoint_status" in value:
        out["stepCheckpointStatus"] = value["step_checkpoint_status"]
    if "step_checkpoint_time" in value:
        import capo_m2.types.timestamp

        out["stepCheckpointTime"] = capo_m2.types.timestamp.serialize_json(
            value["step_checkpoint_time"]
        )
    return out


def deserialize_json(data: dict) -> JobStep:
    out: JobStep = {}  # type: ignore[typeddict-item]
    if "stepNumber" in data:
        out["step_number"] = data["stepNumber"]
    else:
        out["step_number"] = 0
    if "stepName" in data:
        out["step_name"] = data["stepName"]
    if "procStepNumber" in data:
        out["proc_step_number"] = data["procStepNumber"]
    else:
        out["proc_step_number"] = 0
    if "procStepName" in data:
        out["proc_step_name"] = data["procStepName"]
    if "stepCondCode" in data:
        out["step_cond_code"] = data["stepCondCode"]
    if "stepRestartable" in data:
        out["step_restartable"] = data["stepRestartable"]
    else:
        out["step_restartable"] = False
    if "stepCheckpoint" in data:
        out["step_checkpoint"] = data["stepCheckpoint"]
    if "stepCheckpointStatus" in data:
        out["step_checkpoint_status"] = data["stepCheckpointStatus"]
    if "stepCheckpointTime" in data:
        import capo_m2.types.timestamp

        out["step_checkpoint_time"] = capo_m2.types.timestamp.deserialize_json(
            data["stepCheckpointTime"]
        )
    return out
