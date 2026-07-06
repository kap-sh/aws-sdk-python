"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app_version_list
    import aws_sdk_resiliencehub.types.next_token


class ListAppVersionsResponse(TypedDict, closed=True):
    app_versions: "aws_sdk_resiliencehub.types.app_version_list.AppVersionList"
    """<p>The version of the application.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.app_version_list

    out["appVersions"] = aws_sdk_resiliencehub.types.app_version_list.serialize_json(
        value["app_versions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppVersionsResponse:
    out: ListAppVersionsResponse = {}  # type: ignore[typeddict-item]
    if "appVersions" in data:
        import aws_sdk_resiliencehub.types.app_version_list

        out["app_versions"] = (
            aws_sdk_resiliencehub.types.app_version_list.deserialize_json(
                data["appVersions"]
            )
        )
    else:
        raise DeserializationError("ListAppVersionsResponse.app_versions required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
