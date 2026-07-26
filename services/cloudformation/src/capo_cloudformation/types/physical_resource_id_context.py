"""Generated from Smithy shape ``com.amazonaws.cloudformation#PhysicalResourceIdContext``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.physical_resource_id_context_key_value_pair

PhysicalResourceIdContext: TypeAlias = list[
    "capo_cloudformation.types.physical_resource_id_context_key_value_pair.PhysicalResourceIdContextKeyValuePair"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PhysicalResourceIdContext, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.physical_resource_id_context_key_value_pair

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.physical_resource_id_context_key_value_pair.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PhysicalResourceIdContext:
    import capo_cloudformation.types.physical_resource_id_context_key_value_pair

    out: PhysicalResourceIdContext = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.physical_resource_id_context_key_value_pair.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PhysicalResourceIdContext, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.physical_resource_id_context_key_value_pair

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.physical_resource_id_context_key_value_pair.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PhysicalResourceIdContext:
    import capo_cloudformation.types.physical_resource_id_context_key_value_pair

    out: PhysicalResourceIdContext = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.physical_resource_id_context_key_value_pair.deserialize_query(
                child
            )
        )
    return out
