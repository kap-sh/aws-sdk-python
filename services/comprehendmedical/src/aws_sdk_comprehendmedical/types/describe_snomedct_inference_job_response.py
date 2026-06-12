"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#DescribeSNOMEDCTInferenceJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties


class DescribeSNOMEDCTInferenceJobResponse(TypedDict):
    comprehend_medical_async_job_properties: NotRequired[
        "aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties.ComprehendMedicalAsyncJobProperties"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSNOMEDCTInferenceJobResponse) -> dict:
    out: dict = {}
    if "comprehend_medical_async_job_properties" in value:
        import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties

        out["ComprehendMedicalAsyncJobProperties"] = (
            aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties.serialize_aws_json_1_1(
                value["comprehend_medical_async_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSNOMEDCTInferenceJobResponse:
    out: DescribeSNOMEDCTInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if "ComprehendMedicalAsyncJobProperties" in data:
        import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties

        out["comprehend_medical_async_job_properties"] = (
            aws_sdk_comprehendmedical.types.comprehend_medical_async_job_properties.deserialize_aws_json_1_1(
                data["ComprehendMedicalAsyncJobProperties"]
            )
        )
    return out
