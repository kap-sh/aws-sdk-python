"""Generated from Smithy shape ``com.amazonaws.ec2#AddIpamOperatingRegion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class AddIpamOperatingRegion(TypedDict, closed=True):
    region_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the operating Region.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddIpamOperatingRegion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "region_name" in value:
        pairs.append((f"{prefix}.RegionName", str(value["region_name"])))


def deserialize_ec2_query(el: Element) -> AddIpamOperatingRegion:
    out: AddIpamOperatingRegion = {}  # type: ignore[typeddict-item]
    child_region_name = el.find("RegionName")
    if child_region_name is not None:
        out["region_name"] = str(child_region_name.text or "")
    return out
