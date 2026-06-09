"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticInferenceAccelerator``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_inference_accelerator_count
    import aws_sdk_ec2.types.string


class ElasticInferenceAccelerator(TypedDict):
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The type of elastic inference accelerator. The possible values are <code>eia1.medium</code>, <code>eia1.large</code>, <code>eia1.xlarge</code>, <code>eia2.medium</code>, <code>eia2.large</code>, and <code>eia2.xlarge</code>. </p>"""
    count: NotRequired[
        "aws_sdk_ec2.types.elastic_inference_accelerator_count.ElasticInferenceAcceleratorCount"
    ]
    """<p> The number of elastic inference accelerators to attach to the instance. </p> <p>Default: 1</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticInferenceAccelerator, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        pairs.append((f"{prefix}.Type", str(value["type"])))
    if "count" in value:
        pairs.append((f"{prefix}.Count", str(value["count"])))


def deserialize_ec2_query(el: Element) -> ElasticInferenceAccelerator:
    out: ElasticInferenceAccelerator = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    return out
