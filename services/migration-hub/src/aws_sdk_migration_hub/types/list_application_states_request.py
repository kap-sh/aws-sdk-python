"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListApplicationStatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.application_ids
    import aws_sdk_migration_hub.types.max_results
    import aws_sdk_migration_hub.types.token


class ListApplicationStatesRequest(TypedDict):
    application_ids: NotRequired[
        "aws_sdk_migration_hub.types.application_ids.ApplicationIds"
    ]
    """<p>The configurationIds from the Application Discovery Service that uniquely identifies your applications.</p>"""
    next_token: NotRequired["aws_sdk_migration_hub.types.token.Token"]
    """<p>If a <code>NextToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>"""
    max_results: NotRequired["aws_sdk_migration_hub.types.max_results.MaxResults"]
    """<p>Maximum number of results to be returned per page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationStatesRequest) -> dict:
    out: dict = {}
    if "application_ids" in value:
        import aws_sdk_migration_hub.types.application_ids

        out["ApplicationIds"] = (
            aws_sdk_migration_hub.types.application_ids.serialize_aws_json_1_1(
                value["application_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationStatesRequest:
    out: ListApplicationStatesRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationIds" in data:
        import aws_sdk_migration_hub.types.application_ids

        out["application_ids"] = (
            aws_sdk_migration_hub.types.application_ids.deserialize_aws_json_1_1(
                data["ApplicationIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
