"""Generated from Smithy shape ``com.amazonaws.elementalinference#DictionaryStatus``."""

from typing import Literal, TypeAlias, cast

DictionaryStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "REFERENCED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DictionaryStatus) -> str:
    return value


def deserialize_json(data: str) -> DictionaryStatus:
    return cast(DictionaryStatus, data)
