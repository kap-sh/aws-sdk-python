"""Generated from Smithy shape ``com.amazonaws.macie2#DataIdentifierType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of data identifier that detected a specific type of sensitive data in an S3 bucket. Possible values are:</p>"""
DataIdentifierType: TypeAlias = Literal[
    "CUSTOM",
    "MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIdentifierType) -> str:
    return value


def deserialize_json(data: str) -> DataIdentifierType:
    return cast(DataIdentifierType, data)
