"""Generated from Smithy shape ``com.amazonaws.iam#DisableOrganizationsRootSessionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.features_list_type
    import aws_sdk_iam.types.organization_id_type


class DisableOrganizationsRootSessionsResponse(TypedDict):
    organization_id: NotRequired[
        "aws_sdk_iam.types.organization_id_type.OrganizationIdType"
    ]
    """<p>The unique identifier (ID) of an organization.</p>"""
    enabled_features: NotRequired[
        "aws_sdk_iam.types.features_list_type.FeaturesListType"
    ]
    """<p>The features you have enabled for centralized root access of member accounts in your organization.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DisableOrganizationsRootSessionsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "organization_id" in value:
        pairs.append((f"{prefix}.OrganizationId", str(value["organization_id"])))
    if "enabled_features" in value:
        import aws_sdk_iam.types.features_list_type

        aws_sdk_iam.types.features_list_type.serialize_query(
            value["enabled_features"], pairs, f"{prefix}.EnabledFeatures"
        )


def deserialize_query(el: Element) -> DisableOrganizationsRootSessionsResponse:
    out: DisableOrganizationsRootSessionsResponse = {}  # type: ignore[typeddict-item]
    child_organization_id = el.find("OrganizationId")
    if child_organization_id is not None:
        out["organization_id"] = str(child_organization_id.text or "")
    child_enabled_features = el.find("EnabledFeatures")
    if child_enabled_features is not None:
        import aws_sdk_iam.types.features_list_type

        out["enabled_features"] = (
            aws_sdk_iam.types.features_list_type.deserialize_query(
                child_enabled_features
            )
        )
    return out
