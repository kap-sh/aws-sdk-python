"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateElasticInferenceAcceleratorList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_elastic_inference_accelerator

LaunchTemplateElasticInferenceAcceleratorList: TypeAlias = list[
    "capo_ec2.types.launch_template_elastic_inference_accelerator.LaunchTemplateElasticInferenceAccelerator"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateElasticInferenceAcceleratorList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.launch_template_elastic_inference_accelerator

        capo_ec2.types.launch_template_elastic_inference_accelerator.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateElasticInferenceAcceleratorList:
    import capo_ec2.types.launch_template_elastic_inference_accelerator

    out: LaunchTemplateElasticInferenceAcceleratorList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.launch_template_elastic_inference_accelerator.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> LaunchTemplateElasticInferenceAcceleratorList:
    import capo_ec2.types.launch_template_elastic_inference_accelerator

    out: LaunchTemplateElasticInferenceAcceleratorList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.launch_template_elastic_inference_accelerator.deserialize_ec2_query(
                child
            )
        )
    return out
