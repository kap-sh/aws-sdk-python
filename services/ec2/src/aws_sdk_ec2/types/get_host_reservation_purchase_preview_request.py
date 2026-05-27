"""Generated from Smithy shape ``com.amazonaws.ec2#GetHostReservationPurchasePreviewRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.request_host_id_set


class GetHostReservationPurchasePreviewRequest(TypedDict):
    host_id_set: NotRequired["aws_sdk_ec2.types.request_host_id_set.RequestHostIdSet"]
    """<p>The IDs of the Dedicated Hosts with which the reservation is associated.</p>"""
    offering_id: NotRequired["aws_sdk_ec2.types.offering_id.OfferingId"]
    """<p>The offering ID of the reservation.</p>"""
