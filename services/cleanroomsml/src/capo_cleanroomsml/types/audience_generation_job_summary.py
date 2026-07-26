"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceGenerationJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.audience_generation_job_arn
    import capo_cleanroomsml.types.audience_generation_job_status
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.uuid


class AudienceGenerationJobSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the audience generation job was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the audience generation job was updated.</p>"""
    audience_generation_job_arn: (
        "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
    )
    """<p>The Amazon Resource Name (ARN) of the audience generation job.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the audience generation job.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the audience generation job.</p>"""
    status: "capo_cleanroomsml.types.audience_generation_job_status.AudienceGenerationJobStatus"
    """<p>The status of the audience generation job.</p>"""
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that was used for this audience generation job.</p>"""
    collaboration_id: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The identifier of the collaboration that contains this audience generation job.</p>"""
    started_by: NotRequired["capo_cleanroomsml.types.account_id.AccountId"]
    """<p>The AWS Account that submitted the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceGenerationJobSummary) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types._prelude.timestamp

    out["createTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["audienceGenerationJobArn"] = value["audience_generation_job_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanroomsml.types.audience_generation_job_status

    out["status"] = (
        capo_cleanroomsml.types.audience_generation_job_status.serialize_json(
            value["status"]
        )
    )
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    if "collaboration_id" in value:
        out["collaborationId"] = value["collaboration_id"]
    if "started_by" in value:
        out["startedBy"] = value["started_by"]
    return out


def deserialize_json(data: dict) -> AudienceGenerationJobSummary:
    out: AudienceGenerationJobSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("AudienceGenerationJobSummary.create_time required")
    if "updateTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("AudienceGenerationJobSummary.update_time required")
    if "audienceGenerationJobArn" in data:
        out["audience_generation_job_arn"] = data["audienceGenerationJobArn"]
    else:
        raise DeserializationError(
            "AudienceGenerationJobSummary.audience_generation_job_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AudienceGenerationJobSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import capo_cleanroomsml.types.audience_generation_job_status

        out["status"] = (
            capo_cleanroomsml.types.audience_generation_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AudienceGenerationJobSummary.status required")
    if "configuredAudienceModelArn" in data:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "AudienceGenerationJobSummary.configured_audience_model_arn required"
        )
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    if "startedBy" in data:
        out["started_by"] = data["startedBy"]
    return out
