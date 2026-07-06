"""Generated from Smithy shape ``com.amazonaws.securityhub#ListStandardsControlAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.non_empty_string


class ListStandardsControlAssociationsRequest(TypedDict, closed=True):
    security_control_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The identifier of the control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) that you want to determine the enablement status of in each enabled standard. </p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p> Optional pagination parameter. </p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p> An optional parameter that limits the total results of the API response to the specified number. If this parameter isn't provided in the request, the results include the first 25 standard and control associations. The results also include a <code>NextToken</code> parameter that you can use in a subsequent API call to get the next 25 associations. This repeats until all associations for the specified control are returned. The number of results is limited by the number of supported Security Hub CSPM standards that you've enabled in the calling account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStandardsControlAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStandardsControlAssociationsRequest:
    out: ListStandardsControlAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
