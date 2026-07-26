"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.filter_name


class UpdateFilterResponse(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.filter_name.FilterName"]
    """<p>The name of the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFilterResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateFilterResponse:
    out: UpdateFilterResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
