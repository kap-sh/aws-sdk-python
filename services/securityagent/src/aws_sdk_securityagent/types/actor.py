"""Generated from Smithy shape ``com.amazonaws.securityagent#Actor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.authentication
    import aws_sdk_securityagent.types.uri_list


class Actor(TypedDict):
    identifier: NotRequired["str"]
    """<p>The unique identifier for the actor.</p>"""
    uris: NotRequired["aws_sdk_securityagent.types.uri_list.UriList"]
    """<p>The list of URIs that the actor targets during testing.</p>"""
    authentication: NotRequired[
        "aws_sdk_securityagent.types.authentication.Authentication"
    ]
    """<p>The authentication configuration for the actor.</p>"""
    description: NotRequired["str"]
    """<p>A description of the actor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Actor) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "uris" in value:
        import aws_sdk_securityagent.types.uri_list

        out["uris"] = aws_sdk_securityagent.types.uri_list.serialize_json(value["uris"])
    if "authentication" in value:
        import aws_sdk_securityagent.types.authentication

        out["authentication"] = (
            aws_sdk_securityagent.types.authentication.serialize_json(
                value["authentication"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> Actor:
    out: Actor = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    if "uris" in data:
        import aws_sdk_securityagent.types.uri_list

        out["uris"] = aws_sdk_securityagent.types.uri_list.deserialize_json(
            data["uris"]
        )
    if "authentication" in data:
        import aws_sdk_securityagent.types.authentication

        out["authentication"] = (
            aws_sdk_securityagent.types.authentication.deserialize_json(
                data["authentication"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
