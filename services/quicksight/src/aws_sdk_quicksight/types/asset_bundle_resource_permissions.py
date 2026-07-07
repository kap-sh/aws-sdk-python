"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleResourcePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_list
    import aws_sdk_quicksight.types.asset_bundle_principal_list


class AssetBundleResourcePermissions(TypedDict, closed=True):
    principals: (
        "aws_sdk_quicksight.types.asset_bundle_principal_list.AssetBundlePrincipalList"
    )
    """<p>A list of principals to grant permissions on.</p>"""
    actions: "aws_sdk_quicksight.types.action_list.ActionList"
    """<p>A list of IAM actions to grant permissions on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleResourcePermissions) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.asset_bundle_principal_list

    out["Principals"] = (
        aws_sdk_quicksight.types.asset_bundle_principal_list.serialize_json(
            value["principals"]
        )
    )
    import aws_sdk_quicksight.types.action_list

    out["Actions"] = aws_sdk_quicksight.types.action_list.serialize_json(
        value["actions"]
    )
    return out


def deserialize_json(data: dict) -> AssetBundleResourcePermissions:
    out: AssetBundleResourcePermissions = {}  # type: ignore[typeddict-item]
    if "Principals" in data:
        import aws_sdk_quicksight.types.asset_bundle_principal_list

        out["principals"] = (
            aws_sdk_quicksight.types.asset_bundle_principal_list.deserialize_json(
                data["Principals"]
            )
        )
    else:
        raise DeserializationError("AssetBundleResourcePermissions.principals required")
    if "Actions" in data:
        import aws_sdk_quicksight.types.action_list

        out["actions"] = aws_sdk_quicksight.types.action_list.deserialize_json(
            data["Actions"]
        )
    else:
        raise DeserializationError("AssetBundleResourcePermissions.actions required")
    return out
