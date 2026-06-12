"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateVpcOriginRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.tags
    import aws_sdk_cloudfront.types.vpc_origin_endpoint_config


class CreateVpcOriginRequest(TypedDict):
    vpc_origin_endpoint_config: (
        "aws_sdk_cloudfront.types.vpc_origin_endpoint_config.VpcOriginEndpointConfig"
    )
    """<p>The VPC origin endpoint configuration.</p>"""
    tags: NotRequired["aws_sdk_cloudfront.types.tags.Tags"]


# --- restXml ser/de ---
def serialize_xml(value: CreateVpcOriginRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.vpc_origin_endpoint_config

    aws_sdk_cloudfront.types.vpc_origin_endpoint_config.serialize_xml(
        value["vpc_origin_endpoint_config"], el, "VpcOriginEndpointConfig"
    )
    if "tags" in value:
        import aws_sdk_cloudfront.types.tags

        aws_sdk_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateVpcOriginRequest:
    out: CreateVpcOriginRequest = {}  # type: ignore[typeddict-item]
    child_vpc_origin_endpoint_config = el.find("VpcOriginEndpointConfig")
    if child_vpc_origin_endpoint_config is not None:
        import aws_sdk_cloudfront.types.vpc_origin_endpoint_config

        out["vpc_origin_endpoint_config"] = (
            aws_sdk_cloudfront.types.vpc_origin_endpoint_config.deserialize_xml(
                child_vpc_origin_endpoint_config
            )
        )
    else:
        raise DeserializationError(
            "CreateVpcOriginRequest.vpc_origin_endpoint_config required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudfront.types.tags

        out["tags"] = aws_sdk_cloudfront.types.tags.deserialize_xml(child_tags)
    return out
