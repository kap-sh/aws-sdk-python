"""Generated from Smithy shape ``com.amazonaws.xray#InstanceIdDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.string


class InstanceIdDetail(TypedDict, closed=True):
    id: NotRequired["capo_xray.types.string.String"]
    """<p>The ID of a corresponding EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceIdDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> InstanceIdDetail:
    out: InstanceIdDetail = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
