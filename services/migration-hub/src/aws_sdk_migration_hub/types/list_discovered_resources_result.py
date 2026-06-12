"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListDiscoveredResourcesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.discovered_resource_list
    import aws_sdk_migration_hub.types.token


class ListDiscoveredResourcesResult(TypedDict):
    next_token: NotRequired["aws_sdk_migration_hub.types.token.Token"]
    """<p>If there are more discovered resources than the max result, return the next token to be passed to the next call as a bookmark of where to start from.</p>"""
    discovered_resource_list: NotRequired[
        "aws_sdk_migration_hub.types.discovered_resource_list.DiscoveredResourceList"
    ]
    """<p>Returned list of discovered resources associated with the given MigrationTask.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDiscoveredResourcesResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "discovered_resource_list" in value:
        import aws_sdk_migration_hub.types.discovered_resource_list

        out["DiscoveredResourceList"] = (
            aws_sdk_migration_hub.types.discovered_resource_list.serialize_aws_json_1_1(
                value["discovered_resource_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDiscoveredResourcesResult:
    out: ListDiscoveredResourcesResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DiscoveredResourceList" in data:
        import aws_sdk_migration_hub.types.discovered_resource_list

        out["discovered_resource_list"] = (
            aws_sdk_migration_hub.types.discovered_resource_list.deserialize_aws_json_1_1(
                data["DiscoveredResourceList"]
            )
        )
    return out
