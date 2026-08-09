"""Generated from Smithy shape ``com.amazonaws.ec2#Phase1EncryptionAlgorithmsRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.phase1_encryption_algorithms_request_list_value

Phase1EncryptionAlgorithmsRequestList: TypeAlias = list[
    "capo_ec2.types.phase1_encryption_algorithms_request_list_value.Phase1EncryptionAlgorithmsRequestListValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Phase1EncryptionAlgorithmsRequestList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.phase1_encryption_algorithms_request_list_value

        capo_ec2.types.phase1_encryption_algorithms_request_list_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> Phase1EncryptionAlgorithmsRequestList:
    import capo_ec2.types.phase1_encryption_algorithms_request_list_value

    out: Phase1EncryptionAlgorithmsRequestList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.phase1_encryption_algorithms_request_list_value.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> Phase1EncryptionAlgorithmsRequestList:
    import capo_ec2.types.phase1_encryption_algorithms_request_list_value

    out: Phase1EncryptionAlgorithmsRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.phase1_encryption_algorithms_request_list_value.deserialize_ec2_query(
                child
            )
        )
    return out
