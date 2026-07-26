"""Generated from Smithy shape ``com.amazonaws.opensearch#RollbackOnDisable``."""

from typing import Literal, TypeAlias, cast

"""<p>The rollback state while disabling Auto-Tune for the domain.</p>"""
RollbackOnDisable: TypeAlias = Literal[
    "NO_ROLLBACK",
    "DEFAULT_ROLLBACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: RollbackOnDisable) -> str:
    return value


def deserialize_json(data: str) -> RollbackOnDisable:
    return cast(RollbackOnDisable, data)
