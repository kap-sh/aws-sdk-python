"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateVersionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_version

LaunchTemplateVersionSet: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_version.LaunchTemplateVersion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateVersionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.launch_template_version

        aws_sdk_ec2.types.launch_template_version.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> LaunchTemplateVersionSet:
    import aws_sdk_ec2.types.launch_template_version

    out: LaunchTemplateVersionSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.launch_template_version.deserialize_ec2_query(child)
        )
    return out
