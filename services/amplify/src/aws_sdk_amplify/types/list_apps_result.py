"""Generated from Smithy shape ``com.amazonaws.amplify#ListAppsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.apps
    import aws_sdk_amplify.types.next_token


class ListAppsResult(TypedDict):
    apps: "aws_sdk_amplify.types.apps.Apps"
    """<p>A list of Amplify apps. </p>"""
    next_token: NotRequired["aws_sdk_amplify.types.next_token.NextToken"]
    """<p>A pagination token. Set to null to start listing apps from start. If non-null, the pagination token is returned in a result. Pass its value in here to list more projects. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppsResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.apps

    out["apps"] = aws_sdk_amplify.types.apps.serialize_json(value["apps"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppsResult:
    out: ListAppsResult = {}  # type: ignore[typeddict-item]
    if "apps" in data:
        import aws_sdk_amplify.types.apps

        out["apps"] = aws_sdk_amplify.types.apps.deserialize_json(data["apps"])
    else:
        raise DeserializationError("ListAppsResult.apps required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
