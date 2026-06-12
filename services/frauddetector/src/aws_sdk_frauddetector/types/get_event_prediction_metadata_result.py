"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEventPredictionMetadataResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.evaluated_rule_list
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.list_of_evaluated_external_models
    import aws_sdk_frauddetector.types.list_of_evaluated_model_versions
    import aws_sdk_frauddetector.types.list_of_event_variable_summaries
    import aws_sdk_frauddetector.types.list_of_strings
    import aws_sdk_frauddetector.types.rule_execution_mode
    import aws_sdk_frauddetector.types.string
    import aws_sdk_frauddetector.types.time
    import aws_sdk_frauddetector.types.whole_number_version_string


class GetEventPredictionMetadataResult(TypedDict):
    event_id: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p> The event ID. </p>"""
    event_type_name: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p> The event type associated with the detector specified for this prediction. </p>"""
    entity_id: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p> The entity ID. </p>"""
    entity_type: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p> The entity type. </p>"""
    event_timestamp: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p> The timestamp for when the prediction was generated for the associated event ID. </p>"""
    detector_id: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p> The detector ID. </p>"""
    detector_version_id: NotRequired[
        "aws_sdk_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p> The detector version ID. </p>"""
    detector_version_status: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p> The status of the detector version. </p>"""
    event_variables: NotRequired[
        "aws_sdk_frauddetector.types.list_of_event_variable_summaries.ListOfEventVariableSummaries"
    ]
    """<p> A list of event variables that influenced the prediction scores. </p>"""
    rules: NotRequired[
        "aws_sdk_frauddetector.types.evaluated_rule_list.EvaluatedRuleList"
    ]
    """<p> List of rules associated with the detector version that were used for evaluating variable values. </p>"""
    rule_execution_mode: NotRequired[
        "aws_sdk_frauddetector.types.rule_execution_mode.RuleExecutionMode"
    ]
    """<p> The execution mode of the rule used for evaluating variable values. </p>"""
    outcomes: NotRequired["aws_sdk_frauddetector.types.list_of_strings.ListOfStrings"]
    """<p> The outcomes of the matched rule, based on the rule execution mode. </p>"""
    evaluated_model_versions: NotRequired[
        "aws_sdk_frauddetector.types.list_of_evaluated_model_versions.ListOfEvaluatedModelVersions"
    ]
    """<p> Model versions that were evaluated for generating predictions. </p>"""
    evaluated_external_models: NotRequired[
        "aws_sdk_frauddetector.types.list_of_evaluated_external_models.ListOfEvaluatedExternalModels"
    ]
    """<p> External (Amazon SageMaker) models that were evaluated for generating predictions. </p>"""
    prediction_timestamp: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>The timestamp that defines when the prediction was generated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventPredictionMetadataResult) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_type" in value:
        out["entityType"] = value["entity_type"]
    if "event_timestamp" in value:
        out["eventTimestamp"] = value["event_timestamp"]
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "detector_version_id" in value:
        out["detectorVersionId"] = value["detector_version_id"]
    if "detector_version_status" in value:
        out["detectorVersionStatus"] = value["detector_version_status"]
    if "event_variables" in value:
        import aws_sdk_frauddetector.types.list_of_event_variable_summaries

        out["eventVariables"] = (
            aws_sdk_frauddetector.types.list_of_event_variable_summaries.serialize_aws_json_1_1(
                value["event_variables"]
            )
        )
    if "rules" in value:
        import aws_sdk_frauddetector.types.evaluated_rule_list

        out["rules"] = (
            aws_sdk_frauddetector.types.evaluated_rule_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    if "rule_execution_mode" in value:
        import aws_sdk_frauddetector.types.rule_execution_mode

        out["ruleExecutionMode"] = (
            aws_sdk_frauddetector.types.rule_execution_mode.serialize_aws_json_1_1(
                value["rule_execution_mode"]
            )
        )
    if "outcomes" in value:
        import aws_sdk_frauddetector.types.list_of_strings

        out["outcomes"] = (
            aws_sdk_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
                value["outcomes"]
            )
        )
    if "evaluated_model_versions" in value:
        import aws_sdk_frauddetector.types.list_of_evaluated_model_versions

        out["evaluatedModelVersions"] = (
            aws_sdk_frauddetector.types.list_of_evaluated_model_versions.serialize_aws_json_1_1(
                value["evaluated_model_versions"]
            )
        )
    if "evaluated_external_models" in value:
        import aws_sdk_frauddetector.types.list_of_evaluated_external_models

        out["evaluatedExternalModels"] = (
            aws_sdk_frauddetector.types.list_of_evaluated_external_models.serialize_aws_json_1_1(
                value["evaluated_external_models"]
            )
        )
    if "prediction_timestamp" in value:
        out["predictionTimestamp"] = value["prediction_timestamp"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventPredictionMetadataResult:
    out: GetEventPredictionMetadataResult = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "entityType" in data:
        out["entity_type"] = data["entityType"]
    if "eventTimestamp" in data:
        out["event_timestamp"] = data["eventTimestamp"]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "detectorVersionId" in data:
        out["detector_version_id"] = data["detectorVersionId"]
    if "detectorVersionStatus" in data:
        out["detector_version_status"] = data["detectorVersionStatus"]
    if "eventVariables" in data:
        import aws_sdk_frauddetector.types.list_of_event_variable_summaries

        out["event_variables"] = (
            aws_sdk_frauddetector.types.list_of_event_variable_summaries.deserialize_aws_json_1_1(
                data["eventVariables"]
            )
        )
    if "rules" in data:
        import aws_sdk_frauddetector.types.evaluated_rule_list

        out["rules"] = (
            aws_sdk_frauddetector.types.evaluated_rule_list.deserialize_aws_json_1_1(
                data["rules"]
            )
        )
    if "ruleExecutionMode" in data:
        import aws_sdk_frauddetector.types.rule_execution_mode

        out["rule_execution_mode"] = (
            aws_sdk_frauddetector.types.rule_execution_mode.deserialize_aws_json_1_1(
                data["ruleExecutionMode"]
            )
        )
    if "outcomes" in data:
        import aws_sdk_frauddetector.types.list_of_strings

        out["outcomes"] = (
            aws_sdk_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    if "evaluatedModelVersions" in data:
        import aws_sdk_frauddetector.types.list_of_evaluated_model_versions

        out["evaluated_model_versions"] = (
            aws_sdk_frauddetector.types.list_of_evaluated_model_versions.deserialize_aws_json_1_1(
                data["evaluatedModelVersions"]
            )
        )
    if "evaluatedExternalModels" in data:
        import aws_sdk_frauddetector.types.list_of_evaluated_external_models

        out["evaluated_external_models"] = (
            aws_sdk_frauddetector.types.list_of_evaluated_external_models.deserialize_aws_json_1_1(
                data["evaluatedExternalModels"]
            )
        )
    if "predictionTimestamp" in data:
        out["prediction_timestamp"] = data["predictionTimestamp"]
    return out
