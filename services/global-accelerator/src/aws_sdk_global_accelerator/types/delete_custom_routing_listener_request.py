"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DeleteCustomRoutingListenerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string


class DeleteCustomRoutingListenerRequest(TypedDict):
    listener_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the listener to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCustomRoutingListenerRequest) -> dict:
    out: dict = {}
    out["ListenerArn"] = value["listener_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCustomRoutingListenerRequest:
    out: DeleteCustomRoutingListenerRequest = {}  # type: ignore[typeddict-item]
    if "ListenerArn" in data:
        out["listener_arn"] = data["ListenerArn"]
    else:
        raise DeserializationError(
            "DeleteCustomRoutingListenerRequest.listener_arn required"
        )
    return out
