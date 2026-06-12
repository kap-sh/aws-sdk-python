"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.connector_property

ConnectorPropertyList: TypeAlias = list[
    "aws_sdk_glue.types.connector_property.ConnectorProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorPropertyList) -> list:
    import aws_sdk_glue.types.connector_property

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.connector_property.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectorPropertyList:
    import aws_sdk_glue.types.connector_property

    out: ConnectorPropertyList = []
    for item in data:
        out.append(aws_sdk_glue.types.connector_property.deserialize_aws_json_1_1(item))
    return out
