"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanFindingsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.filter_name
    import aws_sdk_imagebuilder.types.image_scan_findings_filter_values


class ImageScanFindingsFilter(TypedDict, closed=True):
    name: NotRequired["aws_sdk_imagebuilder.types.filter_name.FilterName"]
    """<p>The name of the image scan finding filter. Filter names are case-sensitive.</p>"""
    values: NotRequired[
        "aws_sdk_imagebuilder.types.image_scan_findings_filter_values.ImageScanFindingsFilterValues"
    ]
    """<p>The filter values. Filter values are case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanFindingsFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "values" in value:
        import aws_sdk_imagebuilder.types.image_scan_findings_filter_values

        out["values"] = (
            aws_sdk_imagebuilder.types.image_scan_findings_filter_values.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageScanFindingsFilter:
    out: ImageScanFindingsFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "values" in data:
        import aws_sdk_imagebuilder.types.image_scan_findings_filter_values

        out["values"] = (
            aws_sdk_imagebuilder.types.image_scan_findings_filter_values.deserialize_json(
                data["values"]
            )
        )
    return out
