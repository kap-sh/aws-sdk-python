"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListEffectiveDeploymentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.core_device_thing_name
    import aws_sdk_greengrassv2.types.default_max_results
    import aws_sdk_greengrassv2.types.next_token_string


class ListEffectiveDeploymentsRequest(TypedDict):
    core_device_thing_name: (
        "aws_sdk_greengrassv2.types.core_device_thing_name.CoreDeviceThingName"
    )
    """<p>The name of the core device. This is also the name of the IoT thing.</p>"""
    max_results: NotRequired[
        "aws_sdk_greengrassv2.types.default_max_results.DefaultMaxResults"
    ]
    """<p>The maximum number of results to be returned per paginated request.</p>"""
    next_token: NotRequired[
        "aws_sdk_greengrassv2.types.next_token_string.NextTokenString"
    ]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEffectiveDeploymentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEffectiveDeploymentsRequest:
    out: ListEffectiveDeploymentsRequest = {}  # type: ignore[typeddict-item]
    return out
