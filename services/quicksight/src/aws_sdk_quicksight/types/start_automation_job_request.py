"""Generated from Smithy shape ``com.amazonaws.quicksight#StartAutomationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.automate_id
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.sensitive_io_payload


class StartAutomationJobRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the automation.</p>"""
    automation_group_id: "aws_sdk_quicksight.types.automate_id.AutomateId"
    """<p>The ID of the automation group that contains the automation to run.</p>"""
    automation_id: "aws_sdk_quicksight.types.automate_id.AutomateId"
    """<p>The ID of the automation to run.</p>"""
    input_payload: NotRequired[
        "aws_sdk_quicksight.types.sensitive_io_payload.SensitiveIOPayload"
    ]
    """<p>The input payload for the automation job, provided as a JSON string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAutomationJobRequest) -> dict:
    out: dict = {}
    if "input_payload" in value:
        out["InputPayload"] = value["input_payload"]
    return out


def deserialize_json(data: dict) -> StartAutomationJobRequest:
    out: StartAutomationJobRequest = {}  # type: ignore[typeddict-item]
    if "InputPayload" in data:
        out["input_payload"] = data["InputPayload"]
    return out
