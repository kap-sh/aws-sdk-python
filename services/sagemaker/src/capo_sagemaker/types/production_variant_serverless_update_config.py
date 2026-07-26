"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantServerlessUpdateConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.serverless_max_concurrency
    import capo_sagemaker.types.serverless_provisioned_concurrency


class ProductionVariantServerlessUpdateConfig(TypedDict, closed=True):
    max_concurrency: NotRequired[
        "capo_sagemaker.types.serverless_max_concurrency.ServerlessMaxConcurrency"
    ]
    """<p>The updated maximum number of concurrent invocations your serverless endpoint can process.</p>"""
    provisioned_concurrency: NotRequired[
        "capo_sagemaker.types.serverless_provisioned_concurrency.ServerlessProvisionedConcurrency"
    ]
    """<p>The updated amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to <code>MaxConcurrency</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantServerlessUpdateConfig) -> dict:
    out: dict = {}
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "provisioned_concurrency" in value:
        out["ProvisionedConcurrency"] = value["provisioned_concurrency"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductionVariantServerlessUpdateConfig:
    out: ProductionVariantServerlessUpdateConfig = {}  # type: ignore[typeddict-item]
    if "MaxConcurrency" in data:
        out["max_concurrency"] = data["MaxConcurrency"]
    if "ProvisionedConcurrency" in data:
        out["provisioned_concurrency"] = data["ProvisionedConcurrency"]
    return out
