"""Generated from Smithy shape ``com.amazonaws.datazone#ListEnvironmentsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.aws_region
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.environment_profile_id
    import aws_sdk_datazone.types.environment_status
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_id


class ListEnvironmentsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    aws_account_id: NotRequired["aws_sdk_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The identifier of the Amazon Web Services account where you want to list environments.</p>"""
    status: NotRequired["aws_sdk_datazone.types.environment_status.EnvironmentStatus"]
    """<p>The status of the environments that you want to list.</p>"""
    aws_account_region: NotRequired["aws_sdk_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services region where you want to list environments.</p>"""
    project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the Amazon DataZone project.</p>"""
    environment_profile_identifier: NotRequired[
        "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId"
    ]
    """<p>The identifier of the environment profile.</p>"""
    environment_blueprint_identifier: NotRequired[
        "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    ]
    """<p>The identifier of the Amazon DataZone blueprint.</p>"""
    provider: NotRequired["str"]
    """<p>The provider of the environment.</p>"""
    name: NotRequired["str"]
    """<p>The name of the environment.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of environments to return in a single call to <code>ListEnvironments</code>. When the number of environments to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironments</code> to list the next set of environments.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of environments is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environments, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironments</code> to list the next set of environments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnvironmentsInput:
    out: ListEnvironmentsInput = {}  # type: ignore[typeddict-item]
    return out
