"""Generated from Smithy shape ``com.amazonaws.ecs#Attribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.target_type


class Attribute(TypedDict):
    name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the attribute. The <code>name</code> must contain between 1 and 128 characters. The name may contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (_), forward slashes (/), back slashes (\), or periods (.).</p>"""
    value: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The value of the attribute. The <code>value</code> must contain between 1 and 128 characters. It can contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (_), periods (.), at signs (@), forward slashes (/), back slashes (\), colons (:), or spaces. The value can't start or end with a space.</p>"""
    target_type: NotRequired["aws_sdk_ecs.types.target_type.TargetType"]
    """<p>The type of the target to attach the attribute with. This parameter is required if you use the short form ID for a resource instead of the full ARN.</p>"""
    target_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attribute) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    if "target_type" in value:
        import aws_sdk_ecs.types.target_type

        out["targetType"] = aws_sdk_ecs.types.target_type.serialize_aws_json_1_1(
            value["target_type"]
        )
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Attribute.name required")
    if "value" in data:
        out["value"] = data["value"]
    if "targetType" in data:
        import aws_sdk_ecs.types.target_type

        out["target_type"] = aws_sdk_ecs.types.target_type.deserialize_aws_json_1_1(
            data["targetType"]
        )
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    return out
