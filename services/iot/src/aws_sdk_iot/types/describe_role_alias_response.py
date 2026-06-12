"""Generated from Smithy shape ``com.amazonaws.iot#DescribeRoleAliasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.role_alias_description


class DescribeRoleAliasResponse(TypedDict):
    role_alias_description: NotRequired[
        "aws_sdk_iot.types.role_alias_description.RoleAliasDescription"
    ]
    """<p>The role alias description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRoleAliasResponse) -> dict:
    out: dict = {}
    if "role_alias_description" in value:
        import aws_sdk_iot.types.role_alias_description

        out["roleAliasDescription"] = (
            aws_sdk_iot.types.role_alias_description.serialize_json(
                value["role_alias_description"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeRoleAliasResponse:
    out: DescribeRoleAliasResponse = {}  # type: ignore[typeddict-item]
    if "roleAliasDescription" in data:
        import aws_sdk_iot.types.role_alias_description

        out["role_alias_description"] = (
            aws_sdk_iot.types.role_alias_description.deserialize_json(
                data["roleAliasDescription"]
            )
        )
    return out
