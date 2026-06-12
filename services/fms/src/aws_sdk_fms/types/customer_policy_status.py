"""Generated from Smithy shape ``com.amazonaws.fms#CustomerPolicyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

CustomerPolicyStatus: TypeAlias = Literal[
    "ACTIVE",
    "OUT_OF_ADMIN_SCOPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "OUT_OF_ADMIN_SCOPE",
    )
)


def serialize_aws_json_1_1(value: CustomerPolicyStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomerPolicyStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomerPolicyStatus value: {data!r}")
    return cast(CustomerPolicyStatus, data)
