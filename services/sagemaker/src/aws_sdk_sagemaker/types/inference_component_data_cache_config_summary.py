"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentDataCacheConfigSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.enable_caching


class InferenceComponentDataCacheConfigSummary(TypedDict):
    enable_caching: NotRequired["aws_sdk_sagemaker.types.enable_caching.EnableCaching"]
    """<p>Indicates whether the inference component caches model artifacts as part of the auto scaling process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentDataCacheConfigSummary) -> dict:
    out: dict = {}
    if "enable_caching" in value:
        out["EnableCaching"] = value["enable_caching"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentDataCacheConfigSummary:
    out: InferenceComponentDataCacheConfigSummary = {}  # type: ignore[typeddict-item]
    if "EnableCaching" in data:
        out["enable_caching"] = data["EnableCaching"]
    return out
