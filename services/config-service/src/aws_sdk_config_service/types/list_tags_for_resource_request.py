"""Generated from Smithy shape ``com.amazonaws.configservice#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.amazon_resource_name
    import aws_sdk_config_service.types.limit
    import aws_sdk_config_service.types.next_token


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. The following resources are supported:</p> <ul> <li> <p> <code>ConfigurationRecorder</code> </p> </li> <li> <p> <code>ConfigRule</code> </p> </li> <li> <p> <code>OrganizationConfigRule</code> </p> </li> <li> <p> <code>ConformancePack</code> </p> </li> <li> <p> <code>OrganizationConformancePack</code> </p> </li> <li> <p> <code>ConfigurationAggregator</code> </p> </li> <li> <p> <code>AggregationAuthorization</code> </p> </li> <li> <p> <code>StoredQuery</code> </p> </li> </ul>"""
    limit: "aws_sdk_config_service.types.limit.Limit"
    """<p>The maximum number of tags returned on each page. The limit maximum is 50. You cannot specify a number greater than 50. If you specify 0, Config uses the default. </p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
