"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#UpdateDatabaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.resource_name
    import aws_sdk_timestream_write.types.string_value2048


class UpdateDatabaseRequest(TypedDict):
    database_name: "aws_sdk_timestream_write.types.resource_name.ResourceName"
    """<p> The name of the database. </p>"""
    kms_key_id: "aws_sdk_timestream_write.types.string_value2048.StringValue2048"
    """<p> The identifier of the new KMS key (<code>KmsKeyId</code>) to be used to encrypt the data stored in the database. If the <code>KmsKeyId</code> currently registered with the database is the same as the <code>KmsKeyId</code> in the request, there will not be any update. </p> <p>You can specify the <code>KmsKeyId</code> using any of the following:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias ARN: <code>arn:aws:kms:us-east-1:111122223333:alias/ExampleAlias</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDatabaseRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDatabaseRequest:
    out: UpdateDatabaseRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("UpdateDatabaseRequest.database_name required")
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    else:
        raise DeserializationError("UpdateDatabaseRequest.kms_key_id required")
    return out
