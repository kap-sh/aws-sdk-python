"""Generated from Smithy shape ``com.amazonaws.kendra#AclConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.column_name


class AclConfiguration(TypedDict):
    allowed_groups_column_name: "aws_sdk_kendra.types.column_name.ColumnName"
    """<p>A list of groups, separated by semi-colons, that filters a query response based on user context. The document is only returned to users that are in one of the groups specified in the <code>UserContext</code> field of the <code>Query</code> API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AclConfiguration) -> dict:
    out: dict = {}
    out["AllowedGroupsColumnName"] = value["allowed_groups_column_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AclConfiguration:
    out: AclConfiguration = {}  # type: ignore[typeddict-item]
    if "AllowedGroupsColumnName" in data:
        out["allowed_groups_column_name"] = data["AllowedGroupsColumnName"]
    else:
        raise DeserializationError(
            "AclConfiguration.allowed_groups_column_name required"
        )
    return out
