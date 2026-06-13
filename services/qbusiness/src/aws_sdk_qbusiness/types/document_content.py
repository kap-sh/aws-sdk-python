"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentContent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.s3


class _DocumentContent_blob(TypedDict):
    blob: "bytes"


class _DocumentContent_s3(TypedDict):
    s3: "aws_sdk_qbusiness.types.s3.S3"


DocumentContent: TypeAlias = _DocumentContent_blob | _DocumentContent_s3


# --- restJson1 ser/de ---
def serialize_json(value: DocumentContent) -> dict:
    if "blob" in value:
        import aws_sdk_qbusiness.types._prelude.blob

        return {
            "blob": aws_sdk_qbusiness.types._prelude.blob.serialize_json(value["blob"])
        }
    elif "s3" in value:
        import aws_sdk_qbusiness.types.s3

        return {"s3": aws_sdk_qbusiness.types.s3.serialize_json(value["s3"])}
    else:
        raise SerializationError("DocumentContent: no variant present")


def deserialize_json(data: dict) -> DocumentContent:
    if "blob" in data:
        import aws_sdk_qbusiness.types._prelude.blob

        return {
            "blob": aws_sdk_qbusiness.types._prelude.blob.deserialize_json(data["blob"])
        }
    elif "s3" in data:
        import aws_sdk_qbusiness.types.s3

        return {"s3": aws_sdk_qbusiness.types.s3.deserialize_json(data["s3"])}
    else:
        raise DeserializationError("DocumentContent: no recognized variant key")
