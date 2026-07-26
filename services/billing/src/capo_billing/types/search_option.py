"""Generated from Smithy shape ``com.amazonaws.billing#SearchOption``."""

from typing import Literal, TypeAlias, cast

SearchOption: TypeAlias = Literal["STARTS_WITH",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SearchOption:
    return cast(SearchOption, data)
