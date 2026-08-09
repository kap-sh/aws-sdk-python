"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticInferenceAccelerators``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.elastic_inference_accelerator

ElasticInferenceAccelerators: TypeAlias = list[
    "capo_ec2.types.elastic_inference_accelerator.ElasticInferenceAccelerator"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticInferenceAccelerators, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.elastic_inference_accelerator

        capo_ec2.types.elastic_inference_accelerator.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ElasticInferenceAccelerators:
    import capo_ec2.types.elastic_inference_accelerator

    out: ElasticInferenceAccelerators = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.elastic_inference_accelerator.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ElasticInferenceAccelerators:
    import capo_ec2.types.elastic_inference_accelerator

    out: ElasticInferenceAccelerators = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.elastic_inference_accelerator.deserialize_ec2_query(child)
        )
    return out
