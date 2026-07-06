"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetGeneratedPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.generated_policy_result
    import aws_sdk_accessanalyzer.types.job_details


class GetGeneratedPolicyResponse(TypedDict, closed=True):
    job_details: "aws_sdk_accessanalyzer.types.job_details.JobDetails"
    """<p>A <code>GeneratedPolicyDetails</code> object that contains details about the generated policy.</p>"""
    generated_policy_result: (
        "aws_sdk_accessanalyzer.types.generated_policy_result.GeneratedPolicyResult"
    )
    """<p>A <code>GeneratedPolicyResult</code> object that contains the generated policies and associated details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGeneratedPolicyResponse) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.job_details

    out["jobDetails"] = aws_sdk_accessanalyzer.types.job_details.serialize_json(
        value["job_details"]
    )
    import aws_sdk_accessanalyzer.types.generated_policy_result

    out["generatedPolicyResult"] = (
        aws_sdk_accessanalyzer.types.generated_policy_result.serialize_json(
            value["generated_policy_result"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetGeneratedPolicyResponse:
    out: GetGeneratedPolicyResponse = {}  # type: ignore[typeddict-item]
    if "jobDetails" in data:
        import aws_sdk_accessanalyzer.types.job_details

        out["job_details"] = aws_sdk_accessanalyzer.types.job_details.deserialize_json(
            data["jobDetails"]
        )
    else:
        raise DeserializationError("GetGeneratedPolicyResponse.job_details required")
    if "generatedPolicyResult" in data:
        import aws_sdk_accessanalyzer.types.generated_policy_result

        out["generated_policy_result"] = (
            aws_sdk_accessanalyzer.types.generated_policy_result.deserialize_json(
                data["generatedPolicyResult"]
            )
        )
    else:
        raise DeserializationError(
            "GetGeneratedPolicyResponse.generated_policy_result required"
        )
    return out
