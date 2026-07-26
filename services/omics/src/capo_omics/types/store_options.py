"""Generated from Smithy shape ``com.amazonaws.omics#StoreOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_omics.types.tsv_store_options


class _StoreOptions_tsvStoreOptions(TypedDict, closed=True):
    tsvStoreOptions: "capo_omics.types.tsv_store_options.TsvStoreOptions"


StoreOptions: TypeAlias = _StoreOptions_tsvStoreOptions


# --- restJson1 ser/de ---
def serialize_json(value: StoreOptions) -> dict:
    if "tsvStoreOptions" in value:
        import capo_omics.types.tsv_store_options

        return {
            "tsvStoreOptions": capo_omics.types.tsv_store_options.serialize_json(
                value["tsvStoreOptions"]
            )
        }
    else:
        raise SerializationError("StoreOptions: no variant present")


def deserialize_json(data: dict) -> StoreOptions:
    if "tsvStoreOptions" in data:
        import capo_omics.types.tsv_store_options

        return {
            "tsvStoreOptions": capo_omics.types.tsv_store_options.deserialize_json(
                data["tsvStoreOptions"]
            )
        }
    else:
        raise DeserializationError("StoreOptions: no recognized variant key")
