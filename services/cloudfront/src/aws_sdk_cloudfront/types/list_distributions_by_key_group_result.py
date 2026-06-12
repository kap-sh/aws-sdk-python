"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionsByKeyGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_id_list


class ListDistributionsByKeyGroupResult(TypedDict):
    distribution_id_list: NotRequired[
        "aws_sdk_cloudfront.types.distribution_id_list.DistributionIdList"
    ]


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionsByKeyGroupResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution_id_list" in value:
        import aws_sdk_cloudfront.types.distribution_id_list

        aws_sdk_cloudfront.types.distribution_id_list.serialize_xml(
            value["distribution_id_list"], el, "DistributionIdList"
        )


def deserialize_xml(el: Element) -> ListDistributionsByKeyGroupResult:
    out: ListDistributionsByKeyGroupResult = {}  # type: ignore[typeddict-item]
    child_distribution_id_list = el.find("DistributionIdList")
    if child_distribution_id_list is not None:
        import aws_sdk_cloudfront.types.distribution_id_list

        out["distribution_id_list"] = (
            aws_sdk_cloudfront.types.distribution_id_list.deserialize_xml(
                child_distribution_id_list
            )
        )
    return out
