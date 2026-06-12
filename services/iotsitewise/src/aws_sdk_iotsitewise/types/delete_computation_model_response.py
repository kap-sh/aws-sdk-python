"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteComputationModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.computation_model_status


class DeleteComputationModelResponse(TypedDict):
    computation_model_status: (
        "aws_sdk_iotsitewise.types.computation_model_status.ComputationModelStatus"
    )
    """<p>The status of the computation model. It contains a state (DELETING after successfully calling this operation) and any error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteComputationModelResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.computation_model_status

    out["computationModelStatus"] = (
        aws_sdk_iotsitewise.types.computation_model_status.serialize_json(
            value["computation_model_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteComputationModelResponse:
    out: DeleteComputationModelResponse = {}  # type: ignore[typeddict-item]
    if "computationModelStatus" in data:
        import aws_sdk_iotsitewise.types.computation_model_status

        out["computation_model_status"] = (
            aws_sdk_iotsitewise.types.computation_model_status.deserialize_json(
                data["computationModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteComputationModelResponse.computation_model_status required"
        )
    return out
