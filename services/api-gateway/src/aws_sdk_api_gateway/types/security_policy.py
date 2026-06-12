"""Generated from Smithy shape ``com.amazonaws.apigateway#SecurityPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

SecurityPolicy: TypeAlias = Literal[
    "TLS_1_0",
    "TLS_1_2",
    "SecurityPolicy_TLS13_1_3_2025_09",
    "SecurityPolicy_TLS13_1_3_FIPS_2025_09",
    "SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09",
    "SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09",
    "SecurityPolicy_TLS13_1_2_FIPS_PFS_PQ_2025_09",
    "SecurityPolicy_TLS13_1_2_PQ_2025_09",
    "SecurityPolicy_TLS13_1_2_2021_06",
    "SecurityPolicy_TLS13_2025_EDGE",
    "SecurityPolicy_TLS12_PFS_2025_EDGE",
    "SecurityPolicy_TLS12_2018_EDGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TLS_1_0",
        "TLS_1_2",
        "SecurityPolicy_TLS13_1_3_2025_09",
        "SecurityPolicy_TLS13_1_3_FIPS_2025_09",
        "SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09",
        "SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09",
        "SecurityPolicy_TLS13_1_2_FIPS_PFS_PQ_2025_09",
        "SecurityPolicy_TLS13_1_2_PQ_2025_09",
        "SecurityPolicy_TLS13_1_2_2021_06",
        "SecurityPolicy_TLS13_2025_EDGE",
        "SecurityPolicy_TLS12_PFS_2025_EDGE",
        "SecurityPolicy_TLS12_2018_EDGE",
    )
)


def serialize_json(value: SecurityPolicy) -> str:
    return value


def deserialize_json(data: str) -> SecurityPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SecurityPolicy value: {data!r}")
    return cast(SecurityPolicy, data)
