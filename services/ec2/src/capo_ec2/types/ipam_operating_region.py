"""Generated from Smithy shape ``com.amazonaws.ec2#IpamOperatingRegion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class IpamOperatingRegion(TypedDict, closed=True):
    region_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the operating Region.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamOperatingRegion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "region_name" in value:
        pairs.append((f"{key_prefix}RegionName", str(value["region_name"])))


def deserialize_ec2_query(el: Element) -> IpamOperatingRegion:
    out: IpamOperatingRegion = {}  # type: ignore[typeddict-item]
    child_region_name = el.find("regionName")
    if child_region_name is not None:
        out["region_name"] = str(child_region_name.text or "")
    return out
