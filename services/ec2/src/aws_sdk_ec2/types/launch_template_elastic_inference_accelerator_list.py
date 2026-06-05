"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateElasticInferenceAcceleratorList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator

LaunchTemplateElasticInferenceAcceleratorList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_elastic_inference_accelerator.LaunchTemplateElasticInferenceAccelerator"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateElasticInferenceAcceleratorList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator

        aws_sdk_ec2.types.launch_template_elastic_inference_accelerator.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> LaunchTemplateElasticInferenceAcceleratorList:
    import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator

    out: LaunchTemplateElasticInferenceAcceleratorList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.launch_template_elastic_inference_accelerator.deserialize_ec2_query(
                child
            )
        )
    return out
