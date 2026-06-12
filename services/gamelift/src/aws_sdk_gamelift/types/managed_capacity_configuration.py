"""Generated from Smithy shape ``com.amazonaws.gamelift#ManagedCapacityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.scale_in_after_inactivity_minutes
    import aws_sdk_gamelift.types.zero_capacity_strategy


class ManagedCapacityConfiguration(TypedDict):
    zero_capacity_strategy: NotRequired[
        "aws_sdk_gamelift.types.zero_capacity_strategy.ZeroCapacityStrategy"
    ]
    """<p>The strategy Amazon GameLift Servers will use to automatically scale your capacity to and from zero instances in response to game session activity. Game session activity refers to any active running sessions or game session requests.</p> <p>Possible ZeroCapacityStrategy types include:</p> <ul> <li> <p> <b>MANUAL</b> -- (default value) Amazon GameLift Servers will not update capacity to and from zero on your behalf.</p> </li> <li> <p> <b>SCALE_TO_AND_FROM_ZERO</b> -- Amazon GameLift Servers will automatically scale out MinSize and DesiredInstances from 0 to 1 in response to a game session request, and will scale in MinSize and DesiredInstances to 0 after a period with no game session activity. The duration of this scale in period can be configured using ScaleInAfterInactivityMinutes. </p> </li> </ul>"""
    scale_in_after_inactivity_minutes: NotRequired[
        "aws_sdk_gamelift.types.scale_in_after_inactivity_minutes.ScaleInAfterInactivityMinutes"
    ]
    """<p>Length of time, in minutes, that Amazon GameLift Servers will wait before scaling in your MinSize and DesiredInstances to 0 after a period with no game session activity. Default: 30 minutes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedCapacityConfiguration) -> dict:
    out: dict = {}
    if "zero_capacity_strategy" in value:
        import aws_sdk_gamelift.types.zero_capacity_strategy

        out["ZeroCapacityStrategy"] = (
            aws_sdk_gamelift.types.zero_capacity_strategy.serialize_aws_json_1_1(
                value["zero_capacity_strategy"]
            )
        )
    if "scale_in_after_inactivity_minutes" in value:
        out["ScaleInAfterInactivityMinutes"] = value[
            "scale_in_after_inactivity_minutes"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedCapacityConfiguration:
    out: ManagedCapacityConfiguration = {}  # type: ignore[typeddict-item]
    if "ZeroCapacityStrategy" in data:
        import aws_sdk_gamelift.types.zero_capacity_strategy

        out["zero_capacity_strategy"] = (
            aws_sdk_gamelift.types.zero_capacity_strategy.deserialize_aws_json_1_1(
                data["ZeroCapacityStrategy"]
            )
        )
    if "ScaleInAfterInactivityMinutes" in data:
        out["scale_in_after_inactivity_minutes"] = data["ScaleInAfterInactivityMinutes"]
    return out
