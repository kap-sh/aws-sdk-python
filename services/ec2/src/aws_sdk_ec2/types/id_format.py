"""Generated from Smithy shape ``com.amazonaws.ec2#IdFormat``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string


class IdFormat(TypedDict):
    deadline: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date in UTC at which you are permanently switched over to using longer IDs. If a deadline is not yet available for this resource type, this field is not returned.</p>"""
    resource: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of resource.</p>"""
    use_long_ids: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether longer IDs (17-character IDs) are enabled for the resource.</p>"""
