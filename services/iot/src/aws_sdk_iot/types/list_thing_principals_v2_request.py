"""Generated from Smithy shape ``com.amazonaws.iot#ListThingPrincipalsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.registry_max_results
    import aws_sdk_iot.types.thing_name
    import aws_sdk_iot.types.thing_principal_type


class ListThingPrincipalsV2Request(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot.types.registry_max_results.RegistryMaxResults"
    ]
    """<p>The maximum number of results to return in this operation.</p>"""
    thing_name: "aws_sdk_iot.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""
    thing_principal_type: NotRequired[
        "aws_sdk_iot.types.thing_principal_type.ThingPrincipalType"
    ]
    """<p>The type of the relation you want to filter in the response. If no value is provided in this field, the response will list all principals, including both the <code>EXCLUSIVE_THING</code> and <code>NON_EXCLUSIVE_THING</code> attachment types.</p> <ul> <li> <p> <code>EXCLUSIVE_THING</code> - Attaches the specified principal to the specified thing, exclusively. The thing will be the only thing that’s attached to the principal.</p> </li> </ul> <ul> <li> <p> <code>NON_EXCLUSIVE_THING</code> - Attaches the specified principal to the specified thing. Multiple things can be attached to the principal.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingPrincipalsV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThingPrincipalsV2Request:
    out: ListThingPrincipalsV2Request = {}  # type: ignore[typeddict-item]
    return out
