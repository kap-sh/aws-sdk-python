"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DomainNameStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>The status of the domain name migration. The valid values are AVAILABLE, UPDATING, PENDING_CERTIFICATE_REIMPORT, and PENDING_OWNERSHIP_VERIFICATION. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.</p>"""
DomainNameStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UPDATING",
    "PENDING_CERTIFICATE_REIMPORT",
    "PENDING_OWNERSHIP_VERIFICATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "UPDATING",
        "PENDING_CERTIFICATE_REIMPORT",
        "PENDING_OWNERSHIP_VERIFICATION",
    )
)


def serialize_json(value: DomainNameStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainNameStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainNameStatus value: {data!r}")
    return cast(DomainNameStatus, data)
