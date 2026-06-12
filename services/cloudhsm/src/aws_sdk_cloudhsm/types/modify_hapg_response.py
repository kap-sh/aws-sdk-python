"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ModifyHapgResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.hapg_arn


class ModifyHapgResponse(TypedDict):
    hapg_arn: NotRequired["aws_sdk_cloudhsm.types.hapg_arn.HapgArn"]
    """<p>The ARN of the high-availability partition group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyHapgResponse) -> dict:
    out: dict = {}
    if "hapg_arn" in value:
        out["HapgArn"] = value["hapg_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyHapgResponse:
    out: ModifyHapgResponse = {}  # type: ignore[typeddict-item]
    if "HapgArn" in data:
        out["hapg_arn"] = data["HapgArn"]
    return out
