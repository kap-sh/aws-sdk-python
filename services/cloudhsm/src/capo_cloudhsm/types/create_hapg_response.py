"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CreateHapgResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.hapg_arn


class CreateHapgResponse(TypedDict, closed=True):
    hapg_arn: NotRequired["capo_cloudhsm.types.hapg_arn.HapgArn"]
    """<p>The ARN of the high-availability partition group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHapgResponse) -> dict:
    out: dict = {}
    if "hapg_arn" in value:
        out["HapgArn"] = value["hapg_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHapgResponse:
    out: CreateHapgResponse = {}  # type: ignore[typeddict-item]
    if "HapgArn" in data:
        out["hapg_arn"] = data["HapgArn"]
    return out
