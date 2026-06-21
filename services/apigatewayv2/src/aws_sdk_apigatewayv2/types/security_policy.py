"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#SecurityPolicy``."""

from typing import Literal, TypeAlias, cast

"""<p>The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.</p>"""
SecurityPolicy: TypeAlias = Literal[
    "TLS_1_0",
    "TLS_1_2",
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityPolicy) -> str:
    return value


def deserialize_json(data: str) -> SecurityPolicy:
    return cast(SecurityPolicy, data)
