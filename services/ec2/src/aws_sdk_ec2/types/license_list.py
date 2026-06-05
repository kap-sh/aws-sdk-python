"""Generated from Smithy shape ``com.amazonaws.ec2#LicenseList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.license_configuration

LicenseList: TypeAlias = list[
    "aws_sdk_ec2.types.license_configuration.LicenseConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LicenseList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.license_configuration

        aws_sdk_ec2.types.license_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> LicenseList:
    import aws_sdk_ec2.types.license_configuration

    out: LicenseList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.license_configuration.deserialize_ec2_query(child))
    return out
