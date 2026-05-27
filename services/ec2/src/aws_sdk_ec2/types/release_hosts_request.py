"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseHostsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.request_host_id_list


class ReleaseHostsRequest(TypedDict):
    host_ids: NotRequired["aws_sdk_ec2.types.request_host_id_list.RequestHostIdList"]
    """<p>The IDs of the Dedicated Hosts to release.</p>"""
