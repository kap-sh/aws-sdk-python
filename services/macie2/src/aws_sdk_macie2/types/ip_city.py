"""Generated from Smithy shape ``com.amazonaws.macie2#IpCity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class IpCity(TypedDict):
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the city.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpCity) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> IpCity:
    out: IpCity = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
