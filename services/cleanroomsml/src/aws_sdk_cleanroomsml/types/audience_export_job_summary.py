"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceExportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.audience_export_job_status
    import aws_sdk_cleanroomsml.types.audience_generation_job_arn
    import aws_sdk_cleanroomsml.types.audience_size
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.s3_path
    import aws_sdk_cleanroomsml.types.status_details


class AudienceExportJobSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the audience export job was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the audience export job was updated.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the audience export job.</p>"""
    audience_generation_job_arn: "aws_sdk_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
    """<p>The Amazon Resource Name (ARN) of the audience generation job that was exported.</p>"""
    audience_size: "aws_sdk_cleanroomsml.types.audience_size.AudienceSize"
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the audience export job.</p>"""
    status: (
        "aws_sdk_cleanroomsml.types.audience_export_job_status.AudienceExportJobStatus"
    )
    """<p>The status of the audience export job.</p>"""
    status_details: NotRequired[
        "aws_sdk_cleanroomsml.types.status_details.StatusDetails"
    ]
    output_location: NotRequired["aws_sdk_cleanroomsml.types.s3_path.S3Path"]
    """<p>The Amazon S3 bucket where the audience export is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceExportJobSummary) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["name"] = value["name"]
    out["audienceGenerationJobArn"] = value["audience_generation_job_arn"]
    import aws_sdk_cleanroomsml.types.audience_size

    out["audienceSize"] = aws_sdk_cleanroomsml.types.audience_size.serialize_json(
        value["audience_size"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_cleanroomsml.types.audience_export_job_status

    out["status"] = (
        aws_sdk_cleanroomsml.types.audience_export_job_status.serialize_json(
            value["status"]
        )
    )
    if "status_details" in value:
        import aws_sdk_cleanroomsml.types.status_details

        out["statusDetails"] = aws_sdk_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    if "output_location" in value:
        out["outputLocation"] = value["output_location"]
    return out


def deserialize_json(data: dict) -> AudienceExportJobSummary:
    out: AudienceExportJobSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("AudienceExportJobSummary.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
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
        import aws_sdk_cleanroomsml.types.audience_size

        out["audience_size"] = (
            aws_sdk_cleanroomsml.types.audience_size.deserialize_json(
                data["audienceSize"]
            )
        )
    else:
        raise DeserializationError("AudienceExportJobSummary.audience_size required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_cleanroomsml.types.audience_export_job_status

        out["status"] = (
            aws_sdk_cleanroomsml.types.audience_export_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AudienceExportJobSummary.status required")
    if "statusDetails" in data:
        import aws_sdk_cleanroomsml.types.status_details

        out["status_details"] = (
            aws_sdk_cleanroomsml.types.status_details.deserialize_json(
                data["statusDetails"]
            )
        )
    if "outputLocation" in data:
        out["output_location"] = data["outputLocation"]
    return out
