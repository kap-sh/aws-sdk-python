"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeListenerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.listener


class DescribeListenerResponse(TypedDict, closed=True):
    listener: NotRequired["capo_global_accelerator.types.listener.Listener"]
    """<p>The description of a listener.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeListenerResponse) -> dict:
    out: dict = {}
    if "listener" in value:
        import capo_global_accelerator.types.listener

        out["Listener"] = capo_global_accelerator.types.listener.serialize_aws_json_1_1(
            value["listener"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeListenerResponse:
    out: DescribeListenerResponse = {}  # type: ignore[typeddict-item]
    if "Listener" in data:
        import capo_global_accelerator.types.listener

        out["listener"] = (
            capo_global_accelerator.types.listener.deserialize_aws_json_1_1(
                data["Listener"]
            )
        )
    return out
