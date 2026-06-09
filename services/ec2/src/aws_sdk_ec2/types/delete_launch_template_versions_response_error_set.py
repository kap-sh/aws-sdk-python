"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsResponseErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_launch_template_versions_response_error_item

DeleteLaunchTemplateVersionsResponseErrorSet: TypeAlias = list[
    "aws_sdk_ec2.types.delete_launch_template_versions_response_error_item.DeleteLaunchTemplateVersionsResponseErrorItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLaunchTemplateVersionsResponseErrorSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.delete_launch_template_versions_response_error_item

        aws_sdk_ec2.types.delete_launch_template_versions_response_error_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> DeleteLaunchTemplateVersionsResponseErrorSet:
    import aws_sdk_ec2.types.delete_launch_template_versions_response_error_item

    out: DeleteLaunchTemplateVersionsResponseErrorSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.delete_launch_template_versions_response_error_item.deserialize_ec2_query(
                child
            )
        )
    return out
