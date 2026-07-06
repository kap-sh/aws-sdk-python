"""Generated from Smithy shape ``com.amazonaws.iot#DescribeRoleAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.role_alias


class DescribeRoleAliasRequest(TypedDict, closed=True):
    role_alias: "aws_sdk_iot.types.role_alias.RoleAlias"
    """<p>The role alias to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRoleAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRoleAliasRequest:
    out: DescribeRoleAliasRequest = {}  # type: ignore[typeddict-item]
    return out
