"""Generated from Smithy shape ``com.amazonaws.iot#ListThingGroupsForThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.registry_max_results
    import aws_sdk_iot.types.thing_name


class ListThingGroupsForThingRequest(TypedDict):
    thing_name: "aws_sdk_iot.types.thing_name.ThingName"
    """<p>The thing name.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot.types.registry_max_results.RegistryMaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingGroupsForThingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThingGroupsForThingRequest:
    out: ListThingGroupsForThingRequest = {}  # type: ignore[typeddict-item]
    return out
