"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IntermediateStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.s3_location


class IntermediateStorage(TypedDict, closed=True):
    s3_location: "aws_sdk_bedrock_agent.types.s3_location.S3Location"
    """<p>An S3 bucket path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateStorage) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.s3_location

    out["s3Location"] = aws_sdk_bedrock_agent.types.s3_location.serialize_json(
        value["s3_location"]
    )
    return out


def deserialize_json(data: dict) -> IntermediateStorage:
    out: IntermediateStorage = {}  # type: ignore[typeddict-item]
    if "s3Location" in data:
        import aws_sdk_bedrock_agent.types.s3_location

        out["s3_location"] = aws_sdk_bedrock_agent.types.s3_location.deserialize_json(
            data["s3Location"]
        )
    else:
        raise DeserializationError("IntermediateStorage.s3_location required")
    return out
