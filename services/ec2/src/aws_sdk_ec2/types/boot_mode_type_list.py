"""Generated from Smithy shape ``com.amazonaws.ec2#BootModeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boot_mode_type

BootModeTypeList: TypeAlias = list["aws_sdk_ec2.types.boot_mode_type.BootModeType"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BootModeTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.boot_mode_type

        aws_sdk_ec2.types.boot_mode_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> BootModeTypeList:
    import aws_sdk_ec2.types.boot_mode_type

    out: BootModeTypeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.boot_mode_type.deserialize_ec2_query(child))
    return out
