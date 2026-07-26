"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceRefreshProgressDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instance_refresh_live_pool_progress
    import capo_auto_scaling.types.instance_refresh_warm_pool_progress


class InstanceRefreshProgressDetails(TypedDict, closed=True):
    live_pool_progress: NotRequired[
        "capo_auto_scaling.types.instance_refresh_live_pool_progress.InstanceRefreshLivePoolProgress"
    ]
    """<p>Reports progress on replacing instances that are in the Auto Scaling group.</p>"""
    warm_pool_progress: NotRequired[
        "capo_auto_scaling.types.instance_refresh_warm_pool_progress.InstanceRefreshWarmPoolProgress"
    ]
    """<p>Reports progress on replacing instances that are in the warm pool.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceRefreshProgressDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "live_pool_progress" in value:
        import capo_auto_scaling.types.instance_refresh_live_pool_progress

        capo_auto_scaling.types.instance_refresh_live_pool_progress.serialize_query(
            value["live_pool_progress"], pairs, f"{prefix}.LivePoolProgress"
        )
    if "warm_pool_progress" in value:
        import capo_auto_scaling.types.instance_refresh_warm_pool_progress

        capo_auto_scaling.types.instance_refresh_warm_pool_progress.serialize_query(
            value["warm_pool_progress"], pairs, f"{prefix}.WarmPoolProgress"
        )


def deserialize_query(el: Element) -> InstanceRefreshProgressDetails:
    out: InstanceRefreshProgressDetails = {}  # type: ignore[typeddict-item]
    child_live_pool_progress = el.find("LivePoolProgress")
    if child_live_pool_progress is not None:
        import capo_auto_scaling.types.instance_refresh_live_pool_progress

        out["live_pool_progress"] = (
            capo_auto_scaling.types.instance_refresh_live_pool_progress.deserialize_query(
                child_live_pool_progress
            )
        )
    child_warm_pool_progress = el.find("WarmPoolProgress")
    if child_warm_pool_progress is not None:
        import capo_auto_scaling.types.instance_refresh_warm_pool_progress

        out["warm_pool_progress"] = (
            capo_auto_scaling.types.instance_refresh_warm_pool_progress.deserialize_query(
                child_warm_pool_progress
            )
        )
    return out
