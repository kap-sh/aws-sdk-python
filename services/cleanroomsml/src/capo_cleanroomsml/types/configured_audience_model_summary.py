"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredAudienceModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.audience_model_arn
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.configured_audience_model_output_config
    import capo_cleanroomsml.types.configured_audience_model_status
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description


class ConfiguredAudienceModelSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the configured audience model was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured audience model was updated.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured audience model.</p>"""
    audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model that was used to create the configured audience model.</p>"""
    output_config: "capo_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig"
    """<p>The output configuration of the configured audience model.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured audience model.</p>"""
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>"""
    status: "capo_cleanroomsml.types.configured_audience_model_status.ConfiguredAudienceModelStatus"
    """<p>The status of the configured audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredAudienceModelSummary) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types._prelude.timestamp

    out["createTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["name"] = value["name"]
    out["audienceModelArn"] = value["audience_model_arn"]
    import capo_cleanroomsml.types.configured_audience_model_output_config

    out["outputConfig"] = (
        capo_cleanroomsml.types.configured_audience_model_output_config.serialize_json(
            value["output_config"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    import capo_cleanroomsml.types.configured_audience_model_status

    out["status"] = (
        capo_cleanroomsml.types.configured_audience_model_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConfiguredAudienceModelSummary:
    out: ConfiguredAudienceModelSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelSummary.create_time required"
        )
    if "updateTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelSummary.update_time required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfiguredAudienceModelSummary.name required")
    if "audienceModelArn" in data:
        out["audience_model_arn"] = data["audienceModelArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelSummary.audience_model_arn required"
        )
    if "outputConfig" in data:
        import capo_cleanroomsml.types.configured_audience_model_output_config

        out["output_config"] = (
            capo_cleanroomsml.types.configured_audience_model_output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelSummary.output_config required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "configuredAudienceModelArn" in data:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelSummary.configured_audience_model_arn required"
        )
    if "status" in data:
        import capo_cleanroomsml.types.configured_audience_model_status

        out["status"] = (
            capo_cleanroomsml.types.configured_audience_model_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ConfiguredAudienceModelSummary.status required")
    return out
