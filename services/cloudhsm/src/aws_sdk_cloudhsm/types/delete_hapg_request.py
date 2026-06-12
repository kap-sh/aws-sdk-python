"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DeleteHapgRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.hapg_arn


class DeleteHapgRequest(TypedDict):
    hapg_arn: "aws_sdk_cloudhsm.types.hapg_arn.HapgArn"
    """<p>The ARN of the high-availability partition group to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHapgRequest) -> dict:
    out: dict = {}
    out["HapgArn"] = value["hapg_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHapgRequest:
    out: DeleteHapgRequest = {}  # type: ignore[typeddict-item]
    if "HapgArn" in data:
        out["hapg_arn"] = data["HapgArn"]
    else:
        raise DeserializationError("DeleteHapgRequest.hapg_arn required")
    return out
