"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ApplicationPolicies``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.application_policy_list


class ApplicationPolicies(TypedDict):
    critical: NotRequired["bool"]
    """<p>Marks the application policy extension as critical.</p>"""
    policies: (
        "aws_sdk_pca_connector_ad.types.application_policy_list.ApplicationPolicyList"
    )
    """<p>Application policies describe what the certificate can be used for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationPolicies) -> dict:
    out: dict = {}
    if "critical" in value:
        out["Critical"] = value["critical"]
    import aws_sdk_pca_connector_ad.types.application_policy_list

    out["Policies"] = (
        aws_sdk_pca_connector_ad.types.application_policy_list.serialize_json(
            value["policies"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApplicationPolicies:
    out: ApplicationPolicies = {}  # type: ignore[typeddict-item]
    if "Critical" in data:
        out["critical"] = data["Critical"]
    if "Policies" in data:
        import aws_sdk_pca_connector_ad.types.application_policy_list

        out["policies"] = (
            aws_sdk_pca_connector_ad.types.application_policy_list.deserialize_json(
                data["Policies"]
            )
        )
    else:
        raise DeserializationError("ApplicationPolicies.policies required")
    return out
