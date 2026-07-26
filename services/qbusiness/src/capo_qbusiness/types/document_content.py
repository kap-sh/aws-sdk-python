"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.s3


class _DocumentContent_blob(TypedDict, closed=True):
    blob: "bytes"


class _DocumentContent_s3(TypedDict, closed=True):
    s3: "capo_qbusiness.types.s3.S3"


DocumentContent: TypeAlias = _DocumentContent_blob | _DocumentContent_s3


# --- restJson1 ser/de ---
def serialize_json(value: DocumentContent) -> dict:
    if "blob" in value:
        import capo_qbusiness.types._prelude.blob

        return {
            "blob": capo_qbusiness.types._prelude.blob.serialize_json(value["blob"])
        }
    elif "s3" in value:
        import capo_qbusiness.types.s3

        return {"s3": capo_qbusiness.types.s3.serialize_json(value["s3"])}
    else:
        raise SerializationError("DocumentContent: no variant present")


def deserialize_json(data: dict) -> DocumentContent:
    if "blob" in data:
        import capo_qbusiness.types._prelude.blob

        return {
            "blob": capo_qbusiness.types._prelude.blob.deserialize_json(data["blob"])
        }
    elif "s3" in data:
        import capo_qbusiness.types.s3

        return {"s3": capo_qbusiness.types.s3.deserialize_json(data["s3"])}
    else:
        raise DeserializationError("DocumentContent: no recognized variant key")
