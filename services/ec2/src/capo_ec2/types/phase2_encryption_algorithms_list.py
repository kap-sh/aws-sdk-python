"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2EncryptionAlgorithmsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.phase2_encryption_algorithms_list_value

Phase2EncryptionAlgorithmsList: TypeAlias = list[
    "capo_ec2.types.phase2_encryption_algorithms_list_value.Phase2EncryptionAlgorithmsListValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Phase2EncryptionAlgorithmsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.phase2_encryption_algorithms_list_value

        capo_ec2.types.phase2_encryption_algorithms_list_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> Phase2EncryptionAlgorithmsList:
    import capo_ec2.types.phase2_encryption_algorithms_list_value

    out: Phase2EncryptionAlgorithmsList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.phase2_encryption_algorithms_list_value.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> Phase2EncryptionAlgorithmsList:
    import capo_ec2.types.phase2_encryption_algorithms_list_value

    out: Phase2EncryptionAlgorithmsList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.phase2_encryption_algorithms_list_value.deserialize_ec2_query(
                child
            )
        )
    return out
