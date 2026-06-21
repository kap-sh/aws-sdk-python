"""Generated from Smithy shape ``com.amazonaws.route53resolver#BlockResponse``."""

from typing import Literal, TypeAlias, cast

BlockResponse: TypeAlias = Literal[
    "NODATA",
    "NXDOMAIN",
    "OVERRIDE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockResponse) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlockResponse:
    return cast(BlockResponse, data)
