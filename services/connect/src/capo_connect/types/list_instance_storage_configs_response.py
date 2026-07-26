"""Generated from Smithy shape ``com.amazonaws.connect#ListInstanceStorageConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_storage_configs
    import capo_connect.types.next_token


class ListInstanceStorageConfigsResponse(TypedDict, closed=True):
    storage_configs: NotRequired[
        "capo_connect.types.instance_storage_configs.InstanceStorageConfigs"
    ]
    """<p>A valid storage type.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstanceStorageConfigsResponse) -> dict:
    out: dict = {}
    if "storage_configs" in value:
        import capo_connect.types.instance_storage_configs

        out["StorageConfigs"] = (
            capo_connect.types.instance_storage_configs.serialize_json(
                value["storage_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInstanceStorageConfigsResponse:
    out: ListInstanceStorageConfigsResponse = {}  # type: ignore[typeddict-item]
    if "StorageConfigs" in data:
        import capo_connect.types.instance_storage_configs

        out["storage_configs"] = (
            capo_connect.types.instance_storage_configs.deserialize_json(
                data["StorageConfigs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
