"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetConfiguredAudienceModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.audience_model_arn
    import aws_sdk_cleanroomsml.types.audience_size_config
    import aws_sdk_cleanroomsml.types.configured_audience_model_arn
    import aws_sdk_cleanroomsml.types.configured_audience_model_output_config
    import aws_sdk_cleanroomsml.types.configured_audience_model_status
    import aws_sdk_cleanroomsml.types.metrics_list
    import aws_sdk_cleanroomsml.types.min_matching_seed_size
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.tag_on_create_policy


class GetConfiguredAudienceModelResponse(TypedDict):
    create_time: "datetime.datetime"
    """<p>The time at which the configured audience model was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured audience model was updated.</p>"""
    configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured audience model.</p>"""
    audience_model_arn: "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model used for this configured audience model.</p>"""
    output_config: "aws_sdk_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig"
    """<p>The output configuration of the configured audience model</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured audience model.</p>"""
    status: "aws_sdk_cleanroomsml.types.configured_audience_model_status.ConfiguredAudienceModelStatus"
    """<p>The status of the configured audience model.</p>"""
    shared_audience_metrics: "aws_sdk_cleanroomsml.types.metrics_list.MetricsList"
    """<p>Whether audience metrics are shared.</p>"""
    min_matching_seed_size: NotRequired[
        "aws_sdk_cleanroomsml.types.min_matching_seed_size.MinMatchingSeedSize"
    ]
    """<p>The minimum number of users from the seed audience that must match with users in the training data of the audience model.</p>"""
    audience_size_config: NotRequired[
        "aws_sdk_cleanroomsml.types.audience_size_config.AudienceSizeConfig"
    ]
    """<p>The list of output sizes of audiences that can be created using this configured audience model. A request to <a>StartAudienceGenerationJob</a> that uses this configured audience model must have an <code>audienceSize</code> selected from this list. You can use the <code>ABSOLUTE</code> <a>AudienceSize</a> to configure out audience sizes using the count of identifiers in the output. You can use the <code>Percentage</code> <a>AudienceSize</a> to configure sizes in the range 1-100 percent.</p>"""
    tags: NotRequired["aws_sdk_cleanroomsml.types.tag_map.TagMap"]
    """<p>The tags that are associated to this configured audience model.</p>"""
    child_resource_tag_on_create_policy: NotRequired[
        "aws_sdk_cleanroomsml.types.tag_on_create_policy.TagOnCreatePolicy"
    ]
    """<p>Provides the <code>childResourceTagOnCreatePolicy</code> that was used for this configured audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredAudienceModelResponse) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    out["name"] = value["name"]
    out["audienceModelArn"] = value["audience_model_arn"]
    import aws_sdk_cleanroomsml.types.configured_audience_model_output_config

    out["outputConfig"] = (
        aws_sdk_cleanroomsml.types.configured_audience_model_output_config.serialize_json(
            value["output_config"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_cleanroomsml.types.configured_audience_model_status

    out["status"] = (
        aws_sdk_cleanroomsml.types.configured_audience_model_status.serialize_json(
            value["status"]
        )
    )
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
    if "tags" in value:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "child_resource_tag_on_create_policy" in value:
        import aws_sdk_cleanroomsml.types.tag_on_create_policy

        out["childResourceTagOnCreatePolicy"] = (
            aws_sdk_cleanroomsml.types.tag_on_create_policy.serialize_json(
                value["child_resource_tag_on_create_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfiguredAudienceModelResponse:
    out: GetConfiguredAudienceModelResponse = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelResponse.create_time required"
        )
    if "updateTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelResponse.update_time required"
        )
    if "configuredAudienceModelArn" in data:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelResponse.configured_audience_model_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetConfiguredAudienceModelResponse.name required")
    if "audienceModelArn" in data:
        out["audience_model_arn"] = data["audienceModelArn"]
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelResponse.audience_model_arn required"
        )
    if "outputConfig" in data:
        import aws_sdk_cleanroomsml.types.configured_audience_model_output_config

        out["output_config"] = (
            aws_sdk_cleanroomsml.types.configured_audience_model_output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelResponse.output_config required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_cleanroomsml.types.configured_audience_model_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.configured_audience_model_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetConfiguredAudienceModelResponse.status required")
    if "sharedAudienceMetrics" in data:
        import aws_sdk_cleanroomsml.types.metrics_list

        out["shared_audience_metrics"] = (
            aws_sdk_cleanroomsml.types.metrics_list.deserialize_json(
                data["sharedAudienceMetrics"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelResponse.shared_audience_metrics required"
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
    if "tags" in data:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if "childResourceTagOnCreatePolicy" in data:
        import aws_sdk_cleanroomsml.types.tag_on_create_policy

        out["child_resource_tag_on_create_policy"] = (
            aws_sdk_cleanroomsml.types.tag_on_create_policy.deserialize_json(
                data["childResourceTagOnCreatePolicy"]
            )
        )
    return out
