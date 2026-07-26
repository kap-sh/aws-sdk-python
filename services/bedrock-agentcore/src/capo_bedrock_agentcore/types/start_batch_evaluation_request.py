"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartBatchEvaluationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.batch_evaluation_description
    import capo_bedrock_agentcore.types.batch_evaluation_name
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.data_source_config
    import capo_bedrock_agentcore.types.evaluation_metadata
    import capo_bedrock_agentcore.types.evaluator_list


class StartBatchEvaluationRequest(TypedDict, closed=True):
    batch_evaluation_name: (
        "capo_bedrock_agentcore.types.batch_evaluation_name.BatchEvaluationName"
    )
    """<p>The name of the batch evaluation. Must be unique within your account.</p>"""
    evaluators: NotRequired["capo_bedrock_agentcore.types.evaluator_list.EvaluatorList"]
    """<p>The list of evaluators to apply during the batch evaluation. Can include both built-in evaluators and custom evaluators. Maximum of 10 evaluators.</p>"""
    data_source_config: (
        "capo_bedrock_agentcore.types.data_source_config.DataSourceConfig"
    )
    """<p>The data source configuration that specifies where to pull agent session traces from for evaluation.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""
    evaluation_metadata: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_metadata.EvaluationMetadata"
    ]
    """<p>Optional metadata for the evaluation, including session-specific ground truth data and test scenario identifiers.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"
    ]
    """<p>The description of the batch evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBatchEvaluationRequest) -> dict:
    out: dict = {}
    out["batchEvaluationName"] = value["batch_evaluation_name"]
    if "evaluators" in value:
        import capo_bedrock_agentcore.types.evaluator_list

        out["evaluators"] = capo_bedrock_agentcore.types.evaluator_list.serialize_json(
            value["evaluators"]
        )
    import capo_bedrock_agentcore.types.data_source_config

    out["dataSourceConfig"] = (
        capo_bedrock_agentcore.types.data_source_config.serialize_json(
            value["data_source_config"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "evaluation_metadata" in value:
        import capo_bedrock_agentcore.types.evaluation_metadata

        out["evaluationMetadata"] = (
            capo_bedrock_agentcore.types.evaluation_metadata.serialize_json(
                value["evaluation_metadata"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> StartBatchEvaluationRequest:
    out: StartBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
    if "batchEvaluationName" in data:
        out["batch_evaluation_name"] = data["batchEvaluationName"]
    else:
        raise DeserializationError(
            "StartBatchEvaluationRequest.batch_evaluation_name required"
        )
    if "evaluators" in data:
        import capo_bedrock_agentcore.types.evaluator_list

        out["evaluators"] = (
            capo_bedrock_agentcore.types.evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
    if "dataSourceConfig" in data:
        import capo_bedrock_agentcore.types.data_source_config

        out["data_source_config"] = (
            capo_bedrock_agentcore.types.data_source_config.deserialize_json(
                data["dataSourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartBatchEvaluationRequest.data_source_config required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "evaluationMetadata" in data:
        import capo_bedrock_agentcore.types.evaluation_metadata

        out["evaluation_metadata"] = (
            capo_bedrock_agentcore.types.evaluation_metadata.deserialize_json(
                data["evaluationMetadata"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
