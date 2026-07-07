"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdatePackageScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.package_id
    import aws_sdk_opensearch.types.package_scope_operation_enum
    import aws_sdk_opensearch.types.package_user_list


class UpdatePackageScopeRequest(TypedDict, closed=True):
    package_id: "aws_sdk_opensearch.types.package_id.PackageID"
    """<p>ID of the package whose scope is being updated.</p>"""
    operation: "aws_sdk_opensearch.types.package_scope_operation_enum.PackageScopeOperationEnum"
    """<p> The operation to perform on the package scope (e.g., add/remove/override users).</p>"""
    package_user_list: "aws_sdk_opensearch.types.package_user_list.PackageUserList"
    """<p> List of users to be added or removed from the package scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageScopeRequest) -> dict:
    out: dict = {}
    out["PackageID"] = value["package_id"]
    import aws_sdk_opensearch.types.package_scope_operation_enum

    out["Operation"] = (
        aws_sdk_opensearch.types.package_scope_operation_enum.serialize_json(
            value["operation"]
        )
    )
    import aws_sdk_opensearch.types.package_user_list

    out["PackageUserList"] = aws_sdk_opensearch.types.package_user_list.serialize_json(
        value["package_user_list"]
    )
    return out


def deserialize_json(data: dict) -> UpdatePackageScopeRequest:
    out: UpdatePackageScopeRequest = {}  # type: ignore[typeddict-item]
    if "PackageID" in data:
        out["package_id"] = data["PackageID"]
    else:
        raise DeserializationError("UpdatePackageScopeRequest.package_id required")
    if "Operation" in data:
        import aws_sdk_opensearch.types.package_scope_operation_enum

        out["operation"] = (
            aws_sdk_opensearch.types.package_scope_operation_enum.deserialize_json(
                data["Operation"]
            )
        )
    else:
        raise DeserializationError("UpdatePackageScopeRequest.operation required")
    if "PackageUserList" in data:
        import aws_sdk_opensearch.types.package_user_list

        out["package_user_list"] = (
            aws_sdk_opensearch.types.package_user_list.deserialize_json(
                data["PackageUserList"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePackageScopeRequest.package_user_list required"
        )
    return out
