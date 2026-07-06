"""Generated from Smithy shape ``com.amazonaws.workspaces#StorageConnector``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.storage_connector_status_enum
    import aws_sdk_workspaces.types.storage_connector_type_enum


class StorageConnector(TypedDict, closed=True):
    connector_type: (
        "aws_sdk_workspaces.types.storage_connector_type_enum.StorageConnectorTypeEnum"
    )
    """<p>The type of connector used to save user files.</p>"""
    status: "aws_sdk_workspaces.types.storage_connector_status_enum.StorageConnectorStatusEnum"
    """<p>Indicates if the storage connetor is enabled or disabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageConnector) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.storage_connector_type_enum

    out["ConnectorType"] = (
        aws_sdk_workspaces.types.storage_connector_type_enum.serialize_aws_json_1_1(
            value["connector_type"]
        )
    )
    import aws_sdk_workspaces.types.storage_connector_status_enum

    out["Status"] = (
        aws_sdk_workspaces.types.storage_connector_status_enum.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StorageConnector:
    out: StorageConnector = {}  # type: ignore[typeddict-item]
    if "ConnectorType" in data:
        import aws_sdk_workspaces.types.storage_connector_type_enum

        out["connector_type"] = (
            aws_sdk_workspaces.types.storage_connector_type_enum.deserialize_aws_json_1_1(
                data["ConnectorType"]
            )
        )
    else:
        raise DeserializationError("StorageConnector.connector_type required")
    if "Status" in data:
        import aws_sdk_workspaces.types.storage_connector_status_enum

        out["status"] = (
            aws_sdk_workspaces.types.storage_connector_status_enum.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("StorageConnector.status required")
    return out
