"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMetadata``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_s3tables.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.iceberg_metadata


class _TableMetadata_iceberg(TypedDict):
    iceberg: "aws_sdk_s3tables.types.iceberg_metadata.IcebergMetadata"


TableMetadata: TypeAlias = _TableMetadata_iceberg


# --- restJson1 ser/de ---
def serialize_json(value: TableMetadata) -> dict:
    if "iceberg" in value:
        import aws_sdk_s3tables.types.iceberg_metadata

        return {
            "iceberg": aws_sdk_s3tables.types.iceberg_metadata.serialize_json(
                value["iceberg"]
            )
        }
    else:
        raise SerializationError("TableMetadata: no variant present")


def deserialize_json(data: dict) -> TableMetadata:
    if "iceberg" in data:
        import aws_sdk_s3tables.types.iceberg_metadata

        return {
            "iceberg": aws_sdk_s3tables.types.iceberg_metadata.deserialize_json(
                data["iceberg"]
            )
        }
    else:
        raise DeserializationError("TableMetadata: no recognized variant key")
