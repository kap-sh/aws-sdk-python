"""Generated from Smithy shape ``com.amazonaws.connect#ListBotsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.lex_version
    import aws_sdk_connect.types.max_result25
    import aws_sdk_connect.types.next_token


class ListBotsRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result25.MaxResult25"]
    """<p>The maximum number of results to return per page.</p>"""
    lex_version: "aws_sdk_connect.types.lex_version.LexVersion"
    """<p>The version of Amazon Lex or Amazon Lex V2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBotsRequest:
    out: ListBotsRequest = {}  # type: ignore[typeddict-item]
    return out
