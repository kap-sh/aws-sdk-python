"""Generated from Smithy shape ``com.amazonaws.ec2#AthenaIntegrationsSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.athena_integration

AthenaIntegrationsSet: TypeAlias = list[
    "capo_ec2.types.athena_integration.AthenaIntegration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AthenaIntegrationsSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.athena_integration

        capo_ec2.types.athena_integration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AthenaIntegrationsSet:
    import capo_ec2.types.athena_integration

    out: AthenaIntegrationsSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.athena_integration.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AthenaIntegrationsSet:
    import capo_ec2.types.athena_integration

    out: AthenaIntegrationsSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.athena_integration.deserialize_ec2_query(child))
    return out
