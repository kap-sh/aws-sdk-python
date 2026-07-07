"""Generated from Smithy shape ``com.amazonaws.directconnect#RouteFilterPrefix``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.cidr


class RouteFilterPrefix(TypedDict, closed=True):
    cidr: NotRequired["aws_sdk_direct_connect.types.cidr.CIDR"]
    """<p>The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouteFilterPrefix) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RouteFilterPrefix:
    out: RouteFilterPrefix = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    return out
