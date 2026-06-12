"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_detail

ConnectorList: TypeAlias = list[
    "aws_sdk_appflow.types.connector_detail.ConnectorDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorList) -> list:
    import aws_sdk_appflow.types.connector_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.connector_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorList:
    import aws_sdk_appflow.types.connector_detail

    out: ConnectorList = []
    for item in data:
        out.append(aws_sdk_appflow.types.connector_detail.deserialize_json(item))
    return out
