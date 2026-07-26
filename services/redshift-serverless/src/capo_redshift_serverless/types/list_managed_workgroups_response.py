"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListManagedWorkgroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.managed_workgroups
    import capo_redshift_serverless.types.pagination_token


class ListManagedWorkgroupsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token.</p>"""
    managed_workgroups: NotRequired[
        "capo_redshift_serverless.types.managed_workgroups.ManagedWorkgroups"
    ]
    """<p>The returned array of managed workgroups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListManagedWorkgroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "managed_workgroups" in value:
        import capo_redshift_serverless.types.managed_workgroups

        out["managedWorkgroups"] = (
            capo_redshift_serverless.types.managed_workgroups.serialize_aws_json_1_1(
                value["managed_workgroups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListManagedWorkgroupsResponse:
    out: ListManagedWorkgroupsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "managedWorkgroups" in data:
        import capo_redshift_serverless.types.managed_workgroups

        out["managed_workgroups"] = (
            capo_redshift_serverless.types.managed_workgroups.deserialize_aws_json_1_1(
                data["managedWorkgroups"]
            )
        )
    return out
