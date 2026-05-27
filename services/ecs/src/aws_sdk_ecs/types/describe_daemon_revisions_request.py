"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonRevisionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string_list


class DescribeDaemonRevisionsRequest(TypedDict):
    daemon_revision_arns: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The ARN of the daemon revisions to describe. You can specify up to 20 ARNs.</p>"""
