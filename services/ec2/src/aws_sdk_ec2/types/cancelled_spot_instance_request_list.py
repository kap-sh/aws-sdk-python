"""Generated from Smithy shape ``com.amazonaws.ec2#CancelledSpotInstanceRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancelled_spot_instance_request

CancelledSpotInstanceRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.cancelled_spot_instance_request.CancelledSpotInstanceRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelledSpotInstanceRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.cancelled_spot_instance_request

        aws_sdk_ec2.types.cancelled_spot_instance_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> CancelledSpotInstanceRequestList:
    import aws_sdk_ec2.types.cancelled_spot_instance_request

    out: CancelledSpotInstanceRequestList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.cancelled_spot_instance_request.deserialize_ec2_query(
                child
            )
        )
    return out
