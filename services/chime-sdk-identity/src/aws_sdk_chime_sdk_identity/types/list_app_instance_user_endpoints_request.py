"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceUserEndpointsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.max_results
    import aws_sdk_chime_sdk_identity.types.next_token
    import aws_sdk_chime_sdk_identity.types.sensitive_chime_arn


class ListAppInstanceUserEndpointsRequest(TypedDict):
    app_instance_user_arn: (
        "aws_sdk_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn"
    )
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    max_results: NotRequired["aws_sdk_chime_sdk_identity.types.max_results.MaxResults"]
    """<p>The maximum number of endpoints that you want to return.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested endpoints are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceUserEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppInstanceUserEndpointsRequest:
    out: ListAppInstanceUserEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
