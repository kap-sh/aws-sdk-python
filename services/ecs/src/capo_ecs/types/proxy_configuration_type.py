"""Generated from Smithy shape ``com.amazonaws.ecs#ProxyConfigurationType``."""

from typing import Literal, TypeAlias, cast

ProxyConfigurationType: TypeAlias = Literal["APPMESH",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProxyConfigurationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProxyConfigurationType:
    return cast(ProxyConfigurationType, data)
