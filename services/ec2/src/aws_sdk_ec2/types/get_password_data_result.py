"""Generated from Smithy shape ``com.amazonaws.ec2#GetPasswordDataResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.password_data
    import aws_sdk_ec2.types.string


class GetPasswordDataResult(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Windows instance.</p>"""
    timestamp: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time the data was last updated.</p>"""
    password_data: NotRequired["aws_sdk_ec2.types.password_data.PasswordData"]
    """<p>The password of the instance. Returns an empty string if the password is not available.</p>"""
