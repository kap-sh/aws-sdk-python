"""Generated from Smithy shape ``com.amazonaws.iot#ListThingPrincipalsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.thing_principal_objects


class ListThingPrincipalsV2Response(TypedDict, closed=True):
    thing_principal_objects: NotRequired[
        "capo_iot.types.thing_principal_objects.ThingPrincipalObjects"
    ]
    """<p>A list of <code>thingPrincipalObject</code> that represents the principal and the type of relation it has with the thing.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingPrincipalsV2Response) -> dict:
    out: dict = {}
    if "thing_principal_objects" in value:
        import capo_iot.types.thing_principal_objects

        out["thingPrincipalObjects"] = (
            capo_iot.types.thing_principal_objects.serialize_json(
                value["thing_principal_objects"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThingPrincipalsV2Response:
    out: ListThingPrincipalsV2Response = {}  # type: ignore[typeddict-item]
    if "thingPrincipalObjects" in data:
        import capo_iot.types.thing_principal_objects

        out["thing_principal_objects"] = (
            capo_iot.types.thing_principal_objects.deserialize_json(
                data["thingPrincipalObjects"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
