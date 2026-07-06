"""Generated from Smithy shape ``com.amazonaws.geoplaces#BusinessChain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.sensitive_string


class BusinessChain(TypedDict, closed=True):
    name: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The business chain name.</p>"""
    id: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The Business Chain Id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BusinessChain) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> BusinessChain:
    out: BusinessChain = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
