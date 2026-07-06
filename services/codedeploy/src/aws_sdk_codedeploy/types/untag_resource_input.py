"""Generated from Smithy shape ``com.amazonaws.codedeploy#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.arn
    import aws_sdk_codedeploy.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_codedeploy.types.arn.Arn"
    """<p> The Amazon Resource Name (ARN) that specifies from which resource to disassociate the tags with the keys in the <code>TagKeys</code> input parameter. </p>"""
    tag_keys: "aws_sdk_codedeploy.types.tag_key_list.TagKeyList"
    """<p> A list of keys of <code>Tag</code> objects. The <code>Tag</code> objects identified by the keys are disassociated from the resource specified by the <code>ResourceArn</code> input parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_codedeploy.types.tag_key_list

    out["TagKeys"] = aws_sdk_codedeploy.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_codedeploy.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_codedeploy.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
