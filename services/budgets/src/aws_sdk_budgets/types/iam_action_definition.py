"""Generated from Smithy shape ``com.amazonaws.budgets#IamActionDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.groups
    import aws_sdk_budgets.types.policy_arn
    import aws_sdk_budgets.types.roles
    import aws_sdk_budgets.types.users


class IamActionDefinition(TypedDict):
    policy_arn: "aws_sdk_budgets.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy to be attached. </p>"""
    roles: NotRequired["aws_sdk_budgets.types.roles.Roles"]
    """<p>A list of roles to be attached. There must be at least one role. </p>"""
    groups: NotRequired["aws_sdk_budgets.types.groups.Groups"]
    """<p>A list of groups to be attached. There must be at least one group. </p>"""
    users: NotRequired["aws_sdk_budgets.types.users.Users"]
    """<p>A list of users to be attached. There must be at least one user. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IamActionDefinition) -> dict:
    out: dict = {}
    out["PolicyArn"] = value["policy_arn"]
    if "roles" in value:
        import aws_sdk_budgets.types.roles

        out["Roles"] = aws_sdk_budgets.types.roles.serialize_aws_json_1_1(
            value["roles"]
        )
    if "groups" in value:
        import aws_sdk_budgets.types.groups

        out["Groups"] = aws_sdk_budgets.types.groups.serialize_aws_json_1_1(
            value["groups"]
        )
    if "users" in value:
        import aws_sdk_budgets.types.users

        out["Users"] = aws_sdk_budgets.types.users.serialize_aws_json_1_1(
            value["users"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IamActionDefinition:
    out: IamActionDefinition = {}  # type: ignore[typeddict-item]
    if "PolicyArn" in data:
        out["policy_arn"] = data["PolicyArn"]
    else:
        raise DeserializationError("IamActionDefinition.policy_arn required")
    if "Roles" in data:
        import aws_sdk_budgets.types.roles

        out["roles"] = aws_sdk_budgets.types.roles.deserialize_aws_json_1_1(
            data["Roles"]
        )
    if "Groups" in data:
        import aws_sdk_budgets.types.groups

        out["groups"] = aws_sdk_budgets.types.groups.deserialize_aws_json_1_1(
            data["Groups"]
        )
    if "Users" in data:
        import aws_sdk_budgets.types.users

        out["users"] = aws_sdk_budgets.types.users.deserialize_aws_json_1_1(
            data["Users"]
        )
    return out
