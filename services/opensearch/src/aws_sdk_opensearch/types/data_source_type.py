"""Generated from Smithy shape ``com.amazonaws.opensearch#DataSourceType``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_opensearch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.s3_glue_data_catalog


class _DataSourceType_S3GlueDataCatalog(TypedDict):
    S3GlueDataCatalog: "aws_sdk_opensearch.types.s3_glue_data_catalog.S3GlueDataCatalog"


DataSourceType: TypeAlias = _DataSourceType_S3GlueDataCatalog


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceType) -> dict:
    if "S3GlueDataCatalog" in value:
        import aws_sdk_opensearch.types.s3_glue_data_catalog

        return {
            "S3GlueDataCatalog": aws_sdk_opensearch.types.s3_glue_data_catalog.serialize_json(
                value["S3GlueDataCatalog"]
            )
        }
    else:
        raise SerializationError("DataSourceType: no variant present")


def deserialize_json(data: dict) -> DataSourceType:
    if "S3GlueDataCatalog" in data:
        import aws_sdk_opensearch.types.s3_glue_data_catalog

        return {
            "S3GlueDataCatalog": aws_sdk_opensearch.types.s3_glue_data_catalog.deserialize_json(
                data["S3GlueDataCatalog"]
            )
        }
    else:
        raise DeserializationError("DataSourceType: no recognized variant key")
