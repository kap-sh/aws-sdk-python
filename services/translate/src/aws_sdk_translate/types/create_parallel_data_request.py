"""Generated from Smithy shape ``com.amazonaws.translate#CreateParallelDataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.client_token_string
    import aws_sdk_translate.types.description
    import aws_sdk_translate.types.encryption_key
    import aws_sdk_translate.types.parallel_data_config
    import aws_sdk_translate.types.resource_name
    import aws_sdk_translate.types.tag_list


class CreateParallelDataRequest(TypedDict):
    name: "aws_sdk_translate.types.resource_name.ResourceName"
    """<p>A custom name for the parallel data resource in Amazon Translate. You must assign a name that is unique in the account and region.</p>"""
    description: NotRequired["aws_sdk_translate.types.description.Description"]
    """<p>A custom description for the parallel data resource in Amazon Translate.</p>"""
    parallel_data_config: (
        "aws_sdk_translate.types.parallel_data_config.ParallelDataConfig"
    )
    """<p>Specifies the format and S3 location of the parallel data input file.</p>"""
    encryption_key: NotRequired["aws_sdk_translate.types.encryption_key.EncryptionKey"]
    client_token: "aws_sdk_translate.types.client_token_string.ClientTokenString"
    """<p>A unique identifier for the request. This token is automatically generated when you use Amazon Translate through an AWS SDK.</p>"""
    tags: NotRequired["aws_sdk_translate.types.tag_list.TagList"]
    r"""<p>Tags to be associated with this resource. A tag is a key-value pair that adds metadata to a resource. Each tag key for the resource must be unique. For more information, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/tagging.html\"> Tagging your resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateParallelDataRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_translate.types.parallel_data_config

    out["ParallelDataConfig"] = (
        aws_sdk_translate.types.parallel_data_config.serialize_aws_json_1_1(
            value["parallel_data_config"]
        )
    )
    if "encryption_key" in value:
        import aws_sdk_translate.types.encryption_key

        out["EncryptionKey"] = (
            aws_sdk_translate.types.encryption_key.serialize_aws_json_1_1(
                value["encryption_key"]
            )
        )
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_translate.types.tag_list

        out["Tags"] = aws_sdk_translate.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateParallelDataRequest:
    out: CreateParallelDataRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateParallelDataRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ParallelDataConfig" in data:
        import aws_sdk_translate.types.parallel_data_config

        out["parallel_data_config"] = (
            aws_sdk_translate.types.parallel_data_config.deserialize_aws_json_1_1(
                data["ParallelDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateParallelDataRequest.parallel_data_config required"
        )
    if "EncryptionKey" in data:
        import aws_sdk_translate.types.encryption_key

        out["encryption_key"] = (
            aws_sdk_translate.types.encryption_key.deserialize_aws_json_1_1(
                data["EncryptionKey"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateParallelDataRequest.client_token required")
    if "Tags" in data:
        import aws_sdk_translate.types.tag_list

        out["tags"] = aws_sdk_translate.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
