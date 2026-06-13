"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeOutputStream``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connecthealth.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.errors.internal_server_exception
    import aws_sdk_connecthealth.errors.validation_exception
    import aws_sdk_connecthealth.types.medical_scribe_transcript_event


class _MedicalScribeOutputStream_transcriptEvent(TypedDict):
    transcriptEvent: "aws_sdk_connecthealth.types.medical_scribe_transcript_event.MedicalScribeTranscriptEvent"


class _MedicalScribeOutputStream_internalFailureException(TypedDict):
    internalFailureException: "aws_sdk_connecthealth.errors.internal_server_exception.InternalServerException_"


class _MedicalScribeOutputStream_validationException(TypedDict):
    validationException: (
        "aws_sdk_connecthealth.errors.validation_exception.ValidationException_"
    )


MedicalScribeOutputStream: TypeAlias = (
    _MedicalScribeOutputStream_transcriptEvent
    | _MedicalScribeOutputStream_internalFailureException
    | _MedicalScribeOutputStream_validationException
)


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeOutputStream) -> dict:
    if "transcriptEvent" in value:
        import aws_sdk_connecthealth.types.medical_scribe_transcript_event

        return {
            "transcriptEvent": aws_sdk_connecthealth.types.medical_scribe_transcript_event.serialize_json(
                value["transcriptEvent"]
            )
        }
    elif "internalFailureException" in value:
        import aws_sdk_connecthealth.errors.internal_server_exception

        return {
            "internalFailureException": aws_sdk_connecthealth.errors.internal_server_exception.serialize_json(
                value["internalFailureException"]
            )
        }
    elif "validationException" in value:
        import aws_sdk_connecthealth.errors.validation_exception

        return {
            "validationException": aws_sdk_connecthealth.errors.validation_exception.serialize_json(
                value["validationException"]
            )
        }
    else:
        raise SerializationError("MedicalScribeOutputStream: no variant present")


def deserialize_json(data: dict) -> MedicalScribeOutputStream:
    if "transcriptEvent" in data:
        import aws_sdk_connecthealth.types.medical_scribe_transcript_event

        return {
            "transcriptEvent": aws_sdk_connecthealth.types.medical_scribe_transcript_event.deserialize_json(
                data["transcriptEvent"]
            )
        }
    elif "internalFailureException" in data:
        import aws_sdk_connecthealth.errors.internal_server_exception

        return {
            "internalFailureException": aws_sdk_connecthealth.errors.internal_server_exception.deserialize_json(
                data["internalFailureException"]
            )
        }
    elif "validationException" in data:
        import aws_sdk_connecthealth.errors.validation_exception

        return {
            "validationException": aws_sdk_connecthealth.errors.validation_exception.deserialize_json(
                data["validationException"]
            )
        }
    else:
        raise DeserializationError(
            "MedicalScribeOutputStream: no recognized variant key"
        )
