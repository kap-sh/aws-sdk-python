"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceExportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.audience_export_job_status
    import capo_cleanroomsml.types.audience_generation_job_arn
    import capo_cleanroomsml.types.audience_size
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.s3_path
    import capo_cleanroomsml.types.status_details


class AudienceExportJobSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the audience export job was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the audience export job was updated.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the audience export job.</p>"""
    audience_generation_job_arn: (
        "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
    )
    """<p>The Amazon Resource Name (ARN) of the audience generation job that was exported.</p>"""
    audience_size: "capo_cleanroomsml.types.audience_size.AudienceSize"
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the audience export job.</p>"""
    status: "capo_cleanroomsml.types.audience_export_job_status.AudienceExportJobStatus"
    """<p>The status of the audience export job.</p>"""
    status_details: NotRequired["capo_cleanroomsml.types.status_details.StatusDetails"]
    output_location: NotRequired["capo_cleanroomsml.types.s3_path.S3Path"]
    """<p>The Amazon S3 bucket where the audience export is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceExportJobSummary) -> dict:
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
    out["audienceGenerationJobArn"] = value["audience_generation_job_arn"]
    import capo_cleanroomsml.types.audience_size

    out["audienceSize"] = capo_cleanroomsml.types.audience_size.serialize_json(
        value["audience_size"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanroomsml.types.audience_export_job_status

    out["status"] = capo_cleanroomsml.types.audience_export_job_status.serialize_json(
        value["status"]
    )
    if "status_details" in value:
        import capo_cleanroomsml.types.status_details

        out["statusDetails"] = capo_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    if "output_location" in value:
        out["outputLocation"] = value["output_location"]
    return out


def deserialize_json(data: dict) -> AudienceExportJobSummary:
    out: AudienceExportJobSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("AudienceExportJobSummary.create_time required")
    if "updateTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("AudienceExportJobSummary.update_time required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AudienceExportJobSummary.name required")
    if "audienceGenerationJobArn" in data:
        out["audience_generation_job_arn"] = data["audienceGenerationJobArn"]
    else:
        raise DeserializationError(
            "AudienceExportJobSummary.audience_generation_job_arn required"
        )
    if "audienceSize" in data:
        import capo_cleanroomsml.types.audience_size

        out["audience_size"] = capo_cleanroomsml.types.audience_size.deserialize_json(
            data["audienceSize"]
        )
    else:
        raise DeserializationError("AudienceExportJobSummary.audience_size required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import capo_cleanroomsml.types.audience_export_job_status

        out["status"] = (
            capo_cleanroomsml.types.audience_export_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AudienceExportJobSummary.status required")
    if "statusDetails" in data:
        import capo_cleanroomsml.types.status_details

        out["status_details"] = capo_cleanroomsml.types.status_details.deserialize_json(
            data["statusDetails"]
        )
    if "outputLocation" in data:
        out["output_location"] = data["outputLocation"]
    return out
