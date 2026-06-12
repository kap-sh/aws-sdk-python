"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.failed_count
    import aws_sdk_fsx.types.last_updated_time
    import aws_sdk_fsx.types.released_capacity
    import aws_sdk_fsx.types.succeeded_count
    import aws_sdk_fsx.types.total_count


class DataRepositoryTaskStatus(TypedDict):
    total_count: NotRequired["aws_sdk_fsx.types.total_count.TotalCount"]
    """<p>The total number of files that the task will process. While a task is executing, the sum of <code>SucceededCount</code> plus <code>FailedCount</code> may not equal <code>TotalCount</code>. When the task is complete, <code>TotalCount</code> equals the sum of <code>SucceededCount</code> plus <code>FailedCount</code>.</p>"""
    succeeded_count: NotRequired["aws_sdk_fsx.types.succeeded_count.SucceededCount"]
    """<p>A running total of the number of files that the task has successfully processed.</p>"""
    failed_count: NotRequired["aws_sdk_fsx.types.failed_count.FailedCount"]
    """<p>A running total of the number of files that the task failed to process.</p>"""
    last_updated_time: NotRequired[
        "aws_sdk_fsx.types.last_updated_time.LastUpdatedTime"
    ]
    """<p>The time at which the task status was last updated.</p>"""
    released_capacity: NotRequired[
        "aws_sdk_fsx.types.released_capacity.ReleasedCapacity"
    ]
    """<p>The total amount of data, in GiB, released by an Amazon File Cache AUTO_RELEASE_DATA task that automatically releases files from the cache.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskStatus) -> dict:
    out: dict = {}
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    if "succeeded_count" in value:
        out["SucceededCount"] = value["succeeded_count"]
    if "failed_count" in value:
        out["FailedCount"] = value["failed_count"]
    if "last_updated_time" in value:
        import aws_sdk_fsx.types.last_updated_time

        out["LastUpdatedTime"] = (
            aws_sdk_fsx.types.last_updated_time.serialize_aws_json_1_1(
                value["last_updated_time"]
            )
        )
    if "released_capacity" in value:
        out["ReleasedCapacity"] = value["released_capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataRepositoryTaskStatus:
    out: DataRepositoryTaskStatus = {}  # type: ignore[typeddict-item]
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    if "SucceededCount" in data:
        out["succeeded_count"] = data["SucceededCount"]
    if "FailedCount" in data:
        out["failed_count"] = data["FailedCount"]
    if "LastUpdatedTime" in data:
        import aws_sdk_fsx.types.last_updated_time

        out["last_updated_time"] = (
            aws_sdk_fsx.types.last_updated_time.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    if "ReleasedCapacity" in data:
        out["released_capacity"] = data["ReleasedCapacity"]
    return out
