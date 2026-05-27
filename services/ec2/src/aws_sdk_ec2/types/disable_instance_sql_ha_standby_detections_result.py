"""Generated from Smithy shape ``com.amazonaws.ec2#DisableInstanceSqlHaStandbyDetectionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.registered_instance_list


class DisableInstanceSqlHaStandbyDetectionsResult(TypedDict):
    instances: NotRequired[
        "aws_sdk_ec2.types.registered_instance_list.RegisteredInstanceList"
    ]
    """<p>Information about the instances that were disabled from SQL Server High Availability standby detection monitoring.</p>"""
