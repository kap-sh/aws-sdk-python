"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanFindingAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.account_aggregation
    import aws_sdk_imagebuilder.types.image_aggregation
    import aws_sdk_imagebuilder.types.image_pipeline_aggregation
    import aws_sdk_imagebuilder.types.vulnerability_id_aggregation


class ImageScanFindingAggregation(TypedDict):
    account_aggregation: NotRequired[
        "aws_sdk_imagebuilder.types.account_aggregation.AccountAggregation"
    ]
    """<p>Returns an object that contains severity counts based on an account ID.</p>"""
    image_aggregation: NotRequired[
        "aws_sdk_imagebuilder.types.image_aggregation.ImageAggregation"
    ]
    """<p>Returns an object that contains severity counts based on the Amazon Resource Name (ARN) for a specific image.</p>"""
    image_pipeline_aggregation: NotRequired[
        "aws_sdk_imagebuilder.types.image_pipeline_aggregation.ImagePipelineAggregation"
    ]
    """<p>Returns an object that contains severity counts based on an image pipeline ARN.</p>"""
    vulnerability_id_aggregation: NotRequired[
        "aws_sdk_imagebuilder.types.vulnerability_id_aggregation.VulnerabilityIdAggregation"
    ]
    """<p>Returns an object that contains severity counts based on vulnerability ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanFindingAggregation) -> dict:
    out: dict = {}
    if "account_aggregation" in value:
        import aws_sdk_imagebuilder.types.account_aggregation

        out["accountAggregation"] = (
            aws_sdk_imagebuilder.types.account_aggregation.serialize_json(
                value["account_aggregation"]
            )
        )
    if "image_aggregation" in value:
        import aws_sdk_imagebuilder.types.image_aggregation

        out["imageAggregation"] = (
            aws_sdk_imagebuilder.types.image_aggregation.serialize_json(
                value["image_aggregation"]
            )
        )
    if "image_pipeline_aggregation" in value:
        import aws_sdk_imagebuilder.types.image_pipeline_aggregation

        out["imagePipelineAggregation"] = (
            aws_sdk_imagebuilder.types.image_pipeline_aggregation.serialize_json(
                value["image_pipeline_aggregation"]
            )
        )
    if "vulnerability_id_aggregation" in value:
        import aws_sdk_imagebuilder.types.vulnerability_id_aggregation

        out["vulnerabilityIdAggregation"] = (
            aws_sdk_imagebuilder.types.vulnerability_id_aggregation.serialize_json(
                value["vulnerability_id_aggregation"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageScanFindingAggregation:
    out: ImageScanFindingAggregation = {}  # type: ignore[typeddict-item]
    if "accountAggregation" in data:
        import aws_sdk_imagebuilder.types.account_aggregation

        out["account_aggregation"] = (
            aws_sdk_imagebuilder.types.account_aggregation.deserialize_json(
                data["accountAggregation"]
            )
        )
    if "imageAggregation" in data:
        import aws_sdk_imagebuilder.types.image_aggregation

        out["image_aggregation"] = (
            aws_sdk_imagebuilder.types.image_aggregation.deserialize_json(
                data["imageAggregation"]
            )
        )
    if "imagePipelineAggregation" in data:
        import aws_sdk_imagebuilder.types.image_pipeline_aggregation

        out["image_pipeline_aggregation"] = (
            aws_sdk_imagebuilder.types.image_pipeline_aggregation.deserialize_json(
                data["imagePipelineAggregation"]
            )
        )
    if "vulnerabilityIdAggregation" in data:
        import aws_sdk_imagebuilder.types.vulnerability_id_aggregation

        out["vulnerability_id_aggregation"] = (
            aws_sdk_imagebuilder.types.vulnerability_id_aggregation.deserialize_json(
                data["vulnerabilityIdAggregation"]
            )
        )
    return out
