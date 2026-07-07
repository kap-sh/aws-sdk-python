"""Generated from Smithy shape ``com.amazonaws.iam#OrganizationsDecisionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.boolean_type


class OrganizationsDecisionDetail(TypedDict, closed=True):
    allowed_by_organizations: "aws_sdk_iam.types.boolean_type.booleanType"
    """<p>Specifies whether the simulated operation is allowed by the Organizations service control policies that impact the simulated user's account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OrganizationsDecisionDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (
            f"{prefix}.AllowedByOrganizations",
            "true" if value.get("allowed_by_organizations", False) else "false",
        )
    )


def deserialize_query(el: Element) -> OrganizationsDecisionDetail:
    out: OrganizationsDecisionDetail = {}  # type: ignore[typeddict-item]
    child_allowed_by_organizations = el.find("AllowedByOrganizations")
    if child_allowed_by_organizations is not None:
        out["allowed_by_organizations"] = (
            child_allowed_by_organizations.text or ""
        ).lower() == "true"
    else:
        out["allowed_by_organizations"] = False
    return out
