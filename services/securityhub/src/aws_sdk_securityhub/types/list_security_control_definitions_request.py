"""Generated from Smithy shape ``com.amazonaws.securityhub#ListSecurityControlDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.non_empty_string


class ListSecurityControlDefinitionsRequest(TypedDict, closed=True):
    standards_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the standard that you want to view controls for. </p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p> Optional pagination parameter. </p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p> An optional parameter that limits the total results of the API response to the specified number. If this parameter isn't provided in the request, the results include the first 25 security controls that apply to the specified standard. The results also include a <code>NextToken</code> parameter that you can use in a subsequent API call to get the next 25 controls. This repeats until all controls for the standard are returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityControlDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSecurityControlDefinitionsRequest:
    out: ListSecurityControlDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out
