"""Generated from Smithy shape ``com.amazonaws.servicequotas#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_service_quotas.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.amazon_resource_name
    import aws_sdk_service_quotas.types.input_tags


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_service_quotas.types.amazon_resource_name.AmazonResourceName"
    r"""<p>The Amazon Resource Name (ARN) for the applied quota. You can get this information by using the Service Quotas console, or by listing the quotas using the <a href=\"https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html\">list-service-quotas</a> CLI command or the <a href=\"https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html\">ListServiceQuotas</a> Amazon Web Services API operation.</p>"""
    tags: "aws_sdk_service_quotas.types.input_tags.InputTags"
    """<p>The tags that you want to add to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_service_quotas.types.input_tags

    out["Tags"] = aws_sdk_service_quotas.types.input_tags.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_service_quotas.types.input_tags

        out["tags"] = aws_sdk_service_quotas.types.input_tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
