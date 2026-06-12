"""Generated from Smithy shape ``com.amazonaws.sesv2#DataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The data format of a file, can be one of the following:</p> <ul> <li> <p> <code>CSV</code> – A comma-separated values file.</p> </li> <li> <p> <code>JSON</code> – A JSON file.</p> </li> </ul>"""
DataFormat: TypeAlias = Literal[
    "CSV",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "JSON",
    )
)


def serialize_json(value: DataFormat) -> str:
    return value


def deserialize_json(data: str) -> DataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataFormat value: {data!r}")
    return cast(DataFormat, data)
