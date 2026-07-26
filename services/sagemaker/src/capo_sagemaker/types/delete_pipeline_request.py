"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeletePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.idempotency_token
    import capo_sagemaker.types.pipeline_name


class DeletePipelineRequest(TypedDict, closed=True):
    pipeline_name: NotRequired["capo_sagemaker.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline to delete.</p>"""
    client_request_token: NotRequired[
        "capo_sagemaker.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePipelineRequest) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePipelineRequest:
    out: DeletePipelineRequest = {}  # type: ignore[typeddict-item]
    if "PipelineName" in data:
        out["pipeline_name"] = data["PipelineName"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
