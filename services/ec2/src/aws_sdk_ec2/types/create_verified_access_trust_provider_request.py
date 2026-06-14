"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessTrustProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.create_verified_access_native_application_oidc_options
    import aws_sdk_ec2.types.create_verified_access_trust_provider_device_options
    import aws_sdk_ec2.types.create_verified_access_trust_provider_oidc_options
    import aws_sdk_ec2.types.device_trust_provider_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.trust_provider_type
    import aws_sdk_ec2.types.user_trust_provider_type
    import aws_sdk_ec2.types.verified_access_sse_specification_request


class CreateVerifiedAccessTrustProviderRequest(TypedDict):
    trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.trust_provider_type.TrustProviderType"
    ]
    """<p>The type of trust provider.</p>"""
    user_trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.user_trust_provider_type.UserTrustProviderType"
    ]
    """<p>The type of user-based trust provider. This parameter is required when the provider type is <code>user</code>.</p>"""
    device_trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.device_trust_provider_type.DeviceTrustProviderType"
    ]
    """<p>The type of device-based trust provider. This parameter is required when the provider type is <code>device</code>.</p>"""
    oidc_options: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_trust_provider_oidc_options.CreateVerifiedAccessTrustProviderOidcOptions"
    ]
    """<p>The options for a OpenID Connect-compatible user-identity trust provider. This parameter is required when the provider type is <code>user</code>.</p>"""
    device_options: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_trust_provider_device_options.CreateVerifiedAccessTrustProviderDeviceOptions"
    ]
    """<p>The options for a device-based trust provider. This parameter is required when the provider type is <code>device</code>.</p>"""
    policy_reference_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The identifier to be used when working with policy rules.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the Verified Access trust provider.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the Verified Access trust provider.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    sse_specification: NotRequired[
        "aws_sdk_ec2.types.verified_access_sse_specification_request.VerifiedAccessSseSpecificationRequest"
    ]
    """<p>The options for server side encryption.</p>"""
    native_application_oidc_options: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_native_application_oidc_options.CreateVerifiedAccessNativeApplicationOidcOptions"
    ]
    """<p>The OpenID Connect (OIDC) options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessTrustProviderRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "trust_provider_type" in value:
        import aws_sdk_ec2.types.trust_provider_type

        aws_sdk_ec2.types.trust_provider_type.serialize_ec2_query(
            value["trust_provider_type"], pairs, f"{prefix}.TrustProviderType"
        )
    if "user_trust_provider_type" in value:
        import aws_sdk_ec2.types.user_trust_provider_type

        aws_sdk_ec2.types.user_trust_provider_type.serialize_ec2_query(
            value["user_trust_provider_type"], pairs, f"{prefix}.UserTrustProviderType"
        )
    if "device_trust_provider_type" in value:
        import aws_sdk_ec2.types.device_trust_provider_type

        aws_sdk_ec2.types.device_trust_provider_type.serialize_ec2_query(
            value["device_trust_provider_type"],
            pairs,
            f"{prefix}.DeviceTrustProviderType",
        )
    if "oidc_options" in value:
        import aws_sdk_ec2.types.create_verified_access_trust_provider_oidc_options

        aws_sdk_ec2.types.create_verified_access_trust_provider_oidc_options.serialize_ec2_query(
            value["oidc_options"], pairs, f"{prefix}.OidcOptions"
        )
    if "device_options" in value:
        import aws_sdk_ec2.types.create_verified_access_trust_provider_device_options

        aws_sdk_ec2.types.create_verified_access_trust_provider_device_options.serialize_ec2_query(
            value["device_options"], pairs, f"{prefix}.DeviceOptions"
        )
    if "policy_reference_name" in value:
        pairs.append(
            (f"{prefix}.PolicyReferenceName", str(value["policy_reference_name"]))
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "sse_specification" in value:
        import aws_sdk_ec2.types.verified_access_sse_specification_request

        aws_sdk_ec2.types.verified_access_sse_specification_request.serialize_ec2_query(
            value["sse_specification"], pairs, f"{prefix}.SseSpecification"
        )
    if "native_application_oidc_options" in value:
        import aws_sdk_ec2.types.create_verified_access_native_application_oidc_options

        aws_sdk_ec2.types.create_verified_access_native_application_oidc_options.serialize_ec2_query(
            value["native_application_oidc_options"],
            pairs,
            f"{prefix}.NativeApplicationOidcOptions",
        )


def deserialize_ec2_query(el: Element) -> CreateVerifiedAccessTrustProviderRequest:
    out: CreateVerifiedAccessTrustProviderRequest = {}  # type: ignore[typeddict-item]
    child_trust_provider_type = el.find("TrustProviderType")
    if child_trust_provider_type is not None:
        import aws_sdk_ec2.types.trust_provider_type

        out["trust_provider_type"] = (
            aws_sdk_ec2.types.trust_provider_type.deserialize_ec2_query(
                child_trust_provider_type
            )
        )
    child_user_trust_provider_type = el.find("UserTrustProviderType")
    if child_user_trust_provider_type is not None:
        import aws_sdk_ec2.types.user_trust_provider_type

        out["user_trust_provider_type"] = (
            aws_sdk_ec2.types.user_trust_provider_type.deserialize_ec2_query(
                child_user_trust_provider_type
            )
        )
    child_device_trust_provider_type = el.find("DeviceTrustProviderType")
    if child_device_trust_provider_type is not None:
        import aws_sdk_ec2.types.device_trust_provider_type

        out["device_trust_provider_type"] = (
            aws_sdk_ec2.types.device_trust_provider_type.deserialize_ec2_query(
                child_device_trust_provider_type
            )
        )
    child_oidc_options = el.find("OidcOptions")
    if child_oidc_options is not None:
        import aws_sdk_ec2.types.create_verified_access_trust_provider_oidc_options

        out["oidc_options"] = (
            aws_sdk_ec2.types.create_verified_access_trust_provider_oidc_options.deserialize_ec2_query(
                child_oidc_options
            )
        )
    child_device_options = el.find("DeviceOptions")
    if child_device_options is not None:
        import aws_sdk_ec2.types.create_verified_access_trust_provider_device_options

        out["device_options"] = (
            aws_sdk_ec2.types.create_verified_access_trust_provider_device_options.deserialize_ec2_query(
                child_device_options
            )
        )
    child_policy_reference_name = el.find("PolicyReferenceName")
    if child_policy_reference_name is not None:
        out["policy_reference_name"] = str(child_policy_reference_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_sse_specification = el.find("SseSpecification")
    if child_sse_specification is not None:
        import aws_sdk_ec2.types.verified_access_sse_specification_request

        out["sse_specification"] = (
            aws_sdk_ec2.types.verified_access_sse_specification_request.deserialize_ec2_query(
                child_sse_specification
            )
        )
    child_native_application_oidc_options = el.find("NativeApplicationOidcOptions")
    if child_native_application_oidc_options is not None:
        import aws_sdk_ec2.types.create_verified_access_native_application_oidc_options

        out["native_application_oidc_options"] = (
            aws_sdk_ec2.types.create_verified_access_native_application_oidc_options.deserialize_ec2_query(
                child_native_application_oidc_options
            )
        )
    return out
