"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceTypeOption``."""

from typing import Literal, TypeAlias, cast

ServiceTypeOption: TypeAlias = Literal["HTTP",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceTypeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceTypeOption:
    return cast(ServiceTypeOption, data)
