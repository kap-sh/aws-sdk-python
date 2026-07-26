"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEventPredictionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.list_of_external_model_outputs
    import capo_frauddetector.types.list_of_model_scores
    import capo_frauddetector.types.list_of_rule_results


class GetEventPredictionResult(TypedDict, closed=True):
    model_scores: NotRequired[
        "capo_frauddetector.types.list_of_model_scores.ListOfModelScores"
    ]
    """<p>The model scores. Amazon Fraud Detector generates model scores between 0 and 1000, where 0 is low fraud risk and 1000 is high fraud risk. Model scores are directly related to the false positive rate (FPR). For example, a score of 600 corresponds to an estimated 10% false positive rate whereas a score of 900 corresponds to an estimated 2% false positive rate.</p>"""
    rule_results: NotRequired[
        "capo_frauddetector.types.list_of_rule_results.ListOfRuleResults"
    ]
    """<p>The results from the rules.</p>"""
    external_model_outputs: NotRequired[
        "capo_frauddetector.types.list_of_external_model_outputs.ListOfExternalModelOutputs"
    ]
    """<p>The model scores for Amazon SageMaker models.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventPredictionResult) -> dict:
    out: dict = {}
    if "model_scores" in value:
        import capo_frauddetector.types.list_of_model_scores

        out["modelScores"] = (
            capo_frauddetector.types.list_of_model_scores.serialize_aws_json_1_1(
                value["model_scores"]
            )
        )
    if "rule_results" in value:
        import capo_frauddetector.types.list_of_rule_results

        out["ruleResults"] = (
            capo_frauddetector.types.list_of_rule_results.serialize_aws_json_1_1(
                value["rule_results"]
            )
        )
    if "external_model_outputs" in value:
        import capo_frauddetector.types.list_of_external_model_outputs

        out["externalModelOutputs"] = (
            capo_frauddetector.types.list_of_external_model_outputs.serialize_aws_json_1_1(
                value["external_model_outputs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventPredictionResult:
    out: GetEventPredictionResult = {}  # type: ignore[typeddict-item]
    if "modelScores" in data:
        import capo_frauddetector.types.list_of_model_scores

        out["model_scores"] = (
            capo_frauddetector.types.list_of_model_scores.deserialize_aws_json_1_1(
                data["modelScores"]
            )
        )
    if "ruleResults" in data:
        import capo_frauddetector.types.list_of_rule_results

        out["rule_results"] = (
            capo_frauddetector.types.list_of_rule_results.deserialize_aws_json_1_1(
                data["ruleResults"]
            )
        )
    if "externalModelOutputs" in data:
        import capo_frauddetector.types.list_of_external_model_outputs

        out["external_model_outputs"] = (
            capo_frauddetector.types.list_of_external_model_outputs.deserialize_aws_json_1_1(
                data["externalModelOutputs"]
            )
        )
    return out
