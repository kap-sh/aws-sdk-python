"""Generated from Smithy shape ``com.amazonaws.bedrock#EndpointConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.sage_maker_endpoint


class _EndpointConfig_sageMaker(TypedDict):
    sageMaker: "aws_sdk_bedrock.types.sage_maker_endpoint.SageMakerEndpoint"


EndpointConfig: TypeAlias = _EndpointConfig_sageMaker


# --- restJson1 ser/de ---
def serialize_json(value: EndpointConfig) -> dict:
    if "sageMaker" in value:
        import aws_sdk_bedrock.types.sage_maker_endpoint

        return {
            "sageMaker": aws_sdk_bedrock.types.sage_maker_endpoint.serialize_json(
                value["sageMaker"]
            )
        }
    else:
        raise SerializationError("EndpointConfig: no variant present")


def deserialize_json(data: dict) -> EndpointConfig:
    if "sageMaker" in data:
        import aws_sdk_bedrock.types.sage_maker_endpoint

        return {
            "sageMaker": aws_sdk_bedrock.types.sage_maker_endpoint.deserialize_json(
                data["sageMaker"]
            )
        }
    else:
        raise DeserializationError("EndpointConfig: no recognized variant key")
