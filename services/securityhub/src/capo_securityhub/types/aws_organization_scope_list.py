"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOrganizationScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_organization_scope

AwsOrganizationScopeList: TypeAlias = list[
    "capo_securityhub.types.aws_organization_scope.AwsOrganizationScope"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsOrganizationScopeList) -> list:
    import capo_securityhub.types.aws_organization_scope

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.aws_organization_scope.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsOrganizationScopeList:
    import capo_securityhub.types.aws_organization_scope

    out: AwsOrganizationScopeList = []
    for item in data:
        out.append(capo_securityhub.types.aws_organization_scope.deserialize_json(item))
    return out
