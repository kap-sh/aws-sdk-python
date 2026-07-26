"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ApplicationPolicy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pca_connector_ad.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.application_policy_type
    import capo_pca_connector_ad.types.custom_object_identifier


class _ApplicationPolicy_PolicyType(TypedDict, closed=True):
    PolicyType: (
        "capo_pca_connector_ad.types.application_policy_type.ApplicationPolicyType"
    )


class _ApplicationPolicy_PolicyObjectIdentifier(TypedDict, closed=True):
    PolicyObjectIdentifier: (
        "capo_pca_connector_ad.types.custom_object_identifier.CustomObjectIdentifier"
    )


ApplicationPolicy: TypeAlias = (
    _ApplicationPolicy_PolicyType | _ApplicationPolicy_PolicyObjectIdentifier
)


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationPolicy) -> dict:
    if "PolicyType" in value:
        import capo_pca_connector_ad.types.application_policy_type

        return {
            "PolicyType": capo_pca_connector_ad.types.application_policy_type.serialize_json(
                value["PolicyType"]
            )
        }
    elif "PolicyObjectIdentifier" in value:
        return {"PolicyObjectIdentifier": value["PolicyObjectIdentifier"]}
    else:
        raise SerializationError("ApplicationPolicy: no variant present")


def deserialize_json(data: dict) -> ApplicationPolicy:
    if "PolicyType" in data:
        import capo_pca_connector_ad.types.application_policy_type

        return {
            "PolicyType": capo_pca_connector_ad.types.application_policy_type.deserialize_json(
                data["PolicyType"]
            )
        }
    elif "PolicyObjectIdentifier" in data:
        return {"PolicyObjectIdentifier": data["PolicyObjectIdentifier"]}
    else:
        raise DeserializationError("ApplicationPolicy: no recognized variant key")
