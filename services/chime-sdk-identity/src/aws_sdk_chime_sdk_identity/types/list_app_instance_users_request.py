"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceUsersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.max_results
    import aws_sdk_chime_sdk_identity.types.next_token


class ListAppInstanceUsersRequest(TypedDict):
    app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code>.</p>"""
    max_results: NotRequired["aws_sdk_chime_sdk_identity.types.max_results.MaxResults"]
    """<p>The maximum number of requests that you want returned.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested users are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceUsersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppInstanceUsersRequest:
    out: ListAppInstanceUsersRequest = {}  # type: ignore[typeddict-item]
    return out
