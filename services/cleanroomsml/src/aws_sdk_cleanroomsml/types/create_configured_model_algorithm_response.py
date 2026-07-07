"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateConfiguredModelAlgorithmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_arn


class CreateConfiguredModelAlgorithmResponse(TypedDict, closed=True):
    configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredModelAlgorithmResponse) -> dict:
    out: dict = {}
    out["configuredModelAlgorithmArn"] = value["configured_model_algorithm_arn"]
    return out


def deserialize_json(data: dict) -> CreateConfiguredModelAlgorithmResponse:
    out: CreateConfiguredModelAlgorithmResponse = {}  # type: ignore[typeddict-item]
    if "configuredModelAlgorithmArn" in data:
        out["configured_model_algorithm_arn"] = data["configuredModelAlgorithmArn"]
    else:
        raise DeserializationError(
            "CreateConfiguredModelAlgorithmResponse.configured_model_algorithm_arn required"
        )
    return out
