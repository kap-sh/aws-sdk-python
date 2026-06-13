"""Generated from Smithy shape ``com.amazonaws.omics#StoreOptions``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_omics.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.tsv_store_options


class _StoreOptions_tsvStoreOptions(TypedDict):
    tsvStoreOptions: "aws_sdk_omics.types.tsv_store_options.TsvStoreOptions"


StoreOptions: TypeAlias = _StoreOptions_tsvStoreOptions


# --- restJson1 ser/de ---
def serialize_json(value: StoreOptions) -> dict:
    if "tsvStoreOptions" in value:
        import aws_sdk_omics.types.tsv_store_options

        return {
            "tsvStoreOptions": aws_sdk_omics.types.tsv_store_options.serialize_json(
                value["tsvStoreOptions"]
            )
        }
    else:
        raise SerializationError("StoreOptions: no variant present")


def deserialize_json(data: dict) -> StoreOptions:
    if "tsvStoreOptions" in data:
        import aws_sdk_omics.types.tsv_store_options

        return {
            "tsvStoreOptions": aws_sdk_omics.types.tsv_store_options.deserialize_json(
                data["tsvStoreOptions"]
            )
        }
    else:
        raise DeserializationError("StoreOptions: no recognized variant key")
