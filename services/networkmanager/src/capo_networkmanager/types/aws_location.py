"""Generated from Smithy shape ``com.amazonaws.networkmanager#AWSLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.subnet_arn


class AWSLocation(TypedDict, closed=True):
    zone: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The Zone that the device is located in. Specify the ID of an Availability Zone, Local Zone, Wavelength Zone, or an Outpost.</p>"""
    subnet_arn: NotRequired["capo_networkmanager.types.subnet_arn.SubnetArn"]
    """<p>The Amazon Resource Name (ARN) of the subnet that the device is located in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AWSLocation) -> dict:
    out: dict = {}
    if "zone" in value:
        out["Zone"] = value["zone"]
    if "subnet_arn" in value:
        out["SubnetArn"] = value["subnet_arn"]
    return out


def deserialize_json(data: dict) -> AWSLocation:
    out: AWSLocation = {}  # type: ignore[typeddict-item]
    if "Zone" in data:
        out["zone"] = data["Zone"]
    if "SubnetArn" in data:
        out["subnet_arn"] = data["SubnetArn"]
    return out
