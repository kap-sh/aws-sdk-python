"""Generated from Smithy shape ``com.amazonaws.ec2#LoadPermissionModifications``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.load_permission_list_request


class LoadPermissionModifications(TypedDict):
    add: NotRequired[
        "aws_sdk_ec2.types.load_permission_list_request.LoadPermissionListRequest"
    ]
    """<p>The load permissions to add.</p>"""
    remove: NotRequired[
        "aws_sdk_ec2.types.load_permission_list_request.LoadPermissionListRequest"
    ]
    """<p>The load permissions to remove.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LoadPermissionModifications, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "add" in value:
        import aws_sdk_ec2.types.load_permission_list_request

        aws_sdk_ec2.types.load_permission_list_request.serialize_ec2_query(
            value["add"], pairs, f"{prefix}.Add"
        )
    if "remove" in value:
        import aws_sdk_ec2.types.load_permission_list_request

        aws_sdk_ec2.types.load_permission_list_request.serialize_ec2_query(
            value["remove"], pairs, f"{prefix}.Remove"
        )


def deserialize_ec2_query(el: Element) -> LoadPermissionModifications:
    out: LoadPermissionModifications = {}  # type: ignore[typeddict-item]
    if el.find("Add") is not None:
        import aws_sdk_ec2.types.load_permission_list_request

        out["add"] = (
            aws_sdk_ec2.types.load_permission_list_request.deserialize_ec2_query(
                el, "Add"
            )
        )
    if el.find("Remove") is not None:
        import aws_sdk_ec2.types.load_permission_list_request

        out["remove"] = (
            aws_sdk_ec2.types.load_permission_list_request.deserialize_ec2_query(
                el, "Remove"
            )
        )
    return out
