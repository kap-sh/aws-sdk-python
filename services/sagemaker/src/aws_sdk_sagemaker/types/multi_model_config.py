"""Generated from Smithy shape ``com.amazonaws.sagemaker#MultiModelConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_cache_setting


class MultiModelConfig(TypedDict):
    model_cache_setting: NotRequired[
        "aws_sdk_sagemaker.types.model_cache_setting.ModelCacheSetting"
    ]
    """<p>Whether to cache models for a multi-model endpoint. By default, multi-model endpoints cache models so that a model does not have to be loaded into memory each time it is invoked. Some use cases do not benefit from model caching. For example, if an endpoint hosts a large number of models that are each invoked infrequently, the endpoint might perform better if you disable model caching. To disable model caching, set the value of this parameter to <code>Disabled</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiModelConfig) -> dict:
    out: dict = {}
    if "model_cache_setting" in value:
        import aws_sdk_sagemaker.types.model_cache_setting

        out["ModelCacheSetting"] = (
            aws_sdk_sagemaker.types.model_cache_setting.serialize_aws_json_1_1(
                value["model_cache_setting"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MultiModelConfig:
    out: MultiModelConfig = {}  # type: ignore[typeddict-item]
    if "ModelCacheSetting" in data:
        import aws_sdk_sagemaker.types.model_cache_setting

        out["model_cache_setting"] = (
            aws_sdk_sagemaker.types.model_cache_setting.deserialize_aws_json_1_1(
                data["ModelCacheSetting"]
            )
        )
    return out
