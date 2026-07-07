"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeCustomRoutingListenerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_listener


class DescribeCustomRoutingListenerResponse(TypedDict, closed=True):
    listener: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_listener.CustomRoutingListener"
    ]
    """<p>The description of a listener for a custom routing accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomRoutingListenerResponse) -> dict:
    out: dict = {}
    if "listener" in value:
        import aws_sdk_global_accelerator.types.custom_routing_listener

        out["Listener"] = (
            aws_sdk_global_accelerator.types.custom_routing_listener.serialize_aws_json_1_1(
                value["listener"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomRoutingListenerResponse:
    out: DescribeCustomRoutingListenerResponse = {}  # type: ignore[typeddict-item]
    if "Listener" in data:
        import aws_sdk_global_accelerator.types.custom_routing_listener

        out["listener"] = (
            aws_sdk_global_accelerator.types.custom_routing_listener.deserialize_aws_json_1_1(
                data["Listener"]
            )
        )
    return out
