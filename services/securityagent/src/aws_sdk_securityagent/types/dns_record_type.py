"""Generated from Smithy shape ``com.amazonaws.securityagent#DNSRecordType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Type of DNS record.</p>"""
DNSRecordType: TypeAlias = Literal["TXT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TXT",))


def serialize_json(value: DNSRecordType) -> str:
    return value


def deserialize_json(data: str) -> DNSRecordType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DNSRecordType value: {data!r}")
    return cast(DNSRecordType, data)
