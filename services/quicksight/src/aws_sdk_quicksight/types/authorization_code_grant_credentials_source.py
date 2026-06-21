"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizationCodeGrantCredentialsSource``."""

from typing import Literal, TypeAlias, cast

AuthorizationCodeGrantCredentialsSource: TypeAlias = Literal["PLAIN_CREDENTIALS",]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationCodeGrantCredentialsSource) -> str:
    return value


def deserialize_json(data: str) -> AuthorizationCodeGrantCredentialsSource:
    return cast(AuthorizationCodeGrantCredentialsSource, data)
