"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetMarketplaceResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_builder_arn
    import aws_sdk_imagebuilder.types.non_empty_string


class GetMarketplaceResourceResponse(TypedDict):
    resource_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn"
    ]
    """<p>The Amazon Resource Name (ARN) for the Amazon Web Services Marketplace resource that was requested.</p>"""
    url: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The obfuscated S3 URL to download the component artifact from.</p>"""
    data: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Returns obfuscated data that contains the YAML content of the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMarketplaceResourceResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "url" in value:
        out["url"] = value["url"]
    if "data" in value:
        out["data"] = value["data"]
    return out


def deserialize_json(data: dict) -> GetMarketplaceResourceResponse:
    out: GetMarketplaceResourceResponse = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "url" in data:
        out["url"] = data["url"]
    if "data" in data:
        out["data"] = data["data"]
    return out
