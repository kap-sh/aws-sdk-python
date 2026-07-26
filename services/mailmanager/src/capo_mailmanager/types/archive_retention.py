"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveRetention``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.retention_period


class _ArchiveRetention_RetentionPeriod(TypedDict, closed=True):
    RetentionPeriod: "capo_mailmanager.types.retention_period.RetentionPeriod"


ArchiveRetention: TypeAlias = _ArchiveRetention_RetentionPeriod


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveRetention) -> dict:
    if "RetentionPeriod" in value:
        import capo_mailmanager.types.retention_period

        return {
            "RetentionPeriod": capo_mailmanager.types.retention_period.serialize_aws_json_1_0(
                value["RetentionPeriod"]
            )
        }
    else:
        raise SerializationError("ArchiveRetention: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ArchiveRetention:
    if "RetentionPeriod" in data:
        import capo_mailmanager.types.retention_period

        return {
            "RetentionPeriod": capo_mailmanager.types.retention_period.deserialize_aws_json_1_0(
                data["RetentionPeriod"]
            )
        }
    else:
        raise DeserializationError("ArchiveRetention: no recognized variant key")
