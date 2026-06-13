"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_query_distribute_output
    import aws_sdk_cleanrooms.types.protected_query_member_output_list
    import aws_sdk_cleanrooms.types.protected_query_s3_output


class _ProtectedQueryOutput_s3(TypedDict):
    s3: "aws_sdk_cleanrooms.types.protected_query_s3_output.ProtectedQueryS3Output"


class _ProtectedQueryOutput_memberList(TypedDict):
    memberList: "aws_sdk_cleanrooms.types.protected_query_member_output_list.ProtectedQueryMemberOutputList"


class _ProtectedQueryOutput_distribute(TypedDict):
    distribute: "aws_sdk_cleanrooms.types.protected_query_distribute_output.ProtectedQueryDistributeOutput"


ProtectedQueryOutput: TypeAlias = (
    _ProtectedQueryOutput_s3
    | _ProtectedQueryOutput_memberList
    | _ProtectedQueryOutput_distribute
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryOutput) -> dict:
    if "s3" in value:
        import aws_sdk_cleanrooms.types.protected_query_s3_output

        return {
            "s3": aws_sdk_cleanrooms.types.protected_query_s3_output.serialize_json(
                value["s3"]
            )
        }
    elif "memberList" in value:
        import aws_sdk_cleanrooms.types.protected_query_member_output_list

        return {
            "memberList": aws_sdk_cleanrooms.types.protected_query_member_output_list.serialize_json(
                value["memberList"]
            )
        }
    elif "distribute" in value:
        import aws_sdk_cleanrooms.types.protected_query_distribute_output

        return {
            "distribute": aws_sdk_cleanrooms.types.protected_query_distribute_output.serialize_json(
                value["distribute"]
            )
        }
    else:
        raise SerializationError("ProtectedQueryOutput: no variant present")


def deserialize_json(data: dict) -> ProtectedQueryOutput:
    if "s3" in data:
        import aws_sdk_cleanrooms.types.protected_query_s3_output

        return {
            "s3": aws_sdk_cleanrooms.types.protected_query_s3_output.deserialize_json(
                data["s3"]
            )
        }
    elif "memberList" in data:
        import aws_sdk_cleanrooms.types.protected_query_member_output_list

        return {
            "memberList": aws_sdk_cleanrooms.types.protected_query_member_output_list.deserialize_json(
                data["memberList"]
            )
        }
    elif "distribute" in data:
        import aws_sdk_cleanrooms.types.protected_query_distribute_output

        return {
            "distribute": aws_sdk_cleanrooms.types.protected_query_distribute_output.deserialize_json(
                data["distribute"]
            )
        }
    else:
        raise DeserializationError("ProtectedQueryOutput: no recognized variant key")
