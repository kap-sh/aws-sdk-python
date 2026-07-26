"""Generated from Smithy shape ``com.amazonaws.datazone#WorkflowsMwaaPropertiesOutput``."""

from typing_extensions import NotRequired, TypedDict


class WorkflowsMwaaPropertiesOutput(TypedDict, closed=True):
    mwaa_environment_name: NotRequired["str"]
    """<p>The MWAA environment name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowsMwaaPropertiesOutput) -> dict:
    out: dict = {}
    if "mwaa_environment_name" in value:
        out["mwaaEnvironmentName"] = value["mwaa_environment_name"]
    return out


def deserialize_json(data: dict) -> WorkflowsMwaaPropertiesOutput:
    out: WorkflowsMwaaPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "mwaaEnvironmentName" in data:
        out["mwaa_environment_name"] = data["mwaaEnvironmentName"]
    return out
