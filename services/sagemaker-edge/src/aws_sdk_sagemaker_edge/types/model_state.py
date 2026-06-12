"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#ModelState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_edge.errors import DeserializationError

ModelState: TypeAlias = Literal[
    "DEPLOY",
    "UNDEPLOY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEPLOY",
        "UNDEPLOY",
    )
)


def serialize_json(value: ModelState) -> str:
    return value


def deserialize_json(data: str) -> ModelState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelState value: {data!r}")
    return cast(ModelState, data)
