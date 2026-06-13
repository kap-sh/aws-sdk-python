"""Generated from Smithy shape ``com.amazonaws.qbusiness#RetrieverConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.kendra_index_configuration
    import aws_sdk_qbusiness.types.native_index_configuration


class _RetrieverConfiguration_nativeIndexConfiguration(TypedDict):
    nativeIndexConfiguration: (
        "aws_sdk_qbusiness.types.native_index_configuration.NativeIndexConfiguration"
    )


class _RetrieverConfiguration_kendraIndexConfiguration(TypedDict):
    kendraIndexConfiguration: (
        "aws_sdk_qbusiness.types.kendra_index_configuration.KendraIndexConfiguration"
    )


RetrieverConfiguration: TypeAlias = (
    _RetrieverConfiguration_nativeIndexConfiguration
    | _RetrieverConfiguration_kendraIndexConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrieverConfiguration) -> dict:
    if "nativeIndexConfiguration" in value:
        import aws_sdk_qbusiness.types.native_index_configuration

        return {
            "nativeIndexConfiguration": aws_sdk_qbusiness.types.native_index_configuration.serialize_json(
                value["nativeIndexConfiguration"]
            )
        }
    elif "kendraIndexConfiguration" in value:
        import aws_sdk_qbusiness.types.kendra_index_configuration

        return {
            "kendraIndexConfiguration": aws_sdk_qbusiness.types.kendra_index_configuration.serialize_json(
                value["kendraIndexConfiguration"]
            )
        }
    else:
        raise SerializationError("RetrieverConfiguration: no variant present")


def deserialize_json(data: dict) -> RetrieverConfiguration:
    if "nativeIndexConfiguration" in data:
        import aws_sdk_qbusiness.types.native_index_configuration

        return {
            "nativeIndexConfiguration": aws_sdk_qbusiness.types.native_index_configuration.deserialize_json(
                data["nativeIndexConfiguration"]
            )
        }
    elif "kendraIndexConfiguration" in data:
        import aws_sdk_qbusiness.types.kendra_index_configuration

        return {
            "kendraIndexConfiguration": aws_sdk_qbusiness.types.kendra_index_configuration.deserialize_json(
                data["kendraIndexConfiguration"]
            )
        }
    else:
        raise DeserializationError("RetrieverConfiguration: no recognized variant key")
