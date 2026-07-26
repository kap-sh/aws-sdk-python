"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GetEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.amazon_resource_name
    import capo_iotdeviceadvisor.types.authentication_method


class GetEndpointRequest(TypedDict, closed=True):
    thing_arn: NotRequired[
        "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The thing ARN of the device. This is an optional parameter.</p>"""
    certificate_arn: NotRequired[
        "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The certificate ARN of the device. This is an optional parameter.</p>"""
    device_role_arn: NotRequired[
        "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The device role ARN of the device. This is an optional parameter.</p>"""
    authentication_method: NotRequired[
        "capo_iotdeviceadvisor.types.authentication_method.AuthenticationMethod"
    ]
    """<p>The authentication method used during the device connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEndpointRequest:
    out: GetEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
