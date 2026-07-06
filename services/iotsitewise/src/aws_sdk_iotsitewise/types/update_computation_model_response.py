"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateComputationModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.computation_model_status


class UpdateComputationModelResponse(TypedDict, closed=True):
    computation_model_status: (
        "aws_sdk_iotsitewise.types.computation_model_status.ComputationModelStatus"
    )
    """<p>The status of the computation model. It contains a state (UPDATING after successfully calling this operation) and an error message if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateComputationModelResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.computation_model_status

    out["computationModelStatus"] = (
        aws_sdk_iotsitewise.types.computation_model_status.serialize_json(
            value["computation_model_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateComputationModelResponse:
    out: UpdateComputationModelResponse = {}  # type: ignore[typeddict-item]
    if "computationModelStatus" in data:
        import aws_sdk_iotsitewise.types.computation_model_status

        out["computation_model_status"] = (
            aws_sdk_iotsitewise.types.computation_model_status.deserialize_json(
                data["computationModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateComputationModelResponse.computation_model_status required"
        )
    return out
