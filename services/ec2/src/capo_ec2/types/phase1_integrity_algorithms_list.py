"""Generated from Smithy shape ``com.amazonaws.ec2#Phase1IntegrityAlgorithmsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.phase1_integrity_algorithms_list_value

Phase1IntegrityAlgorithmsList: TypeAlias = list[
    "capo_ec2.types.phase1_integrity_algorithms_list_value.Phase1IntegrityAlgorithmsListValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Phase1IntegrityAlgorithmsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.phase1_integrity_algorithms_list_value

        capo_ec2.types.phase1_integrity_algorithms_list_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> Phase1IntegrityAlgorithmsList:
    import capo_ec2.types.phase1_integrity_algorithms_list_value

    out: Phase1IntegrityAlgorithmsList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.phase1_integrity_algorithms_list_value.deserialize_ec2_query(
                child
            )
        )
    return out
