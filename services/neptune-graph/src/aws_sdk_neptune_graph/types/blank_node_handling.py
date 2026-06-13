"""Generated from Smithy shape ``com.amazonaws.neptunegraph#BlankNodeHandling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

BlankNodeHandling: TypeAlias = Literal["convertToIri",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("convertToIri",))


def serialize_json(value: BlankNodeHandling) -> str:
    return value


def deserialize_json(data: str) -> BlankNodeHandling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlankNodeHandling value: {data!r}")
    return cast(BlankNodeHandling, data)
