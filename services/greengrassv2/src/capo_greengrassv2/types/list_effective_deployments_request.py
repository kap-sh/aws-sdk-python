"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListEffectiveDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.core_device_thing_name
    import capo_greengrassv2.types.default_max_results
    import capo_greengrassv2.types.next_token_string


class ListEffectiveDeploymentsRequest(TypedDict, closed=True):
    core_device_thing_name: (
        "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName"
    )
    """<p>The name of the core device. This is also the name of the IoT thing.</p>"""
    max_results: NotRequired[
        "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
    ]
    """<p>The maximum number of results to be returned per paginated request.</p>"""
    next_token: NotRequired["capo_greengrassv2.types.next_token_string.NextTokenString"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEffectiveDeploymentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEffectiveDeploymentsRequest:
    out: ListEffectiveDeploymentsRequest = {}  # type: ignore[typeddict-item]
    return out
