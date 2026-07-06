"""Generated from Smithy shape ``com.amazonaws.deadline#GetJobEntityError``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.environment_details_error
    import aws_sdk_deadline.types.job_attachment_details_error
    import aws_sdk_deadline.types.job_details_error
    import aws_sdk_deadline.types.step_details_error


class _GetJobEntityError_jobDetails(TypedDict, closed=True):
    jobDetails: "aws_sdk_deadline.types.job_details_error.JobDetailsError"


class _GetJobEntityError_jobAttachmentDetails(TypedDict, closed=True):
    jobAttachmentDetails: (
        "aws_sdk_deadline.types.job_attachment_details_error.JobAttachmentDetailsError"
    )


class _GetJobEntityError_stepDetails(TypedDict, closed=True):
    stepDetails: "aws_sdk_deadline.types.step_details_error.StepDetailsError"


class _GetJobEntityError_environmentDetails(TypedDict, closed=True):
    environmentDetails: (
        "aws_sdk_deadline.types.environment_details_error.EnvironmentDetailsError"
    )


GetJobEntityError: TypeAlias = (
    _GetJobEntityError_jobDetails
    | _GetJobEntityError_jobAttachmentDetails
    | _GetJobEntityError_stepDetails
    | _GetJobEntityError_environmentDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: GetJobEntityError) -> dict:
    if "jobDetails" in value:
        import aws_sdk_deadline.types.job_details_error

        return {
            "jobDetails": aws_sdk_deadline.types.job_details_error.serialize_json(
                value["jobDetails"]
            )
        }
    elif "jobAttachmentDetails" in value:
        import aws_sdk_deadline.types.job_attachment_details_error

        return {
            "jobAttachmentDetails": aws_sdk_deadline.types.job_attachment_details_error.serialize_json(
                value["jobAttachmentDetails"]
            )
        }
    elif "stepDetails" in value:
        import aws_sdk_deadline.types.step_details_error

        return {
            "stepDetails": aws_sdk_deadline.types.step_details_error.serialize_json(
                value["stepDetails"]
            )
        }
    elif "environmentDetails" in value:
        import aws_sdk_deadline.types.environment_details_error

        return {
            "environmentDetails": aws_sdk_deadline.types.environment_details_error.serialize_json(
                value["environmentDetails"]
            )
        }
    else:
        raise SerializationError("GetJobEntityError: no variant present")


def deserialize_json(data: dict) -> GetJobEntityError:
    if "jobDetails" in data:
        import aws_sdk_deadline.types.job_details_error

        return {
            "jobDetails": aws_sdk_deadline.types.job_details_error.deserialize_json(
                data["jobDetails"]
            )
        }
    elif "jobAttachmentDetails" in data:
        import aws_sdk_deadline.types.job_attachment_details_error

        return {
            "jobAttachmentDetails": aws_sdk_deadline.types.job_attachment_details_error.deserialize_json(
                data["jobAttachmentDetails"]
            )
        }
    elif "stepDetails" in data:
        import aws_sdk_deadline.types.step_details_error

        return {
            "stepDetails": aws_sdk_deadline.types.step_details_error.deserialize_json(
                data["stepDetails"]
            )
        }
    elif "environmentDetails" in data:
        import aws_sdk_deadline.types.environment_details_error

        return {
            "environmentDetails": aws_sdk_deadline.types.environment_details_error.deserialize_json(
                data["environmentDetails"]
            )
        }
    else:
        raise DeserializationError("GetJobEntityError: no recognized variant key")
