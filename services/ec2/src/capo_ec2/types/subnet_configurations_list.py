"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.subnet_configuration

SubnetConfigurationsList: TypeAlias = list[
    "capo_ec2.types.subnet_configuration.SubnetConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetConfigurationsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.subnet_configuration

        capo_ec2.types.subnet_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SubnetConfigurationsList:
    import capo_ec2.types.subnet_configuration

    out: SubnetConfigurationsList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.subnet_configuration.deserialize_ec2_query(child))
    return out
