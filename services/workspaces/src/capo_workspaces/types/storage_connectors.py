"""Generated from Smithy shape ``com.amazonaws.workspaces#StorageConnectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.storage_connector

StorageConnectors: TypeAlias = list[
    "capo_workspaces.types.storage_connector.StorageConnector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageConnectors) -> list:
    import capo_workspaces.types.storage_connector

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.storage_connector.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StorageConnectors:
    import capo_workspaces.types.storage_connector

    out: StorageConnectors = []
    for item in data:
        out.append(
            capo_workspaces.types.storage_connector.deserialize_aws_json_1_1(item)
        )
    return out
