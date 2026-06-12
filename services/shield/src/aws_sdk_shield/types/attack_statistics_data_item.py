"""Generated from Smithy shape ``com.amazonaws.shield#AttackStatisticsDataItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.attack_volume
    import aws_sdk_shield.types.long


class AttackStatisticsDataItem(TypedDict):
    attack_volume: NotRequired["aws_sdk_shield.types.attack_volume.AttackVolume"]
    """<p>Information about the volume of attacks during the time period. If the accompanying <code>AttackCount</code> is zero, this setting might be empty.</p>"""
    attack_count: "aws_sdk_shield.types.long.Long"
    """<p>The number of attacks detected during the time period. This is always present, but might be zero. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackStatisticsDataItem) -> dict:
    out: dict = {}
    if "attack_volume" in value:
        import aws_sdk_shield.types.attack_volume

        out["AttackVolume"] = aws_sdk_shield.types.attack_volume.serialize_aws_json_1_1(
            value["attack_volume"]
        )
    out["AttackCount"] = value.get("attack_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackStatisticsDataItem:
    out: AttackStatisticsDataItem = {}  # type: ignore[typeddict-item]
    if "AttackVolume" in data:
        import aws_sdk_shield.types.attack_volume

        out["attack_volume"] = (
            aws_sdk_shield.types.attack_volume.deserialize_aws_json_1_1(
                data["AttackVolume"]
            )
        )
    if "AttackCount" in data:
        out["attack_count"] = data["AttackCount"]
    else:
        out["attack_count"] = 0
    return out
