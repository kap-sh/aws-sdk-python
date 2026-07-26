"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeCustomRoutingAcceleratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string


class DescribeCustomRoutingAcceleratorRequest(TypedDict, closed=True):
    accelerator_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the accelerator to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomRoutingAcceleratorRequest) -> dict:
    out: dict = {}
    out["AcceleratorArn"] = value["accelerator_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomRoutingAcceleratorRequest:
    out: DescribeCustomRoutingAcceleratorRequest = {}  # type: ignore[typeddict-item]
    if "AcceleratorArn" in data:
        out["accelerator_arn"] = data["AcceleratorArn"]
    else:
        raise DeserializationError(
            "DescribeCustomRoutingAcceleratorRequest.accelerator_arn required"
        )
    return out
