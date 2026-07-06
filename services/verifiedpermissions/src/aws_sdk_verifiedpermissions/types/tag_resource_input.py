"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.amazon_resource_name
    import aws_sdk_verifiedpermissions.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_verifiedpermissions.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the resource that you're adding tags to.</p>"""
    tags: "aws_sdk_verifiedpermissions.types.tag_map.TagMap"
    """<p>The list of key-value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_verifiedpermissions.types.tag_map

    out["tags"] = aws_sdk_verifiedpermissions.types.tag_map.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "tags" in data:
        import aws_sdk_verifiedpermissions.types.tag_map

        out["tags"] = (
            aws_sdk_verifiedpermissions.types.tag_map.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
