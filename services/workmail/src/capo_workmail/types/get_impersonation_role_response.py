"""Generated from Smithy shape ``com.amazonaws.workmail#GetImpersonationRoleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.impersonation_role_description
    import capo_workmail.types.impersonation_role_id
    import capo_workmail.types.impersonation_role_name
    import capo_workmail.types.impersonation_role_type
    import capo_workmail.types.impersonation_rule_list
    import capo_workmail.types.timestamp


class GetImpersonationRoleResponse(TypedDict, closed=True):
    impersonation_role_id: NotRequired[
        "capo_workmail.types.impersonation_role_id.ImpersonationRoleId"
    ]
    """<p>The impersonation role ID.</p>"""
    name: NotRequired[
        "capo_workmail.types.impersonation_role_name.ImpersonationRoleName"
    ]
    """<p>The impersonation role name.</p>"""
    type: NotRequired[
        "capo_workmail.types.impersonation_role_type.ImpersonationRoleType"
    ]
    """<p>The impersonation role type.</p>"""
    description: NotRequired[
        "capo_workmail.types.impersonation_role_description.ImpersonationRoleDescription"
    ]
    """<p>The impersonation role description.</p>"""
    rules: NotRequired[
        "capo_workmail.types.impersonation_rule_list.ImpersonationRuleList"
    ]
    """<p>The list of rules for the given impersonation role.</p>"""
    date_created: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date when the impersonation role was created.</p>"""
    date_modified: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date when the impersonation role was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetImpersonationRoleResponse) -> dict:
    out: dict = {}
    if "impersonation_role_id" in value:
        out["ImpersonationRoleId"] = value["impersonation_role_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_workmail.types.impersonation_role_type

        out["Type"] = (
            capo_workmail.types.impersonation_role_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "rules" in value:
        import capo_workmail.types.impersonation_rule_list

        out["Rules"] = (
            capo_workmail.types.impersonation_rule_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    if "date_created" in value:
        import capo_workmail.types.timestamp

        out["DateCreated"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_created"]
        )
    if "date_modified" in value:
        import capo_workmail.types.timestamp

        out["DateModified"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_modified"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetImpersonationRoleResponse:
    out: GetImpersonationRoleResponse = {}  # type: ignore[typeddict-item]
    if "ImpersonationRoleId" in data:
        out["impersonation_role_id"] = data["ImpersonationRoleId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import capo_workmail.types.impersonation_role_type

        out["type"] = (
            capo_workmail.types.impersonation_role_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Rules" in data:
        import capo_workmail.types.impersonation_rule_list

        out["rules"] = (
            capo_workmail.types.impersonation_rule_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    if "DateCreated" in data:
        import capo_workmail.types.timestamp

        out["date_created"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateCreated"]
        )
    if "DateModified" in data:
        import capo_workmail.types.timestamp

        out["date_modified"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateModified"]
        )
    return out
