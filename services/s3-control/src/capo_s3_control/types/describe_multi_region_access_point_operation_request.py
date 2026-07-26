"""Generated from Smithy shape ``com.amazonaws.s3control#DescribeMultiRegionAccessPointOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.async_request_token_arn


class DescribeMultiRegionAccessPointOperationRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>"""
    request_token_arn: (
        "capo_s3_control.types.async_request_token_arn.AsyncRequestTokenARN"
    )
    """<p>The request token associated with the request you want to know about. This request token is returned as part of the response when you make an asynchronous request. You provide this token to query about the status of the asynchronous action.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DescribeMultiRegionAccessPointOperationRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DescribeMultiRegionAccessPointOperationRequest:
    out: DescribeMultiRegionAccessPointOperationRequest = {}  # type: ignore[typeddict-item]
    return out
