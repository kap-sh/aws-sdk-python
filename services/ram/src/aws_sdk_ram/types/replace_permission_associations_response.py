"""Generated from Smithy shape ``com.amazonaws.ram#ReplacePermissionAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.replace_permission_associations_work
    import aws_sdk_ram.types.string


class ReplacePermissionAssociationsResponse(TypedDict):
    replace_permission_associations_work: NotRequired[
        "aws_sdk_ram.types.replace_permission_associations_work.ReplacePermissionAssociationsWork"
    ]
    """<p>Specifies a data structure that you can use to track the asynchronous tasks that RAM performs to complete this operation. You can use the <a>ListReplacePermissionAssociationsWork</a> operation and pass the <code>id</code> value returned in this structure.</p>"""
    client_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplacePermissionAssociationsResponse) -> dict:
    out: dict = {}
    if "replace_permission_associations_work" in value:
        import aws_sdk_ram.types.replace_permission_associations_work

        out["replacePermissionAssociationsWork"] = (
            aws_sdk_ram.types.replace_permission_associations_work.serialize_json(
                value["replace_permission_associations_work"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ReplacePermissionAssociationsResponse:
    out: ReplacePermissionAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "replacePermissionAssociationsWork" in data:
        import aws_sdk_ram.types.replace_permission_associations_work

        out["replace_permission_associations_work"] = (
            aws_sdk_ram.types.replace_permission_associations_work.deserialize_json(
                data["replacePermissionAssociationsWork"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
