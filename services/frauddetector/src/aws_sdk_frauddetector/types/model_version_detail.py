"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelVersionDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.external_events_detail
    import aws_sdk_frauddetector.types.float_version_string
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.ingested_events_detail
    import aws_sdk_frauddetector.types.model_identifier
    import aws_sdk_frauddetector.types.model_type_enum
    import aws_sdk_frauddetector.types.string
    import aws_sdk_frauddetector.types.time
    import aws_sdk_frauddetector.types.training_data_schema
    import aws_sdk_frauddetector.types.training_data_source_enum
    import aws_sdk_frauddetector.types.training_result
    import aws_sdk_frauddetector.types.training_result_v2


class ModelVersionDetail(TypedDict):
    model_id: NotRequired[
        "aws_sdk_frauddetector.types.model_identifier.modelIdentifier"
    ]
    """<p>The model ID.</p>"""
    model_type: NotRequired["aws_sdk_frauddetector.types.model_type_enum.ModelTypeEnum"]
    """<p>The model type.</p>"""
    model_version_number: NotRequired[
        "aws_sdk_frauddetector.types.float_version_string.floatVersionString"
    ]
    """<p>The model version number.</p>"""
    status: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The status of the model version.</p>"""
    training_data_source: NotRequired[
        "aws_sdk_frauddetector.types.training_data_source_enum.TrainingDataSourceEnum"
    ]
    """<p>The model version training data source.</p>"""
    training_data_schema: NotRequired[
        "aws_sdk_frauddetector.types.training_data_schema.TrainingDataSchema"
    ]
    """<p>The training data schema.</p>"""
    external_events_detail: NotRequired[
        "aws_sdk_frauddetector.types.external_events_detail.ExternalEventsDetail"
    ]
    """<p>The external events data details. This will be populated if the <code>trainingDataSource</code> for the model version is specified as <code>EXTERNAL_EVENTS</code>.</p>"""
    ingested_events_detail: NotRequired[
        "aws_sdk_frauddetector.types.ingested_events_detail.IngestedEventsDetail"
    ]
    """<p>The ingested events data details. This will be populated if the <code>trainingDataSource</code> for the model version is specified as <code>INGESTED_EVENTS</code>.</p>"""
    training_result: NotRequired[
        "aws_sdk_frauddetector.types.training_result.TrainingResult"
    ]
    """<p>The training results.</p>"""
    last_updated_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>The timestamp when the model was last updated.</p>"""
    created_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>The timestamp when the model was created.</p>"""
    arn: NotRequired["aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The model version ARN.</p>"""
    training_result_v2: NotRequired[
        "aws_sdk_frauddetector.types.training_result_v2.TrainingResultV2"
    ]
    """<p> The training result details. The details include the relative importance of the variables. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelVersionDetail) -> dict:
    out: dict = {}
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "model_type" in value:
        import aws_sdk_frauddetector.types.model_type_enum

        out["modelType"] = (
            aws_sdk_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
                value["model_type"]
            )
        )
    if "model_version_number" in value:
        out["modelVersionNumber"] = value["model_version_number"]
    if "status" in value:
        out["status"] = value["status"]
    if "training_data_source" in value:
        import aws_sdk_frauddetector.types.training_data_source_enum

        out["trainingDataSource"] = (
            aws_sdk_frauddetector.types.training_data_source_enum.serialize_aws_json_1_1(
                value["training_data_source"]
            )
        )
    if "training_data_schema" in value:
        import aws_sdk_frauddetector.types.training_data_schema

        out["trainingDataSchema"] = (
            aws_sdk_frauddetector.types.training_data_schema.serialize_aws_json_1_1(
                value["training_data_schema"]
            )
        )
    if "external_events_detail" in value:
        import aws_sdk_frauddetector.types.external_events_detail

        out["externalEventsDetail"] = (
            aws_sdk_frauddetector.types.external_events_detail.serialize_aws_json_1_1(
                value["external_events_detail"]
            )
        )
    if "ingested_events_detail" in value:
        import aws_sdk_frauddetector.types.ingested_events_detail

        out["ingestedEventsDetail"] = (
            aws_sdk_frauddetector.types.ingested_events_detail.serialize_aws_json_1_1(
                value["ingested_events_detail"]
            )
        )
    if "training_result" in value:
        import aws_sdk_frauddetector.types.training_result

        out["trainingResult"] = (
            aws_sdk_frauddetector.types.training_result.serialize_aws_json_1_1(
                value["training_result"]
            )
        )
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "training_result_v2" in value:
        import aws_sdk_frauddetector.types.training_result_v2

        out["trainingResultV2"] = (
            aws_sdk_frauddetector.types.training_result_v2.serialize_aws_json_1_1(
                value["training_result_v2"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelVersionDetail:
    out: ModelVersionDetail = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    if "modelType" in data:
        import aws_sdk_frauddetector.types.model_type_enum

        out["model_type"] = (
            aws_sdk_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    if "modelVersionNumber" in data:
        out["model_version_number"] = data["modelVersionNumber"]
    if "status" in data:
        out["status"] = data["status"]
    if "trainingDataSource" in data:
        import aws_sdk_frauddetector.types.training_data_source_enum

        out["training_data_source"] = (
            aws_sdk_frauddetector.types.training_data_source_enum.deserialize_aws_json_1_1(
                data["trainingDataSource"]
            )
        )
    if "trainingDataSchema" in data:
        import aws_sdk_frauddetector.types.training_data_schema

        out["training_data_schema"] = (
            aws_sdk_frauddetector.types.training_data_schema.deserialize_aws_json_1_1(
                data["trainingDataSchema"]
            )
        )
    if "externalEventsDetail" in data:
        import aws_sdk_frauddetector.types.external_events_detail

        out["external_events_detail"] = (
            aws_sdk_frauddetector.types.external_events_detail.deserialize_aws_json_1_1(
                data["externalEventsDetail"]
            )
        )
    if "ingestedEventsDetail" in data:
        import aws_sdk_frauddetector.types.ingested_events_detail

        out["ingested_events_detail"] = (
            aws_sdk_frauddetector.types.ingested_events_detail.deserialize_aws_json_1_1(
                data["ingestedEventsDetail"]
            )
        )
    if "trainingResult" in data:
        import aws_sdk_frauddetector.types.training_result

        out["training_result"] = (
            aws_sdk_frauddetector.types.training_result.deserialize_aws_json_1_1(
                data["trainingResult"]
            )
        )
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "createdTime" in data:
        out["created_time"] = data["createdTime"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "trainingResultV2" in data:
        import aws_sdk_frauddetector.types.training_result_v2

        out["training_result_v2"] = (
            aws_sdk_frauddetector.types.training_result_v2.deserialize_aws_json_1_1(
                data["trainingResultV2"]
            )
        )
    return out
