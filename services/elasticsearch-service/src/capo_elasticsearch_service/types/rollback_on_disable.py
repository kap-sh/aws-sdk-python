"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#RollbackOnDisable``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the rollback state while disabling Auto-Tune for the domain. Valid values are NO_ROLLBACK, DEFAULT_ROLLBACK.</p>"""
RollbackOnDisable: TypeAlias = Literal[
    "NO_ROLLBACK",
    "DEFAULT_ROLLBACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: RollbackOnDisable) -> str:
    return value


def deserialize_json(data: str) -> RollbackOnDisable:
    return cast(RollbackOnDisable, data)
