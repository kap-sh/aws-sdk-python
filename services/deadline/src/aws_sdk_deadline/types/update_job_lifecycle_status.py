"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateJobLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

UpdateJobLifecycleStatus: TypeAlias = Literal["ARCHIVED",]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJobLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> UpdateJobLifecycleStatus:
    return cast(UpdateJobLifecycleStatus, data)
