"""Generated from Smithy shape ``com.amazonaws.ec2#CancelledSpotInstanceRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cancelled_spot_instance_request

CancelledSpotInstanceRequestList: TypeAlias = list[
    "capo_ec2.types.cancelled_spot_instance_request.CancelledSpotInstanceRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelledSpotInstanceRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.cancelled_spot_instance_request

        capo_ec2.types.cancelled_spot_instance_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CancelledSpotInstanceRequestList:
    import capo_ec2.types.cancelled_spot_instance_request

    out: CancelledSpotInstanceRequestList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.cancelled_spot_instance_request.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CancelledSpotInstanceRequestList:
    import capo_ec2.types.cancelled_spot_instance_request

    out: CancelledSpotInstanceRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.cancelled_spot_instance_request.deserialize_ec2_query(child)
        )
    return out
