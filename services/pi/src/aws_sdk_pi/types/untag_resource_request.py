"""Generated from Smithy shape ``com.amazonaws.pi#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.amazon_resource_name
    import aws_sdk_pi.types.service_type
    import aws_sdk_pi.types.tag_key_list


class UntagResourceRequest(TypedDict):
    service_type: "aws_sdk_pi.types.service_type.ServiceType"
    """<p>List the tags for the Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>"""
    resource_arn: "aws_sdk_pi.types.amazon_resource_name.AmazonResourceName"
    r"""<p>The Amazon RDS Performance Insights resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing\"> Constructing an RDS Amazon Resource Name (ARN)</a>.</p>"""
    tag_keys: "aws_sdk_pi.types.tag_key_list.TagKeyList"
    """<p>The metadata assigned to an Amazon RDS Performance Insights resource consisting of a key-value pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.service_type

    out["ServiceType"] = aws_sdk_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_pi.types.tag_key_list

    out["TagKeys"] = aws_sdk_pi.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        import aws_sdk_pi.types.service_type

        out["service_type"] = aws_sdk_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.service_type required")
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_pi.types.tag_key_list

        out["tag_keys"] = aws_sdk_pi.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
