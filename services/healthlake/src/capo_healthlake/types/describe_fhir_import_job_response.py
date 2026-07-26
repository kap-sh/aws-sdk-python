"""Generated from Smithy shape ``com.amazonaws.healthlake#DescribeFHIRImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.import_job_properties


class DescribeFHIRImportJobResponse(TypedDict, closed=True):
    import_job_properties: (
        "capo_healthlake.types.import_job_properties.ImportJobProperties"
    )
    """<p>The import job properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFHIRImportJobResponse) -> dict:
    out: dict = {}
    import capo_healthlake.types.import_job_properties

    out["ImportJobProperties"] = (
        capo_healthlake.types.import_job_properties.serialize_aws_json_1_0(
            value["import_job_properties"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFHIRImportJobResponse:
    out: DescribeFHIRImportJobResponse = {}  # type: ignore[typeddict-item]
    if "ImportJobProperties" in data:
        import capo_healthlake.types.import_job_properties

        out["import_job_properties"] = (
            capo_healthlake.types.import_job_properties.deserialize_aws_json_1_0(
                data["ImportJobProperties"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeFHIRImportJobResponse.import_job_properties required"
        )
    return out
