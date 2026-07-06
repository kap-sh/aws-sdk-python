"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListStreamingDistributionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.streaming_distribution_list


class ListStreamingDistributionsResult(TypedDict, closed=True):
    streaming_distribution_list: NotRequired[
        "aws_sdk_cloudfront.types.streaming_distribution_list.StreamingDistributionList"
    ]
    """<p>The <code>StreamingDistributionList</code> type.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListStreamingDistributionsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "streaming_distribution_list" in value:
        import aws_sdk_cloudfront.types.streaming_distribution_list

        aws_sdk_cloudfront.types.streaming_distribution_list.serialize_xml(
            value["streaming_distribution_list"], el, "StreamingDistributionList"
        )


def deserialize_xml(el: Element) -> ListStreamingDistributionsResult:
    out: ListStreamingDistributionsResult = {}  # type: ignore[typeddict-item]
    child_streaming_distribution_list = el.find("StreamingDistributionList")
    if child_streaming_distribution_list is not None:
        import aws_sdk_cloudfront.types.streaming_distribution_list

        out["streaming_distribution_list"] = (
            aws_sdk_cloudfront.types.streaming_distribution_list.deserialize_xml(
                child_streaming_distribution_list
            )
        )
    return out
