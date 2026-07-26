"""Generated from Smithy shape ``com.amazonaws.ram#ListReplacePermissionAssociationsWorkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.max_results
    import capo_ram.types.replace_permission_associations_work_id_list
    import capo_ram.types.replace_permission_associations_work_status
    import capo_ram.types.string


class ListReplacePermissionAssociationsWorkRequest(TypedDict, closed=True):
    work_ids: NotRequired[
        "capo_ram.types.replace_permission_associations_work_id_list.ReplacePermissionAssociationsWorkIdList"
    ]
    """<p>A list of IDs. These values come from the <code>id</code>field of the <code>replacePermissionAssociationsWork</code>structure returned by the <a>ReplacePermissionAssociations</a> operation. </p>"""
    status: NotRequired[
        "capo_ram.types.replace_permission_associations_work_status.ReplacePermissionAssociationsWorkStatus"
    ]
    """<p>Specifies that you want to see only the details about requests with a status that matches this value.</p>"""
    next_token: NotRequired["capo_ram.types.string.String"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["capo_ram.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReplacePermissionAssociationsWorkRequest) -> dict:
    out: dict = {}
    if "work_ids" in value:
        import capo_ram.types.replace_permission_associations_work_id_list

        out["workIds"] = (
            capo_ram.types.replace_permission_associations_work_id_list.serialize_json(
                value["work_ids"]
            )
        )
    if "status" in value:
        import capo_ram.types.replace_permission_associations_work_status

        out["status"] = (
            capo_ram.types.replace_permission_associations_work_status.serialize_json(
                value["status"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListReplacePermissionAssociationsWorkRequest:
    out: ListReplacePermissionAssociationsWorkRequest = {}  # type: ignore[typeddict-item]
    if "workIds" in data:
        import capo_ram.types.replace_permission_associations_work_id_list

        out["work_ids"] = (
            capo_ram.types.replace_permission_associations_work_id_list.deserialize_json(
                data["workIds"]
            )
        )
    if "status" in data:
        import capo_ram.types.replace_permission_associations_work_status

        out["status"] = (
            capo_ram.types.replace_permission_associations_work_status.deserialize_json(
                data["status"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
