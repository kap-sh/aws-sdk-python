"""Generated from Smithy shape ``com.amazonaws.drs#DescribeRecoverySnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.describe_recovery_snapshots_request_filters
    import aws_sdk_drs.types.pagination_token
    import aws_sdk_drs.types.recovery_snapshots_order
    import aws_sdk_drs.types.source_server_id
    import aws_sdk_drs.types.strictly_positive_integer


class DescribeRecoverySnapshotsRequest(TypedDict, closed=True):
    source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID"
    """<p>Filter Recovery Snapshots by Source Server ID.</p>"""
    filters: NotRequired[
        "aws_sdk_drs.types.describe_recovery_snapshots_request_filters.DescribeRecoverySnapshotsRequestFilters"
    ]
    """<p>A set of filters by which to return Recovery Snapshots.</p>"""
    order: NotRequired[
        "aws_sdk_drs.types.recovery_snapshots_order.RecoverySnapshotsOrder"
    ]
    """<p>The sorted ordering by which to return Recovery Snapshots.</p>"""
    max_results: NotRequired[
        "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Maximum number of Recovery Snapshots to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Recovery Snapshot to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoverySnapshotsRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "filters" in value:
        import aws_sdk_drs.types.describe_recovery_snapshots_request_filters

        out["filters"] = (
            aws_sdk_drs.types.describe_recovery_snapshots_request_filters.serialize_json(
                value["filters"]
            )
        )
    if "order" in value:
        out["order"] = value["order"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeRecoverySnapshotsRequest:
    out: DescribeRecoverySnapshotsRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError(
            "DescribeRecoverySnapshotsRequest.source_server_id required"
        )
    if "filters" in data:
        import aws_sdk_drs.types.describe_recovery_snapshots_request_filters

        out["filters"] = (
            aws_sdk_drs.types.describe_recovery_snapshots_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if "order" in data:
        out["order"] = data["order"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
