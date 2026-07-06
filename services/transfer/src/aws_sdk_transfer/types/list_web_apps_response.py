"""Generated from Smithy shape ``com.amazonaws.transfer#ListWebAppsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_web_apps
    import aws_sdk_transfer.types.next_token


class ListWebAppsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>Provide this value for the <code>NextToken</code> parameter in a subsequent command to continue listing additional web apps.</p>"""
    web_apps: "aws_sdk_transfer.types.listed_web_apps.ListedWebApps"
    """<p>Returns, for each listed web app, a structure that contains details for the web app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWebAppsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_transfer.types.listed_web_apps

    out["WebApps"] = aws_sdk_transfer.types.listed_web_apps.serialize_aws_json_1_1(
        value["web_apps"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWebAppsResponse:
    out: ListWebAppsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "WebApps" in data:
        import aws_sdk_transfer.types.listed_web_apps

        out["web_apps"] = (
            aws_sdk_transfer.types.listed_web_apps.deserialize_aws_json_1_1(
                data["WebApps"]
            )
        )
    else:
        raise DeserializationError("ListWebAppsResponse.web_apps required")
    return out
