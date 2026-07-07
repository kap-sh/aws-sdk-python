"""Generated from Smithy shape ``com.amazonaws.deadline#JobEntityIdentifiersUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.environment_details_identifiers
    import aws_sdk_deadline.types.job_attachment_details_identifiers
    import aws_sdk_deadline.types.job_details_identifiers
    import aws_sdk_deadline.types.step_details_identifiers


class _JobEntityIdentifiersUnion_jobDetails(TypedDict, closed=True):
    jobDetails: "aws_sdk_deadline.types.job_details_identifiers.JobDetailsIdentifiers"


class _JobEntityIdentifiersUnion_jobAttachmentDetails(TypedDict, closed=True):
    jobAttachmentDetails: "aws_sdk_deadline.types.job_attachment_details_identifiers.JobAttachmentDetailsIdentifiers"


class _JobEntityIdentifiersUnion_stepDetails(TypedDict, closed=True):
    stepDetails: (
        "aws_sdk_deadline.types.step_details_identifiers.StepDetailsIdentifiers"
    )


class _JobEntityIdentifiersUnion_environmentDetails(TypedDict, closed=True):
    environmentDetails: "aws_sdk_deadline.types.environment_details_identifiers.EnvironmentDetailsIdentifiers"


JobEntityIdentifiersUnion: TypeAlias = (
    _JobEntityIdentifiersUnion_jobDetails
    | _JobEntityIdentifiersUnion_jobAttachmentDetails
    | _JobEntityIdentifiersUnion_stepDetails
    | _JobEntityIdentifiersUnion_environmentDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: JobEntityIdentifiersUnion) -> dict:
    if "jobDetails" in value:
        import aws_sdk_deadline.types.job_details_identifiers

        return {
            "jobDetails": aws_sdk_deadline.types.job_details_identifiers.serialize_json(
                value["jobDetails"]
            )
        }
    elif "jobAttachmentDetails" in value:
        import aws_sdk_deadline.types.job_attachment_details_identifiers

        return {
            "jobAttachmentDetails": aws_sdk_deadline.types.job_attachment_details_identifiers.serialize_json(
                value["jobAttachmentDetails"]
            )
        }
    elif "stepDetails" in value:
        import aws_sdk_deadline.types.step_details_identifiers

        return {
            "stepDetails": aws_sdk_deadline.types.step_details_identifiers.serialize_json(
                value["stepDetails"]
            )
        }
    elif "environmentDetails" in value:
        import aws_sdk_deadline.types.environment_details_identifiers

        return {
            "environmentDetails": aws_sdk_deadline.types.environment_details_identifiers.serialize_json(
                value["environmentDetails"]
            )
        }
    else:
        raise SerializationError("JobEntityIdentifiersUnion: no variant present")


def deserialize_json(data: dict) -> JobEntityIdentifiersUnion:
    if "jobDetails" in data:
        import aws_sdk_deadline.types.job_details_identifiers

        return {
            "jobDetails": aws_sdk_deadline.types.job_details_identifiers.deserialize_json(
                data["jobDetails"]
            )
        }
    elif "jobAttachmentDetails" in data:
        import aws_sdk_deadline.types.job_attachment_details_identifiers

        return {
            "jobAttachmentDetails": aws_sdk_deadline.types.job_attachment_details_identifiers.deserialize_json(
                data["jobAttachmentDetails"]
            )
        }
    elif "stepDetails" in data:
        import aws_sdk_deadline.types.step_details_identifiers

        return {
            "stepDetails": aws_sdk_deadline.types.step_details_identifiers.deserialize_json(
                data["stepDetails"]
            )
        }
    elif "environmentDetails" in data:
        import aws_sdk_deadline.types.environment_details_identifiers

        return {
            "environmentDetails": aws_sdk_deadline.types.environment_details_identifiers.deserialize_json(
                data["environmentDetails"]
            )
        }
    else:
        raise DeserializationError(
            "JobEntityIdentifiersUnion: no recognized variant key"
        )
