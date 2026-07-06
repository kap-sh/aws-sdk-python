"""Generated from Smithy shape ``com.amazonaws.qconnect#ConnectConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_string


class ConnectConfiguration(TypedDict, closed=True):
    instance_id: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the Amazon Connect instance. You can find the instanceId in the ARN of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectConfiguration) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    return out


def deserialize_json(data: dict) -> ConnectConfiguration:
    out: ConnectConfiguration = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    return out
