"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DomainNameStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the domain name migration. The valid values are AVAILABLE, UPDATING, PENDING_CERTIFICATE_REIMPORT, and PENDING_OWNERSHIP_VERIFICATION. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.</p>"""
DomainNameStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UPDATING",
    "PENDING_CERTIFICATE_REIMPORT",
    "PENDING_OWNERSHIP_VERIFICATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainNameStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainNameStatus:
    return cast(DomainNameStatus, data)
