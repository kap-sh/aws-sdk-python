"""Generated from Smithy shape ``com.amazonaws.bedrockagent#APISchema``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.payload
    import aws_sdk_bedrock_agent.types.s3_identifier


class _APISchema_s3(TypedDict):
    s3: "aws_sdk_bedrock_agent.types.s3_identifier.S3Identifier"


class _APISchema_payload(TypedDict):
    payload: "aws_sdk_bedrock_agent.types.payload.Payload"


APISchema: TypeAlias = _APISchema_s3 | _APISchema_payload


# --- restJson1 ser/de ---
def serialize_json(value: APISchema) -> dict:
    if "s3" in value:
        import aws_sdk_bedrock_agent.types.s3_identifier

        return {
            "s3": aws_sdk_bedrock_agent.types.s3_identifier.serialize_json(value["s3"])
        }
    elif "payload" in value:
        return {"payload": value["payload"]}
    else:
        raise SerializationError("APISchema: no variant present")


def deserialize_json(data: dict) -> APISchema:
    if "s3" in data:
        import aws_sdk_bedrock_agent.types.s3_identifier

        return {
            "s3": aws_sdk_bedrock_agent.types.s3_identifier.deserialize_json(data["s3"])
        }
    elif "payload" in data:
        return {"payload": data["payload"]}
    else:
        raise DeserializationError("APISchema: no recognized variant key")
