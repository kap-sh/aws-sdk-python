"""Generated from Smithy shape ``com.amazonaws.appflow#OAuth2GrantTypeSupportedList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.o_auth2_grant_type

OAuth2GrantTypeSupportedList: TypeAlias = list[
    "aws_sdk_appflow.types.o_auth2_grant_type.OAuth2GrantType"
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2GrantTypeSupportedList) -> list:
    import aws_sdk_appflow.types.o_auth2_grant_type

    out: list = []
    for item in value:
        out.append(aws_sdk_appflow.types.o_auth2_grant_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> OAuth2GrantTypeSupportedList:
    import aws_sdk_appflow.types.o_auth2_grant_type

    out: OAuth2GrantTypeSupportedList = []
    for item in data:
        out.append(aws_sdk_appflow.types.o_auth2_grant_type.deserialize_json(item))
    return out
