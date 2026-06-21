"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentVersionStatus``."""

from typing import Literal, TypeAlias, cast

DocumentVersionStatus: TypeAlias = Literal["ACTIVE",]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> DocumentVersionStatus:
    return cast(DocumentVersionStatus, data)
