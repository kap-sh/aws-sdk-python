"""Generated from Smithy shape ``com.amazonaws.invoicing#ConnectionTestingMethod``."""

from typing import Literal, TypeAlias, cast

ConnectionTestingMethod: TypeAlias = Literal[
    "PROD_ENV_DOLLAR_TEST",
    "TEST_ENV_REPLAY_TEST",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionTestingMethod) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionTestingMethod:
    return cast(ConnectionTestingMethod, data)
