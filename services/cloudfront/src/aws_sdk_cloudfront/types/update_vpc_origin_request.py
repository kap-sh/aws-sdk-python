"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateVpcOriginRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.vpc_origin_endpoint_config


class UpdateVpcOriginRequest(TypedDict, closed=True):
    vpc_origin_endpoint_config: (
        "aws_sdk_cloudfront.types.vpc_origin_endpoint_config.VpcOriginEndpointConfig"
    )
    """<p>The VPC origin endpoint configuration.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The VPC origin ID.</p>"""
    if_match: "aws_sdk_cloudfront.types.string.string"
    """<p>The VPC origin to update, if a match occurs.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateVpcOriginRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.vpc_origin_endpoint_config

    aws_sdk_cloudfront.types.vpc_origin_endpoint_config.serialize_xml(
        value["vpc_origin_endpoint_config"], el, "VpcOriginEndpointConfig"
    )


def deserialize_xml(el: Element) -> UpdateVpcOriginRequest:
    out: UpdateVpcOriginRequest = {}  # type: ignore[typeddict-item]
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
            "UpdateVpcOriginRequest.vpc_origin_endpoint_config required"
        )
    return out
