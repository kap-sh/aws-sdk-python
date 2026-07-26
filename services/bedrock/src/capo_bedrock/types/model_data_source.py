"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelDataSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.s3_data_source


class _ModelDataSource_s3DataSource(TypedDict, closed=True):
    s3DataSource: "capo_bedrock.types.s3_data_source.S3DataSource"


ModelDataSource: TypeAlias = _ModelDataSource_s3DataSource


# --- restJson1 ser/de ---
def serialize_json(value: ModelDataSource) -> dict:
    if "s3DataSource" in value:
        import capo_bedrock.types.s3_data_source

        return {
            "s3DataSource": capo_bedrock.types.s3_data_source.serialize_json(
                value["s3DataSource"]
            )
        }
    else:
        raise SerializationError("ModelDataSource: no variant present")


def deserialize_json(data: dict) -> ModelDataSource:
    if "s3DataSource" in data:
        import capo_bedrock.types.s3_data_source

        return {
            "s3DataSource": capo_bedrock.types.s3_data_source.deserialize_json(
                data["s3DataSource"]
            )
        }
    else:
        raise DeserializationError("ModelDataSource: no recognized variant key")
