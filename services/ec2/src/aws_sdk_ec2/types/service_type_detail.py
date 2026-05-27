"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceTypeDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_type


class ServiceTypeDetail(TypedDict):
    service_type: NotRequired["aws_sdk_ec2.types.service_type.ServiceType"]
    """<p>The type of service.</p>"""
