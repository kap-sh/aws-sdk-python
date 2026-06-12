"""Generated from Smithy shape ``com.amazonaws.kinesis#WarmThroughputObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.natural_integer_object


class WarmThroughputObject(TypedDict):
    target_mi_bps: NotRequired[
        "aws_sdk_kinesis.types.natural_integer_object.NaturalIntegerObject"
    ]
    """<p>The target warm throughput value on the stream. This indicates that the stream is currently scaling towards this target value.</p>"""
    current_mi_bps: NotRequired[
        "aws_sdk_kinesis.types.natural_integer_object.NaturalIntegerObject"
    ]
    """<p>The current warm throughput value on the stream. This is the write throughput in MiBps that the stream is currently scaled to handle.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WarmThroughputObject) -> dict:
    out: dict = {}
    if "target_mi_bps" in value:
        out["TargetMiBps"] = value["target_mi_bps"]
    if "current_mi_bps" in value:
        out["CurrentMiBps"] = value["current_mi_bps"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WarmThroughputObject:
    out: WarmThroughputObject = {}  # type: ignore[typeddict-item]
    if "TargetMiBps" in data:
        out["target_mi_bps"] = data["TargetMiBps"]
    if "CurrentMiBps" in data:
        out["current_mi_bps"] = data["CurrentMiBps"]
    return out
