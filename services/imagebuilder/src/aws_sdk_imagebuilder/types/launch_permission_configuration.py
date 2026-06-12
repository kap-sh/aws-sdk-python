"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LaunchPermissionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.account_list
    import aws_sdk_imagebuilder.types.organization_arn_list
    import aws_sdk_imagebuilder.types.organizational_unit_arn_list
    import aws_sdk_imagebuilder.types.string_list


class LaunchPermissionConfiguration(TypedDict):
    user_ids: NotRequired["aws_sdk_imagebuilder.types.account_list.AccountList"]
    """<p>The Amazon Web Services account ID.</p>"""
    user_groups: NotRequired["aws_sdk_imagebuilder.types.string_list.StringList"]
    """<p>The name of the group.</p>"""
    organization_arns: NotRequired[
        "aws_sdk_imagebuilder.types.organization_arn_list.OrganizationArnList"
    ]
    """<p>The ARN for an Amazon Web Services Organization that you want to share your AMI with. For more information, see <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html\">What is Organizations?</a>.</p>"""
    organizational_unit_arns: NotRequired[
        "aws_sdk_imagebuilder.types.organizational_unit_arn_list.OrganizationalUnitArnList"
    ]
    """<p>The ARN for an Organizations organizational unit (OU) that you want to share your AMI with. For more information about key concepts for Organizations, see <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html\">Organizations terminology and concepts</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchPermissionConfiguration) -> dict:
    out: dict = {}
    if "user_ids" in value:
        import aws_sdk_imagebuilder.types.account_list

        out["userIds"] = aws_sdk_imagebuilder.types.account_list.serialize_json(
            value["user_ids"]
        )
    if "user_groups" in value:
        import aws_sdk_imagebuilder.types.string_list

        out["userGroups"] = aws_sdk_imagebuilder.types.string_list.serialize_json(
            value["user_groups"]
        )
    if "organization_arns" in value:
        import aws_sdk_imagebuilder.types.organization_arn_list

        out["organizationArns"] = (
            aws_sdk_imagebuilder.types.organization_arn_list.serialize_json(
                value["organization_arns"]
            )
        )
    if "organizational_unit_arns" in value:
        import aws_sdk_imagebuilder.types.organizational_unit_arn_list

        out["organizationalUnitArns"] = (
            aws_sdk_imagebuilder.types.organizational_unit_arn_list.serialize_json(
                value["organizational_unit_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> LaunchPermissionConfiguration:
    out: LaunchPermissionConfiguration = {}  # type: ignore[typeddict-item]
    if "userIds" in data:
        import aws_sdk_imagebuilder.types.account_list

        out["user_ids"] = aws_sdk_imagebuilder.types.account_list.deserialize_json(
            data["userIds"]
        )
    if "userGroups" in data:
        import aws_sdk_imagebuilder.types.string_list

        out["user_groups"] = aws_sdk_imagebuilder.types.string_list.deserialize_json(
            data["userGroups"]
        )
    if "organizationArns" in data:
        import aws_sdk_imagebuilder.types.organization_arn_list

        out["organization_arns"] = (
            aws_sdk_imagebuilder.types.organization_arn_list.deserialize_json(
                data["organizationArns"]
            )
        )
    if "organizationalUnitArns" in data:
        import aws_sdk_imagebuilder.types.organizational_unit_arn_list

        out["organizational_unit_arns"] = (
            aws_sdk_imagebuilder.types.organizational_unit_arn_list.deserialize_json(
                data["organizationalUnitArns"]
            )
        )
    return out
