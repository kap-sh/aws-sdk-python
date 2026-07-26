"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceConfigurationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.service_configuration

ServiceConfigurationSet: TypeAlias = list[
    "capo_ec2.types.service_configuration.ServiceConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ServiceConfigurationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.service_configuration

        capo_ec2.types.service_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ServiceConfigurationSet:
    import capo_ec2.types.service_configuration

    out: ServiceConfigurationSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.service_configuration.deserialize_ec2_query(child))
    return out
