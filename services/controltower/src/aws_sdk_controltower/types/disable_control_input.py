"""Generated from Smithy shape ``com.amazonaws.controltower#DisableControlInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.control_identifier
    import aws_sdk_controltower.types.target_identifier


class DisableControlInput(TypedDict):
    control_identifier: NotRequired[
        "aws_sdk_controltower.types.control_identifier.ControlIdentifier"
    ]
    """<p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>"""
    target_identifier: NotRequired[
        "aws_sdk_controltower.types.target_identifier.TargetIdentifier"
    ]
    """<p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>"""
    enabled_control_identifier: NotRequired["aws_sdk_controltower.types.arn.Arn"]
    """<p>The ARN of the enabled control to be disabled, which uniquely identifies the control instance on the target organizational unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableControlInput) -> dict:
    out: dict = {}
    if "control_identifier" in value:
        out["controlIdentifier"] = value["control_identifier"]
    if "target_identifier" in value:
        out["targetIdentifier"] = value["target_identifier"]
    if "enabled_control_identifier" in value:
        out["enabledControlIdentifier"] = value["enabled_control_identifier"]
    return out


def deserialize_json(data: dict) -> DisableControlInput:
    out: DisableControlInput = {}  # type: ignore[typeddict-item]
    if "controlIdentifier" in data:
        out["control_identifier"] = data["controlIdentifier"]
    if "targetIdentifier" in data:
        out["target_identifier"] = data["targetIdentifier"]
    if "enabledControlIdentifier" in data:
        out["enabled_control_identifier"] = data["enabledControlIdentifier"]
    return out
