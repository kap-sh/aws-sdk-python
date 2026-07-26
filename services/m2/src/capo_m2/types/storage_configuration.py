"""Generated from Smithy shape ``com.amazonaws.m2#StorageConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_m2.types.efs_storage_configuration
    import capo_m2.types.fsx_storage_configuration


class _StorageConfiguration_efs(TypedDict, closed=True):
    efs: "capo_m2.types.efs_storage_configuration.EfsStorageConfiguration"


class _StorageConfiguration_fsx(TypedDict, closed=True):
    fsx: "capo_m2.types.fsx_storage_configuration.FsxStorageConfiguration"


StorageConfiguration: TypeAlias = _StorageConfiguration_efs | _StorageConfiguration_fsx


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfiguration) -> dict:
    if "efs" in value:
        import capo_m2.types.efs_storage_configuration

        return {
            "efs": capo_m2.types.efs_storage_configuration.serialize_json(value["efs"])
        }
    elif "fsx" in value:
        import capo_m2.types.fsx_storage_configuration

        return {
            "fsx": capo_m2.types.fsx_storage_configuration.serialize_json(value["fsx"])
        }
    else:
        raise SerializationError("StorageConfiguration: no variant present")


def deserialize_json(data: dict) -> StorageConfiguration:
    if "efs" in data:
        import capo_m2.types.efs_storage_configuration

        return {
            "efs": capo_m2.types.efs_storage_configuration.deserialize_json(data["efs"])
        }
    elif "fsx" in data:
        import capo_m2.types.fsx_storage_configuration

        return {
            "fsx": capo_m2.types.fsx_storage_configuration.deserialize_json(data["fsx"])
        }
    else:
        raise DeserializationError("StorageConfiguration: no recognized variant key")
