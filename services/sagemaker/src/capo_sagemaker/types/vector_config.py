"""Generated from Smithy shape ``com.amazonaws.sagemaker#VectorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.dimension


class VectorConfig(TypedDict, closed=True):
    dimension: NotRequired["capo_sagemaker.types.dimension.Dimension"]
    """<p>The number of elements in your vector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VectorConfig) -> dict:
    out: dict = {}
    if "dimension" in value:
        out["Dimension"] = value["dimension"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VectorConfig:
    out: VectorConfig = {}  # type: ignore[typeddict-item]
    if "Dimension" in data:
        out["dimension"] = data["Dimension"]
    return out
