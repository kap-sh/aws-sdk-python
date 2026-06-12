"""Generated from Smithy shape ``com.amazonaws.appflow#TokenUrlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.token_url

TokenUrlList: TypeAlias = list["aws_sdk_appflow.types.token_url.TokenUrl"]


# --- restJson1 ser/de ---
def serialize_json(value: TokenUrlList) -> list:
    return list(value)


def deserialize_json(data: list) -> TokenUrlList:
    return list(data)
