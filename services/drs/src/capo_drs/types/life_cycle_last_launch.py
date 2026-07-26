"""Generated from Smithy shape ``com.amazonaws.drs#LifeCycleLastLaunch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.launch_status
    import capo_drs.types.life_cycle_last_launch_initiated


class LifeCycleLastLaunch(TypedDict, closed=True):
    initiated: NotRequired[
        "capo_drs.types.life_cycle_last_launch_initiated.LifeCycleLastLaunchInitiated"
    ]
    """<p>An object containing information regarding the initiation of the last launch of a Source Server.</p>"""
    status: NotRequired["capo_drs.types.launch_status.LaunchStatus"]
    """<p>Status of Source Server's last launch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleLastLaunch) -> dict:
    out: dict = {}
    if "initiated" in value:
        import capo_drs.types.life_cycle_last_launch_initiated

        out["initiated"] = (
            capo_drs.types.life_cycle_last_launch_initiated.serialize_json(
                value["initiated"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> LifeCycleLastLaunch:
    out: LifeCycleLastLaunch = {}  # type: ignore[typeddict-item]
    if "initiated" in data:
        import capo_drs.types.life_cycle_last_launch_initiated

        out["initiated"] = (
            capo_drs.types.life_cycle_last_launch_initiated.deserialize_json(
                data["initiated"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    return out
