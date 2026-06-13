"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateAudienceModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.kms_key_arn
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.training_dataset_arn


class CreateAudienceModelRequest(TypedDict):
    training_data_start_time: NotRequired["datetime.datetime"]
    """<p>The start date and time of the training window.</p>"""
    training_data_end_time: NotRequired["datetime.datetime"]
    """<p>The end date and time of the training window.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the audience model resource.</p>"""
    training_dataset_arn: (
        "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn"
    )
    """<p>The Amazon Resource Name (ARN) of the training dataset for this audience model.</p>"""
    kms_key_arn: NotRequired["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.</p>"""
    tags: NotRequired["aws_sdk_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAudienceModelRequest) -> dict:
    out: dict = {}
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
    out["name"] = value["name"]
    out["trainingDatasetArn"] = value["training_dataset_arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateAudienceModelRequest:
    out: CreateAudienceModelRequest = {}  # type: ignore[typeddict-item]
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
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAudienceModelRequest.name required")
    if "trainingDatasetArn" in data:
        out["training_dataset_arn"] = data["trainingDatasetArn"]
    else:
        raise DeserializationError(
            "CreateAudienceModelRequest.training_dataset_arn required"
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "tags" in data:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if "description" in data:
        out["description"] = data["description"]
    return out
