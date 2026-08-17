"""Generated from Smithy shape ``com.amazonaws.lambda#ScalingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.maximum_concurrency


class ScalingConfig(TypedDict, closed=True):
    maximum_concurrency: NotRequired[
        "capo_lambda.types.maximum_concurrency.MaximumConcurrency"
    ]
    """<p>Limits the number of concurrent instances that the Amazon SQS event source can invoke.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScalingConfig) -> dict:
    out: dict = {}
    if "maximum_concurrency" in value:
        out["MaximumConcurrency"] = value["maximum_concurrency"]
    return out


def deserialize_json(data: dict) -> ScalingConfig:
    out: ScalingConfig = {}  # type: ignore[typeddict-item]
    if data.get("MaximumConcurrency") is not None:
        out["maximum_concurrency"] = data["MaximumConcurrency"]
    return out
