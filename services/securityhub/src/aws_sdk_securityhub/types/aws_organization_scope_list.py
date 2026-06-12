"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOrganizationScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_organization_scope

AwsOrganizationScopeList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_organization_scope.AwsOrganizationScope"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsOrganizationScopeList) -> list:
    import aws_sdk_securityhub.types.aws_organization_scope

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_organization_scope.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsOrganizationScopeList:
    import aws_sdk_securityhub.types.aws_organization_scope

    out: AwsOrganizationScopeList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_organization_scope.deserialize_json(item)
        )
    return out
