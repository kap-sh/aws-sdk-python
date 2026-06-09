"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateBlockDeviceMappingRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_block_device_mapping_request

LaunchTemplateBlockDeviceMappingRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_block_device_mapping_request.LaunchTemplateBlockDeviceMappingRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateBlockDeviceMappingRequestList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.launch_template_block_device_mapping_request

        aws_sdk_ec2.types.launch_template_block_device_mapping_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> LaunchTemplateBlockDeviceMappingRequestList:
    import aws_sdk_ec2.types.launch_template_block_device_mapping_request

    out: LaunchTemplateBlockDeviceMappingRequestList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.launch_template_block_device_mapping_request.deserialize_ec2_query(
                child
            )
        )
    return out
