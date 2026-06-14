"""Generated from Smithy shape ``com.amazonaws.workspaces#Application``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

Application: TypeAlias = Literal[
    "Microsoft_Office_2016",
    "Microsoft_Office_2019",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Microsoft_Office_2016",
        "Microsoft_Office_2019",
    )
)


def serialize_aws_json_1_1(value: Application) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Application:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Application value: {data!r}")
    return cast(Application, data)
