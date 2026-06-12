"""Generated from Smithy shape ``com.amazonaws.s3control#ListMultiRegionAccessPointsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.max_results
    import aws_sdk_s3_control.types.non_empty_max_length1024_string


class ListMultiRegionAccessPointsRequest(TypedDict):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>"""
    next_token: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p>Not currently used. Do not use this parameter.</p>"""
    max_results: "aws_sdk_s3_control.types.max_results.MaxResults"
    """<p>Not currently used. Do not use this parameter.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListMultiRegionAccessPointsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListMultiRegionAccessPointsRequest:
    out: ListMultiRegionAccessPointsRequest = {}  # type: ignore[typeddict-item]
    return out
