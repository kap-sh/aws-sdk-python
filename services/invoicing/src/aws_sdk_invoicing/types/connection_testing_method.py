"""Generated from Smithy shape ``com.amazonaws.invoicing#ConnectionTestingMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

ConnectionTestingMethod: TypeAlias = Literal[
    "PROD_ENV_DOLLAR_TEST",
    "TEST_ENV_REPLAY_TEST",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROD_ENV_DOLLAR_TEST",
        "TEST_ENV_REPLAY_TEST",
    )
)


def serialize_aws_json_1_0(value: ConnectionTestingMethod) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionTestingMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionTestingMethod value: {data!r}")
    return cast(ConnectionTestingMethod, data)
