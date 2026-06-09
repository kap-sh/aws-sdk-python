"""Generated from Smithy shape ``com.amazonaws.ec2#IpamExternalResourceVerificationTokenSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_external_resource_verification_token

IpamExternalResourceVerificationTokenSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_external_resource_verification_token.IpamExternalResourceVerificationToken"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamExternalResourceVerificationTokenSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_external_resource_verification_token

        aws_sdk_ec2.types.ipam_external_resource_verification_token.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> IpamExternalResourceVerificationTokenSet:
    import aws_sdk_ec2.types.ipam_external_resource_verification_token

    out: IpamExternalResourceVerificationTokenSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.ipam_external_resource_verification_token.deserialize_ec2_query(
                child
            )
        )
    return out
