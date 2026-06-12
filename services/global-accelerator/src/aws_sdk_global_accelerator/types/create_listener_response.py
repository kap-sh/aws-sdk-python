"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateListenerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.listener


class CreateListenerResponse(TypedDict):
    listener: NotRequired["aws_sdk_global_accelerator.types.listener.Listener"]
    """<p>The listener that you've created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateListenerResponse) -> dict:
    out: dict = {}
    if "listener" in value:
        import aws_sdk_global_accelerator.types.listener

        out["Listener"] = (
            aws_sdk_global_accelerator.types.listener.serialize_aws_json_1_1(
                value["listener"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateListenerResponse:
    out: CreateListenerResponse = {}  # type: ignore[typeddict-item]
    if "Listener" in data:
        import aws_sdk_global_accelerator.types.listener

        out["listener"] = (
            aws_sdk_global_accelerator.types.listener.deserialize_aws_json_1_1(
                data["Listener"]
            )
        )
    return out
