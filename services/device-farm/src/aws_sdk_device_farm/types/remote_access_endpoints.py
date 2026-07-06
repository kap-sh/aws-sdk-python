"""Generated from Smithy shape ``com.amazonaws.devicefarm#RemoteAccessEndpoints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.sensitive_url


class RemoteAccessEndpoints(TypedDict, closed=True):
    remote_driver_endpoint: NotRequired[
        "aws_sdk_device_farm.types.sensitive_url.SensitiveURL"
    ]
    """<p>URL for controlling the device using WebDriver-compliant clients, like Appium, during the remote access session.</p>"""
    interactive_endpoint: NotRequired[
        "aws_sdk_device_farm.types.sensitive_url.SensitiveURL"
    ]
    """<p>URL for viewing and interacting with the device during the remote access session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoteAccessEndpoints) -> dict:
    out: dict = {}
    if "remote_driver_endpoint" in value:
        out["remoteDriverEndpoint"] = value["remote_driver_endpoint"]
    if "interactive_endpoint" in value:
        out["interactiveEndpoint"] = value["interactive_endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoteAccessEndpoints:
    out: RemoteAccessEndpoints = {}  # type: ignore[typeddict-item]
    if "remoteDriverEndpoint" in data:
        out["remote_driver_endpoint"] = data["remoteDriverEndpoint"]
    if "interactiveEndpoint" in data:
        out["interactive_endpoint"] = data["interactiveEndpoint"]
    return out
