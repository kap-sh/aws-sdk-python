"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ListEntitiesDetectionV2JobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties_list
    import aws_sdk_comprehendmedical.types.string


class ListEntitiesDetectionV2JobsResponse(TypedDict, closed=True):
    comprehend_medical_async_job_properties_list: NotRequired[
        "aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties_list.ComprehendMedicalAsyncJobPropertiesList"
    ]
    """<p>A list containing the properties of each job returned.</p>"""
    next_token: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntitiesDetectionV2JobsResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ListEntitiesDetectionV2JobsResponse:
    out: ListEntitiesDetectionV2JobsResponse = {}  # type: ignore[typeddict-item]
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
