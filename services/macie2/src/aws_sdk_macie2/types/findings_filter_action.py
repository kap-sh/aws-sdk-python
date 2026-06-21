"""Generated from Smithy shape ``com.amazonaws.macie2#FindingsFilterAction``."""

from typing import Literal, TypeAlias, cast

"""<p>The action to perform on findings that match the filter criteria. To suppress (automatically archive) findings that match the criteria, set this value to ARCHIVE. Valid values are:</p>"""
FindingsFilterAction: TypeAlias = Literal[
    "ARCHIVE",
    "NOOP",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsFilterAction) -> str:
    return value


def deserialize_json(data: str) -> FindingsFilterAction:
    return cast(FindingsFilterAction, data)
