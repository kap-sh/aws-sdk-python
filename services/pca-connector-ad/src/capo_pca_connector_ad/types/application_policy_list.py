"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ApplicationPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.application_policy

ApplicationPolicyList: TypeAlias = list[
    "capo_pca_connector_ad.types.application_policy.ApplicationPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationPolicyList) -> list:
    import capo_pca_connector_ad.types.application_policy

    out: list = []
    for item in value:
        out.append(capo_pca_connector_ad.types.application_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationPolicyList:
    import capo_pca_connector_ad.types.application_policy

    out: ApplicationPolicyList = []
    for item in data:
        out.append(
            capo_pca_connector_ad.types.application_policy.deserialize_json(item)
        )
    return out
