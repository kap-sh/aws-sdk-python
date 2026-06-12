"""Generated from Smithy shape ``com.amazonaws.iot#ListThingRegistrationTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.registry_max_results
    import aws_sdk_iot.types.status


class ListThingRegistrationTasksRequest(TypedDict):
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot.types.registry_max_results.RegistryMaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""
    status: NotRequired["aws_sdk_iot.types.status.Status"]
    """<p>The status of the bulk thing provisioning task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingRegistrationTasksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThingRegistrationTasksRequest:
    out: ListThingRegistrationTasksRequest = {}  # type: ignore[typeddict-item]
    return out
