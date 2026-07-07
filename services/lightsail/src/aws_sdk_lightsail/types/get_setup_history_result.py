"""Generated from Smithy shape ``com.amazonaws.lightsail#GetSetupHistoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.setup_history_list
    import aws_sdk_lightsail.types.setup_history_page_token


class GetSetupHistoryResult(TypedDict, closed=True):
    setup_history: NotRequired[
        "aws_sdk_lightsail.types.setup_history_list.setupHistoryList"
    ]
    """<p>The historical information that's returned.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_lightsail.types.setup_history_page_token.SetupHistoryPageToken"
    ]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetSetupHistory</code> request and specify the next page token using the pageToken parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSetupHistoryResult) -> dict:
    out: dict = {}
    if "setup_history" in value:
        import aws_sdk_lightsail.types.setup_history_list

        out["setupHistory"] = (
            aws_sdk_lightsail.types.setup_history_list.serialize_aws_json_1_1(
                value["setup_history"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSetupHistoryResult:
    out: GetSetupHistoryResult = {}  # type: ignore[typeddict-item]
    if "setupHistory" in data:
        import aws_sdk_lightsail.types.setup_history_list

        out["setup_history"] = (
            aws_sdk_lightsail.types.setup_history_list.deserialize_aws_json_1_1(
                data["setupHistory"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
