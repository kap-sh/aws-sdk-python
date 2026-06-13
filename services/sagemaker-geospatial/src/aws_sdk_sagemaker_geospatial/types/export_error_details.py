"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportErrorDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.export_error_details_output


class ExportErrorDetails(TypedDict):
    export_results: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.export_error_details_output.ExportErrorDetailsOutput"
    ]
    """<p>The structure for returning the export error details while exporting results of an Earth Observation job.</p>"""
    export_source_images: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.export_error_details_output.ExportErrorDetailsOutput"
    ]
    """<p>The structure for returning the export error details while exporting the source images of an Earth Observation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportErrorDetails) -> dict:
    out: dict = {}
    if "export_results" in value:
        import aws_sdk_sagemaker_geospatial.types.export_error_details_output

        out["ExportResults"] = (
            aws_sdk_sagemaker_geospatial.types.export_error_details_output.serialize_json(
                value["export_results"]
            )
        )
    if "export_source_images" in value:
        import aws_sdk_sagemaker_geospatial.types.export_error_details_output

        out["ExportSourceImages"] = (
            aws_sdk_sagemaker_geospatial.types.export_error_details_output.serialize_json(
                value["export_source_images"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExportErrorDetails:
    out: ExportErrorDetails = {}  # type: ignore[typeddict-item]
    if "ExportResults" in data:
        import aws_sdk_sagemaker_geospatial.types.export_error_details_output

        out["export_results"] = (
            aws_sdk_sagemaker_geospatial.types.export_error_details_output.deserialize_json(
                data["ExportResults"]
            )
        )
    if "ExportSourceImages" in data:
        import aws_sdk_sagemaker_geospatial.types.export_error_details_output

        out["export_source_images"] = (
            aws_sdk_sagemaker_geospatial.types.export_error_details_output.deserialize_json(
                data["ExportSourceImages"]
            )
        )
    return out
