"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionsByAnycastIpListIdResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_list


class ListDistributionsByAnycastIpListIdResult(TypedDict):
    distribution_list: NotRequired[
        "aws_sdk_cloudfront.types.distribution_list.DistributionList"
    ]


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionsByAnycastIpListIdResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution_list" in value:
        import aws_sdk_cloudfront.types.distribution_list

        aws_sdk_cloudfront.types.distribution_list.serialize_xml(
            value["distribution_list"], el, "DistributionList"
        )


def deserialize_xml(el: Element) -> ListDistributionsByAnycastIpListIdResult:
    out: ListDistributionsByAnycastIpListIdResult = {}  # type: ignore[typeddict-item]
    child_distribution_list = el.find("DistributionList")
    if child_distribution_list is not None:
        import aws_sdk_cloudfront.types.distribution_list

        out["distribution_list"] = (
            aws_sdk_cloudfront.types.distribution_list.deserialize_xml(
                child_distribution_list
            )
        )
    return out
