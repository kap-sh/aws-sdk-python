"""Generated from Smithy shape ``com.amazonaws.datazone#ListEnvironmentActionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token


class ListEnvironmentActionsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the environment actions are listed.</p>"""
    environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the envrironment whose environment actions are listed.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of environment actions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environment actions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentActions</code> to list the next set of environment actions.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of environment actions to return in a single call to <code>ListEnvironmentActions</code>. When the number of environment actions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentActions</code> to list the next set of environment actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentActionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnvironmentActionsInput:
    out: ListEnvironmentActionsInput = {}  # type: ignore[typeddict-item]
    return out
