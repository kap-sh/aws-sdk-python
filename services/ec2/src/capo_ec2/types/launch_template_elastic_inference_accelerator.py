"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateElasticInferenceAccelerator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_elastic_inference_accelerator_count
    import capo_ec2.types.string


class LaunchTemplateElasticInferenceAccelerator(TypedDict, closed=True):
    type: NotRequired["capo_ec2.types.string.String"]
    """<p> The type of elastic inference accelerator. The possible values are eia1.medium, eia1.large, and eia1.xlarge. </p>"""
    count: NotRequired[
        "capo_ec2.types.launch_template_elastic_inference_accelerator_count.LaunchTemplateElasticInferenceAcceleratorCount"
    ]
    """<p>The number of elastic inference accelerators to attach to the instance. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateElasticInferenceAccelerator,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "type" in value:
        pairs.append((f"{prefix}.Type", str(value["type"])))
    if "count" in value:
        pairs.append((f"{prefix}.Count", str(value["count"])))


def deserialize_ec2_query(el: Element) -> LaunchTemplateElasticInferenceAccelerator:
    out: LaunchTemplateElasticInferenceAccelerator = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    return out
