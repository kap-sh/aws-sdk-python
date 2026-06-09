"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonRevisionDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_capacity_provider_list
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.string


class DaemonRevisionDetail(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon revision.</p>"""
    capacity_providers: NotRequired[
        "aws_sdk_ecs.types.daemon_capacity_provider_list.DaemonCapacityProviderList"
    ]
    """<p>The capacity providers associated with this daemon revision.</p>"""
    total_running_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The total number of daemon tasks running for this revision.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonRevisionDetail) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "capacity_providers" in value:
        import aws_sdk_ecs.types.daemon_capacity_provider_list

        out["capacityProviders"] = (
            aws_sdk_ecs.types.daemon_capacity_provider_list.serialize_aws_json_1_1(
                value["capacity_providers"]
            )
        )
    out["totalRunningCount"] = value.get("total_running_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonRevisionDetail:
    out: DaemonRevisionDetail = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "capacityProviders" in data:
        import aws_sdk_ecs.types.daemon_capacity_provider_list

        out["capacity_providers"] = (
            aws_sdk_ecs.types.daemon_capacity_provider_list.deserialize_aws_json_1_1(
                data["capacityProviders"]
            )
        )
    if "totalRunningCount" in data:
        out["total_running_count"] = data["totalRunningCount"]
    else:
        out["total_running_count"] = 0
    return out
