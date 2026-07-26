"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SalesforceAuthType``."""

from typing import Literal, TypeAlias, cast

SalesforceAuthType: TypeAlias = Literal["OAUTH2_CLIENT_CREDENTIALS",]


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceAuthType) -> str:
    return value


def deserialize_json(data: str) -> SalesforceAuthType:
    return cast(SalesforceAuthType, data)
