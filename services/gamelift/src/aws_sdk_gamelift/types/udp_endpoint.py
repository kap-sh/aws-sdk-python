"""Generated from Smithy shape ``com.amazonaws.gamelift#UDPEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.positive_integer


class UDPEndpoint(TypedDict):
    domain: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>The domain name of the UDP endpoint.</p>"""
    port: NotRequired["aws_sdk_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The port number of the UDP endpoint. For Amazon GameLift Servers ping beacons, this is typically port 7770.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UDPEndpoint) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "port" in value:
        out["Port"] = value["port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UDPEndpoint:
    out: UDPEndpoint = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "Port" in data:
        out["port"] = data["Port"]
    return out
