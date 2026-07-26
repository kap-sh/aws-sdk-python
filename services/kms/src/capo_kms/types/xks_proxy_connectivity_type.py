"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyConnectivityType``."""

from typing import Literal, TypeAlias, cast

XksProxyConnectivityType: TypeAlias = Literal[
    "PUBLIC_ENDPOINT",
    "VPC_ENDPOINT_SERVICE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XksProxyConnectivityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> XksProxyConnectivityType:
    return cast(XksProxyConnectivityType, data)
