"""Generated from Smithy shape ``com.amazonaws.pinpointemail#TlsPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint_email.errors import DeserializationError

"""<p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is <code>Require</code>, messages are only delivered if a TLS connection can be established. If the value is <code>Optional</code>, messages can be delivered in plain text if a TLS connection can't be established.</p>"""
TlsPolicy: TypeAlias = Literal[
    "REQUIRE",
    "OPTIONAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRE",
        "OPTIONAL",
    )
)


def serialize_json(value: TlsPolicy) -> str:
    return value


def deserialize_json(data: str) -> TlsPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TlsPolicy value: {data!r}")
    return cast(TlsPolicy, data)
