"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#KinesisResource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.arn
    import aws_sdk_bedrock_agentcore_control.types.content_configuration_list


class KinesisResource(TypedDict):
    data_stream_arn: "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
    """<p>ARN of the Kinesis Data Stream.</p>"""
    content_configurations: "aws_sdk_bedrock_agentcore_control.types.content_configuration_list.ContentConfigurationList"
    """<p>Content configurations for stream delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisResource) -> dict:
    out: dict = {}
    out["dataStreamArn"] = value["data_stream_arn"]
    import aws_sdk_bedrock_agentcore_control.types.content_configuration_list

    out["contentConfigurations"] = (
        aws_sdk_bedrock_agentcore_control.types.content_configuration_list.serialize_json(
            value["content_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> KinesisResource:
    out: KinesisResource = {}  # type: ignore[typeddict-item]
    if "dataStreamArn" in data:
        out["data_stream_arn"] = data["dataStreamArn"]
    else:
        raise DeserializationError("KinesisResource.data_stream_arn required")
    if "contentConfigurations" in data:
        import aws_sdk_bedrock_agentcore_control.types.content_configuration_list

        out["content_configurations"] = (
            aws_sdk_bedrock_agentcore_control.types.content_configuration_list.deserialize_json(
                data["contentConfigurations"]
            )
        )
    else:
        raise DeserializationError("KinesisResource.content_configurations required")
    return out
