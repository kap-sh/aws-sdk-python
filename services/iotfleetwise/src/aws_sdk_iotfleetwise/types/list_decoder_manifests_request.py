"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListDecoderManifestsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.list_response_scope
    import aws_sdk_iotfleetwise.types.max_results
    import aws_sdk_iotfleetwise.types.next_token


class ListDecoderManifestsRequest(TypedDict, closed=True):
    model_manifest_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p> The Amazon Resource Name (ARN) of a vehicle model (model manifest) associated with the decoder manifest. </p>"""
    next_token: NotRequired["aws_sdk_iotfleetwise.types.next_token.nextToken"]
    """<p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>"""
    max_results: NotRequired["aws_sdk_iotfleetwise.types.max_results.maxResults"]
    """<p>The maximum number of items to return, between 1 and 100, inclusive.</p>"""
    list_response_scope: NotRequired[
        "aws_sdk_iotfleetwise.types.list_response_scope.ListResponseScope"
    ]
    """<p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: decoder manifest name, Amazon Resource Name (ARN), creation time, and last modification time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDecoderManifestsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDecoderManifestsRequest:
    out: ListDecoderManifestsRequest = {}  # type: ignore[typeddict-item]
    return out
