"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseContentType``."""

from typing import Literal, TypeAlias, cast

ResponseContentType: TypeAlias = Literal[
    "TEXT_PLAIN",
    "TEXT_HTML",
    "APPLICATION_JSON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResponseContentType:
    return cast(ResponseContentType, data)
