"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateDatasetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.dataset_name
    import aws_sdk_lookoutequipment.types.dataset_schema
    import aws_sdk_lookoutequipment.types.idempotence_token
    import aws_sdk_lookoutequipment.types.name_or_arn
    import aws_sdk_lookoutequipment.types.tag_list


class CreateDatasetRequest(TypedDict):
    dataset_name: "aws_sdk_lookoutequipment.types.dataset_name.DatasetName"
    """<p>The name of the dataset being created. </p>"""
    dataset_schema: NotRequired[
        "aws_sdk_lookoutequipment.types.dataset_schema.DatasetSchema"
    ]
    """<p>A JSON description of the data that is in each time series dataset, including names, column names, and data types. </p>"""
    server_side_kms_key_id: NotRequired[
        "aws_sdk_lookoutequipment.types.name_or_arn.NameOrArn"
    ]
    """<p>Provides the identifier of the KMS key used to encrypt dataset data by Amazon Lookout for Equipment. </p>"""
    client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p> A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>"""
    tags: NotRequired["aws_sdk_lookoutequipment.types.tag_list.TagList"]
    """<p>Any tags associated with the ingested data described in the dataset. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    out["DatasetName"] = value["dataset_name"]
    if "dataset_schema" in value:
        import aws_sdk_lookoutequipment.types.dataset_schema

        out["DatasetSchema"] = (
            aws_sdk_lookoutequipment.types.dataset_schema.serialize_aws_json_1_0(
                value["dataset_schema"]
            )
        )
    if "server_side_kms_key_id" in value:
        out["ServerSideKmsKeyId"] = value["server_side_kms_key_id"]
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_lookoutequipment.types.tag_list

        out["Tags"] = aws_sdk_lookoutequipment.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_name required")
    if "DatasetSchema" in data:
        import aws_sdk_lookoutequipment.types.dataset_schema

        out["dataset_schema"] = (
            aws_sdk_lookoutequipment.types.dataset_schema.deserialize_aws_json_1_0(
                data["DatasetSchema"]
            )
        )
    if "ServerSideKmsKeyId" in data:
        out["server_side_kms_key_id"] = data["ServerSideKmsKeyId"]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateDatasetRequest.client_token required")
    if "Tags" in data:
        import aws_sdk_lookoutequipment.types.tag_list

        out["tags"] = aws_sdk_lookoutequipment.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
