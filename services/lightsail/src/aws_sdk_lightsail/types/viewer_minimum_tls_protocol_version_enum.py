"""Generated from Smithy shape ``com.amazonaws.lightsail#ViewerMinimumTlsProtocolVersionEnum``."""

from typing import Literal, TypeAlias, cast

ViewerMinimumTlsProtocolVersionEnum: TypeAlias = Literal[
    "TLSv1.1_2016",
    "TLSv1.2_2018",
    "TLSv1.2_2019",
    "TLSv1.2_2021",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewerMinimumTlsProtocolVersionEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ViewerMinimumTlsProtocolVersionEnum:
    return cast(ViewerMinimumTlsProtocolVersionEnum, data)
