"""Generated from Smithy shape ``com.amazonaws.connect#AnswerMachineDetectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean


class AnswerMachineDetectionConfig(TypedDict, closed=True):
    enable_answer_machine_detection: "aws_sdk_connect.types.boolean.Boolean"
    """<p>The flag to indicate if answer machine detection analysis needs to be performed for a voice call. If set to <code>true</code>, <code>TrafficType</code> must be set as <code>CAMPAIGN</code>. </p>"""
    await_answer_machine_prompt: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Wait for the answering machine prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnswerMachineDetectionConfig) -> dict:
    out: dict = {}
    out["EnableAnswerMachineDetection"] = value.get(
        "enable_answer_machine_detection", False
    )
    out["AwaitAnswerMachinePrompt"] = value.get("await_answer_machine_prompt", False)
    return out


def deserialize_json(data: dict) -> AnswerMachineDetectionConfig:
    out: AnswerMachineDetectionConfig = {}  # type: ignore[typeddict-item]
    if "EnableAnswerMachineDetection" in data:
        out["enable_answer_machine_detection"] = data["EnableAnswerMachineDetection"]
    else:
        out["enable_answer_machine_detection"] = False
    if "AwaitAnswerMachinePrompt" in data:
        out["await_answer_machine_prompt"] = data["AwaitAnswerMachinePrompt"]
    else:
        out["await_answer_machine_prompt"] = False
    return out
