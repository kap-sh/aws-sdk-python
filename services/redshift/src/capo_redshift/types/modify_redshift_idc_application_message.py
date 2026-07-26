"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyRedshiftIdcApplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.authorized_token_issuer_list
    import capo_redshift.types.idc_display_name_string
    import capo_redshift.types.identity_namespace_string
    import capo_redshift.types.service_integration_list
    import capo_redshift.types.string


class ModifyRedshiftIdcApplicationMessage(TypedDict, closed=True):
    redshift_idc_application_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>"""
    identity_namespace: NotRequired[
        "capo_redshift.types.identity_namespace_string.IdentityNamespaceString"
    ]
    """<p>The namespace for the Amazon Redshift IAM Identity Center application to change. It determines which managed application verifies the connection token.</p>"""
    iam_role_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The IAM role ARN associated with the Amazon Redshift IAM Identity Center application to change. It has the required permissions to be assumed and invoke the IDC Identity Center API.</p>"""
    idc_display_name: NotRequired[
        "capo_redshift.types.idc_display_name_string.IdcDisplayNameString"
    ]
    """<p>The display name for the Amazon Redshift IAM Identity Center application to change. It appears on the console.</p>"""
    authorized_token_issuer_list: NotRequired[
        "capo_redshift.types.authorized_token_issuer_list.AuthorizedTokenIssuerList"
    ]
    """<p>The authorized token issuer list for the Amazon Redshift IAM Identity Center application to change.</p>"""
    service_integrations: NotRequired[
        "capo_redshift.types.service_integration_list.ServiceIntegrationList"
    ]
    """<p>A collection of service integrations associated with the application.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyRedshiftIdcApplicationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "redshift_idc_application_arn" in value:
        pairs.append(
            (
                f"{prefix}.RedshiftIdcApplicationArn",
                str(value["redshift_idc_application_arn"]),
            )
        )
    if "identity_namespace" in value:
        pairs.append((f"{prefix}.IdentityNamespace", str(value["identity_namespace"])))
    if "iam_role_arn" in value:
        pairs.append((f"{prefix}.IamRoleArn", str(value["iam_role_arn"])))
    if "idc_display_name" in value:
        pairs.append((f"{prefix}.IdcDisplayName", str(value["idc_display_name"])))
    if "authorized_token_issuer_list" in value:
        import capo_redshift.types.authorized_token_issuer_list

        capo_redshift.types.authorized_token_issuer_list.serialize_query(
            value["authorized_token_issuer_list"],
            pairs,
            f"{prefix}.AuthorizedTokenIssuerList",
        )
    if "service_integrations" in value:
        import capo_redshift.types.service_integration_list

        capo_redshift.types.service_integration_list.serialize_query(
            value["service_integrations"], pairs, f"{prefix}.ServiceIntegrations"
        )


def deserialize_query(el: Element) -> ModifyRedshiftIdcApplicationMessage:
    out: ModifyRedshiftIdcApplicationMessage = {}  # type: ignore[typeddict-item]
    child_redshift_idc_application_arn = el.find("RedshiftIdcApplicationArn")
    if child_redshift_idc_application_arn is not None:
        out["redshift_idc_application_arn"] = str(
            child_redshift_idc_application_arn.text or ""
        )
    child_identity_namespace = el.find("IdentityNamespace")
    if child_identity_namespace is not None:
        out["identity_namespace"] = str(child_identity_namespace.text or "")
    child_iam_role_arn = el.find("IamRoleArn")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    child_idc_display_name = el.find("IdcDisplayName")
    if child_idc_display_name is not None:
        out["idc_display_name"] = str(child_idc_display_name.text or "")
    child_authorized_token_issuer_list = el.find("AuthorizedTokenIssuerList")
    if child_authorized_token_issuer_list is not None:
        import capo_redshift.types.authorized_token_issuer_list

        out["authorized_token_issuer_list"] = (
            capo_redshift.types.authorized_token_issuer_list.deserialize_query(
                child_authorized_token_issuer_list
            )
        )
    child_service_integrations = el.find("ServiceIntegrations")
    if child_service_integrations is not None:
        import capo_redshift.types.service_integration_list

        out["service_integrations"] = (
            capo_redshift.types.service_integration_list.deserialize_query(
                child_service_integrations
            )
        )
    return out
