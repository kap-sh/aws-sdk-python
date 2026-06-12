"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateWorkforceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.workforce_arn


class CreateWorkforceResponse(TypedDict):
    workforce_arn: NotRequired["aws_sdk_sagemaker.types.workforce_arn.WorkforceArn"]
    """<p>The Amazon Resource Name (ARN) of the workforce.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkforceResponse) -> dict:
    out: dict = {}
    if "workforce_arn" in value:
        out["WorkforceArn"] = value["workforce_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkforceResponse:
    out: CreateWorkforceResponse = {}  # type: ignore[typeddict-item]
    if "WorkforceArn" in data:
        out["workforce_arn"] = data["WorkforceArn"]
    return out
