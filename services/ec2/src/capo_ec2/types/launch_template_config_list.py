"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_config

LaunchTemplateConfigList: TypeAlias = list[
    "capo_ec2.types.launch_template_config.LaunchTemplateConfig"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateConfigList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.launch_template_config

        capo_ec2.types.launch_template_config.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateConfigList:
    import capo_ec2.types.launch_template_config

    out: LaunchTemplateConfigList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.launch_template_config.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LaunchTemplateConfigList:
    import capo_ec2.types.launch_template_config

    out: LaunchTemplateConfigList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.launch_template_config.deserialize_ec2_query(child))
    return out
