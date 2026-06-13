"""Generated from Smithy shape ``com.amazonaws.neptunedata#StartMLModelTrainingJobOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class StartMLModelTrainingJobOutput(TypedDict):
    id: NotRequired["str"]
    """<p>The unique ID of the new model training job.</p>"""
    arn: NotRequired["str"]
    """<p>The ARN of the new model training job.</p>"""
    creation_time_in_millis: NotRequired["int"]
    """<p>The model training job creation time, in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMLModelTrainingJobOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "creation_time_in_millis" in value:
        out["creationTimeInMillis"] = value["creation_time_in_millis"]
    return out


def deserialize_json(data: dict) -> StartMLModelTrainingJobOutput:
    out: StartMLModelTrainingJobOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "creationTimeInMillis" in data:
        out["creation_time_in_millis"] = data["creationTimeInMillis"]
    return out
