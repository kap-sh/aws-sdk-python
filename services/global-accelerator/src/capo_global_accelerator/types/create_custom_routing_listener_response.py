"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateCustomRoutingListenerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_listener


class CreateCustomRoutingListenerResponse(TypedDict, closed=True):
    listener: NotRequired[
        "capo_global_accelerator.types.custom_routing_listener.CustomRoutingListener"
    ]
    """<p>The listener that you've created for a custom routing accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomRoutingListenerResponse) -> dict:
    out: dict = {}
    if "listener" in value:
        import capo_global_accelerator.types.custom_routing_listener

        out["Listener"] = (
            capo_global_accelerator.types.custom_routing_listener.serialize_aws_json_1_1(
                value["listener"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomRoutingListenerResponse:
    out: CreateCustomRoutingListenerResponse = {}  # type: ignore[typeddict-item]
    if "Listener" in data:
        import capo_global_accelerator.types.custom_routing_listener

        out["listener"] = (
            capo_global_accelerator.types.custom_routing_listener.deserialize_aws_json_1_1(
                data["Listener"]
            )
        )
    return out
