"""Generated from Smithy shape ``com.amazonaws.m2#BatchJobIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_m2.types.file_batch_job_identifier
    import capo_m2.types.restart_batch_job_identifier
    import capo_m2.types.s3_batch_job_identifier
    import capo_m2.types.script_batch_job_identifier


class _BatchJobIdentifier_fileBatchJobIdentifier(TypedDict, closed=True):
    fileBatchJobIdentifier: (
        "capo_m2.types.file_batch_job_identifier.FileBatchJobIdentifier"
    )


class _BatchJobIdentifier_scriptBatchJobIdentifier(TypedDict, closed=True):
    scriptBatchJobIdentifier: (
        "capo_m2.types.script_batch_job_identifier.ScriptBatchJobIdentifier"
    )


class _BatchJobIdentifier_s3BatchJobIdentifier(TypedDict, closed=True):
    s3BatchJobIdentifier: "capo_m2.types.s3_batch_job_identifier.S3BatchJobIdentifier"


class _BatchJobIdentifier_restartBatchJobIdentifier(TypedDict, closed=True):
    restartBatchJobIdentifier: (
        "capo_m2.types.restart_batch_job_identifier.RestartBatchJobIdentifier"
    )


BatchJobIdentifier: TypeAlias = (
    _BatchJobIdentifier_fileBatchJobIdentifier
    | _BatchJobIdentifier_scriptBatchJobIdentifier
    | _BatchJobIdentifier_s3BatchJobIdentifier
    | _BatchJobIdentifier_restartBatchJobIdentifier
)


# --- restJson1 ser/de ---
def serialize_json(value: BatchJobIdentifier) -> dict:
    if "fileBatchJobIdentifier" in value:
        import capo_m2.types.file_batch_job_identifier

        return {
            "fileBatchJobIdentifier": capo_m2.types.file_batch_job_identifier.serialize_json(
                value["fileBatchJobIdentifier"]
            )
        }
    elif "scriptBatchJobIdentifier" in value:
        import capo_m2.types.script_batch_job_identifier

        return {
            "scriptBatchJobIdentifier": capo_m2.types.script_batch_job_identifier.serialize_json(
                value["scriptBatchJobIdentifier"]
            )
        }
    elif "s3BatchJobIdentifier" in value:
        import capo_m2.types.s3_batch_job_identifier

        return {
            "s3BatchJobIdentifier": capo_m2.types.s3_batch_job_identifier.serialize_json(
                value["s3BatchJobIdentifier"]
            )
        }
    elif "restartBatchJobIdentifier" in value:
        import capo_m2.types.restart_batch_job_identifier

        return {
            "restartBatchJobIdentifier": capo_m2.types.restart_batch_job_identifier.serialize_json(
                value["restartBatchJobIdentifier"]
            )
        }
    else:
        raise SerializationError("BatchJobIdentifier: no variant present")


def deserialize_json(data: dict) -> BatchJobIdentifier:
    if "fileBatchJobIdentifier" in data:
        import capo_m2.types.file_batch_job_identifier

        return {
            "fileBatchJobIdentifier": capo_m2.types.file_batch_job_identifier.deserialize_json(
                data["fileBatchJobIdentifier"]
            )
        }
    elif "scriptBatchJobIdentifier" in data:
        import capo_m2.types.script_batch_job_identifier

        return {
            "scriptBatchJobIdentifier": capo_m2.types.script_batch_job_identifier.deserialize_json(
                data["scriptBatchJobIdentifier"]
            )
        }
    elif "s3BatchJobIdentifier" in data:
        import capo_m2.types.s3_batch_job_identifier

        return {
            "s3BatchJobIdentifier": capo_m2.types.s3_batch_job_identifier.deserialize_json(
                data["s3BatchJobIdentifier"]
            )
        }
    elif "restartBatchJobIdentifier" in data:
        import capo_m2.types.restart_batch_job_identifier

        return {
            "restartBatchJobIdentifier": capo_m2.types.restart_batch_job_identifier.deserialize_json(
                data["restartBatchJobIdentifier"]
            )
        }
    else:
        raise DeserializationError("BatchJobIdentifier: no recognized variant key")
