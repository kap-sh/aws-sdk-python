"""Generated from Smithy shape ``com.amazonaws.datazone#AwsAccount``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.aws_account_id
    import capo_datazone.types.parameter_store_path


class _AwsAccount_awsAccountId(TypedDict, closed=True):
    awsAccountId: "capo_datazone.types.aws_account_id.AwsAccountId"


class _AwsAccount_awsAccountIdPath(TypedDict, closed=True):
    awsAccountIdPath: "capo_datazone.types.parameter_store_path.ParameterStorePath"


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
