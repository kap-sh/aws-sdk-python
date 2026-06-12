"""Generated from Smithy shape ``com.amazonaws.configservice#PutExternalEvaluationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_name
    import aws_sdk_config_service.types.external_evaluation


class PutExternalEvaluationRequest(TypedDict):
    config_rule_name: "aws_sdk_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule.</p>"""
    external_evaluation: (
        "aws_sdk_config_service.types.external_evaluation.ExternalEvaluation"
    )
    """<p>An <code>ExternalEvaluation</code> object that provides details about compliance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutExternalEvaluationRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    import aws_sdk_config_service.types.external_evaluation

    out["ExternalEvaluation"] = (
        aws_sdk_config_service.types.external_evaluation.serialize_aws_json_1_1(
            value["external_evaluation"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutExternalEvaluationRequest:
    out: PutExternalEvaluationRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        raise DeserializationError(
            "PutExternalEvaluationRequest.config_rule_name required"
        )
    if "ExternalEvaluation" in data:
        import aws_sdk_config_service.types.external_evaluation

        out["external_evaluation"] = (
            aws_sdk_config_service.types.external_evaluation.deserialize_aws_json_1_1(
                data["ExternalEvaluation"]
            )
        )
    else:
        raise DeserializationError(
            "PutExternalEvaluationRequest.external_evaluation required"
        )
    return out
