"""Generated from Smithy shape ``com.amazonaws.securityhub#IpFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class IpFilter(TypedDict, closed=True):
    cidr: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A finding's CIDR value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpFilter) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["Cidr"] = value["cidr"]
    return out


def deserialize_json(data: dict) -> IpFilter:
    out: IpFilter = {}  # type: ignore[typeddict-item]
    if "Cidr" in data:
        out["cidr"] = data["Cidr"]
    return out
