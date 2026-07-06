"""Generated from Smithy shape ``com.amazonaws.health#DescribeAffectedEntitiesForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_health.types.describe_affected_entities_for_organization_failed_set
    import aws_sdk_health.types.entity_list
    import aws_sdk_health.types.next_token


class DescribeAffectedEntitiesForOrganizationResponse(TypedDict, closed=True):
    entities: NotRequired["aws_sdk_health.types.entity_list.EntityList"]
    """<p>A JSON set of elements including the <code>awsAccountId</code> and its <code>entityArn</code>, <code>entityValue</code> and its <code>entityArn</code>, <code>lastUpdatedTime</code>, and <code>statusCode</code>.</p>"""
    failed_set: NotRequired[
        "aws_sdk_health.types.describe_affected_entities_for_organization_failed_set.DescribeAffectedEntitiesForOrganizationFailedSet"
    ]
    """<p>A JSON set of elements of the failed response, including the <code>awsAccountId</code>, <code>errorMessage</code>, <code>errorName</code>, and <code>eventArn</code>.</p>"""
    next_token: NotRequired["aws_sdk_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeAffectedEntitiesForOrganizationResponse,
) -> dict:
    out: dict = {}
    if "entities" in value:
        import aws_sdk_health.types.entity_list

        out["entities"] = aws_sdk_health.types.entity_list.serialize_aws_json_1_1(
            value["entities"]
        )
    if "failed_set" in value:
        import aws_sdk_health.types.describe_affected_entities_for_organization_failed_set

        out["failedSet"] = (
            aws_sdk_health.types.describe_affected_entities_for_organization_failed_set.serialize_aws_json_1_1(
                value["failed_set"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeAffectedEntitiesForOrganizationResponse:
    out: DescribeAffectedEntitiesForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "entities" in data:
        import aws_sdk_health.types.entity_list

        out["entities"] = aws_sdk_health.types.entity_list.deserialize_aws_json_1_1(
            data["entities"]
        )
    if "failedSet" in data:
        import aws_sdk_health.types.describe_affected_entities_for_organization_failed_set

        out["failed_set"] = (
            aws_sdk_health.types.describe_affected_entities_for_organization_failed_set.deserialize_aws_json_1_1(
                data["failedSet"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
