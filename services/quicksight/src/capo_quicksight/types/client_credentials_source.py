"""Generated from Smithy shape ``com.amazonaws.quicksight#ClientCredentialsSource``."""

from typing import Literal, TypeAlias, cast

ClientCredentialsSource: TypeAlias = Literal["PLAIN_CREDENTIALS",]


# --- restJson1 ser/de ---
def serialize_json(value: ClientCredentialsSource) -> str:
    return value


def deserialize_json(data: str) -> ClientCredentialsSource:
    return cast(ClientCredentialsSource, data)
