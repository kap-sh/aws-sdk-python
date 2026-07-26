"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetStorageConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.storage_configuration


class GetStorageConfigurationResponse(TypedDict, closed=True):
    storage_configuration: NotRequired[
        "capo_ivs_realtime.types.storage_configuration.StorageConfiguration"
    ]
    """<p>The StorageConfiguration that was returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStorageConfigurationResponse) -> dict:
    out: dict = {}
    if "storage_configuration" in value:
        import capo_ivs_realtime.types.storage_configuration

        out["storageConfiguration"] = (
            capo_ivs_realtime.types.storage_configuration.serialize_json(
                value["storage_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetStorageConfigurationResponse:
    out: GetStorageConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "storageConfiguration" in data:
        import capo_ivs_realtime.types.storage_configuration

        out["storage_configuration"] = (
            capo_ivs_realtime.types.storage_configuration.deserialize_json(
                data["storageConfiguration"]
            )
        )
    return out
