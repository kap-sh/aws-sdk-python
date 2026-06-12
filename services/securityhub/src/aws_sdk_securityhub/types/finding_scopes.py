"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingScopes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_organization_scope_list


class FindingScopes(TypedDict):
    aws_organizations: NotRequired[
        "aws_sdk_securityhub.types.aws_organization_scope_list.AwsOrganizationScopeList"
    ]
    """<p>A list of Organizations scopes to include in the query results. Each entry in the list specifies an organization or organizational unit to include for the delegated administrator's account. If the list specifies multiple entries, the entries are combined using OR logic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingScopes) -> dict:
    out: dict = {}
    if "aws_organizations" in value:
        import aws_sdk_securityhub.types.aws_organization_scope_list

        out["AwsOrganizations"] = (
            aws_sdk_securityhub.types.aws_organization_scope_list.serialize_json(
                value["aws_organizations"]
            )
        )
    return out


def deserialize_json(data: dict) -> FindingScopes:
    out: FindingScopes = {}  # type: ignore[typeddict-item]
    if "AwsOrganizations" in data:
        import aws_sdk_securityhub.types.aws_organization_scope_list

        out["aws_organizations"] = (
            aws_sdk_securityhub.types.aws_organization_scope_list.deserialize_json(
                data["AwsOrganizations"]
            )
        )
    return out
