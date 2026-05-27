"""Generated from Smithy shape ``com.amazonaws.ec2#CancelImportTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CancelImportTaskResult(TypedDict):
    import_task_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the task being canceled.</p>"""
    previous_state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the task being canceled.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the task being canceled.</p>"""
