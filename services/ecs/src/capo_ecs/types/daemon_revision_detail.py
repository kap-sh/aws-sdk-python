"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonRevisionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_capacity_provider_list
    import capo_ecs.types.integer
    import capo_ecs.types.string


class DaemonRevisionDetail(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon revision.</p>"""
    capacity_providers: NotRequired[
        "capo_ecs.types.daemon_capacity_provider_list.DaemonCapacityProviderList"
    ]
    """<p>The capacity providers associated with this daemon revision.</p>"""
    total_running_count: "capo_ecs.types.integer.Integer"
    """<p>The total number of daemon tasks running for this revision.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonRevisionDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "capacity_providers" in value:
        import capo_ecs.types.daemon_capacity_provider_list

        out["capacityProviders"] = (
            capo_ecs.types.daemon_capacity_provider_list.serialize_aws_json_1_1(
                value["capacity_providers"]
            )
        )
    out["totalRunningCount"] = value.get("total_running_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonRevisionDetail:
    out: DaemonRevisionDetail = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("capacityProviders") is not None:
        import capo_ecs.types.daemon_capacity_provider_list

        out["capacity_providers"] = (
            capo_ecs.types.daemon_capacity_provider_list.deserialize_aws_json_1_1(
                data["capacityProviders"]
            )
        )
    if data.get("totalRunningCount") is not None:
        out["total_running_count"] = data["totalRunningCount"]
    else:
        out["total_running_count"] = 0
    return out
