"""Generated from Smithy shape ``com.amazonaws.evs#ConnectorType``."""

from typing import Literal, TypeAlias, cast

ConnectorType: TypeAlias = Literal["VCENTER",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectorType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectorType:
    return cast(ConnectorType, data)
