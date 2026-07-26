"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetModelVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.external_events_detail
    import capo_frauddetector.types.float_version_string
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.ingested_events_detail
    import capo_frauddetector.types.model_identifier
    import capo_frauddetector.types.model_type_enum
    import capo_frauddetector.types.string
    import capo_frauddetector.types.training_data_schema
    import capo_frauddetector.types.training_data_source_enum


class GetModelVersionResult(TypedDict, closed=True):
    model_id: NotRequired["capo_frauddetector.types.model_identifier.modelIdentifier"]
    """<p>The model ID.</p>"""
    model_type: NotRequired["capo_frauddetector.types.model_type_enum.ModelTypeEnum"]
    """<p>The model type.</p>"""
    model_version_number: NotRequired[
        "capo_frauddetector.types.float_version_string.floatVersionString"
    ]
    """<p>The model version number.</p>"""
    training_data_source: NotRequired[
        "capo_frauddetector.types.training_data_source_enum.TrainingDataSourceEnum"
    ]
    """<p>The training data source.</p>"""
    training_data_schema: NotRequired[
        "capo_frauddetector.types.training_data_schema.TrainingDataSchema"
    ]
    """<p>The training data schema.</p>"""
    external_events_detail: NotRequired[
        "capo_frauddetector.types.external_events_detail.ExternalEventsDetail"
    ]
    """<p>The details of the external events data used for training the model version. This will be populated if the <code>trainingDataSource</code> is <code>EXTERNAL_EVENTS</code> </p>"""
    ingested_events_detail: NotRequired[
        "capo_frauddetector.types.ingested_events_detail.IngestedEventsDetail"
    ]
    """<p>The details of the ingested events data used for training the model version. This will be populated if the <code>trainingDataSource</code> is <code>INGESTED_EVENTS</code>.</p>"""
    status: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The model version status.</p> <p>Possible values are:</p> <ul> <li> <p> <code>TRAINING_IN_PROGRESS</code> </p> </li> <li> <p> <code>TRAINING_COMPLETE</code> </p> </li> <li> <p> <code>ACTIVATE_REQUESTED</code> </p> </li> <li> <p> <code>ACTIVATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>INACTIVATE_REQUESTED</code> </p> </li> <li> <p> <code>INACTIVATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>INACTIVE</code> </p> </li> <li> <p> <code>ERROR</code> </p> </li> </ul>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The model version ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetModelVersionResult) -> dict:
    out: dict = {}
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "model_type" in value:
        import capo_frauddetector.types.model_type_enum

        out["modelType"] = (
            capo_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
                value["model_type"]
            )
        )
    if "model_version_number" in value:
        out["modelVersionNumber"] = value["model_version_number"]
    if "training_data_source" in value:
        import capo_frauddetector.types.training_data_source_enum

        out["trainingDataSource"] = (
            capo_frauddetector.types.training_data_source_enum.serialize_aws_json_1_1(
                value["training_data_source"]
            )
        )
    if "training_data_schema" in value:
        import capo_frauddetector.types.training_data_schema

        out["trainingDataSchema"] = (
            capo_frauddetector.types.training_data_schema.serialize_aws_json_1_1(
                value["training_data_schema"]
            )
        )
    if "external_events_detail" in value:
        import capo_frauddetector.types.external_events_detail

        out["externalEventsDetail"] = (
            capo_frauddetector.types.external_events_detail.serialize_aws_json_1_1(
                value["external_events_detail"]
            )
        )
    if "ingested_events_detail" in value:
        import capo_frauddetector.types.ingested_events_detail

        out["ingestedEventsDetail"] = (
            capo_frauddetector.types.ingested_events_detail.serialize_aws_json_1_1(
                value["ingested_events_detail"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetModelVersionResult:
    out: GetModelVersionResult = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    if "modelType" in data:
        import capo_frauddetector.types.model_type_enum

        out["model_type"] = (
            capo_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    if "modelVersionNumber" in data:
        out["model_version_number"] = data["modelVersionNumber"]
    if "trainingDataSource" in data:
        import capo_frauddetector.types.training_data_source_enum

        out["training_data_source"] = (
            capo_frauddetector.types.training_data_source_enum.deserialize_aws_json_1_1(
                data["trainingDataSource"]
            )
        )
    if "trainingDataSchema" in data:
        import capo_frauddetector.types.training_data_schema

        out["training_data_schema"] = (
            capo_frauddetector.types.training_data_schema.deserialize_aws_json_1_1(
                data["trainingDataSchema"]
            )
        )
    if "externalEventsDetail" in data:
        import capo_frauddetector.types.external_events_detail

        out["external_events_detail"] = (
            capo_frauddetector.types.external_events_detail.deserialize_aws_json_1_1(
                data["externalEventsDetail"]
            )
        )
    if "ingestedEventsDetail" in data:
        import capo_frauddetector.types.ingested_events_detail

        out["ingested_events_detail"] = (
            capo_frauddetector.types.ingested_events_detail.deserialize_aws_json_1_1(
                data["ingestedEventsDetail"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
