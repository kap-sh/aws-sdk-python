"""Generated from Smithy shape ``com.amazonaws.datazone#AwsAccount``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.parameter_store_path


class _AwsAccount_awsAccountId(TypedDict):
    awsAccountId: "aws_sdk_datazone.types.aws_account_id.AwsAccountId"


class _AwsAccount_awsAccountIdPath(TypedDict):
    awsAccountIdPath: "aws_sdk_datazone.types.parameter_store_path.ParameterStorePath"


AwsAccount: TypeAlias = _AwsAccount_awsAccountId | _AwsAccount_awsAccountIdPath


# --- restJson1 ser/de ---
def serialize_json(value: AwsAccount) -> dict:
    if "awsAccountId" in value:
        return {"awsAccountId": value["awsAccountId"]}
    elif "awsAccountIdPath" in value:
        return {"awsAccountIdPath": value["awsAccountIdPath"]}
    else:
        raise SerializationError("AwsAccount: no variant present")


def deserialize_json(data: dict) -> AwsAccount:
    if "awsAccountId" in data:
        return {"awsAccountId": data["awsAccountId"]}
    elif "awsAccountIdPath" in data:
        return {"awsAccountIdPath": data["awsAccountIdPath"]}
    else:
        raise DeserializationError("AwsAccount: no recognized variant key")
