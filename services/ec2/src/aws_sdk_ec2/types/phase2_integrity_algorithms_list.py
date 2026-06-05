"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2IntegrityAlgorithmsList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.phase2_integrity_algorithms_list_value

Phase2IntegrityAlgorithmsList: TypeAlias = list[
    "aws_sdk_ec2.types.phase2_integrity_algorithms_list_value.Phase2IntegrityAlgorithmsListValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Phase2IntegrityAlgorithmsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.phase2_integrity_algorithms_list_value

        aws_sdk_ec2.types.phase2_integrity_algorithms_list_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> Phase2IntegrityAlgorithmsList:
    import aws_sdk_ec2.types.phase2_integrity_algorithms_list_value

    out: Phase2IntegrityAlgorithmsList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.phase2_integrity_algorithms_list_value.deserialize_ec2_query(
                child
            )
        )
    return out
