"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#ListTargetsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.next_token
    import aws_sdk_codestar_notifications.types.targets_batch


class ListTargetsResult(TypedDict):
    targets: NotRequired[
        "aws_sdk_codestar_notifications.types.targets_batch.TargetsBatch"
    ]
    """<p>The list of notification rule targets. </p>"""
    next_token: NotRequired["aws_sdk_codestar_notifications.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsResult) -> dict:
    out: dict = {}
    if "targets" in value:
        import aws_sdk_codestar_notifications.types.targets_batch

        out["Targets"] = (
            aws_sdk_codestar_notifications.types.targets_batch.serialize_json(
                value["targets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTargetsResult:
    out: ListTargetsResult = {}  # type: ignore[typeddict-item]
    if "Targets" in data:
        import aws_sdk_codestar_notifications.types.targets_batch

        out["targets"] = (
            aws_sdk_codestar_notifications.types.targets_batch.deserialize_json(
                data["Targets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
