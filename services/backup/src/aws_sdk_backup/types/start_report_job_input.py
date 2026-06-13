"""Generated from Smithy shape ``com.amazonaws.backup#StartReportJobInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.report_plan_name
    import aws_sdk_backup.types.string


class StartReportJobInput(TypedDict):
    report_plan_name: "aws_sdk_backup.types.report_plan_name.ReportPlanName"
    """<p>The unique name of a report plan.</p>"""
    idempotency_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartReportJobInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReportJobInput) -> dict:
    out: dict = {}
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_json(data: dict) -> StartReportJobInput:
    out: StartReportJobInput = {}  # type: ignore[typeddict-item]
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
