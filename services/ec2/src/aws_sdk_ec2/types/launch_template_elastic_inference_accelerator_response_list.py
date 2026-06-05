"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateElasticInferenceAcceleratorResponseList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_response

LaunchTemplateElasticInferenceAcceleratorResponseList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_response.LaunchTemplateElasticInferenceAcceleratorResponse"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateElasticInferenceAcceleratorResponseList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_response

        aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_response.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> LaunchTemplateElasticInferenceAcceleratorResponseList:
    import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_response

    out: LaunchTemplateElasticInferenceAcceleratorResponseList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_response.deserialize_ec2_query(
                child
            )
        )
    return out
