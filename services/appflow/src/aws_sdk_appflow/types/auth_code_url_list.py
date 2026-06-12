"""Generated from Smithy shape ``com.amazonaws.appflow#AuthCodeUrlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.auth_code_url

AuthCodeUrlList: TypeAlias = list["aws_sdk_appflow.types.auth_code_url.AuthCodeUrl"]


# --- restJson1 ser/de ---
def serialize_json(value: AuthCodeUrlList) -> list:
    return list(value)


def deserialize_json(data: list) -> AuthCodeUrlList:
    return list(data)
