"""Generated from Smithy shape ``com.amazonaws.mgn#OS``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.bounded_string


class OS(TypedDict):
    full_string: NotRequired["aws_sdk_mgn.types.bounded_string.BoundedString"]
    """<p>OS full string.</p>"""


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
