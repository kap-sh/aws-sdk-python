"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceFunctionCriticality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

ServiceFunctionCriticality: TypeAlias = Literal[
    "PRIMARY",
    "SUPPLEMENTAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "SUPPLEMENTAL",
    )
)


def serialize_json(value: ServiceFunctionCriticality) -> str:
    return value


def deserialize_json(data: str) -> ServiceFunctionCriticality:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceFunctionCriticality value: {data!r}"
        )
    return cast(ServiceFunctionCriticality, data)
