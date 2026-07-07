"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_error
    import aws_sdk_fis.types.experiment_status
    import aws_sdk_fis.types.experiment_status_reason


class ExperimentState(TypedDict, closed=True):
    status: NotRequired["aws_sdk_fis.types.experiment_status.ExperimentStatus"]
    """<p>The state of the experiment.</p>"""
    reason: NotRequired[
        "aws_sdk_fis.types.experiment_status_reason.ExperimentStatusReason"
    ]
    """<p>The reason for the state.</p>"""
    error: NotRequired["aws_sdk_fis.types.experiment_error.ExperimentError"]
    """<p>The error information of the experiment when the action has <code>failed</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_fis.types.experiment_status

        out["status"] = aws_sdk_fis.types.experiment_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    if "error" in value:
        import aws_sdk_fis.types.experiment_error

        out["error"] = aws_sdk_fis.types.experiment_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> ExperimentState:
    out: ExperimentState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_fis.types.experiment_status

        out["status"] = aws_sdk_fis.types.experiment_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    if "error" in data:
        import aws_sdk_fis.types.experiment_error

        out["error"] = aws_sdk_fis.types.experiment_error.deserialize_json(
            data["error"]
        )
    return out
