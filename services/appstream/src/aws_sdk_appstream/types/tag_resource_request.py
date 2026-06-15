"""Generated from Smithy shape ``com.amazonaws.appstream#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.tags


class TagResourceRequest(TypedDict):
    resource_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: NotRequired["aws_sdk_appstream.types.tags.Tags"]
    r"""<p>The tags to associate. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=. </p> <p>If you do not specify a value, the value is set to an empty string.</p> <p>Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters: </p> <p>_ . : / = + \ - @</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import aws_sdk_appstream.types.tags

        out["Tags"] = aws_sdk_appstream.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Tags" in data:
        import aws_sdk_appstream.types.tags

        out["tags"] = aws_sdk_appstream.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
