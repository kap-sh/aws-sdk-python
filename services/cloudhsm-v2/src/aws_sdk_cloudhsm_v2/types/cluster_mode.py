"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ClusterMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudhsm_v2.errors import DeserializationError

ClusterMode: TypeAlias = Literal[
    "FIPS",
    "NON_FIPS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIPS",
        "NON_FIPS",
    )
)


def serialize_aws_json_1_1(value: ClusterMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterMode value: {data!r}")
    return cast(ClusterMode, data)
