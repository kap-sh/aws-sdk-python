"""Generated from Smithy shape ``com.amazonaws.sesv2#DataFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The data format of a file, can be one of the following:</p> <ul> <li> <p> <code>CSV</code> – A comma-separated values file.</p> </li> <li> <p> <code>JSON</code> – A JSON file.</p> </li> </ul>"""
DataFormat: TypeAlias = Literal[
    "CSV",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataFormat) -> str:
    return value


def deserialize_json(data: str) -> DataFormat:
    return cast(DataFormat, data)
