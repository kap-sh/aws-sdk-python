"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceAnswerSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.choice_id
    import aws_sdk_wellarchitected.types.choice_reason
    import aws_sdk_wellarchitected.types.choice_status


class ChoiceAnswerSummary(TypedDict):
    choice_id: NotRequired["aws_sdk_wellarchitected.types.choice_id.ChoiceId"]
    status: NotRequired["aws_sdk_wellarchitected.types.choice_status.ChoiceStatus"]
    """<p>The status of a choice.</p>"""
    reason: NotRequired["aws_sdk_wellarchitected.types.choice_reason.ChoiceReason"]
    """<p>The reason why a choice is non-applicable to a question in your workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChoiceAnswerSummary) -> dict:
    out: dict = {}
    if "choice_id" in value:
        out["ChoiceId"] = value["choice_id"]
    if "status" in value:
        import aws_sdk_wellarchitected.types.choice_status

        out["Status"] = aws_sdk_wellarchitected.types.choice_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        import aws_sdk_wellarchitected.types.choice_reason

        out["Reason"] = aws_sdk_wellarchitected.types.choice_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> ChoiceAnswerSummary:
    out: ChoiceAnswerSummary = {}  # type: ignore[typeddict-item]
    if "ChoiceId" in data:
        out["choice_id"] = data["ChoiceId"]
    if "Status" in data:
        import aws_sdk_wellarchitected.types.choice_status

        out["status"] = aws_sdk_wellarchitected.types.choice_status.deserialize_json(
            data["Status"]
        )
    if "Reason" in data:
        import aws_sdk_wellarchitected.types.choice_reason

        out["reason"] = aws_sdk_wellarchitected.types.choice_reason.deserialize_json(
            data["Reason"]
        )
    return out
