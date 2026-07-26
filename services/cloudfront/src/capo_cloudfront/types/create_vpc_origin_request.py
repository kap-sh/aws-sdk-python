"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateVpcOriginRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.tags
    import capo_cloudfront.types.vpc_origin_endpoint_config


class CreateVpcOriginRequest(TypedDict, closed=True):
    vpc_origin_endpoint_config: (
        "capo_cloudfront.types.vpc_origin_endpoint_config.VpcOriginEndpointConfig"
    )
    """<p>The VPC origin endpoint configuration.</p>"""
    tags: NotRequired["capo_cloudfront.types.tags.Tags"]


# --- restXml ser/de ---
def serialize_xml(value: CreateVpcOriginRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.vpc_origin_endpoint_config

    capo_cloudfront.types.vpc_origin_endpoint_config.serialize_xml(
        value["vpc_origin_endpoint_config"], el, "VpcOriginEndpointConfig"
    )
    if "tags" in value:
        import capo_cloudfront.types.tags

        capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateVpcOriginRequest:
    out: CreateVpcOriginRequest = {}  # type: ignore[typeddict-item]
    child_vpc_origin_endpoint_config = el.find("VpcOriginEndpointConfig")
    if child_vpc_origin_endpoint_config is not None:
        import capo_cloudfront.types.vpc_origin_endpoint_config

        out["vpc_origin_endpoint_config"] = (
            capo_cloudfront.types.vpc_origin_endpoint_config.deserialize_xml(
                child_vpc_origin_endpoint_config
            )
        )
    else:
        raise DeserializationError(
            "CreateVpcOriginRequest.vpc_origin_endpoint_config required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    return out
