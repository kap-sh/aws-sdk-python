"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProfileDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_profile

ConnectorProfileDetailList: TypeAlias = list[
    "aws_sdk_appflow.types.connector_profile.ConnectorProfile"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProfileDetailList) -> list:
    import aws_sdk_appflow.types.connector_profile

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.connector_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorProfileDetailList:
    import aws_sdk_appflow.types.connector_profile

    out: ConnectorProfileDetailList = []
    for item in data:
        out.append(aws_sdk_appflow.types.connector_profile.deserialize_json(item))
    return out
