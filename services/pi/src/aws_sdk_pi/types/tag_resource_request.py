"""Generated from Smithy shape ``com.amazonaws.pi#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.amazon_resource_name
    import aws_sdk_pi.types.service_type
    import aws_sdk_pi.types.tag_list


class TagResourceRequest(TypedDict):
    service_type: "aws_sdk_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>"""
    resource_arn: "aws_sdk_pi.types.amazon_resource_name.AmazonResourceName"
    r"""<p>The Amazon RDS Performance Insights resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing\"> Constructing an RDS Amazon Resource Name (ARN)</a>.</p>"""
    tags: "aws_sdk_pi.types.tag_list.TagList"
    """<p>The metadata assigned to an Amazon RDS resource consisting of a key-value pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.service_type

    out["ServiceType"] = aws_sdk_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_pi.types.tag_list

    out["Tags"] = aws_sdk_pi.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        import aws_sdk_pi.types.service_type

        out["service_type"] = aws_sdk_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError("TagResourceRequest.service_type required")
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_pi.types.tag_list

        out["tags"] = aws_sdk_pi.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
