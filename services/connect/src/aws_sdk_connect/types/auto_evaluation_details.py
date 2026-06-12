"""Generated from Smithy shape ``com.amazonaws.connect#AutoEvaluationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.auto_evaluation_status
    import aws_sdk_connect.types.boolean


class AutoEvaluationDetails(TypedDict):
    auto_evaluation_enabled: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Whether automated evaluation is enabled.</p>"""
    auto_evaluation_status: NotRequired[
        "aws_sdk_connect.types.auto_evaluation_status.AutoEvaluationStatus"
    ]
    """<p>The status of the contact auto-evaluation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoEvaluationDetails) -> dict:
    out: dict = {}
    out["AutoEvaluationEnabled"] = value.get("auto_evaluation_enabled", False)
    if "auto_evaluation_status" in value:
        import aws_sdk_connect.types.auto_evaluation_status

        out["AutoEvaluationStatus"] = (
            aws_sdk_connect.types.auto_evaluation_status.serialize_json(
                value["auto_evaluation_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoEvaluationDetails:
    out: AutoEvaluationDetails = {}  # type: ignore[typeddict-item]
    if "AutoEvaluationEnabled" in data:
        out["auto_evaluation_enabled"] = data["AutoEvaluationEnabled"]
    else:
        out["auto_evaluation_enabled"] = False
    if "AutoEvaluationStatus" in data:
        import aws_sdk_connect.types.auto_evaluation_status

        out["auto_evaluation_status"] = (
            aws_sdk_connect.types.auto_evaluation_status.deserialize_json(
                data["AutoEvaluationStatus"]
            )
        )
    return out
