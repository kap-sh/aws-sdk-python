"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListSourceResourcesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.source_resource_list
    import aws_sdk_migration_hub.types.token


class ListSourceResourcesResult(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_migration_hub.types.token.Token"]
    """<p>If the response includes a <code>NextToken</code> value, that means that there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. To retrieve the next page of results, call this API again and specify this <code>NextToken</code> value in the request. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>"""
    source_resource_list: NotRequired[
        "aws_sdk_migration_hub.types.source_resource_list.SourceResourceList"
    ]
    """<p>The list of source resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSourceResourcesResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "source_resource_list" in value:
        import aws_sdk_migration_hub.types.source_resource_list

        out["SourceResourceList"] = (
            aws_sdk_migration_hub.types.source_resource_list.serialize_aws_json_1_1(
                value["source_resource_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSourceResourcesResult:
    out: ListSourceResourcesResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "SourceResourceList" in data:
        import aws_sdk_migration_hub.types.source_resource_list

        out["source_resource_list"] = (
            aws_sdk_migration_hub.types.source_resource_list.deserialize_aws_json_1_1(
                data["SourceResourceList"]
            )
        )
    return out
