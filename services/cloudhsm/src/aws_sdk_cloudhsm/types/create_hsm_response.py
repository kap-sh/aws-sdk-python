"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CreateHsmResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.hsm_arn


class CreateHsmResponse(TypedDict):
    hsm_arn: NotRequired["aws_sdk_cloudhsm.types.hsm_arn.HsmArn"]
    """<p>The ARN of the HSM.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHsmResponse) -> dict:
    out: dict = {}
    if "hsm_arn" in value:
        out["HsmArn"] = value["hsm_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHsmResponse:
    out: CreateHsmResponse = {}  # type: ignore[typeddict-item]
    if "HsmArn" in data:
        out["hsm_arn"] = data["HsmArn"]
    return out
