"""Generated from Smithy shape ``com.amazonaws.datazone#ListEnvironmentProfilesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.aws_region
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.environment_profile_name
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_id


class ListEnvironmentProfilesInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    aws_account_id: NotRequired["aws_sdk_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The identifier of the Amazon Web Services account where you want to list environment profiles.</p>"""
    aws_account_region: NotRequired["aws_sdk_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services region where you want to list environment profiles.</p>"""
    environment_blueprint_identifier: NotRequired[
        "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    ]
    """<p>The identifier of the blueprint that was used to create the environment profiles that you want to list.</p>"""
    project_identifier: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the Amazon DataZone project.</p>"""
    name: NotRequired[
        "aws_sdk_datazone.types.environment_profile_name.EnvironmentProfileName"
    ]
    """<p/>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of environment profiles is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environment profiles, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentProfiles</code> to list the next set of environment profiles.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of environment profiles to return in a single call to <code>ListEnvironmentProfiles</code>. When the number of environment profiles to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentProfiles</code> to list the next set of environment profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentProfilesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnvironmentProfilesInput:
    out: ListEnvironmentProfilesInput = {}  # type: ignore[typeddict-item]
    return out
