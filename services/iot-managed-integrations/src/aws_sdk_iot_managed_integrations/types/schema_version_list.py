"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SchemaVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.schema_version_list_item

SchemaVersionList: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.schema_version_list_item.SchemaVersionListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaVersionList) -> list:
    import aws_sdk_iot_managed_integrations.types.schema_version_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.schema_version_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SchemaVersionList:
    import aws_sdk_iot_managed_integrations.types.schema_version_list_item

    out: SchemaVersionList = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.schema_version_list_item.deserialize_json(
                item
            )
        )
    return out
