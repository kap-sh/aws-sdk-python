"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointConfigSortKey``."""

from typing import Literal, TypeAlias, cast

EndpointConfigSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointConfigSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointConfigSortKey:
    return cast(EndpointConfigSortKey, data)
