"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeMapRunOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn
    import aws_sdk_sfn.types.long_arn
    import aws_sdk_sfn.types.map_run_execution_counts
    import aws_sdk_sfn.types.map_run_item_counts
    import aws_sdk_sfn.types.map_run_status
    import aws_sdk_sfn.types.max_concurrency
    import aws_sdk_sfn.types.redrive_count
    import aws_sdk_sfn.types.timestamp
    import aws_sdk_sfn.types.tolerated_failure_count
    import aws_sdk_sfn.types.tolerated_failure_percentage


class DescribeMapRunOutput(TypedDict, closed=True):
    map_run_arn: "aws_sdk_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) that identifies a Map Run.</p>"""
    execution_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the execution in which the Map Run was started.</p>"""
    status: "aws_sdk_sfn.types.map_run_status.MapRunStatus"
    """<p>The current status of the Map Run.</p>"""
    start_date: "aws_sdk_sfn.types.timestamp.Timestamp"
    """<p>The date when the Map Run was started.</p>"""
    stop_date: NotRequired["aws_sdk_sfn.types.timestamp.Timestamp"]
    """<p>The date when the Map Run was stopped.</p>"""
    max_concurrency: "aws_sdk_sfn.types.max_concurrency.MaxConcurrency"
    """<p>The maximum number of child workflow executions configured to run in parallel for the Map Run at the same time.</p>"""
    tolerated_failure_percentage: (
        "aws_sdk_sfn.types.tolerated_failure_percentage.ToleratedFailurePercentage"
    )
    """<p>The maximum percentage of failed child workflow executions before the Map Run fails.</p>"""
    tolerated_failure_count: (
        "aws_sdk_sfn.types.tolerated_failure_count.ToleratedFailureCount"
    )
    """<p>The maximum number of failed child workflow executions before the Map Run fails.</p>"""
    item_counts: "aws_sdk_sfn.types.map_run_item_counts.MapRunItemCounts"
    """<p>A JSON object that contains information about the total number of items, and the item count for each processing status, such as <code>pending</code> and <code>failed</code>.</p>"""
    execution_counts: "aws_sdk_sfn.types.map_run_execution_counts.MapRunExecutionCounts"
    """<p>A JSON object that contains information about the total number of child workflow executions for the Map Run, and the count of child workflow executions for each status, such as <code>failed</code> and <code>succeeded</code>.</p>"""
    redrive_count: NotRequired["aws_sdk_sfn.types.redrive_count.RedriveCount"]
    """<p>The number of times you've redriven a Map Run. If you have not yet redriven a Map Run, the <code>redriveCount</code> is 0. This count is only updated if you successfully redrive a Map Run.</p>"""
    redrive_date: NotRequired["aws_sdk_sfn.types.timestamp.Timestamp"]
    """<p>The date a Map Run was last redriven. If you have not yet redriven a Map Run, the <code>redriveDate</code> is null.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeMapRunOutput) -> dict:
    out: dict = {}
    out["mapRunArn"] = value["map_run_arn"]
    out["executionArn"] = value["execution_arn"]
    import aws_sdk_sfn.types.map_run_status

    out["status"] = aws_sdk_sfn.types.map_run_status.serialize_aws_json_1_0(
        value["status"]
    )
    import aws_sdk_sfn.types.timestamp

    out["startDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    if "stop_date" in value:
        import aws_sdk_sfn.types.timestamp

        out["stopDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
            value["stop_date"]
        )
    out["maxConcurrency"] = value.get("max_concurrency", 0)
    out["toleratedFailurePercentage"] = value.get("tolerated_failure_percentage", 0)
    out["toleratedFailureCount"] = value.get("tolerated_failure_count", 0)
    import aws_sdk_sfn.types.map_run_item_counts

    out["itemCounts"] = aws_sdk_sfn.types.map_run_item_counts.serialize_aws_json_1_0(
        value["item_counts"]
    )
    import aws_sdk_sfn.types.map_run_execution_counts

    out["executionCounts"] = (
        aws_sdk_sfn.types.map_run_execution_counts.serialize_aws_json_1_0(
            value["execution_counts"]
        )
    )
    if "redrive_count" in value:
        out["redriveCount"] = value["redrive_count"]
    if "redrive_date" in value:
        import aws_sdk_sfn.types.timestamp

        out["redriveDate"] = aws_sdk_sfn.types.timestamp.serialize_aws_json_1_0(
            value["redrive_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeMapRunOutput:
    out: DescribeMapRunOutput = {}  # type: ignore[typeddict-item]
    if "mapRunArn" in data:
        out["map_run_arn"] = data["mapRunArn"]
    else:
        raise DeserializationError("DescribeMapRunOutput.map_run_arn required")
    if "executionArn" in data:
        out["execution_arn"] = data["executionArn"]
    else:
        raise DeserializationError("DescribeMapRunOutput.execution_arn required")
    if "status" in data:
        import aws_sdk_sfn.types.map_run_status

        out["status"] = aws_sdk_sfn.types.map_run_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("DescribeMapRunOutput.status required")
    if "startDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["start_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["startDate"]
        )
    else:
        raise DeserializationError("DescribeMapRunOutput.start_date required")
    if "stopDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["stop_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["stopDate"]
        )
    if "maxConcurrency" in data:
        out["max_concurrency"] = data["maxConcurrency"]
    else:
        out["max_concurrency"] = 0
    if "toleratedFailurePercentage" in data:
        out["tolerated_failure_percentage"] = data["toleratedFailurePercentage"]
    else:
        out["tolerated_failure_percentage"] = 0
    if "toleratedFailureCount" in data:
        out["tolerated_failure_count"] = data["toleratedFailureCount"]
    else:
        out["tolerated_failure_count"] = 0
    if "itemCounts" in data:
        import aws_sdk_sfn.types.map_run_item_counts

        out["item_counts"] = (
            aws_sdk_sfn.types.map_run_item_counts.deserialize_aws_json_1_0(
                data["itemCounts"]
            )
        )
    else:
        raise DeserializationError("DescribeMapRunOutput.item_counts required")
    if "executionCounts" in data:
        import aws_sdk_sfn.types.map_run_execution_counts

        out["execution_counts"] = (
            aws_sdk_sfn.types.map_run_execution_counts.deserialize_aws_json_1_0(
                data["executionCounts"]
            )
        )
    else:
        raise DeserializationError("DescribeMapRunOutput.execution_counts required")
    if "redriveCount" in data:
        out["redrive_count"] = data["redriveCount"]
    if "redriveDate" in data:
        import aws_sdk_sfn.types.timestamp

        out["redrive_date"] = aws_sdk_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["redriveDate"]
        )
    return out
