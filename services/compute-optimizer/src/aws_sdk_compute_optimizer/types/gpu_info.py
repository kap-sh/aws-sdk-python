"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GpuInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.gpus


class GpuInfo(TypedDict):
    gpus: NotRequired["aws_sdk_compute_optimizer.types.gpus.Gpus"]
    """<p> Describes the GPU accelerators for the instance type. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GpuInfo) -> dict:
    out: dict = {}
    if "gpus" in value:
        import aws_sdk_compute_optimizer.types.gpus

        out["gpus"] = aws_sdk_compute_optimizer.types.gpus.serialize_aws_json_1_0(
            value["gpus"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GpuInfo:
    out: GpuInfo = {}  # type: ignore[typeddict-item]
    if "gpus" in data:
        import aws_sdk_compute_optimizer.types.gpus

        out["gpus"] = aws_sdk_compute_optimizer.types.gpus.deserialize_aws_json_1_0(
            data["gpus"]
        )
    return out
