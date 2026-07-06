"""Generated from Smithy shape ``com.amazonaws.odb#GetOciOnboardingStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.oci_iam_role_list
    import aws_sdk_odb.types.oci_identity_domain
    import aws_sdk_odb.types.oci_onboarding_status
    import aws_sdk_odb.types.subscription_errors


class GetOciOnboardingStatusOutput(TypedDict, closed=True):
    status: NotRequired["aws_sdk_odb.types.oci_onboarding_status.OciOnboardingStatus"]
    existing_tenancy_activation_link: NotRequired["str"]
    """<p>The existing OCI tenancy activation link for your Amazon Web Services account.</p>"""
    new_tenancy_activation_link: NotRequired["str"]
    """<p>A new OCI tenancy activation link for your Amazon Web Services account.</p>"""
    oci_identity_domain: NotRequired[
        "aws_sdk_odb.types.oci_identity_domain.OciIdentityDomain"
    ]
    """<p>The Oracle Cloud Infrastructure (OCI) identity domain information in the onboarding status response.</p>"""
    autonomous_database_oci_integration_iam_roles: NotRequired[
        "aws_sdk_odb.types.oci_iam_role_list.OciIamRoleList"
    ]
    """<p>The list of Amazon Web Services Identity and Access Management (IAM) service roles used for Autonomous Database integration with Oracle Cloud Infrastructure (OCI).</p>"""
    linked_oci_tenancy_id: NotRequired["str"]
    """<p>The unique identifier of the Oracle Cloud Infrastructure (OCI) tenancy that is linked to your Amazon Web Services account.</p>"""
    linked_oci_compartment_id: NotRequired["str"]
    """<p>The unique identifier of the Oracle Cloud Infrastructure (OCI) compartment that is linked to your Amazon Web Services account.</p>"""
    subscription_errors: NotRequired[
        "aws_sdk_odb.types.subscription_errors.SubscriptionErrors"
    ]
    """<p>The list of errors that occurred during the subscription process for your Amazon Web Services account, if any.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOciOnboardingStatusOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_odb.types.oci_onboarding_status

        out["status"] = aws_sdk_odb.types.oci_onboarding_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "existing_tenancy_activation_link" in value:
        out["existingTenancyActivationLink"] = value["existing_tenancy_activation_link"]
    if "new_tenancy_activation_link" in value:
        out["newTenancyActivationLink"] = value["new_tenancy_activation_link"]
    if "oci_identity_domain" in value:
        import aws_sdk_odb.types.oci_identity_domain

        out["ociIdentityDomain"] = (
            aws_sdk_odb.types.oci_identity_domain.serialize_aws_json_1_0(
                value["oci_identity_domain"]
            )
        )
    if "autonomous_database_oci_integration_iam_roles" in value:
        import aws_sdk_odb.types.oci_iam_role_list

        out["autonomousDatabaseOciIntegrationIamRoles"] = (
            aws_sdk_odb.types.oci_iam_role_list.serialize_aws_json_1_0(
                value["autonomous_database_oci_integration_iam_roles"]
            )
        )
    if "linked_oci_tenancy_id" in value:
        out["linkedOciTenancyId"] = value["linked_oci_tenancy_id"]
    if "linked_oci_compartment_id" in value:
        out["linkedOciCompartmentId"] = value["linked_oci_compartment_id"]
    if "subscription_errors" in value:
        import aws_sdk_odb.types.subscription_errors

        out["subscriptionErrors"] = (
            aws_sdk_odb.types.subscription_errors.serialize_aws_json_1_0(
                value["subscription_errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOciOnboardingStatusOutput:
    out: GetOciOnboardingStatusOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_odb.types.oci_onboarding_status

        out["status"] = (
            aws_sdk_odb.types.oci_onboarding_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "existingTenancyActivationLink" in data:
        out["existing_tenancy_activation_link"] = data["existingTenancyActivationLink"]
    if "newTenancyActivationLink" in data:
        out["new_tenancy_activation_link"] = data["newTenancyActivationLink"]
    if "ociIdentityDomain" in data:
        import aws_sdk_odb.types.oci_identity_domain

        out["oci_identity_domain"] = (
            aws_sdk_odb.types.oci_identity_domain.deserialize_aws_json_1_0(
                data["ociIdentityDomain"]
            )
        )
    if "autonomousDatabaseOciIntegrationIamRoles" in data:
        import aws_sdk_odb.types.oci_iam_role_list

        out["autonomous_database_oci_integration_iam_roles"] = (
            aws_sdk_odb.types.oci_iam_role_list.deserialize_aws_json_1_0(
                data["autonomousDatabaseOciIntegrationIamRoles"]
            )
        )
    if "linkedOciTenancyId" in data:
        out["linked_oci_tenancy_id"] = data["linkedOciTenancyId"]
    if "linkedOciCompartmentId" in data:
        out["linked_oci_compartment_id"] = data["linkedOciCompartmentId"]
    if "subscriptionErrors" in data:
        import aws_sdk_odb.types.subscription_errors

        out["subscription_errors"] = (
            aws_sdk_odb.types.subscription_errors.deserialize_aws_json_1_0(
                data["subscriptionErrors"]
            )
        )
    return out
