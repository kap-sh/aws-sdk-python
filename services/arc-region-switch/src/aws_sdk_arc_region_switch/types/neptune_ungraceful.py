"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#NeptuneUngraceful``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.neptune_ungraceful_behavior


class NeptuneUngraceful(TypedDict, closed=True):
    ungraceful: NotRequired[
        "aws_sdk_arc_region_switch.types.neptune_ungraceful_behavior.NeptuneUngracefulBehavior"
    ]
    """<p>The settings for ungraceful execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NeptuneUngraceful) -> dict:
    out: dict = {}
    if "ungraceful" in value:
        import aws_sdk_arc_region_switch.types.neptune_ungraceful_behavior

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.neptune_ungraceful_behavior.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> NeptuneUngraceful:
    out: NeptuneUngraceful = {}  # type: ignore[typeddict-item]
    if "ungraceful" in data:
        import aws_sdk_arc_region_switch.types.neptune_ungraceful_behavior

        out["ungraceful"] = (
            aws_sdk_arc_region_switch.types.neptune_ungraceful_behavior.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    return out
