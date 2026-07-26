"""Generated from Smithy shape ``com.amazonaws.odb#NetServicesArchitecture``."""

from typing import Literal, TypeAlias, cast

NetServicesArchitecture: TypeAlias = Literal[
    "DEDICATED",
    "SHARED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetServicesArchitecture) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NetServicesArchitecture:
    return cast(NetServicesArchitecture, data)
