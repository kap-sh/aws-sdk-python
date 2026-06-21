"""Generated from Smithy shape ``com.amazonaws.devopsagent#SourceAccountType``."""

from typing import Literal, TypeAlias, cast

"""<p>AWS association type for source account.</p>"""
SourceAccountType: TypeAlias = Literal["source",]


# --- restJson1 ser/de ---
def serialize_json(value: SourceAccountType) -> str:
    return value


def deserialize_json(data: str) -> SourceAccountType:
    return cast(SourceAccountType, data)
