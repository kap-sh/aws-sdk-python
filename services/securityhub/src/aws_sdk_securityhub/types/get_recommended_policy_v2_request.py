"""Generated from Smithy shape ``com.amazonaws.securityhub#GetRecommendedPolicyV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.non_empty_string


class GetRecommendedPolicyV2Request(TypedDict):
    metadata_uid: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The unique identifier (ID) of Security Hub OCSF findings found under the <code>metadata.uid</code> field of the finding.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token used to paginate the <code>RecommendationSteps</code> list returned. On your first call to <code>GetRecommendedPolicyV2</code>, omit this parameter or set it to <code>NULL</code>. For subsequent calls, use the <code>NextToken</code> value returned in the previous response to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of recommendation steps to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendedPolicyV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommendedPolicyV2Request:
    out: GetRecommendedPolicyV2Request = {}  # type: ignore[typeddict-item]
    return out
