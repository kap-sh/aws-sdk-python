"""Generated from Smithy shape ``com.amazonaws.amplify#ListBackendEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.environment_name
    import aws_sdk_amplify.types.max_results
    import aws_sdk_amplify.types.next_token


class ListBackendEnvironmentsRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p>The unique ID for an Amplify app. </p>"""
    environment_name: NotRequired[
        "aws_sdk_amplify.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the backend environment </p>"""
    next_token: NotRequired["aws_sdk_amplify.types.next_token.NextToken"]
    """<p>A pagination token. Set to null to start listing backend environments from the start. If a non-null pagination token is returned in a result, pass its value in here to list more backend environments. </p>"""
    max_results: "aws_sdk_amplify.types.max_results.MaxResults"
    """<p>The maximum number of records to list in a single response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackendEnvironmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBackendEnvironmentsRequest:
    out: ListBackendEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    return out
