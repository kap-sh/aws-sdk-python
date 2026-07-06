"""Generated from Smithy shape ``com.amazonaws.ecs#InfrastructureOptimization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class InfrastructureOptimization(TypedDict, closed=True):
    scale_in_after: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>This parameter defines the number of seconds Amazon ECS Managed Instances waits before optimizing EC2 instances that have become idle or underutilized. A longer delay increases the likelihood of placing new tasks on idle or underutilized instances instances, reducing startup time. A shorter delay helps reduce infrastructure costs by optimizing idle or underutilized instances,instances more quickly.</p> <p>Valid values are:</p> <ul> <li> <p> <code>null</code> - Uses the default optimization behavior.</p> </li> <li> <p> <code>-1</code> - Disables automatic infrastructure optimization.</p> </li> <li> <p>A value between <code>0</code> and <code>3600</code> (inclusive) - Specifies the number of seconds to wait before optimizing instances.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InfrastructureOptimization) -> dict:
    out: dict = {}
    if "scale_in_after" in value:
        out["scaleInAfter"] = value["scale_in_after"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InfrastructureOptimization:
    out: InfrastructureOptimization = {}  # type: ignore[typeddict-item]
    if "scaleInAfter" in data:
        out["scale_in_after"] = data["scaleInAfter"]
    return out
