"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteWorkforceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.workforce_name


class DeleteWorkforceRequest(TypedDict):
    workforce_name: NotRequired["aws_sdk_sagemaker.types.workforce_name.WorkforceName"]
    """<p>The name of the workforce.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkforceRequest) -> dict:
    out: dict = {}
    if "workforce_name" in value:
        out["WorkforceName"] = value["workforce_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkforceRequest:
    out: DeleteWorkforceRequest = {}  # type: ignore[typeddict-item]
    if "WorkforceName" in data:
        out["workforce_name"] = data["WorkforceName"]
    return out
