"""Generated from Smithy shape ``com.amazonaws.datazone#ListConnectionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.connection_name
    import aws_sdk_datazone.types.connection_scope
    import aws_sdk_datazone.types.connection_type
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.sort_field_connection
    import aws_sdk_datazone.types.sort_order


class ListConnectionsInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to list connections.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of connections to return in a single call to ListConnections. When the number of connections to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListConnections to list the next set of connections.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of connections is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of connections, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListConnections to list the next set of connections.</p>"""
    sort_by: NotRequired[
        "aws_sdk_datazone.types.sort_field_connection.SortFieldConnection"
    ]
    """<p>Specifies how you want to sort the listed connections.</p>"""
    sort_order: NotRequired["aws_sdk_datazone.types.sort_order.SortOrder"]
    """<p>Specifies the sort order for the listed connections.</p>"""
    name: NotRequired["aws_sdk_datazone.types.connection_name.ConnectionName"]
    """<p>The name of the connection.</p>"""
    environment_identifier: NotRequired[
        "aws_sdk_datazone.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the environment where you want to list connections.</p>"""
    project_identifier: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The ID of the project where you want to list connections.</p>"""
    type: NotRequired["aws_sdk_datazone.types.connection_type.ConnectionType"]
    """<p>The type of connection.</p>"""
    scope: NotRequired["aws_sdk_datazone.types.connection_scope.ConnectionScope"]
    """<p>The scope of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectionsInput:
    out: ListConnectionsInput = {}  # type: ignore[typeddict-item]
    return out
