"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainingDatasetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.training_dataset_arn
    import aws_sdk_cleanroomsml.types.training_dataset_status


class TrainingDatasetSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the training dataset was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the training dataset was updated.</p>"""
    training_dataset_arn: (
        "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn"
    )
    """<p>The Amazon Resource Name (ARN) of the training dataset.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the training dataset.</p>"""
    status: "aws_sdk_cleanroomsml.types.training_dataset_status.TrainingDatasetStatus"
    """<p>The status of the training dataset.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the training dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainingDatasetSummary) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["trainingDatasetArn"] = value["training_dataset_arn"]
    out["name"] = value["name"]
    import aws_sdk_cleanroomsml.types.training_dataset_status

    out["status"] = aws_sdk_cleanroomsml.types.training_dataset_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> TrainingDatasetSummary:
    out: TrainingDatasetSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("TrainingDatasetSummary.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("TrainingDatasetSummary.update_time required")
    if "trainingDatasetArn" in data:
        out["training_dataset_arn"] = data["trainingDatasetArn"]
    else:
        raise DeserializationError(
            "TrainingDatasetSummary.training_dataset_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TrainingDatasetSummary.name required")
    if "status" in data:
        import aws_sdk_cleanroomsml.types.training_dataset_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.training_dataset_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("TrainingDatasetSummary.status required")
    if "description" in data:
        out["description"] = data["description"]
    return out
