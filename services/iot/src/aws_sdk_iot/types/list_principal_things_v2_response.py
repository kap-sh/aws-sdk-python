"""Generated from Smithy shape ``com.amazonaws.iot#ListPrincipalThingsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.principal_thing_objects


class ListPrincipalThingsV2Response(TypedDict, closed=True):
    principal_thing_objects: NotRequired[
        "aws_sdk_iot.types.principal_thing_objects.PrincipalThingObjects"
    ]
    """<p>A list of <code>thingPrincipalObject</code> that represents the principal and the type of relation it has with the thing.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrincipalThingsV2Response) -> dict:
    out: dict = {}
    if "principal_thing_objects" in value:
        import aws_sdk_iot.types.principal_thing_objects

        out["principalThingObjects"] = (
            aws_sdk_iot.types.principal_thing_objects.serialize_json(
                value["principal_thing_objects"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPrincipalThingsV2Response:
    out: ListPrincipalThingsV2Response = {}  # type: ignore[typeddict-item]
    if "principalThingObjects" in data:
        import aws_sdk_iot.types.principal_thing_objects

        out["principal_thing_objects"] = (
            aws_sdk_iot.types.principal_thing_objects.deserialize_json(
                data["principalThingObjects"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
