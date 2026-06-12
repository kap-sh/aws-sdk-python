"""Generated from Smithy shape ``com.amazonaws.connect#Prompt``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.common_name_length127
    import aws_sdk_connect.types.prompt_description
    import aws_sdk_connect.types.prompt_id
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class Prompt(TypedDict):
    prompt_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the prompt.</p>"""
    prompt_id: NotRequired["aws_sdk_connect.types.prompt_id.PromptId"]
    """<p>A unique identifier for the prompt.</p>"""
    name: NotRequired["aws_sdk_connect.types.common_name_length127.CommonNameLength127"]
    """<p>The name of the prompt.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.prompt_description.PromptDescription"
    ]
    """<p>The description of the prompt.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Prompt) -> dict:
    out: dict = {}
    if "prompt_arn" in value:
        out["PromptARN"] = value["prompt_arn"]
    if "prompt_id" in value:
        out["PromptId"] = value["prompt_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> Prompt:
    out: Prompt = {}  # type: ignore[typeddict-item]
    if "PromptARN" in data:
        out["prompt_arn"] = data["PromptARN"]
    if "PromptId" in data:
        out["prompt_id"] = data["PromptId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
