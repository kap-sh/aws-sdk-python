"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.amazon_resource_name
    import aws_sdk_verifiedpermissions.types.tag_key_list


class UntagResourceInput(TypedDict):
    resource_arn: (
        "aws_sdk_verifiedpermissions.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the resource from which you are removing tags.</p>"""
    tag_keys: "aws_sdk_verifiedpermissions.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_verifiedpermissions.types.tag_key_list

    out["tagKeys"] = (
        aws_sdk_verifiedpermissions.types.tag_key_list.serialize_aws_json_1_0(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_verifiedpermissions.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_verifiedpermissions.types.tag_key_list.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
