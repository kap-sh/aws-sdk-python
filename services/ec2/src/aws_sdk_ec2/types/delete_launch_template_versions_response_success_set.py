"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsResponseSuccessSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_launch_template_versions_response_success_item

DeleteLaunchTemplateVersionsResponseSuccessSet: TypeAlias = list[
    "aws_sdk_ec2.types.delete_launch_template_versions_response_success_item.DeleteLaunchTemplateVersionsResponseSuccessItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLaunchTemplateVersionsResponseSuccessSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.delete_launch_template_versions_response_success_item

        aws_sdk_ec2.types.delete_launch_template_versions_response_success_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> DeleteLaunchTemplateVersionsResponseSuccessSet:
    import aws_sdk_ec2.types.delete_launch_template_versions_response_success_item

    out: DeleteLaunchTemplateVersionsResponseSuccessSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.delete_launch_template_versions_response_success_item.deserialize_ec2_query(
                child
            )
        )
    return out
