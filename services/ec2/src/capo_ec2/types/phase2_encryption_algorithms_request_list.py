"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2EncryptionAlgorithmsRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.phase2_encryption_algorithms_request_list_value

Phase2EncryptionAlgorithmsRequestList: TypeAlias = list[
    "capo_ec2.types.phase2_encryption_algorithms_request_list_value.Phase2EncryptionAlgorithmsRequestListValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Phase2EncryptionAlgorithmsRequestList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.phase2_encryption_algorithms_request_list_value

        capo_ec2.types.phase2_encryption_algorithms_request_list_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> Phase2EncryptionAlgorithmsRequestList:
    import capo_ec2.types.phase2_encryption_algorithms_request_list_value

    out: Phase2EncryptionAlgorithmsRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.phase2_encryption_algorithms_request_list_value.deserialize_ec2_query(
                child
            )
        )
    return out
