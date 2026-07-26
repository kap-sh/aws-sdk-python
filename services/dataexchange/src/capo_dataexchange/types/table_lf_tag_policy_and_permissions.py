"""Generated from Smithy shape ``com.amazonaws.dataexchange#TableLFTagPolicyAndPermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.list_of_lf_tags
    import capo_dataexchange.types.list_of_table_tag_policy_lf_permissions


class TableLFTagPolicyAndPermissions(TypedDict, closed=True):
    expression: "capo_dataexchange.types.list_of_lf_tags.ListOfLFTags"
    """<p>A list of LF-tag conditions that apply to table resources.</p>"""
    permissions: "capo_dataexchange.types.list_of_table_tag_policy_lf_permissions.ListOfTableTagPolicyLFPermissions"
    """<p>The permissions granted to subscribers on table resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableLFTagPolicyAndPermissions) -> dict:
    out: dict = {}
    import capo_dataexchange.types.list_of_lf_tags

    out["Expression"] = capo_dataexchange.types.list_of_lf_tags.serialize_json(
        value["expression"]
    )
    import capo_dataexchange.types.list_of_table_tag_policy_lf_permissions

    out["Permissions"] = (
        capo_dataexchange.types.list_of_table_tag_policy_lf_permissions.serialize_json(
            value["permissions"]
        )
    )
    return out


def deserialize_json(data: dict) -> TableLFTagPolicyAndPermissions:
    out: TableLFTagPolicyAndPermissions = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        import capo_dataexchange.types.list_of_lf_tags

        out["expression"] = capo_dataexchange.types.list_of_lf_tags.deserialize_json(
            data["Expression"]
        )
    else:
        raise DeserializationError("TableLFTagPolicyAndPermissions.expression required")
    if "Permissions" in data:
        import capo_dataexchange.types.list_of_table_tag_policy_lf_permissions

        out["permissions"] = (
            capo_dataexchange.types.list_of_table_tag_policy_lf_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError(
            "TableLFTagPolicyAndPermissions.permissions required"
        )
    return out
