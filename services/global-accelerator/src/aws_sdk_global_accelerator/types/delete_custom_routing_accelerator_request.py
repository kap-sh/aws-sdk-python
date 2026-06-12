"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DeleteCustomRoutingAcceleratorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string


class DeleteCustomRoutingAcceleratorRequest(TypedDict):
    accelerator_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the custom routing accelerator to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCustomRoutingAcceleratorRequest) -> dict:
    out: dict = {}
    out["AcceleratorArn"] = value["accelerator_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCustomRoutingAcceleratorRequest:
    out: DeleteCustomRoutingAcceleratorRequest = {}  # type: ignore[typeddict-item]
    if "AcceleratorArn" in data:
        out["accelerator_arn"] = data["AcceleratorArn"]
    else:
        raise DeserializationError(
            "DeleteCustomRoutingAcceleratorRequest.accelerator_arn required"
        )
    return out
