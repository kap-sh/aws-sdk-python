"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsResponseSuccessSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.delete_launch_template_versions_response_success_item

DeleteLaunchTemplateVersionsResponseSuccessSet: TypeAlias = list[
    "capo_ec2.types.delete_launch_template_versions_response_success_item.DeleteLaunchTemplateVersionsResponseSuccessItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLaunchTemplateVersionsResponseSuccessSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.delete_launch_template_versions_response_success_item

        capo_ec2.types.delete_launch_template_versions_response_success_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> DeleteLaunchTemplateVersionsResponseSuccessSet:
    import capo_ec2.types.delete_launch_template_versions_response_success_item

    out: DeleteLaunchTemplateVersionsResponseSuccessSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.delete_launch_template_versions_response_success_item.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> DeleteLaunchTemplateVersionsResponseSuccessSet:
    import capo_ec2.types.delete_launch_template_versions_response_success_item

    out: DeleteLaunchTemplateVersionsResponseSuccessSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.delete_launch_template_versions_response_success_item.deserialize_ec2_query(
                child
            )
        )
    return out
