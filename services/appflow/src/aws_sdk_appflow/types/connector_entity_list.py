"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_entity

ConnectorEntityList: TypeAlias = list[
    "aws_sdk_appflow.types.connector_entity.ConnectorEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorEntityList) -> list:
    import aws_sdk_appflow.types.connector_entity

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.connector_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorEntityList:
    import aws_sdk_appflow.types.connector_entity

    out: ConnectorEntityList = []
    for item in data:
        out.append(aws_sdk_appflow.types.connector_entity.deserialize_json(item))
    return out
