"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetConfiguredModelAlgorithmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_arn


class GetConfiguredModelAlgorithmRequest(TypedDict, closed=True):
    configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to return information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredModelAlgorithmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfiguredModelAlgorithmRequest:
    out: GetConfiguredModelAlgorithmRequest = {}  # type: ignore[typeddict-item]
    return out
