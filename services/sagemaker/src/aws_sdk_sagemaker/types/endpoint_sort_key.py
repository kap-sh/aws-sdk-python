"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointSortKey``."""

from typing import Literal, TypeAlias, cast

EndpointSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointSortKey:
    return cast(EndpointSortKey, data)
