"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateHostsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.response_host_id_list


class AllocateHostsResult(TypedDict):
    host_ids: NotRequired["aws_sdk_ec2.types.response_host_id_list.ResponseHostIdList"]
    """<p>The ID of the allocated Dedicated Host. This is used to launch an instance onto a specific host.</p>"""
