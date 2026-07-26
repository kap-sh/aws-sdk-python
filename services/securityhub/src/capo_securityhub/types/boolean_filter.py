"""Generated from Smithy shape ``com.amazonaws.securityhub#BooleanFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean


class BooleanFilter(TypedDict, closed=True):
    value: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>The value of the boolean.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BooleanFilter) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> BooleanFilter:
    out: BooleanFilter = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
