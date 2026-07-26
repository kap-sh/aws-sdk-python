"""Generated from Smithy shape ``com.amazonaws.omics#VersionOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_omics.types.tsv_version_options


class _VersionOptions_tsvVersionOptions(TypedDict, closed=True):
    tsvVersionOptions: "capo_omics.types.tsv_version_options.TsvVersionOptions"


VersionOptions: TypeAlias = _VersionOptions_tsvVersionOptions


# --- restJson1 ser/de ---
def serialize_json(value: VersionOptions) -> dict:
    if "tsvVersionOptions" in value:
        import capo_omics.types.tsv_version_options

        return {
            "tsvVersionOptions": capo_omics.types.tsv_version_options.serialize_json(
                value["tsvVersionOptions"]
            )
        }
    else:
        raise SerializationError("VersionOptions: no variant present")


def deserialize_json(data: dict) -> VersionOptions:
    if "tsvVersionOptions" in data:
        import capo_omics.types.tsv_version_options

        return {
            "tsvVersionOptions": capo_omics.types.tsv_version_options.deserialize_json(
                data["tsvVersionOptions"]
            )
        }
    else:
        raise DeserializationError("VersionOptions: no recognized variant key")
