"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentDataCacheConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.enable_caching


class InferenceComponentDataCacheConfig(TypedDict, closed=True):
    enable_caching: NotRequired["aws_sdk_sagemaker.types.enable_caching.EnableCaching"]
    """<p>Sets whether the endpoint that hosts the inference component caches the model artifacts and container image.</p> <p>With caching enabled, the endpoint caches this data in each instance that it provisions for the inference component. That way, the inference component deploys faster during the auto scaling process. If caching isn't enabled, the inference component takes longer to deploy because of the time it spends downloading the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentDataCacheConfig) -> dict:
    out: dict = {}
    if "enable_caching" in value:
        out["EnableCaching"] = value["enable_caching"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentDataCacheConfig:
    out: InferenceComponentDataCacheConfig = {}  # type: ignore[typeddict-item]
    if "EnableCaching" in data:
        out["enable_caching"] = data["EnableCaching"]
    return out
