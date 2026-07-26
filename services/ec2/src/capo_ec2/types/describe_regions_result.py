"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRegionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.region_list


class DescribeRegionsResult(TypedDict, closed=True):
    regions: NotRequired["capo_ec2.types.region_list.RegionList"]
    """<p>Information about the Regions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeRegionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "regions" in value:
        import capo_ec2.types.region_list

        capo_ec2.types.region_list.serialize_ec2_query(
            value["regions"], pairs, f"{prefix}.RegionInfo"
        )


def deserialize_ec2_query(el: Element) -> DescribeRegionsResult:
    out: DescribeRegionsResult = {}  # type: ignore[typeddict-item]
    if el.find("RegionInfo") is not None:
        import capo_ec2.types.region_list

        out["regions"] = capo_ec2.types.region_list.deserialize_ec2_query(
            el, "RegionInfo"
        )
    return out
