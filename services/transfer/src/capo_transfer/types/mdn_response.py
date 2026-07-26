"""Generated from Smithy shape ``com.amazonaws.transfer#MdnResponse``."""

from typing import Literal, TypeAlias, cast

MdnResponse: TypeAlias = Literal[
    "SYNC",
    "NONE",
    "ASYNC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MdnResponse) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MdnResponse:
    return cast(MdnResponse, data)
