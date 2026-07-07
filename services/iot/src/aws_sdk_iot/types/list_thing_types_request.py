"""Generated from Smithy shape ``com.amazonaws.iot#ListThingTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.registry_max_results
    import aws_sdk_iot.types.thing_type_name


class ListThingTypesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot.types.registry_max_results.RegistryMaxResults"
    ]
    """<p>The maximum number of results to return in this operation.</p>"""
    thing_type_name: NotRequired["aws_sdk_iot.types.thing_type_name.ThingTypeName"]
    """<p>The name of the thing type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingTypesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThingTypesRequest:
    out: ListThingTypesRequest = {}  # type: ignore[typeddict-item]
    return out
