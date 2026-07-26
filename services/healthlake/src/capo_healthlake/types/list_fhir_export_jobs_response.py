"""Generated from Smithy shape ``com.amazonaws.healthlake#ListFHIRExportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.export_job_properties_list
    import capo_healthlake.types.next_token


class ListFHIRExportJobsResponse(TypedDict, closed=True):
    export_job_properties_list: (
        "capo_healthlake.types.export_job_properties_list.ExportJobPropertiesList"
    )
    """<p>The properties of listed FHIR export jobs.</p>"""
    next_token: NotRequired["capo_healthlake.types.next_token.NextToken"]
    """<p>The pagination token used to identify the next page of results to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFHIRExportJobsResponse) -> dict:
    out: dict = {}
    import capo_healthlake.types.export_job_properties_list

    out["ExportJobPropertiesList"] = (
        capo_healthlake.types.export_job_properties_list.serialize_aws_json_1_0(
            value["export_job_properties_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFHIRExportJobsResponse:
    out: ListFHIRExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "ExportJobPropertiesList" in data:
        import capo_healthlake.types.export_job_properties_list

        out["export_job_properties_list"] = (
            capo_healthlake.types.export_job_properties_list.deserialize_aws_json_1_0(
                data["ExportJobPropertiesList"]
            )
        )
    else:
        raise DeserializationError(
            "ListFHIRExportJobsResponse.export_job_properties_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
