"""Generated from Smithy shape ``com.amazonaws.health#DescribeAffectedEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_health.types.entity_list
    import aws_sdk_health.types.next_token


class DescribeAffectedEntitiesResponse(TypedDict, closed=True):
    entities: NotRequired["aws_sdk_health.types.entity_list.EntityList"]
    """<p>The entities that match the filter criteria.</p>"""
    next_token: NotRequired["aws_sdk_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAffectedEntitiesResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import aws_sdk_health.types.entity_list

        out["entities"] = aws_sdk_health.types.entity_list.serialize_aws_json_1_1(
            value["entities"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAffectedEntitiesResponse:
    out: DescribeAffectedEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "entities" in data:
        import aws_sdk_health.types.entity_list

        out["entities"] = aws_sdk_health.types.entity_list.deserialize_aws_json_1_1(
            data["entities"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
