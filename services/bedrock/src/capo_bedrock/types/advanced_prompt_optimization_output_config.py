"""Generated from Smithy shape ``com.amazonaws.bedrock#AdvancedPromptOptimizationOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.s3_uri_folder


class AdvancedPromptOptimizationOutputConfig(TypedDict, closed=True):
    s3_uri: "capo_bedrock.types.s3_uri_folder.S3UriFolder"
    """<p>The S3 URI prefix where the optimization results will be written.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedPromptOptimizationOutputConfig) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> AdvancedPromptOptimizationOutputConfig:
    out: AdvancedPromptOptimizationOutputConfig = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError(
            "AdvancedPromptOptimizationOutputConfig.s3_uri required"
        )
    return out
