"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#InferenceContainerExecutionParameters``."""

from typing import TypedDict

from typing_extensions import NotRequired


class InferenceContainerExecutionParameters(TypedDict):
    max_payload_in_mb: NotRequired["int"]
    """<p>The maximum size of the inference container payload, specified in MB. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceContainerExecutionParameters) -> dict:
    out: dict = {}
    if "max_payload_in_mb" in value:
        out["maxPayloadInMB"] = value["max_payload_in_mb"]
    return out


def deserialize_json(data: dict) -> InferenceContainerExecutionParameters:
    out: InferenceContainerExecutionParameters = {}  # type: ignore[typeddict-item]
    if "maxPayloadInMB" in data:
        out["max_payload_in_mb"] = data["maxPayloadInMB"]
    return out
