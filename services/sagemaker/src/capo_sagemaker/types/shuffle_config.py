"""Generated from Smithy shape ``com.amazonaws.sagemaker#ShuffleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.seed


class ShuffleConfig(TypedDict, closed=True):
    seed: NotRequired["capo_sagemaker.types.seed.Seed"]
    """<p>Determines the shuffling order in <code>ShuffleConfig</code> value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShuffleConfig) -> dict:
    out: dict = {}
    if "seed" in value:
        out["Seed"] = value["seed"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ShuffleConfig:
    out: ShuffleConfig = {}  # type: ignore[typeddict-item]
    if "Seed" in data:
        out["seed"] = data["Seed"]
    return out
