"""Generated from Smithy shape ``com.amazonaws.securityagent#DNSRecordType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of DNS record.</p>"""
DNSRecordType: TypeAlias = Literal["TXT",]


# --- restJson1 ser/de ---
def serialize_json(value: DNSRecordType) -> str:
    return value


def deserialize_json(data: str) -> DNSRecordType:
    return cast(DNSRecordType, data)
