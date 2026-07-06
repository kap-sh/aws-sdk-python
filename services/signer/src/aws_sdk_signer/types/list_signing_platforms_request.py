"""Generated from Smithy shape ``com.amazonaws.signer#ListSigningPlatformsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.max_results
    import aws_sdk_signer.types.string


class ListSigningPlatformsRequest(TypedDict, closed=True):
    category: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>The category type of a signing platform.</p>"""
    partner: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>Any partner entities connected to a signing platform.</p>"""
    target: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>The validation template that is used by the target signing platform.</p>"""
    max_results: NotRequired["aws_sdk_signer.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned by this operation.</p>"""
    next_token: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of <code>nextToken</code> from the response that you just received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSigningPlatformsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSigningPlatformsRequest:
    out: ListSigningPlatformsRequest = {}  # type: ignore[typeddict-item]
    return out
