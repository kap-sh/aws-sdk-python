"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointPortRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_verified_access_endpoint_port_range

CreateVerifiedAccessEndpointPortRangeList: TypeAlias = list[
    "aws_sdk_ec2.types.create_verified_access_endpoint_port_range.CreateVerifiedAccessEndpointPortRange"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessEndpointPortRangeList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.create_verified_access_endpoint_port_range

        aws_sdk_ec2.types.create_verified_access_endpoint_port_range.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> CreateVerifiedAccessEndpointPortRangeList:
    import aws_sdk_ec2.types.create_verified_access_endpoint_port_range

    out: CreateVerifiedAccessEndpointPortRangeList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.create_verified_access_endpoint_port_range.deserialize_ec2_query(
                child
            )
        )
    return out
