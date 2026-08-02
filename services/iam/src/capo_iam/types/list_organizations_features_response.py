"""Generated from Smithy shape ``com.amazonaws.iam#ListOrganizationsFeaturesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.features_list_type
    import capo_iam.types.organization_id_type


class ListOrganizationsFeaturesResponse(TypedDict, closed=True):
    organization_id: NotRequired[
        "capo_iam.types.organization_id_type.OrganizationIdType"
    ]
    """<p>The unique identifier (ID) of an organization.</p>"""
    enabled_features: NotRequired["capo_iam.types.features_list_type.FeaturesListType"]
    """<p>Specifies the features that are currently available in your organization.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListOrganizationsFeaturesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "organization_id" in value:
        pairs.append((f"{key_prefix}OrganizationId", str(value["organization_id"])))
    if "enabled_features" in value:
        import capo_iam.types.features_list_type

        capo_iam.types.features_list_type.serialize_query(
            value["enabled_features"], pairs, f"{key_prefix}EnabledFeatures"
        )


def deserialize_query(el: Element) -> ListOrganizationsFeaturesResponse:
    out: ListOrganizationsFeaturesResponse = {}  # type: ignore[typeddict-item]
    child_organization_id = el.find("OrganizationId")
    if child_organization_id is not None:
        out["organization_id"] = str(child_organization_id.text or "")
    child_enabled_features = el.find("EnabledFeatures")
    if child_enabled_features is not None:
        import capo_iam.types.features_list_type

        out["enabled_features"] = capo_iam.types.features_list_type.deserialize_query(
            child_enabled_features
        )
    return out
