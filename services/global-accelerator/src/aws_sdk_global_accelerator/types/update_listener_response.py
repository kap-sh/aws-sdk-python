"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateListenerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.listener


class UpdateListenerResponse(TypedDict):
    listener: NotRequired["aws_sdk_global_accelerator.types.listener.Listener"]
    """<p>Information for the updated listener.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateListenerResponse) -> dict:
    out: dict = {}
    if "listener" in value:
        import aws_sdk_global_accelerator.types.listener

        out["Listener"] = (
            aws_sdk_global_accelerator.types.listener.serialize_aws_json_1_1(
                value["listener"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateListenerResponse:
    out: UpdateListenerResponse = {}  # type: ignore[typeddict-item]
    if "Listener" in data:
        import aws_sdk_global_accelerator.types.listener

        out["listener"] = (
            aws_sdk_global_accelerator.types.listener.deserialize_aws_json_1_1(
                data["Listener"]
            )
        )
    return out
