"""Generated from Smithy shape ``com.amazonaws.batch#RegisterJobDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.string


class RegisterJobDefinitionResponse(TypedDict):
    job_definition_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the job definition.</p>"""
    job_definition_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the job definition.</p>"""
    revision: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The revision of the job definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterJobDefinitionResponse) -> dict:
    out: dict = {}
    if "job_definition_name" in value:
        out["jobDefinitionName"] = value["job_definition_name"]
    if "job_definition_arn" in value:
        out["jobDefinitionArn"] = value["job_definition_arn"]
    if "revision" in value:
        out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> RegisterJobDefinitionResponse:
    out: RegisterJobDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "jobDefinitionName" in data:
        out["job_definition_name"] = data["jobDefinitionName"]
    if "jobDefinitionArn" in data:
        out["job_definition_arn"] = data["jobDefinitionArn"]
    if "revision" in data:
        out["revision"] = data["revision"]
    return out
