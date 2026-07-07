"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#TargetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.target_address
    import aws_sdk_codestar_notifications.types.target_status
    import aws_sdk_codestar_notifications.types.target_type


class TargetSummary(TypedDict, closed=True):
    target_address: NotRequired[
        "aws_sdk_codestar_notifications.types.target_address.TargetAddress"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client.</p>"""
    target_type: NotRequired[
        "aws_sdk_codestar_notifications.types.target_type.TargetType"
    ]
    """<p>The type of the target (for example, <code>SNS</code>).</p> <ul> <li> <p>Amazon Q Developer in chat applications topics are specified as <code>SNS</code>.</p> </li> <li> <p>Amazon Q Developer in chat applications clients are specified as <code>AWSChatbotSlack</code>.</p> </li> </ul>"""
    target_status: NotRequired[
        "aws_sdk_codestar_notifications.types.target_status.TargetStatus"
    ]
    """<p>The status of the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummary) -> dict:
    out: dict = {}
    if "target_address" in value:
        out["TargetAddress"] = value["target_address"]
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    if "target_status" in value:
        import aws_sdk_codestar_notifications.types.target_status

        out["TargetStatus"] = (
            aws_sdk_codestar_notifications.types.target_status.serialize_json(
                value["target_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> TargetSummary:
    out: TargetSummary = {}  # type: ignore[typeddict-item]
    if "TargetAddress" in data:
        out["target_address"] = data["TargetAddress"]
    if "TargetType" in data:
        out["target_type"] = data["TargetType"]
    if "TargetStatus" in data:
        import aws_sdk_codestar_notifications.types.target_status

        out["target_status"] = (
            aws_sdk_codestar_notifications.types.target_status.deserialize_json(
                data["TargetStatus"]
            )
        )
    return out
