"""Generated from Smithy shape ``com.amazonaws.m2#JobStepRestartMarker``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.boolean
    import aws_sdk_m2.types.integer


class JobStepRestartMarker(TypedDict, closed=True):
    from_step: "str"
    """<p>The step name that a batch job was restarted from.</p>"""
    from_proc_step: NotRequired["str"]
    """<p>The procedure step name that a batch job was restarted from.</p>"""
    to_step: NotRequired["str"]
    """<p>The step name that a batch job was restarted to.</p>"""
    to_proc_step: NotRequired["str"]
    """<p>The procedure step name that a batch job was restarted to.</p>"""
    step_checkpoint: NotRequired["aws_sdk_m2.types.integer.Integer"]
    """<p>Skip selected step and issue a restart from immediate successor step for an Amazon Web Services Blu Age application batch job.</p>"""
    skip: NotRequired["aws_sdk_m2.types.boolean.Boolean"]
    """<p>The step-level checkpoint timestamp (creation or last modification) for an Amazon Web Services Blu Age application batch job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobStepRestartMarker) -> dict:
    out: dict = {}
    out["fromStep"] = value["from_step"]
    if "from_proc_step" in value:
        out["fromProcStep"] = value["from_proc_step"]
    if "to_step" in value:
        out["toStep"] = value["to_step"]
    if "to_proc_step" in value:
        out["toProcStep"] = value["to_proc_step"]
    if "step_checkpoint" in value:
        out["stepCheckpoint"] = value["step_checkpoint"]
    if "skip" in value:
        out["skip"] = value["skip"]
    return out


def deserialize_json(data: dict) -> JobStepRestartMarker:
    out: JobStepRestartMarker = {}  # type: ignore[typeddict-item]
    if "fromStep" in data:
        out["from_step"] = data["fromStep"]
    else:
        raise DeserializationError("JobStepRestartMarker.from_step required")
    if "fromProcStep" in data:
        out["from_proc_step"] = data["fromProcStep"]
    if "toStep" in data:
        out["to_step"] = data["toStep"]
    if "toProcStep" in data:
        out["to_proc_step"] = data["toProcStep"]
    if "stepCheckpoint" in data:
        out["step_checkpoint"] = data["stepCheckpoint"]
    if "skip" in data:
        out["skip"] = data["skip"]
    return out
