"""Generated from Smithy shape ``com.amazonaws.lambda#DurableConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.execution_timeout
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.retention_period_in_days


class DurableConfig(TypedDict, closed=True):
    kms_key_arn: NotRequired["capo_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p>The ARN of the Key Management Service (KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.</p>"""
    retention_period_in_days: NotRequired[
        "capo_lambda.types.retention_period_in_days.RetentionPeriodInDays"
    ]
    """<p>The number of days to retain execution history after a durable execution completes. After this period, execution history is no longer available through the GetDurableExecutionHistory API.</p>"""
    execution_timeout: NotRequired[
        "capo_lambda.types.execution_timeout.ExecutionTimeout"
    ]
    """<p>The maximum time (in seconds) that a durable execution can run before timing out. This timeout applies to the entire durable execution, not individual function invocations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DurableConfig) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["KMSKeyArn"] = value["kms_key_arn"]
    if "retention_period_in_days" in value:
        out["RetentionPeriodInDays"] = value["retention_period_in_days"]
    if "execution_timeout" in value:
        out["ExecutionTimeout"] = value["execution_timeout"]
    return out


def deserialize_json(data: dict) -> DurableConfig:
    out: DurableConfig = {}  # type: ignore[typeddict-item]
    if data.get("KMSKeyArn") is not None:
        out["kms_key_arn"] = data["KMSKeyArn"]
    if data.get("RetentionPeriodInDays") is not None:
        out["retention_period_in_days"] = data["RetentionPeriodInDays"]
    if data.get("ExecutionTimeout") is not None:
        out["execution_timeout"] = data["ExecutionTimeout"]
    return out
