"""Generated from Smithy shape ``com.amazonaws.emr#ClusterStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_state
    import aws_sdk_emr.types.cluster_state_change_reason
    import aws_sdk_emr.types.cluster_timeline
    import aws_sdk_emr.types.error_detail_list


class ClusterStatus(TypedDict):
    state: NotRequired["aws_sdk_emr.types.cluster_state.ClusterState"]
    """<p>The current state of the cluster.</p>"""
    state_change_reason: NotRequired[
        "aws_sdk_emr.types.cluster_state_change_reason.ClusterStateChangeReason"
    ]
    """<p>The reason for the cluster status change.</p>"""
    timeline: NotRequired["aws_sdk_emr.types.cluster_timeline.ClusterTimeline"]
    """<p>A timeline that represents the status of a cluster over the lifetime of the cluster.</p>"""
    error_details: NotRequired["aws_sdk_emr.types.error_detail_list.ErrorDetailList"]
    """<p>A list of tuples that provides information about the errors that caused a cluster to terminate. This structure can contain up to 10 different <code>ErrorDetail</code> tuples.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_emr.types.cluster_state

        out["State"] = aws_sdk_emr.types.cluster_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_change_reason" in value:
        import aws_sdk_emr.types.cluster_state_change_reason

        out["StateChangeReason"] = (
            aws_sdk_emr.types.cluster_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "timeline" in value:
        import aws_sdk_emr.types.cluster_timeline

        out["Timeline"] = aws_sdk_emr.types.cluster_timeline.serialize_aws_json_1_1(
            value["timeline"]
        )
    if "error_details" in value:
        import aws_sdk_emr.types.error_detail_list

        out["ErrorDetails"] = (
            aws_sdk_emr.types.error_detail_list.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterStatus:
    out: ClusterStatus = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_emr.types.cluster_state

        out["state"] = aws_sdk_emr.types.cluster_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateChangeReason" in data:
        import aws_sdk_emr.types.cluster_state_change_reason

        out["state_change_reason"] = (
            aws_sdk_emr.types.cluster_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if "Timeline" in data:
        import aws_sdk_emr.types.cluster_timeline

        out["timeline"] = aws_sdk_emr.types.cluster_timeline.deserialize_aws_json_1_1(
            data["Timeline"]
        )
    if "ErrorDetails" in data:
        import aws_sdk_emr.types.error_detail_list

        out["error_details"] = (
            aws_sdk_emr.types.error_detail_list.deserialize_aws_json_1_1(
                data["ErrorDetails"]
            )
        )
    return out
