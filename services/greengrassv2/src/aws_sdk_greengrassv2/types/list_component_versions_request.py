"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListComponentVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_arn
    import aws_sdk_greengrassv2.types.default_max_results
    import aws_sdk_greengrassv2.types.next_token_string


class ListComponentVersionsRequest(TypedDict):
    arn: "aws_sdk_greengrassv2.types.component_arn.ComponentARN"
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component.</p>"""
    max_results: NotRequired[
        "aws_sdk_greengrassv2.types.default_max_results.DefaultMaxResults"
    ]
    """<p>The maximum number of results to be returned per paginated request.</p>"""
    next_token: NotRequired[
        "aws_sdk_greengrassv2.types.next_token_string.NextTokenString"
    ]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListComponentVersionsRequest:
    out: ListComponentVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
