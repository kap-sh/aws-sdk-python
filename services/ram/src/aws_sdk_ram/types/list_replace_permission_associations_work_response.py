"""Generated from Smithy shape ``com.amazonaws.ram#ListReplacePermissionAssociationsWorkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.replace_permission_associations_work_list
    import aws_sdk_ram.types.string


class ListReplacePermissionAssociationsWorkResponse(TypedDict, closed=True):
    replace_permission_associations_works: NotRequired[
        "aws_sdk_ram.types.replace_permission_associations_work_list.ReplacePermissionAssociationsWorkList"
    ]
    """<p>An array of data structures that provide details of the matching work IDs.</p>"""
    next_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReplacePermissionAssociationsWorkResponse) -> dict:
    out: dict = {}
    if "replace_permission_associations_works" in value:
        import aws_sdk_ram.types.replace_permission_associations_work_list

        out["replacePermissionAssociationsWorks"] = (
            aws_sdk_ram.types.replace_permission_associations_work_list.serialize_json(
                value["replace_permission_associations_works"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReplacePermissionAssociationsWorkResponse:
    out: ListReplacePermissionAssociationsWorkResponse = {}  # type: ignore[typeddict-item]
    if "replacePermissionAssociationsWorks" in data:
        import aws_sdk_ram.types.replace_permission_associations_work_list

        out["replace_permission_associations_works"] = (
            aws_sdk_ram.types.replace_permission_associations_work_list.deserialize_json(
                data["replacePermissionAssociationsWorks"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
