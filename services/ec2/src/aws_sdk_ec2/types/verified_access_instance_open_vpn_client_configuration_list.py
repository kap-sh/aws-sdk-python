"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceOpenVpnClientConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration

VerifiedAccessInstanceOpenVpnClientConfigurationList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration.VerifiedAccessInstanceOpenVpnClientConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessInstanceOpenVpnClientConfigurationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration

        aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> VerifiedAccessInstanceOpenVpnClientConfigurationList:
    import aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration

    out: VerifiedAccessInstanceOpenVpnClientConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.verified_access_instance_open_vpn_client_configuration.deserialize_ec2_query(
                child
            )
        )
    return out
