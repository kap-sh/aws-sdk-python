"""Generated from Smithy shape ``com.amazonaws.ec2#CustomKeyValuePairResponseSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.custom_tag_key_value_response_pair

CustomKeyValuePairResponseSet: TypeAlias = list[
    "capo_ec2.types.custom_tag_key_value_response_pair.CustomTagKeyValueResponsePair"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CustomKeyValuePairResponseSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.custom_tag_key_value_response_pair

        capo_ec2.types.custom_tag_key_value_response_pair.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CustomKeyValuePairResponseSet:
    import capo_ec2.types.custom_tag_key_value_response_pair

    out: CustomKeyValuePairResponseSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.custom_tag_key_value_response_pair.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CustomKeyValuePairResponseSet:
    import capo_ec2.types.custom_tag_key_value_response_pair

    out: CustomKeyValuePairResponseSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.custom_tag_key_value_response_pair.deserialize_ec2_query(
                child
            )
        )
    return out
