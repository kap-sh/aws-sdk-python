"""Generated from Smithy shape ``com.amazonaws.apprunner#ListObservabilityConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.boolean
    import aws_sdk_apprunner.types.max_results
    import aws_sdk_apprunner.types.next_token
    import aws_sdk_apprunner.types.observability_configuration_name


class ListObservabilityConfigurationsRequest(TypedDict):
    observability_configuration_name: NotRequired[
        "aws_sdk_apprunner.types.observability_configuration_name.ObservabilityConfigurationName"
    ]
    """<p>The name of the App Runner observability configuration that you want to list. If specified, App Runner lists revisions that share this name. If not specified, App Runner returns revisions of all active configurations.</p>"""
    latest_only: "aws_sdk_apprunner.types.boolean.Boolean"
    """<p>Set to <code>true</code> to list only the latest revision for each requested configuration name.</p> <p>Set to <code>false</code> to list all revisions for each requested configuration name.</p> <p>Default: <code>true</code> </p>"""
    max_results: NotRequired["aws_sdk_apprunner.types.max_results.MaxResults"]
    """<p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>"""
    next_token: NotRequired["aws_sdk_apprunner.types.next_token.NextToken"]
    """<p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones that are specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListObservabilityConfigurationsRequest) -> dict:
    out: dict = {}
    if "observability_configuration_name" in value:
        out["ObservabilityConfigurationName"] = value[
            "observability_configuration_name"
        ]
    out["LatestOnly"] = value.get("latest_only", False)
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListObservabilityConfigurationsRequest:
    out: ListObservabilityConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "ObservabilityConfigurationName" in data:
        out["observability_configuration_name"] = data["ObservabilityConfigurationName"]
    if "LatestOnly" in data:
        out["latest_only"] = data["LatestOnly"]
    else:
        out["latest_only"] = False
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
