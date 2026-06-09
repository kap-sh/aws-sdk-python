"""Generated from Smithy shape ``com.amazonaws.ec2#GetHostReservationPurchasePreviewRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.request_host_id_set


class GetHostReservationPurchasePreviewRequest(TypedDict):
    host_id_set: NotRequired["aws_sdk_ec2.types.request_host_id_set.RequestHostIdSet"]
    """<p>The IDs of the Dedicated Hosts with which the reservation is associated.</p>"""
    offering_id: NotRequired["aws_sdk_ec2.types.offering_id.OfferingId"]
    """<p>The offering ID of the reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetHostReservationPurchasePreviewRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "host_id_set" in value:
        import aws_sdk_ec2.types.request_host_id_set

        aws_sdk_ec2.types.request_host_id_set.serialize_ec2_query(
            value["host_id_set"], pairs, f"{prefix}.HostIdSet"
        )
    if "offering_id" in value:
        pairs.append((f"{prefix}.OfferingId", str(value["offering_id"])))


def deserialize_ec2_query(el: Element) -> GetHostReservationPurchasePreviewRequest:
    out: GetHostReservationPurchasePreviewRequest = {}  # type: ignore[typeddict-item]
    if el.find("HostIdSet") is not None:
        import aws_sdk_ec2.types.request_host_id_set

        out["host_id_set"] = (
            aws_sdk_ec2.types.request_host_id_set.deserialize_ec2_query(el, "HostIdSet")
        )
    child_offering_id = el.find("OfferingId")
    if child_offering_id is not None:
        out["offering_id"] = str(child_offering_id.text or "")
    return out
