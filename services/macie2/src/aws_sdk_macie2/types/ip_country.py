"""Generated from Smithy shape ``com.amazonaws.macie2#IpCountry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class IpCountry(TypedDict):
    code: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country that the IP address originated from. For example, US for the United States.</p>"""
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the country that the IP address originated from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpCountry) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> IpCountry:
    out: IpCountry = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "name" in data:
        out["name"] = data["name"]
    return out
