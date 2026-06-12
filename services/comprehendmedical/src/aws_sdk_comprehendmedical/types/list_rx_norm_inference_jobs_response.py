"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ListRxNormInferenceJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties_list
    import aws_sdk_comprehendmedical.types.string


class ListRxNormInferenceJobsResponse(TypedDict):
    comprehend_medical_async_job_properties_list: NotRequired[
        "aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties_list.ComprehendMedicalAsyncJobPropertiesList"
    ]
    """<p>The maximum number of results to return in each page. The default is 100.</p>"""
    next_token: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRxNormInferenceJobsResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ListRxNormInferenceJobsResponse:
    out: ListRxNormInferenceJobsResponse = {}  # type: ignore[typeddict-item]
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
