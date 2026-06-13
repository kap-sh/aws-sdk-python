"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ModelTrainingDataChannel``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.ml_input_channel_arn
    import aws_sdk_cleanroomsml.types.model_training_data_channel_name
    import aws_sdk_cleanroomsml.types.s3_data_distribution_type


class ModelTrainingDataChannel(TypedDict):
    ml_input_channel_arn: (
        "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel for this model training data channel.</p>"""
    channel_name: "aws_sdk_cleanroomsml.types.model_training_data_channel_name.ModelTrainingDataChannelName"
    """<p>The name of the training data channel.</p>"""
    s3_data_distribution_type: (
        "aws_sdk_cleanroomsml.types.s3_data_distribution_type.S3DataDistributionType"
    )
    """<p>Specifies how the training data stored in Amazon S3 should be distributed to training instances. This parameter controls the data distribution strategy for the training job:</p> <ul> <li> <p> <code>FullyReplicated</code> - The entire dataset is replicated on each training instance. This is suitable for smaller datasets and algorithms that require access to the complete dataset.</p> </li> <li> <p> <code>ShardedByS3Key</code> - The dataset is distributed across training instances based on Amazon S3 key names. This is suitable for larger datasets and distributed training scenarios where each instance processes a subset of the data.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelTrainingDataChannel) -> dict:
    out: dict = {}
    out["mlInputChannelArn"] = value["ml_input_channel_arn"]
    out["channelName"] = value["channel_name"]
    import aws_sdk_cleanroomsml.types.s3_data_distribution_type

    out["s3DataDistributionType"] = (
        aws_sdk_cleanroomsml.types.s3_data_distribution_type.serialize_json(
            value.get("s3_data_distribution_type", "FullyReplicated")
        )
    )
    return out


def deserialize_json(data: dict) -> ModelTrainingDataChannel:
    out: ModelTrainingDataChannel = {}  # type: ignore[typeddict-item]
    if "mlInputChannelArn" in data:
        out["ml_input_channel_arn"] = data["mlInputChannelArn"]
    else:
        raise DeserializationError(
            "ModelTrainingDataChannel.ml_input_channel_arn required"
        )
    if "channelName" in data:
        out["channel_name"] = data["channelName"]
    else:
        raise DeserializationError("ModelTrainingDataChannel.channel_name required")
    if "s3DataDistributionType" in data:
        import aws_sdk_cleanroomsml.types.s3_data_distribution_type

        out["s3_data_distribution_type"] = (
            aws_sdk_cleanroomsml.types.s3_data_distribution_type.deserialize_json(
                data["s3DataDistributionType"]
            )
        )
    else:
        out["s3_data_distribution_type"] = "FullyReplicated"
    return out
