"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#UpdateConfiguredAudienceModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_model_arn
    import aws_sdk_cleanroomsml.types.audience_size_config
    import aws_sdk_cleanroomsml.types.configured_audience_model_arn
    import aws_sdk_cleanroomsml.types.configured_audience_model_output_config
    import aws_sdk_cleanroomsml.types.metrics_list
    import aws_sdk_cleanroomsml.types.min_matching_seed_size
    import aws_sdk_cleanroomsml.types.resource_description


class UpdateConfiguredAudienceModelRequest(TypedDict):
    configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that you want to update.</p>"""
    output_config: NotRequired[
        "aws_sdk_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig"
    ]
    """<p>The new output configuration.</p>"""
    audience_model_arn: NotRequired[
        "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the new audience model that you want to use.</p>"""
    shared_audience_metrics: NotRequired[
        "aws_sdk_cleanroomsml.types.metrics_list.MetricsList"
    ]
    """<p>The new value for whether to share audience metrics.</p>"""
    min_matching_seed_size: NotRequired[
        "aws_sdk_cleanroomsml.types.min_matching_seed_size.MinMatchingSeedSize"
    ]
    """<p>The minimum number of users from the seed audience that must match with users in the training data of the audience model.</p>"""
    audience_size_config: NotRequired[
        "aws_sdk_cleanroomsml.types.audience_size_config.AudienceSizeConfig"
    ]
    """<p>The new audience size configuration.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The new description of the configured audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredAudienceModelRequest) -> dict:
    out: dict = {}
    if "output_config" in value:
        import aws_sdk_cleanroomsml.types.configured_audience_model_output_config

        out["outputConfig"] = (
            aws_sdk_cleanroomsml.types.configured_audience_model_output_config.serialize_json(
                value["output_config"]
            )
        )
    if "audience_model_arn" in value:
        out["audienceModelArn"] = value["audience_model_arn"]
    if "shared_audience_metrics" in value:
        import aws_sdk_cleanroomsml.types.metrics_list

        out["sharedAudienceMetrics"] = (
            aws_sdk_cleanroomsml.types.metrics_list.serialize_json(
                value["shared_audience_metrics"]
            )
        )
    if "min_matching_seed_size" in value:
        out["minMatchingSeedSize"] = value["min_matching_seed_size"]
    if "audience_size_config" in value:
        import aws_sdk_cleanroomsml.types.audience_size_config

        out["audienceSizeConfig"] = (
            aws_sdk_cleanroomsml.types.audience_size_config.serialize_json(
                value["audience_size_config"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateConfiguredAudienceModelRequest:
    out: UpdateConfiguredAudienceModelRequest = {}  # type: ignore[typeddict-item]
    if "outputConfig" in data:
        import aws_sdk_cleanroomsml.types.configured_audience_model_output_config

        out["output_config"] = (
            aws_sdk_cleanroomsml.types.configured_audience_model_output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    if "audienceModelArn" in data:
        out["audience_model_arn"] = data["audienceModelArn"]
    if "sharedAudienceMetrics" in data:
        import aws_sdk_cleanroomsml.types.metrics_list

        out["shared_audience_metrics"] = (
            aws_sdk_cleanroomsml.types.metrics_list.deserialize_json(
                data["sharedAudienceMetrics"]
            )
        )
    if "minMatchingSeedSize" in data:
        out["min_matching_seed_size"] = data["minMatchingSeedSize"]
    if "audienceSizeConfig" in data:
        import aws_sdk_cleanroomsml.types.audience_size_config

        out["audience_size_config"] = (
            aws_sdk_cleanroomsml.types.audience_size_config.deserialize_json(
                data["audienceSizeConfig"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
