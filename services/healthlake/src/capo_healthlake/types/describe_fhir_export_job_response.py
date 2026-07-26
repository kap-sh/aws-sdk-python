"""Generated from Smithy shape ``com.amazonaws.healthlake#DescribeFHIRExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.export_job_properties


class DescribeFHIRExportJobResponse(TypedDict, closed=True):
    export_job_properties: (
        "capo_healthlake.types.export_job_properties.ExportJobProperties"
    )
    """<p>The export job properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFHIRExportJobResponse) -> dict:
    out: dict = {}
    import capo_healthlake.types.export_job_properties

    out["ExportJobProperties"] = (
        capo_healthlake.types.export_job_properties.serialize_aws_json_1_0(
            value["export_job_properties"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFHIRExportJobResponse:
    out: DescribeFHIRExportJobResponse = {}  # type: ignore[typeddict-item]
    if "ExportJobProperties" in data:
        import capo_healthlake.types.export_job_properties

        out["export_job_properties"] = (
            capo_healthlake.types.export_job_properties.deserialize_aws_json_1_0(
                data["ExportJobProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeFHIRExportJobResponse.export_job_properties required"
        )
    return out
