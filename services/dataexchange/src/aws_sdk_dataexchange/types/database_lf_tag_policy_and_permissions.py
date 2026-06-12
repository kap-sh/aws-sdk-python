"""Generated from Smithy shape ``com.amazonaws.dataexchange#DatabaseLFTagPolicyAndPermissions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of_database_lf_tag_policy_permissions
    import aws_sdk_dataexchange.types.list_of_lf_tags


class DatabaseLFTagPolicyAndPermissions(TypedDict):
    expression: "aws_sdk_dataexchange.types.list_of_lf_tags.ListOfLFTags"
    """<p>A list of LF-tag conditions that apply to database resources.</p>"""
    permissions: "aws_sdk_dataexchange.types.list_of_database_lf_tag_policy_permissions.ListOfDatabaseLFTagPolicyPermissions"
    """<p>The permissions granted to subscribers on database resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseLFTagPolicyAndPermissions) -> dict:
    out: dict = {}
    import aws_sdk_dataexchange.types.list_of_lf_tags

    out["Expression"] = aws_sdk_dataexchange.types.list_of_lf_tags.serialize_json(
        value["expression"]
    )
    import aws_sdk_dataexchange.types.list_of_database_lf_tag_policy_permissions

    out["Permissions"] = (
        aws_sdk_dataexchange.types.list_of_database_lf_tag_policy_permissions.serialize_json(
            value["permissions"]
        )
    )
    return out


def deserialize_json(data: dict) -> DatabaseLFTagPolicyAndPermissions:
    out: DatabaseLFTagPolicyAndPermissions = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        import aws_sdk_dataexchange.types.list_of_lf_tags

        out["expression"] = aws_sdk_dataexchange.types.list_of_lf_tags.deserialize_json(
            data["Expression"]
        )
    else:
        raise DeserializationError(
            "DatabaseLFTagPolicyAndPermissions.expression required"
        )
    if "Permissions" in data:
        import aws_sdk_dataexchange.types.list_of_database_lf_tag_policy_permissions

        out["permissions"] = (
            aws_sdk_dataexchange.types.list_of_database_lf_tag_policy_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError(
            "DatabaseLFTagPolicyAndPermissions.permissions required"
        )
    return out
