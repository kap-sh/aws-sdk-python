"""Generated from Smithy shape ``com.amazonaws.qbusiness#APISchema``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_qbusiness.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.s3
    import aws_sdk_qbusiness.types.payload

class _APISchema_payload(TypedDict):
    payload: "aws_sdk_qbusiness.types.payload.Payload"


class _APISchema_s3(TypedDict):
    s3: "aws_sdk_qbusiness.types.s3.S3"

APISchema: TypeAlias = _APISchema_payload | _APISchema_s3

# --- restJson1 ser/de ---
def serialize_json(value: APISchema) -> dict:
    if "payload" in value:
        return {"payload": value["payload"]}
    elif "s3" in value:
        import aws_sdk_qbusiness.types.s3
        return {"s3": aws_sdk_qbusiness.types.s3.serialize_json(value["s3"])}
    else:
        raise SerializationError("APISchema: no variant present")


def deserialize_json(data: dict) -> APISchema:
    if "payload" in data:
        return {"payload": data["payload"]}
    elif "s3" in data:
        import aws_sdk_qbusiness.types.s3
        return {"s3": aws_sdk_qbusiness.types.s3.deserialize_json(data["s3"])}
    else:
        raise DeserializationError("APISchema: no recognized variant key")