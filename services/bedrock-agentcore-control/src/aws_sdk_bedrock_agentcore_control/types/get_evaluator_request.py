"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetEvaluatorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.evaluator_id
    import aws_sdk_bedrock_agentcore_control.types.included_data


class GetEvaluatorRequest(TypedDict):
    evaluator_id: "aws_sdk_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the evaluator to retrieve. Can be a built-in evaluator ID (e.g., Builtin.Helpfulness) or a custom evaluator ID. </p>"""
    included_data: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.included_data.IncludedData"
    ]
    """<p> Controls which data is returned in the response. <code>ALL_DATA</code> (default) returns the full evaluator including decrypted instructions and rating scale. For evaluators encrypted with a customer managed KMS key, this requires <code>kms:Decrypt</code> permission on the key. <code>METADATA_ONLY</code> returns evaluator metadata and model configuration without instructions or rating scale, and does not require any KMS permissions. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvaluatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEvaluatorRequest:
    out: GetEvaluatorRequest = {}  # type: ignore[typeddict-item]
    return out
