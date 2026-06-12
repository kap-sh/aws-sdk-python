"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListServicesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id
    import aws_sdk_migration_hub_refactor_spaces.types.max_results
    import aws_sdk_migration_hub_refactor_spaces.types.next_token


class ListServicesRequest(TypedDict):
    environment_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The ID of the environment. </p>"""
    application_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    )
    """<p>The ID of the application. </p>"""
    next_token: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServicesRequest:
    out: ListServicesRequest = {}  # type: ignore[typeddict-item]
    return out
