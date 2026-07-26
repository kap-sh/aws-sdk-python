"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryStatus``."""

from typing import Literal, TypeAlias, cast

GlossaryStatus: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryStatus) -> str:
    return value


def deserialize_json(data: str) -> GlossaryStatus:
    return cast(GlossaryStatus, data)
