"""Generated from Smithy shape ``com.amazonaws.sfn#UpdateMapRunInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.long_arn
    import aws_sdk_sfn.types.max_concurrency
    import aws_sdk_sfn.types.tolerated_failure_count
    import aws_sdk_sfn.types.tolerated_failure_percentage


class UpdateMapRunInput(TypedDict):
    map_run_arn: "aws_sdk_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) of a Map Run.</p>"""
    max_concurrency: NotRequired["aws_sdk_sfn.types.max_concurrency.MaxConcurrency"]
    """<p>The maximum number of child workflow executions that can be specified to run in parallel for the Map Run at the same time.</p>"""
    tolerated_failure_percentage: NotRequired[
        "aws_sdk_sfn.types.tolerated_failure_percentage.ToleratedFailurePercentage"
    ]
    """<p>The maximum percentage of failed items before the Map Run fails.</p>"""
    tolerated_failure_count: NotRequired[
        "aws_sdk_sfn.types.tolerated_failure_count.ToleratedFailureCount"
    ]
    """<p>The maximum number of failed items before the Map Run fails.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateMapRunInput) -> dict:
    out: dict = {}
    out["mapRunArn"] = value["map_run_arn"]
    if "max_concurrency" in value:
        out["maxConcurrency"] = value["max_concurrency"]
    if "tolerated_failure_percentage" in value:
        out["toleratedFailurePercentage"] = value["tolerated_failure_percentage"]
    if "tolerated_failure_count" in value:
        out["toleratedFailureCount"] = value["tolerated_failure_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateMapRunInput:
    out: UpdateMapRunInput = {}  # type: ignore[typeddict-item]
    if "mapRunArn" in data:
        out["map_run_arn"] = data["mapRunArn"]
    else:
        raise DeserializationError("UpdateMapRunInput.map_run_arn required")
    if "maxConcurrency" in data:
        out["max_concurrency"] = data["maxConcurrency"]
    if "toleratedFailurePercentage" in data:
        out["tolerated_failure_percentage"] = data["toleratedFailurePercentage"]
    if "toleratedFailureCount" in data:
        out["tolerated_failure_count"] = data["toleratedFailureCount"]
    return out
