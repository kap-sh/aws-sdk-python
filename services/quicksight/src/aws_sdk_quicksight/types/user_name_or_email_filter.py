"""Generated from Smithy shape ``com.amazonaws.quicksight#UserNameOrEmailFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filter_value


class UserNameOrEmailFilter(TypedDict):
    prefix: "aws_sdk_quicksight.types.filter_value.FilterValue"
    """<p>The prefix to match against username or email (starts-with match).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserNameOrEmailFilter) -> dict:
    out: dict = {}
    out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> UserNameOrEmailFilter:
    out: UserNameOrEmailFilter = {}  # type: ignore[typeddict-item]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    else:
        raise DeserializationError("UserNameOrEmailFilter.prefix required")
    return out
