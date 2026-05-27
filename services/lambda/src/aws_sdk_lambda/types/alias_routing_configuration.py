"""Generated from Smithy shape ``com.amazonaws.lambda#AliasRoutingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.additional_version_weights


class AliasRoutingConfiguration(TypedDict):
    additional_version_weights: NotRequired[
        "aws_sdk_lambda.types.additional_version_weights.AdditionalVersionWeights"
    ]
    """<p>The second version, and the percentage of traffic that's routed to it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AliasRoutingConfiguration) -> dict:
    out: dict = {}
    if "additional_version_weights" in value:
        import aws_sdk_lambda.types.additional_version_weights

        out["AdditionalVersionWeights"] = (
            aws_sdk_lambda.types.additional_version_weights.serialize_json(
                value["additional_version_weights"]
            )
        )
    return out


def deserialize_json(data: dict) -> AliasRoutingConfiguration:
    out: AliasRoutingConfiguration = {}  # type: ignore[typeddict-item]
    if "AdditionalVersionWeights" in data:
        import aws_sdk_lambda.types.additional_version_weights

        out["additional_version_weights"] = (
            aws_sdk_lambda.types.additional_version_weights.deserialize_json(
                data["AdditionalVersionWeights"]
            )
        )
    return out
