"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePathRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.path_statement_request
    import aws_sdk_ec2.types.through_resources_statement_request_list


class AccessScopePathRequest(TypedDict):
    source: NotRequired["aws_sdk_ec2.types.path_statement_request.PathStatementRequest"]
    """<p>The source.</p>"""
    destination: NotRequired[
        "aws_sdk_ec2.types.path_statement_request.PathStatementRequest"
    ]
    """<p>The destination.</p>"""
    through_resources: NotRequired[
        "aws_sdk_ec2.types.through_resources_statement_request_list.ThroughResourcesStatementRequestList"
    ]
    """<p>The through resources.</p>"""
