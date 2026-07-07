"""Generated from Smithy shape ``com.amazonaws.dataexchange#TableLFTagPolicyAndPermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of_lf_tags
    import aws_sdk_dataexchange.types.list_of_table_tag_policy_lf_permissions


class TableLFTagPolicyAndPermissions(TypedDict, closed=True):
    expression: "aws_sdk_dataexchange.types.list_of_lf_tags.ListOfLFTags"
    """<p>A list of LF-tag conditions that apply to table resources.</p>"""
    permissions: "aws_sdk_dataexchange.types.list_of_table_tag_policy_lf_permissions.ListOfTableTagPolicyLFPermissions"
    """<p>The permissions granted to subscribers on table resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableLFTagPolicyAndPermissions) -> dict:
    out: dict = {}
    import aws_sdk_dataexchange.types.list_of_lf_tags

    out["Expression"] = aws_sdk_dataexchange.types.list_of_lf_tags.serialize_json(
        value["expression"]
    )
    import aws_sdk_dataexchange.types.list_of_table_tag_policy_lf_permissions

    out["Permissions"] = (
        aws_sdk_dataexchange.types.list_of_table_tag_policy_lf_permissions.serialize_json(
            value["permissions"]
        )
    )
    return out


def deserialize_json(data: dict) -> TableLFTagPolicyAndPermissions:
    out: TableLFTagPolicyAndPermissions = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        import aws_sdk_dataexchange.types.list_of_lf_tags

        out["expression"] = aws_sdk_dataexchange.types.list_of_lf_tags.deserialize_json(
            data["Expression"]
        )
    else:
        raise DeserializationError("TableLFTagPolicyAndPermissions.expression required")
    if "Permissions" in data:
        import aws_sdk_dataexchange.types.list_of_table_tag_policy_lf_permissions

        out["permissions"] = (
            aws_sdk_dataexchange.types.list_of_table_tag_policy_lf_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError(
            "TableLFTagPolicyAndPermissions.permissions required"
        )
    return out
