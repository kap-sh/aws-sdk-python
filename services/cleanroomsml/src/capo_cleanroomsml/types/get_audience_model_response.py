"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetAudienceModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.audience_model_arn
    import capo_cleanroomsml.types.audience_model_status
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.status_details
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.training_dataset_arn


class GetAudienceModelResponse(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the audience model was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the audience model was updated.</p>"""
    training_data_start_time: NotRequired["datetime.datetime"]
    """<p>The start date specified for the training window.</p>"""
    training_data_end_time: NotRequired["datetime.datetime"]
    """<p>The end date specified for the training window.</p>"""
    audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the audience model.</p>"""
    training_dataset_arn: (
        "capo_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn"
    )
    """<p>The Amazon Resource Name (ARN) of the training dataset that was used for this audience model.</p>"""
    status: "capo_cleanroomsml.types.audience_model_status.AudienceModelStatus"
    """<p>The status of the audience model.</p>"""
    status_details: NotRequired["capo_cleanroomsml.types.status_details.StatusDetails"]
    """<p>Details about the status of the audience model.</p>"""
    kms_key_arn: NotRequired["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The KMS key ARN used for the audience model.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The tags that are assigned to the audience model.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAudienceModelResponse) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types._prelude.timestamp

    out["createTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    if "training_data_start_time" in value:
        import capo_cleanroomsml.types._prelude.timestamp

        out["trainingDataStartTime"] = (
            capo_cleanroomsml.types._prelude.timestamp.serialize_json(
                value["training_data_start_time"]
            )
        )
    if "training_data_end_time" in value:
        import capo_cleanroomsml.types._prelude.timestamp

        out["trainingDataEndTime"] = (
            capo_cleanroomsml.types._prelude.timestamp.serialize_json(
                value["training_data_end_time"]
            )
        )
    out["audienceModelArn"] = value["audience_model_arn"]
    out["name"] = value["name"]
    out["trainingDatasetArn"] = value["training_dataset_arn"]
    import capo_cleanroomsml.types.audience_model_status

    out["status"] = capo_cleanroomsml.types.audience_model_status.serialize_json(
        value["status"]
    )
    if "status_details" in value:
        import capo_cleanroomsml.types.status_details

        out["statusDetails"] = capo_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> GetAudienceModelResponse:
    out: GetAudienceModelResponse = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("GetAudienceModelResponse.create_time required")
    if "updateTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("GetAudienceModelResponse.update_time required")
    if "trainingDataStartTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["training_data_start_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["trainingDataStartTime"]
            )
        )
    if "trainingDataEndTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["training_data_end_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
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
        import capo_cleanroomsml.types.audience_model_status

        out["status"] = capo_cleanroomsml.types.audience_model_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetAudienceModelResponse.status required")
    if "statusDetails" in data:
        import capo_cleanroomsml.types.status_details

        out["status_details"] = capo_cleanroomsml.types.status_details.deserialize_json(
            data["statusDetails"]
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "tags" in data:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if "description" in data:
        out["description"] = data["description"]
    return out
