"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdatePackageScopeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.package_id
    import aws_sdk_opensearch.types.package_scope_operation_enum
    import aws_sdk_opensearch.types.package_user_list


class UpdatePackageScopeResponse(TypedDict):
    package_id: NotRequired["aws_sdk_opensearch.types.package_id.PackageID"]
    """<p> ID of the package whose scope was updated.</p>"""
    operation: NotRequired[
        "aws_sdk_opensearch.types.package_scope_operation_enum.PackageScopeOperationEnum"
    ]
    """<p>The operation that was performed on the package scope.</p>"""
    package_user_list: NotRequired[
        "aws_sdk_opensearch.types.package_user_list.PackageUserList"
    ]
    """<p> List of users who have access to the package after the scope update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageScopeResponse) -> dict:
    out: dict = {}
    if "package_id" in value:
        out["PackageID"] = value["package_id"]
    if "operation" in value:
        import aws_sdk_opensearch.types.package_scope_operation_enum

        out["Operation"] = (
            aws_sdk_opensearch.types.package_scope_operation_enum.serialize_json(
                value["operation"]
            )
        )
    if "package_user_list" in value:
        import aws_sdk_opensearch.types.package_user_list

        out["PackageUserList"] = (
            aws_sdk_opensearch.types.package_user_list.serialize_json(
                value["package_user_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePackageScopeResponse:
    out: UpdatePackageScopeResponse = {}  # type: ignore[typeddict-item]
    if "PackageID" in data:
        out["package_id"] = data["PackageID"]
    if "Operation" in data:
        import aws_sdk_opensearch.types.package_scope_operation_enum

        out["operation"] = (
            aws_sdk_opensearch.types.package_scope_operation_enum.deserialize_json(
                data["Operation"]
            )
        )
    if "PackageUserList" in data:
        import aws_sdk_opensearch.types.package_user_list

        out["package_user_list"] = (
            aws_sdk_opensearch.types.package_user_list.deserialize_json(
                data["PackageUserList"]
            )
        )
    return out
