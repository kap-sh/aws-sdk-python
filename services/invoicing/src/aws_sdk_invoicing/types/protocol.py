"""Generated from Smithy shape ``com.amazonaws.invoicing#Protocol``."""

from typing import Literal, TypeAlias, cast

Protocol: TypeAlias = Literal["CXML",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Protocol) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Protocol:
    return cast(Protocol, data)
