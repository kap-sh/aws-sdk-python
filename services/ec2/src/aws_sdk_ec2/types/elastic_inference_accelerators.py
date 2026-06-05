"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticInferenceAccelerators``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_inference_accelerator

ElasticInferenceAccelerators: TypeAlias = list[
    "aws_sdk_ec2.types.elastic_inference_accelerator.ElasticInferenceAccelerator"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticInferenceAccelerators, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.elastic_inference_accelerator

        aws_sdk_ec2.types.elastic_inference_accelerator.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ElasticInferenceAccelerators:
    import aws_sdk_ec2.types.elastic_inference_accelerator

    out: ElasticInferenceAccelerators = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.elastic_inference_accelerator.deserialize_ec2_query(child)
        )
    return out
