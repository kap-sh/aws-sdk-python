"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetTrainingDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.dataset_list
    import aws_sdk_cleanroomsml.types.iam_role_arn
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.training_dataset_arn
    import aws_sdk_cleanroomsml.types.training_dataset_status


class GetTrainingDatasetResponse(TypedDict, closed=True):
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
    training_data: "aws_sdk_cleanroomsml.types.dataset_list.DatasetList"
    """<p>Metadata about the requested training data. </p>"""
    status: "aws_sdk_cleanroomsml.types.training_dataset_status.TrainingDatasetStatus"
    """<p>The status of the training dataset.</p>"""
    role_arn: "aws_sdk_cleanroomsml.types.iam_role_arn.IamRoleArn"
    """<p>The IAM role used to read the training data.</p>"""
    tags: NotRequired["aws_sdk_cleanroomsml.types.tag_map.TagMap"]
    """<p>The tags that are assigned to this training dataset.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the training dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrainingDatasetResponse) -> dict:
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
    import aws_sdk_cleanroomsml.types.dataset_list

    out["trainingData"] = aws_sdk_cleanroomsml.types.dataset_list.serialize_json(
        value["training_data"]
    )
    import aws_sdk_cleanroomsml.types.training_dataset_status

    out["status"] = aws_sdk_cleanroomsml.types.training_dataset_status.serialize_json(
        value["status"]
    )
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> GetTrainingDatasetResponse:
    out: GetTrainingDatasetResponse = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("GetTrainingDatasetResponse.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("GetTrainingDatasetResponse.update_time required")
    if "trainingDatasetArn" in data:
        out["training_dataset_arn"] = data["trainingDatasetArn"]
    else:
        raise DeserializationError(
            "GetTrainingDatasetResponse.training_dataset_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetTrainingDatasetResponse.name required")
    if "trainingData" in data:
        import aws_sdk_cleanroomsml.types.dataset_list

        out["training_data"] = aws_sdk_cleanroomsml.types.dataset_list.deserialize_json(
            data["trainingData"]
        )
    else:
        raise DeserializationError("GetTrainingDatasetResponse.training_data required")
    if "status" in data:
        import aws_sdk_cleanroomsml.types.training_dataset_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.training_dataset_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetTrainingDatasetResponse.status required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetTrainingDatasetResponse.role_arn required")
    if "tags" in data:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if "description" in data:
        out["description"] = data["description"]
    return out
