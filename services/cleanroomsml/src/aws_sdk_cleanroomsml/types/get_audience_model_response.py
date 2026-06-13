"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetAudienceModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.audience_model_arn
    import aws_sdk_cleanroomsml.types.audience_model_status
    import aws_sdk_cleanroomsml.types.kms_key_arn
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.status_details
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.training_dataset_arn


class GetAudienceModelResponse(TypedDict):
    create_time: "datetime.datetime"
    """<p>The time at which the audience model was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the audience model was updated.</p>"""
    training_data_start_time: NotRequired["datetime.datetime"]
    """<p>The start date specified for the training window.</p>"""
    training_data_end_time: NotRequired["datetime.datetime"]
    """<p>The end date specified for the training window.</p>"""
    audience_model_arn: "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the audience model.</p>"""
    training_dataset_arn: (
        "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn"
    )
    """<p>The Amazon Resource Name (ARN) of the training dataset that was used for this audience model.</p>"""
    status: "aws_sdk_cleanroomsml.types.audience_model_status.AudienceModelStatus"
    """<p>The status of the audience model.</p>"""
    status_details: NotRequired[
        "aws_sdk_cleanroomsml.types.status_details.StatusDetails"
    ]
    """<p>Details about the status of the audience model.</p>"""
    kms_key_arn: NotRequired["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The KMS key ARN used for the audience model.</p>"""
    tags: NotRequired["aws_sdk_cleanroomsml.types.tag_map.TagMap"]
    """<p>The tags that are assigned to the audience model.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAudienceModelResponse) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    if "training_data_start_time" in value:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["trainingDataStartTime"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
                value["training_data_start_time"]
            )
        )
    if "training_data_end_time" in value:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["trainingDataEndTime"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
                value["training_data_end_time"]
            )
        )
    out["audienceModelArn"] = value["audience_model_arn"]
    out["name"] = value["name"]
    out["trainingDatasetArn"] = value["training_dataset_arn"]
    import aws_sdk_cleanroomsml.types.audience_model_status

    out["status"] = aws_sdk_cleanroomsml.types.audience_model_status.serialize_json(
        value["status"]
    )
    if "status_details" in value:
        import aws_sdk_cleanroomsml.types.status_details

        out["statusDetails"] = aws_sdk_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> GetAudienceModelResponse:
    out: GetAudienceModelResponse = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("GetAudienceModelResponse.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("GetAudienceModelResponse.update_time required")
    if "trainingDataStartTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["training_data_start_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["trainingDataStartTime"]
            )
        )
    if "trainingDataEndTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["training_data_end_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["trainingDataEndTime"]
            )
        )
    if "audienceModelArn" in data:
        out["audience_model_arn"] = data["audienceModelArn"]
    else:
        raise DeserializationError(
            "GetAudienceModelResponse.audience_model_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetAudienceModelResponse.name required")
    if "trainingDatasetArn" in data:
        out["training_dataset_arn"] = data["trainingDatasetArn"]
    else:
        raise DeserializationError(
            "GetAudienceModelResponse.training_dataset_arn required"
        )
    if "status" in data:
        import aws_sdk_cleanroomsml.types.audience_model_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.audience_model_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetAudienceModelResponse.status required")
    if "statusDetails" in data:
        import aws_sdk_cleanroomsml.types.status_details

        out["status_details"] = (
            aws_sdk_cleanroomsml.types.status_details.deserialize_json(
                data["statusDetails"]
            )
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "tags" in data:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if "description" in data:
        out["description"] = data["description"]
    return out
