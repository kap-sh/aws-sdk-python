"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_member_output_list
    import aws_sdk_cleanrooms.types.protected_job_s3_output


class _ProtectedJobOutput_s3(TypedDict, closed=True):
    s3: "aws_sdk_cleanrooms.types.protected_job_s3_output.ProtectedJobS3Output"


class _ProtectedJobOutput_memberList(TypedDict, closed=True):
    memberList: "aws_sdk_cleanrooms.types.protected_job_member_output_list.ProtectedJobMemberOutputList"


ProtectedJobOutput: TypeAlias = _ProtectedJobOutput_s3 | _ProtectedJobOutput_memberList


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobOutput) -> dict:
    if "s3" in value:
        import aws_sdk_cleanrooms.types.protected_job_s3_output

        return {
            "s3": aws_sdk_cleanrooms.types.protected_job_s3_output.serialize_json(
                value["s3"]
            )
        }
    elif "memberList" in value:
        import aws_sdk_cleanrooms.types.protected_job_member_output_list

        return {
            "memberList": aws_sdk_cleanrooms.types.protected_job_member_output_list.serialize_json(
                value["memberList"]
            )
        }
    else:
        raise SerializationError("ProtectedJobOutput: no variant present")


def deserialize_json(data: dict) -> ProtectedJobOutput:
    if "s3" in data:
        import aws_sdk_cleanrooms.types.protected_job_s3_output

        return {
            "s3": aws_sdk_cleanrooms.types.protected_job_s3_output.deserialize_json(
                data["s3"]
            )
        }
    elif "memberList" in data:
        import aws_sdk_cleanrooms.types.protected_job_member_output_list

        return {
            "memberList": aws_sdk_cleanrooms.types.protected_job_member_output_list.deserialize_json(
                data["memberList"]
            )
        }
    else:
        raise DeserializationError("ProtectedJobOutput: no recognized variant key")
