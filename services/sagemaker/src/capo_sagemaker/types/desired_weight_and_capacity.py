"""Generated from Smithy shape ``com.amazonaws.sagemaker#DesiredWeightAndCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.production_variant_serverless_update_config
    import capo_sagemaker.types.task_count
    import capo_sagemaker.types.variant_name
    import capo_sagemaker.types.variant_weight


class DesiredWeightAndCapacity(TypedDict, closed=True):
    variant_name: NotRequired["capo_sagemaker.types.variant_name.VariantName"]
    """<p>The name of the variant to update.</p>"""
    desired_weight: NotRequired["capo_sagemaker.types.variant_weight.VariantWeight"]
    """<p>The variant's weight.</p>"""
    desired_instance_count: NotRequired["capo_sagemaker.types.task_count.TaskCount"]
    """<p>The variant's capacity.</p>"""
    serverless_update_config: NotRequired[
        "capo_sagemaker.types.production_variant_serverless_update_config.ProductionVariantServerlessUpdateConfig"
    ]
    """<p>Specifies the serverless update concurrency configuration for an endpoint variant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DesiredWeightAndCapacity) -> dict:
    out: dict = {}
    if "variant_name" in value:
        out["VariantName"] = value["variant_name"]
    if "desired_weight" in value:
        out["DesiredWeight"] = value["desired_weight"]
    if "desired_instance_count" in value:
        out["DesiredInstanceCount"] = value["desired_instance_count"]
    if "serverless_update_config" in value:
        import capo_sagemaker.types.production_variant_serverless_update_config

        out["ServerlessUpdateConfig"] = (
            capo_sagemaker.types.production_variant_serverless_update_config.serialize_aws_json_1_1(
                value["serverless_update_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DesiredWeightAndCapacity:
    out: DesiredWeightAndCapacity = {}  # type: ignore[typeddict-item]
    if "VariantName" in data:
        out["variant_name"] = data["VariantName"]
    if "DesiredWeight" in data:
        out["desired_weight"] = data["DesiredWeight"]
    if "DesiredInstanceCount" in data:
        out["desired_instance_count"] = data["DesiredInstanceCount"]
    if "ServerlessUpdateConfig" in data:
        import capo_sagemaker.types.production_variant_serverless_update_config

        out["serverless_update_config"] = (
            capo_sagemaker.types.production_variant_serverless_update_config.deserialize_aws_json_1_1(
                data["ServerlessUpdateConfig"]
            )
        )
    return out
