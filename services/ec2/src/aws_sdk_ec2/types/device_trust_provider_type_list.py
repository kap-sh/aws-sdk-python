"""Generated from Smithy shape ``com.amazonaws.ec2#DeviceTrustProviderTypeList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.device_trust_provider_type

DeviceTrustProviderTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.device_trust_provider_type.DeviceTrustProviderType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeviceTrustProviderTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.device_trust_provider_type

        aws_sdk_ec2.types.device_trust_provider_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> DeviceTrustProviderTypeList:
    import aws_sdk_ec2.types.device_trust_provider_type

    out: DeviceTrustProviderTypeList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.device_trust_provider_type.deserialize_ec2_query(child)
        )
    return out
