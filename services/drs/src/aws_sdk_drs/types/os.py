"""Generated from Smithy shape ``com.amazonaws.drs#OS``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.bounded_string


class OS(TypedDict, closed=True):
    full_string: NotRequired["aws_sdk_drs.types.bounded_string.BoundedString"]
    """<p>The long name of the Operating System.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OS) -> dict:
    out: dict = {}
    if "full_string" in value:
        out["fullString"] = value["full_string"]
    return out


def deserialize_json(data: dict) -> OS:
    out: OS = {}  # type: ignore[typeddict-item]
    if "fullString" in data:
        out["full_string"] = data["fullString"]
    return out
