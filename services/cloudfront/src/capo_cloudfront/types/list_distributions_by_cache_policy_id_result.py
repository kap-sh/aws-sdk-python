"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionsByCachePolicyIdResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution_id_list


class ListDistributionsByCachePolicyIdResult(TypedDict, closed=True):
    distribution_id_list: NotRequired[
        "capo_cloudfront.types.distribution_id_list.DistributionIdList"
    ]
    """<p>A list of distribution IDs.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionsByCachePolicyIdResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution_id_list" in value:
        import capo_cloudfront.types.distribution_id_list

        capo_cloudfront.types.distribution_id_list.serialize_xml(
            value["distribution_id_list"], el, "DistributionIdList"
        )


def deserialize_xml(el: Element) -> ListDistributionsByCachePolicyIdResult:
    out: ListDistributionsByCachePolicyIdResult = {}  # type: ignore[typeddict-item]
    child_distribution_id_list = el.find("DistributionIdList")
    if child_distribution_id_list is not None:
        import capo_cloudfront.types.distribution_id_list

        out["distribution_id_list"] = (
            capo_cloudfront.types.distribution_id_list.deserialize_xml(
                child_distribution_id_list
            )
        )
    return out
