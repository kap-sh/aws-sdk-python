"""Generated from Smithy shape ``com.amazonaws.batch#DeregisterJobDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class DeregisterJobDefinitionRequest(TypedDict):
    job_definition: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name and revision (<code>name:revision</code>) or full Amazon Resource Name (ARN) of the job definition to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterJobDefinitionRequest) -> dict:
    out: dict = {}
    if "job_definition" in value:
        out["jobDefinition"] = value["job_definition"]
    return out


def deserialize_json(data: dict) -> DeregisterJobDefinitionRequest:
    out: DeregisterJobDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "jobDefinition" in data:
        out["job_definition"] = data["jobDefinition"]
    return out
