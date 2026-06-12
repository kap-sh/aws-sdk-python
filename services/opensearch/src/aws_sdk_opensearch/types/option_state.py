"""Generated from Smithy shape ``com.amazonaws.opensearch#OptionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The state of a requested domain configuration change. Can be one of the following:</p> <ul> <li> <p> <b>Processing</b> - The requested change is still in progress.</p> </li> <li> <p> <b>Active</b> - The requested change is processed and deployed to the domain.</p> </li> </ul>"""
OptionState: TypeAlias = Literal[
    "RequiresIndexDocuments",
    "Processing",
    "Active",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RequiresIndexDocuments",
        "Processing",
        "Active",
    )
)


def serialize_json(value: OptionState) -> str:
    return value


def deserialize_json(data: str) -> OptionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OptionState value: {data!r}")
    return cast(OptionState, data)
