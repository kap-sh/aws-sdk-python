"""Generated from Smithy shape ``com.amazonaws.deadline#JobEntity``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.environment_details_entity
    import aws_sdk_deadline.types.job_attachment_details_entity
    import aws_sdk_deadline.types.job_details_entity
    import aws_sdk_deadline.types.step_details_entity


class _JobEntity_jobDetails(TypedDict, closed=True):
    jobDetails: "aws_sdk_deadline.types.job_details_entity.JobDetailsEntity"


class _JobEntity_jobAttachmentDetails(TypedDict, closed=True):
    jobAttachmentDetails: "aws_sdk_deadline.types.job_attachment_details_entity.JobAttachmentDetailsEntity"


class _JobEntity_stepDetails(TypedDict, closed=True):
    stepDetails: "aws_sdk_deadline.types.step_details_entity.StepDetailsEntity"


class _JobEntity_environmentDetails(TypedDict, closed=True):
    environmentDetails: (
        "aws_sdk_deadline.types.environment_details_entity.EnvironmentDetailsEntity"
    )


JobEntity: TypeAlias = (
    _JobEntity_jobDetails
    | _JobEntity_jobAttachmentDetails
    | _JobEntity_stepDetails
    | _JobEntity_environmentDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: JobEntity) -> dict:
    if "jobDetails" in value:
        import aws_sdk_deadline.types.job_details_entity

        return {
            "jobDetails": aws_sdk_deadline.types.job_details_entity.serialize_json(
                value["jobDetails"]
            )
        }
    elif "jobAttachmentDetails" in value:
        import aws_sdk_deadline.types.job_attachment_details_entity

        return {
            "jobAttachmentDetails": aws_sdk_deadline.types.job_attachment_details_entity.serialize_json(
                value["jobAttachmentDetails"]
            )
        }
    elif "stepDetails" in value:
        import aws_sdk_deadline.types.step_details_entity

        return {
            "stepDetails": aws_sdk_deadline.types.step_details_entity.serialize_json(
                value["stepDetails"]
            )
        }
    elif "environmentDetails" in value:
        import aws_sdk_deadline.types.environment_details_entity

        return {
            "environmentDetails": aws_sdk_deadline.types.environment_details_entity.serialize_json(
                value["environmentDetails"]
            )
        }
    else:
        raise SerializationError("JobEntity: no variant present")


def deserialize_json(data: dict) -> JobEntity:
    if "jobDetails" in data:
        import aws_sdk_deadline.types.job_details_entity

        return {
            "jobDetails": aws_sdk_deadline.types.job_details_entity.deserialize_json(
                data["jobDetails"]
            )
        }
    elif "jobAttachmentDetails" in data:
        import aws_sdk_deadline.types.job_attachment_details_entity

        return {
            "jobAttachmentDetails": aws_sdk_deadline.types.job_attachment_details_entity.deserialize_json(
                data["jobAttachmentDetails"]
            )
        }
    elif "stepDetails" in data:
        import aws_sdk_deadline.types.step_details_entity

        return {
            "stepDetails": aws_sdk_deadline.types.step_details_entity.deserialize_json(
                data["stepDetails"]
            )
        }
    elif "environmentDetails" in data:
        import aws_sdk_deadline.types.environment_details_entity

        return {
            "environmentDetails": aws_sdk_deadline.types.environment_details_entity.deserialize_json(
                data["environmentDetails"]
            )
        }
    else:
        raise DeserializationError("JobEntity: no recognized variant key")
