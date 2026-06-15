"""Generated from Smithy shape ``com.amazonaws.connect#CreatePromptRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.common_name_length127
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.prompt_description
    import aws_sdk_connect.types.s3_uri
    import aws_sdk_connect.types.tag_map


class CreatePromptRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "aws_sdk_connect.types.common_name_length127.CommonNameLength127"
    """<p>The name of the prompt.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.prompt_description.PromptDescription"
    ]
    """<p>The description of the prompt.</p>"""
    s3_uri: "aws_sdk_connect.types.s3_uri.S3Uri"
    r"""<p>The URI for the S3 bucket where the prompt is stored. You can provide S3 pre-signed URLs returned by the <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_GetPromptFile.html\">GetPromptFile</a> API instead of providing S3 URIs.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePromptRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["S3Uri"] = value["s3_uri"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePromptRequest:
    out: CreatePromptRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreatePromptRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("CreatePromptRequest.s3_uri required")
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
