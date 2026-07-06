"""Generated from Smithy shape ``com.amazonaws.shield#AttackVolumeStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_shield.types.double


class AttackVolumeStatistics(TypedDict, closed=True):
    max: "aws_sdk_shield.types.double.Double"
    """<p>The maximum attack volume observed for the given unit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackVolumeStatistics) -> dict:
    out: dict = {}
    out["Max"] = value.get("max", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackVolumeStatistics:
    out: AttackVolumeStatistics = {}  # type: ignore[typeddict-item]
    if "Max" in data:
        out["max"] = data["Max"]
    else:
        out["max"] = 0
    return out
