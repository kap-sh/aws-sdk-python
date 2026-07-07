"""Generated from Smithy shape ``com.amazonaws.connect#GetPromptFileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.prompt_presigned_url
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class GetPromptFileResponse(TypedDict, closed=True):
    prompt_presigned_url: NotRequired[
        "aws_sdk_connect.types.prompt_presigned_url.PromptPresignedUrl"
    ]
    """<p>A generated URL to the prompt that can be given to an unauthorized user so they can access the prompt in S3.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPromptFileResponse) -> dict:
    out: dict = {}
    if "prompt_presigned_url" in value:
        out["PromptPresignedUrl"] = value["prompt_presigned_url"]
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> GetPromptFileResponse:
    out: GetPromptFileResponse = {}  # type: ignore[typeddict-item]
    if "PromptPresignedUrl" in data:
        out["prompt_presigned_url"] = data["PromptPresignedUrl"]
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
