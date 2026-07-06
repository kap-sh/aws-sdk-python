"""Generated from Smithy shape ``com.amazonaws.lambda#DurableConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.execution_timeout
    import aws_sdk_lambda.types.retention_period_in_days


class DurableConfig(TypedDict, closed=True):
    retention_period_in_days: NotRequired[
        "aws_sdk_lambda.types.retention_period_in_days.RetentionPeriodInDays"
    ]
    """<p>The number of days to retain execution history after a durable execution completes. After this period, execution history is no longer available through the GetDurableExecutionHistory API.</p>"""
    execution_timeout: NotRequired[
        "aws_sdk_lambda.types.execution_timeout.ExecutionTimeout"
    ]
    """<p>The maximum time (in seconds) that a durable execution can run before timing out. This timeout applies to the entire durable execution, not individual function invocations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DurableConfig) -> dict:
    out: dict = {}
    if "retention_period_in_days" in value:
        out["RetentionPeriodInDays"] = value["retention_period_in_days"]
    if "execution_timeout" in value:
        out["ExecutionTimeout"] = value["execution_timeout"]
    return out


def deserialize_json(data: dict) -> DurableConfig:
    out: DurableConfig = {}  # type: ignore[typeddict-item]
    if "RetentionPeriodInDays" in data:
        out["retention_period_in_days"] = data["RetentionPeriodInDays"]
    if "ExecutionTimeout" in data:
        out["execution_timeout"] = data["ExecutionTimeout"]
    return out
