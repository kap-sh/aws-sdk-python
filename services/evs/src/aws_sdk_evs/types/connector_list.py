"""Generated from Smithy shape ``com.amazonaws.evs#ConnectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.connector

ConnectorList: TypeAlias = list["aws_sdk_evs.types.connector.Connector"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectorList) -> list:
    import aws_sdk_evs.types.connector

    out: list = []
    for item in value:
        out.append(aws_sdk_evs.types.connector.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ConnectorList:
    import aws_sdk_evs.types.connector

    out: ConnectorList = []
    for item in data:
        out.append(aws_sdk_evs.types.connector.deserialize_aws_json_1_0(item))
    return out
