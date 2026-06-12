"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ListSNOMEDCTInferenceJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties_list
    import aws_sdk_comprehendmedical.types.string


class ListSNOMEDCTInferenceJobsResponse(TypedDict):
    comprehend_medical_async_job_properties_list: NotRequired[
        "aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties_list.ComprehendMedicalAsyncJobPropertiesList"
    ]
    """<p> A list containing the properties of each job that is returned. </p>"""
    next_token: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p> Identifies the next page of results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSNOMEDCTInferenceJobsResponse) -> dict:
    out: dict = {}
    if "comprehend_medical_async_job_properties_list" in value:
        import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties_list

        out["ComprehendMedicalAsyncJobPropertiesList"] = (
            aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties_list.serialize_aws_json_1_1(
                value["comprehend_medical_async_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSNOMEDCTInferenceJobsResponse:
    out: ListSNOMEDCTInferenceJobsResponse = {}  # type: ignore[typeddict-item]
    if "ComprehendMedicalAsyncJobPropertiesList" in data:
        import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties_list

        out["comprehend_medical_async_job_properties_list"] = (
            aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties_list.deserialize_aws_json_1_1(
                data["ComprehendMedicalAsyncJobPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
