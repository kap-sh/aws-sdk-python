"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetMarketplaceResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_builder_arn
    import aws_sdk_imagebuilder.types.marketplace_resource_location
    import aws_sdk_imagebuilder.types.marketplace_resource_type


class GetMarketplaceResourceRequest(TypedDict, closed=True):
    resource_type: (
        "aws_sdk_imagebuilder.types.marketplace_resource_type.MarketplaceResourceType"
    )
    """<p>Specifies which type of Amazon Web Services Marketplace resource Image Builder retrieves.</p>"""
    resource_arn: "aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies an Amazon Web Services Marketplace resource.</p>"""
    resource_location: NotRequired[
        "aws_sdk_imagebuilder.types.marketplace_resource_location.MarketplaceResourceLocation"
    ]
    """<p>The bucket path that you can specify to download the resource from Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMarketplaceResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_imagebuilder.types.marketplace_resource_type

    out["resourceType"] = (
        aws_sdk_imagebuilder.types.marketplace_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    out["resourceArn"] = value["resource_arn"]
    if "resource_location" in value:
        out["resourceLocation"] = value["resource_location"]
    return out


def deserialize_json(data: dict) -> GetMarketplaceResourceRequest:
    out: GetMarketplaceResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import aws_sdk_imagebuilder.types.marketplace_resource_type

        out["resource_type"] = (
            aws_sdk_imagebuilder.types.marketplace_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError(
            "GetMarketplaceResourceRequest.resource_type required"
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "GetMarketplaceResourceRequest.resource_arn required"
        )
    if "resourceLocation" in data:
        out["resource_location"] = data["resourceLocation"]
    return out
