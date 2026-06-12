"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOrganizationScope``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsOrganizationScope(TypedDict):
    organization_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The unique identifier (ID) of the organization (for example, <code>o-abcd1234567890</code>). The organization must be the delegated administrator's own organization. If you omit this value and provide <code>OrganizationalUnitId</code>, Security Hub uses the caller's organization ID.</p>"""
    organizational_unit_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The unique identifier (ID) of the organizational unit (OU) (for example, <code>ou-ab12-cd345678</code>). The OU must exist within the delegated administrator's own organization. When specified, the results include only data from accounts in this OU.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsOrganizationScope) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    if "organizational_unit_id" in value:
        out["OrganizationalUnitId"] = value["organizational_unit_id"]
    return out


def deserialize_json(data: dict) -> AwsOrganizationScope:
    out: AwsOrganizationScope = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    if "OrganizationalUnitId" in data:
        out["organizational_unit_id"] = data["OrganizationalUnitId"]
    return out
