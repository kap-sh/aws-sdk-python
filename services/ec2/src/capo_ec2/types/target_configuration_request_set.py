"""Generated from Smithy shape ``com.amazonaws.ec2#TargetConfigurationRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.target_configuration_request

TargetConfigurationRequestSet: TypeAlias = list[
    "capo_ec2.types.target_configuration_request.TargetConfigurationRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetConfigurationRequestSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.target_configuration_request

        capo_ec2.types.target_configuration_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> TargetConfigurationRequestSet:
    import capo_ec2.types.target_configuration_request

    out: TargetConfigurationRequestSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.target_configuration_request.deserialize_ec2_query(child)
        )
    return out
