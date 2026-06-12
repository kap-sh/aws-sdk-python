"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DeleteListenerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string


class DeleteListenerRequest(TypedDict):
    listener_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteListenerRequest) -> dict:
    out: dict = {}
    out["ListenerArn"] = value["listener_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteListenerRequest:
    out: DeleteListenerRequest = {}  # type: ignore[typeddict-item]
    if "ListenerArn" in data:
        out["listener_arn"] = data["ListenerArn"]
    else:
        raise DeserializationError("DeleteListenerRequest.listener_arn required")
    return out
