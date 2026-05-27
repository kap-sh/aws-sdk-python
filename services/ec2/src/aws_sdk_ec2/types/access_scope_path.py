"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePath``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.path_statement
    import aws_sdk_ec2.types.through_resources_statement_list


class AccessScopePath(TypedDict):
    source: NotRequired["aws_sdk_ec2.types.path_statement.PathStatement"]
    """<p>The source.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.path_statement.PathStatement"]
    """<p>The destination.</p>"""
    through_resources: NotRequired[
        "aws_sdk_ec2.types.through_resources_statement_list.ThroughResourcesStatementList"
    ]
    """<p>The through resources.</p>"""
