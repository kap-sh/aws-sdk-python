"""Generated from Smithy shape ``com.amazonaws.lightsail#ResourceLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.region_name
    import capo_lightsail.types.string


class ResourceLocation(TypedDict, closed=True):
    availability_zone: NotRequired["capo_lightsail.types.string.string"]
    """<p>The Availability Zone. Follows the format <code>us-east-2a</code> (case-sensitive).</p>"""
    region_name: NotRequired["capo_lightsail.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceLocation) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "region_name" in value:
        import capo_lightsail.types.region_name

        out["regionName"] = capo_lightsail.types.region_name.serialize_aws_json_1_1(
            value["region_name"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceLocation:
    out: ResourceLocation = {}  # type: ignore[typeddict-item]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "regionName" in data:
        import capo_lightsail.types.region_name

        out["region_name"] = capo_lightsail.types.region_name.deserialize_aws_json_1_1(
            data["regionName"]
        )
    return out
