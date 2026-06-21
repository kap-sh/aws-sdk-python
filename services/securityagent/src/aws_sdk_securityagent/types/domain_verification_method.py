"""Generated from Smithy shape ``com.amazonaws.securityagent#DomainVerificationMethod``."""

from typing import Literal, TypeAlias, cast

"""<p>Method used to verify domain ownership.</p>"""
DomainVerificationMethod: TypeAlias = Literal[
    "DNS_TXT",
    "HTTP_ROUTE",
    "PRIVATE_VPC",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainVerificationMethod) -> str:
    return value


def deserialize_json(data: str) -> DomainVerificationMethod:
    return cast(DomainVerificationMethod, data)
