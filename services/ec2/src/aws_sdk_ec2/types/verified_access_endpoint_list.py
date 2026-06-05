"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_endpoint

VerifiedAccessEndpointList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_endpoint.VerifiedAccessEndpoint"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessEndpointList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.verified_access_endpoint

        aws_sdk_ec2.types.verified_access_endpoint.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VerifiedAccessEndpointList:
    import aws_sdk_ec2.types.verified_access_endpoint

    out: VerifiedAccessEndpointList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.verified_access_endpoint.deserialize_ec2_query(child)
        )
    return out
