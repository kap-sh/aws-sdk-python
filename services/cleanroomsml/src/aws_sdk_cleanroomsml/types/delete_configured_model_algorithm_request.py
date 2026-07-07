"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteConfiguredModelAlgorithmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_arn


class DeleteConfiguredModelAlgorithmRequest(TypedDict, closed=True):
    configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfiguredModelAlgorithmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfiguredModelAlgorithmRequest:
    out: DeleteConfiguredModelAlgorithmRequest = {}  # type: ignore[typeddict-item]
    return out
