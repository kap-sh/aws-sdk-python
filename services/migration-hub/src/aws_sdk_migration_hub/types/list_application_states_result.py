"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListApplicationStatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.application_state_list
    import aws_sdk_migration_hub.types.token


class ListApplicationStatesResult(TypedDict, closed=True):
    application_state_list: NotRequired[
        "aws_sdk_migration_hub.types.application_state_list.ApplicationStateList"
    ]
    """<p>A list of Applications that exist in Application Discovery Service.</p>"""
    next_token: NotRequired["aws_sdk_migration_hub.types.token.Token"]
    """<p>If a <code>NextToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationStatesResult) -> dict:
    out: dict = {}
    if "application_state_list" in value:
        import aws_sdk_migration_hub.types.application_state_list

        out["ApplicationStateList"] = (
            aws_sdk_migration_hub.types.application_state_list.serialize_aws_json_1_1(
                value["application_state_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationStatesResult:
    out: ListApplicationStatesResult = {}  # type: ignore[typeddict-item]
    if "ApplicationStateList" in data:
        import aws_sdk_migration_hub.types.application_state_list

        out["application_state_list"] = (
            aws_sdk_migration_hub.types.application_state_list.deserialize_aws_json_1_1(
                data["ApplicationStateList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
