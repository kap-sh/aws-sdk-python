"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DescribeHapgRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.hapg_arn


class DescribeHapgRequest(TypedDict):
    hapg_arn: "aws_sdk_cloudhsm.types.hapg_arn.HapgArn"
    """<p>The ARN of the high-availability partition group to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHapgRequest) -> dict:
    out: dict = {}
    out["HapgArn"] = value["hapg_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHapgRequest:
    out: DescribeHapgRequest = {}  # type: ignore[typeddict-item]
    if "HapgArn" in data:
        out["hapg_arn"] = data["HapgArn"]
    else:
        raise DeserializationError("DescribeHapgRequest.hapg_arn required")
    return out
