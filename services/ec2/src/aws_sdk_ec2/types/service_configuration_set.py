"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceConfigurationSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_configuration

ServiceConfigurationSet: TypeAlias = list[
    "aws_sdk_ec2.types.service_configuration.ServiceConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ServiceConfigurationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.service_configuration

        aws_sdk_ec2.types.service_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ServiceConfigurationSet:
    import aws_sdk_ec2.types.service_configuration

    out: ServiceConfigurationSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.service_configuration.deserialize_ec2_query(child))
    return out
