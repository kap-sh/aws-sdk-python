"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceModelSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.audience_model_arn
    import aws_sdk_cleanroomsml.types.audience_model_status
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.training_dataset_arn


class AudienceModelSummary(TypedDict):
    create_time: "datetime.datetime"
    """<p>The time at which the audience model was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the audience model was updated.</p>"""
    audience_model_arn: "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the audience model.</p>"""
    training_dataset_arn: (
        "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn"
    )
    """<p>The Amazon Resource Name (ARN) of the training dataset that was used for the audience model.</p>"""
    status: "aws_sdk_cleanroomsml.types.audience_model_status.AudienceModelStatus"
    """<p>The status of the audience model.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceModelSummary) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["audienceModelArn"] = value["audience_model_arn"]
    out["name"] = value["name"]
    out["trainingDatasetArn"] = value["training_dataset_arn"]
    import aws_sdk_cleanroomsml.types.audience_model_status

    out["status"] = aws_sdk_cleanroomsml.types.audience_model_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AudienceModelSummary:
    out: AudienceModelSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("AudienceModelSummary.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("AudienceModelSummary.update_time required")
    if "audienceModelArn" in data:
        out["audience_model_arn"] = data["audienceModelArn"]
    else:
        raise DeserializationError("AudienceModelSummary.audience_model_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AudienceModelSummary.name required")
    if "trainingDatasetArn" in data:
        out["training_dataset_arn"] = data["trainingDatasetArn"]
    else:
        raise DeserializationError("AudienceModelSummary.training_dataset_arn required")
    if "status" in data:
        import aws_sdk_cleanroomsml.types.audience_model_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.audience_model_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AudienceModelSummary.status required")
    if "description" in data:
        out["description"] = data["description"]
    return out
