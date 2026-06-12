"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_type

ConnectorTypeList: TypeAlias = list[
    "aws_sdk_appflow.types.connector_type.ConnectorType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorTypeList) -> list:
    import aws_sdk_appflow.types.connector_type

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.connector_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorTypeList:
    import aws_sdk_appflow.types.connector_type

    out: ConnectorTypeList = []
    for item in data:
        out.append(aws_sdk_appflow.types.connector_type.deserialize_json(item))
    return out
