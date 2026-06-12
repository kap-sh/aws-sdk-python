"""Generated from Smithy shape ``com.amazonaws.frauddetector#CreateModelVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.external_events_detail
    import aws_sdk_frauddetector.types.ingested_events_detail
    import aws_sdk_frauddetector.types.model_identifier
    import aws_sdk_frauddetector.types.model_type_enum
    import aws_sdk_frauddetector.types.tag_list
    import aws_sdk_frauddetector.types.training_data_schema
    import aws_sdk_frauddetector.types.training_data_source_enum


class CreateModelVersionRequest(TypedDict):
    model_id: "aws_sdk_frauddetector.types.model_identifier.modelIdentifier"
    """<p>The model ID. </p>"""
    model_type: "aws_sdk_frauddetector.types.model_type_enum.ModelTypeEnum"
    """<p>The model type.</p>"""
    training_data_source: (
        "aws_sdk_frauddetector.types.training_data_source_enum.TrainingDataSourceEnum"
    )
    """<p>The training data source location in Amazon S3. </p>"""
    training_data_schema: (
        "aws_sdk_frauddetector.types.training_data_schema.TrainingDataSchema"
    )
    """<p>The training data schema.</p>"""
    external_events_detail: NotRequired[
        "aws_sdk_frauddetector.types.external_events_detail.ExternalEventsDetail"
    ]
    """<p>Details of the external events data used for model version training. Required if <code>trainingDataSource</code> is <code>EXTERNAL_EVENTS</code>.</p>"""
    ingested_events_detail: NotRequired[
        "aws_sdk_frauddetector.types.ingested_events_detail.IngestedEventsDetail"
    ]
    """<p>Details of the ingested events data used for model version training. Required if <code>trainingDataSource</code> is <code>INGESTED_EVENTS</code>.</p>"""
    tags: NotRequired["aws_sdk_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelVersionRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import aws_sdk_frauddetector.types.model_type_enum

    out["modelType"] = (
        aws_sdk_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
            value["model_type"]
        )
    )
    import aws_sdk_frauddetector.types.training_data_source_enum

    out["trainingDataSource"] = (
        aws_sdk_frauddetector.types.training_data_source_enum.serialize_aws_json_1_1(
            value["training_data_source"]
        )
    )
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
    if "tags" in value:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelVersionRequest:
    out: CreateModelVersionRequest = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("CreateModelVersionRequest.model_id required")
    if "modelType" in data:
        import aws_sdk_frauddetector.types.model_type_enum

        out["model_type"] = (
            aws_sdk_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    else:
        raise DeserializationError("CreateModelVersionRequest.model_type required")
    if "trainingDataSource" in data:
        import aws_sdk_frauddetector.types.training_data_source_enum

        out["training_data_source"] = (
            aws_sdk_frauddetector.types.training_data_source_enum.deserialize_aws_json_1_1(
                data["trainingDataSource"]
            )
        )
    else:
        raise DeserializationError(
            "CreateModelVersionRequest.training_data_source required"
        )
    if "trainingDataSchema" in data:
        import aws_sdk_frauddetector.types.training_data_schema

        out["training_data_schema"] = (
            aws_sdk_frauddetector.types.training_data_schema.deserialize_aws_json_1_1(
                data["trainingDataSchema"]
            )
        )
    else:
        raise DeserializationError(
            "CreateModelVersionRequest.training_data_schema required"
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
    if "tags" in data:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
