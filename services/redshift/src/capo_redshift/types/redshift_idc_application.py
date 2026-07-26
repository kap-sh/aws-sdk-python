"""Generated from Smithy shape ``com.amazonaws.redshift#RedshiftIdcApplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.application_type
    import capo_redshift.types.authorized_token_issuer_list
    import capo_redshift.types.idc_display_name_string
    import capo_redshift.types.identity_namespace_string
    import capo_redshift.types.redshift_idc_application_name
    import capo_redshift.types.service_integration_list
    import capo_redshift.types.string
    import capo_redshift.types.tag_key_list
    import capo_redshift.types.tag_list


class RedshiftIdcApplication(TypedDict, closed=True):
    idc_instance_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The ARN for the IAM Identity Center instance that Redshift integrates with.</p>"""
    redshift_idc_application_name: NotRequired[
        "capo_redshift.types.redshift_idc_application_name.RedshiftIdcApplicationName"
    ]
    """<p>The name of the Redshift application in IAM Identity Center.</p>"""
    redshift_idc_application_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>"""
    identity_namespace: NotRequired[
        "capo_redshift.types.identity_namespace_string.IdentityNamespaceString"
    ]
    """<p>The identity namespace for the Amazon Redshift IAM Identity Center application. It determines which managed application verifies the connection token.</p>"""
    idc_display_name: NotRequired[
        "capo_redshift.types.idc_display_name_string.IdcDisplayNameString"
    ]
    """<p>The display name for the Amazon Redshift IAM Identity Center application. It appears on the console.</p>"""
    iam_role_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The ARN for the Amazon Redshift IAM Identity Center application. It has the required permissions to be assumed and invoke the IDC Identity Center API.</p>"""
    idc_managed_application_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The ARN for the Amazon Redshift IAM Identity Center application.</p>"""
    idc_onboard_status: NotRequired["capo_redshift.types.string.String"]
    """<p>The onboarding status for the Amazon Redshift IAM Identity Center application.</p>"""
    authorized_token_issuer_list: NotRequired[
        "capo_redshift.types.authorized_token_issuer_list.AuthorizedTokenIssuerList"
    ]
    """<p>The authorized token issuer list for the Amazon Redshift IAM Identity Center application.</p>"""
    service_integrations: NotRequired[
        "capo_redshift.types.service_integration_list.ServiceIntegrationList"
    ]
    """<p>A list of service integrations for the Redshift IAM Identity Center application.</p>"""
    application_type: NotRequired[
        "capo_redshift.types.application_type.ApplicationType"
    ]
    """<p>The type of application being created. Valid values are <code>None</code> or <code>Lakehouse</code>. Use <code>Lakehouse</code> to enable Amazon Redshift federated permissions on cluster.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>A list of tags.</p>"""
    sso_tag_keys: NotRequired["capo_redshift.types.tag_key_list.TagKeyList"]
    """<p>A list of tags keys that Redshift Identity Center applications copy to IAM Identity Center. For each input key, the tag corresponding to the key-value pair is propagated.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RedshiftIdcApplication, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "idc_instance_arn" in value:
        pairs.append((f"{prefix}.IdcInstanceArn", str(value["idc_instance_arn"])))
    if "redshift_idc_application_name" in value:
        pairs.append(
            (
                f"{prefix}.RedshiftIdcApplicationName",
                str(value["redshift_idc_application_name"]),
            )
        )
    if "redshift_idc_application_arn" in value:
        pairs.append(
            (
                f"{prefix}.RedshiftIdcApplicationArn",
                str(value["redshift_idc_application_arn"]),
            )
        )
    if "identity_namespace" in value:
        pairs.append((f"{prefix}.IdentityNamespace", str(value["identity_namespace"])))
    if "idc_display_name" in value:
        pairs.append((f"{prefix}.IdcDisplayName", str(value["idc_display_name"])))
    if "iam_role_arn" in value:
        pairs.append((f"{prefix}.IamRoleArn", str(value["iam_role_arn"])))
    if "idc_managed_application_arn" in value:
        pairs.append(
            (
                f"{prefix}.IdcManagedApplicationArn",
                str(value["idc_managed_application_arn"]),
            )
        )
    if "idc_onboard_status" in value:
        pairs.append((f"{prefix}.IdcOnboardStatus", str(value["idc_onboard_status"])))
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
    if "application_type" in value:
        import capo_redshift.types.application_type

        capo_redshift.types.application_type.serialize_query(
            value["application_type"], pairs, f"{prefix}.ApplicationType"
        )
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "sso_tag_keys" in value:
        import capo_redshift.types.tag_key_list

        capo_redshift.types.tag_key_list.serialize_query(
            value["sso_tag_keys"], pairs, f"{prefix}.SsoTagKeys"
        )


def deserialize_query(el: Element) -> RedshiftIdcApplication:
    out: RedshiftIdcApplication = {}  # type: ignore[typeddict-item]
    child_idc_instance_arn = el.find("IdcInstanceArn")
    if child_idc_instance_arn is not None:
        out["idc_instance_arn"] = str(child_idc_instance_arn.text or "")
    child_redshift_idc_application_name = el.find("RedshiftIdcApplicationName")
    if child_redshift_idc_application_name is not None:
        out["redshift_idc_application_name"] = str(
            child_redshift_idc_application_name.text or ""
        )
    child_redshift_idc_application_arn = el.find("RedshiftIdcApplicationArn")
    if child_redshift_idc_application_arn is not None:
        out["redshift_idc_application_arn"] = str(
            child_redshift_idc_application_arn.text or ""
        )
    child_identity_namespace = el.find("IdentityNamespace")
    if child_identity_namespace is not None:
        out["identity_namespace"] = str(child_identity_namespace.text or "")
    child_idc_display_name = el.find("IdcDisplayName")
    if child_idc_display_name is not None:
        out["idc_display_name"] = str(child_idc_display_name.text or "")
    child_iam_role_arn = el.find("IamRoleArn")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    child_idc_managed_application_arn = el.find("IdcManagedApplicationArn")
    if child_idc_managed_application_arn is not None:
        out["idc_managed_application_arn"] = str(
            child_idc_managed_application_arn.text or ""
        )
    child_idc_onboard_status = el.find("IdcOnboardStatus")
    if child_idc_onboard_status is not None:
        out["idc_onboard_status"] = str(child_idc_onboard_status.text or "")
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
    child_application_type = el.find("ApplicationType")
    if child_application_type is not None:
        import capo_redshift.types.application_type

        out["application_type"] = (
            capo_redshift.types.application_type.deserialize_query(
                child_application_type
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    child_sso_tag_keys = el.find("SsoTagKeys")
    if child_sso_tag_keys is not None:
        import capo_redshift.types.tag_key_list

        out["sso_tag_keys"] = capo_redshift.types.tag_key_list.deserialize_query(
            child_sso_tag_keys
        )
    return out
