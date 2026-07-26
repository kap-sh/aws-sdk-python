"""Generated from Smithy shape ``com.amazonaws.opensearch#AWSServicePrincipal``."""

from typing import Literal, TypeAlias, cast

AWSServicePrincipal: TypeAlias = Literal["application.opensearchservice.amazonaws.com",]


# --- restJson1 ser/de ---
def serialize_json(value: AWSServicePrincipal) -> str:
    return value


def deserialize_json(data: str) -> AWSServicePrincipal:
    return cast(AWSServicePrincipal, data)
