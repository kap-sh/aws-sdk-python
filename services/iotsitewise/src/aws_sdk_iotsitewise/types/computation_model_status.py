"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.computation_model_state
    import aws_sdk_iotsitewise.types.error_details


class ComputationModelStatus(TypedDict, closed=True):
    state: "aws_sdk_iotsitewise.types.computation_model_state.ComputationModelState"
    """<p>The current state of the computation model.</p>"""
    error: NotRequired["aws_sdk_iotsitewise.types.error_details.ErrorDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelStatus) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.computation_model_state

    out["state"] = aws_sdk_iotsitewise.types.computation_model_state.serialize_json(
        value["state"]
    )
    if "error" in value:
        import aws_sdk_iotsitewise.types.error_details

        out["error"] = aws_sdk_iotsitewise.types.error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> ComputationModelStatus:
    out: ComputationModelStatus = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_iotsitewise.types.computation_model_state

        out["state"] = (
            aws_sdk_iotsitewise.types.computation_model_state.deserialize_json(
                data["state"]
            )
        )
    else:
        raise DeserializationError("ComputationModelStatus.state required")
    if "error" in data:
        import aws_sdk_iotsitewise.types.error_details

        out["error"] = aws_sdk_iotsitewise.types.error_details.deserialize_json(
            data["error"]
        )
    return out
