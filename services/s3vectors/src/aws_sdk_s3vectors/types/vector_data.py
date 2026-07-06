"""Generated from Smithy shape ``com.amazonaws.s3vectors#VectorData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_s3vectors.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.float32_vector_data


class _VectorData_float32(TypedDict, closed=True):
    float32: "aws_sdk_s3vectors.types.float32_vector_data.Float32VectorData"


VectorData: TypeAlias = _VectorData_float32


# --- restJson1 ser/de ---
def serialize_json(value: VectorData) -> dict:
    if "float32" in value:
        import aws_sdk_s3vectors.types.float32_vector_data

        return {
            "float32": aws_sdk_s3vectors.types.float32_vector_data.serialize_json(
                value["float32"]
            )
        }
    else:
        raise SerializationError("VectorData: no variant present")


def deserialize_json(data: dict) -> VectorData:
    if "float32" in data:
        import aws_sdk_s3vectors.types.float32_vector_data

        return {
            "float32": aws_sdk_s3vectors.types.float32_vector_data.deserialize_json(
                data["float32"]
            )
        }
    else:
        raise DeserializationError("VectorData: no recognized variant key")
