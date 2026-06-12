"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#OptionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

"""<p>The state of a requested change. One of the following:</p> <ul> <li>Processing: The request change is still in-process.</li> <li>Active: The request change is processed and deployed to the Elasticsearch domain.</li> </ul>"""
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
