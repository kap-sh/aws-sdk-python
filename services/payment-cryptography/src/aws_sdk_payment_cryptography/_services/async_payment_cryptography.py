"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#PaymentCryptographyControlPlane``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_payment_cryptography._auth._signers
import aws_sdk_payment_cryptography._auth._sigv4
from aws_sdk_payment_cryptography._auth._identity import Credentials
from aws_sdk_payment_cryptography._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_payment_cryptography._auth._zapros_handler import AuthMiddleware
from aws_sdk_payment_cryptography._pagination import resolve_path as _resolve_path
from aws_sdk_payment_cryptography._resources.payment_cryptography_control_plane.alias_resource import (
    AsyncAliasResource,
)
from aws_sdk_payment_cryptography._resources.payment_cryptography_control_plane.key_resource import (
    AsyncKeyResource,
)
from aws_sdk_payment_cryptography._services._aws_config import aaws_config
from aws_sdk_payment_cryptography._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.associate_mpa_team_input
    import aws_sdk_payment_cryptography.types.associate_mpa_team_output
    import aws_sdk_payment_cryptography.types.certificate_subject_type
    import aws_sdk_payment_cryptography.types.delete_resource_policy_input
    import aws_sdk_payment_cryptography.types.delete_resource_policy_output
    import aws_sdk_payment_cryptography.types.disable_default_key_replication_regions_input
    import aws_sdk_payment_cryptography.types.disable_default_key_replication_regions_output
    import aws_sdk_payment_cryptography.types.disassociate_mpa_team_input
    import aws_sdk_payment_cryptography.types.disassociate_mpa_team_output
    import aws_sdk_payment_cryptography.types.enable_default_key_replication_regions_input
    import aws_sdk_payment_cryptography.types.enable_default_key_replication_regions_output
    import aws_sdk_payment_cryptography.types.export_attributes
    import aws_sdk_payment_cryptography.types.export_key_input
    import aws_sdk_payment_cryptography.types.export_key_material
    import aws_sdk_payment_cryptography.types.export_key_output
    import aws_sdk_payment_cryptography.types.get_certificate_signing_request_input
    import aws_sdk_payment_cryptography.types.get_certificate_signing_request_output
    import aws_sdk_payment_cryptography.types.get_default_key_replication_regions_input
    import aws_sdk_payment_cryptography.types.get_default_key_replication_regions_output
    import aws_sdk_payment_cryptography.types.get_mpa_team_association_input
    import aws_sdk_payment_cryptography.types.get_mpa_team_association_output
    import aws_sdk_payment_cryptography.types.get_parameters_for_export_input
    import aws_sdk_payment_cryptography.types.get_parameters_for_export_output
    import aws_sdk_payment_cryptography.types.get_parameters_for_import_input
    import aws_sdk_payment_cryptography.types.get_parameters_for_import_output
    import aws_sdk_payment_cryptography.types.get_public_key_certificate_input
    import aws_sdk_payment_cryptography.types.get_public_key_certificate_output
    import aws_sdk_payment_cryptography.types.get_resource_policy_input
    import aws_sdk_payment_cryptography.types.get_resource_policy_output
    import aws_sdk_payment_cryptography.types.import_key_input
    import aws_sdk_payment_cryptography.types.import_key_material
    import aws_sdk_payment_cryptography.types.import_key_output
    import aws_sdk_payment_cryptography.types.key_algorithm
    import aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography.types.key_check_value_algorithm
    import aws_sdk_payment_cryptography.types.key_material_type
    import aws_sdk_payment_cryptography.types.list_tags_for_resource_input
    import aws_sdk_payment_cryptography.types.list_tags_for_resource_output
    import aws_sdk_payment_cryptography.types.max_results
    import aws_sdk_payment_cryptography.types.mpa_operation
    import aws_sdk_payment_cryptography.types.mpa_requester_comment
    import aws_sdk_payment_cryptography.types.mpa_team_arn
    import aws_sdk_payment_cryptography.types.next_token
    import aws_sdk_payment_cryptography.types.put_resource_policy_input
    import aws_sdk_payment_cryptography.types.put_resource_policy_output
    import aws_sdk_payment_cryptography.types.regions
    import aws_sdk_payment_cryptography.types.resource_arn
    import aws_sdk_payment_cryptography.types.resource_policy
    import aws_sdk_payment_cryptography.types.signing_algorithm_type
    import aws_sdk_payment_cryptography.types.tag
    import aws_sdk_payment_cryptography.types.tag_keys
    import aws_sdk_payment_cryptography.types.tag_resource_input
    import aws_sdk_payment_cryptography.types.tag_resource_output
    import aws_sdk_payment_cryptography.types.tags
    import aws_sdk_payment_cryptography.types.untag_resource_input
    import aws_sdk_payment_cryptography.types.untag_resource_output


class AsyncPaymentCryptographyClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncPaymentCryptographyClient:
    """A client for the ``PaymentCryptography`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncPaymentCryptographyClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.alias_resource = AsyncAliasResource(self)
        self.key_resource = AsyncKeyResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPaymentCryptographyClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_mpa_team(
        self,
        action: "aws_sdk_payment_cryptography.types.mpa_operation.MpaOperation",
        mpa_team_arn: "aws_sdk_payment_cryptography.types.mpa_team_arn.MpaTeamArn",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        requester_comment: Optional[
            "aws_sdk_payment_cryptography.types.mpa_requester_comment.MpaRequesterComment"
        ] = None,
    ) -> "aws_sdk_payment_cryptography.types.associate_mpa_team_output.AssociateMpaTeamOutput":
        r"""<p>Associates a Multi-Party Approval (MPA) team with a protected operation. For more information, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/mpa.html\">Multi-Party Approval</a> in the <i>Amazon Web Services Payment Cryptography User Guide.</i> </p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DisassociateMpaTeam.html\">DisassociateMpaTeam</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetMpaTeamAssociation.html\">GetMpaTeamAssociation</a> </p> </li> </ul>

        Args:
            action: <p>The protected operation to associate with the MPA team. Currently, the only supported value is <code>IMPORT_ROOT_PUBLIC_KEY_CERTIFICATE</code>.</p>
            mpa_team_arn: <p>The ARN of the MPA team to associate with the protected operation.</p>
            requester_comment: <p>The comment from the requester explaining the reason for the association.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.associate_mpa_team_input.AssociateMpaTeamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.associate_mpa_team_output.AssociateMpaTeamOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.associate_mpa_team

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.associate_mpa_team.async_associate_mpa_team(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.associate_mpa_team_input.AssociateMpaTeamInput = {}  # type: ignore[typeddict-item]
        input_["action"] = action
        input_["mpa_team_arn"] = mpa_team_arn
        if requester_comment is not None:
            input_["requester_comment"] = requester_comment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_payment_cryptography.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "aws_sdk_payment_cryptography.types.delete_resource_policy_output.DeleteResourcePolicyOutput":
        r"""<p>Removes the resource-based policy attached to an Amazon Web Services Payment Cryptography key.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_PutResourcePolicy.html\">PutResourcePolicy</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetResourcePolicy.html\">GetResourcePolicy</a> </p> </li> </ul>

        Args:
            resource_arn: <p>The <code>KeyARN</code> of the key whose resource-based policy you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.delete_resource_policy_input.DeleteResourcePolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.delete_resource_policy_output.DeleteResourcePolicyOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.delete_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.delete_resource_policy_input.DeleteResourcePolicyInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_default_key_replication_regions(
        self,
        replication_regions: "aws_sdk_payment_cryptography.types.regions.Regions",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "aws_sdk_payment_cryptography.types.disable_default_key_replication_regions_output.DisableDefaultKeyReplicationRegionsOutput":
        r"""<p>Disables <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html\">Multi-Region key replication</a> settings for the specified Amazon Web Services Regions in your Amazon Web Services account, preventing new keys from being automatically replicated to those regions.</p> <p>After disabling Multi-Region key replication for specific regions, new keys created in your account will not be automatically replicated to those regions. You can still manually add replication to those regions for individual keys using the <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_AddKeyReplicationRegions.html\">AddKeyReplicationRegions</a> operation.</p> <p>This operation does not affect existing keys or their current replication configuration.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_EnableDefaultKeyReplicationRegions.html\">EnableDefaultKeyReplicationRegions</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetDefaultKeyReplicationRegions.html\">GetDefaultKeyReplicationRegions</a> </p> </li> </ul>

        Args:
            replication_regions: <p>The list of Amazon Web Services Regions to remove from the account's default replication regions.</p> <p>New keys created after this operation will not automatically be replicated to these regions, though existing keys with replication to these regions will be unaffected.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.disable_default_key_replication_regions_input.DisableDefaultKeyReplicationRegionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.disable_default_key_replication_regions_output.DisableDefaultKeyReplicationRegionsOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.disable_default_key_replication_regions

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.disable_default_key_replication_regions.async_disable_default_key_replication_regions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.disable_default_key_replication_regions_input.DisableDefaultKeyReplicationRegionsInput = {}  # type: ignore[typeddict-item]
        input_["replication_regions"] = replication_regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_mpa_team(
        self,
        action: "aws_sdk_payment_cryptography.types.mpa_operation.MpaOperation",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        requester_comment: Optional[
            "aws_sdk_payment_cryptography.types.mpa_requester_comment.MpaRequesterComment"
        ] = None,
    ) -> "aws_sdk_payment_cryptography.types.disassociate_mpa_team_output.DisassociateMpaTeamOutput":
        r"""<p>Removes the association between a Multi-Party Approval (MPA) team and a protected operation.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_AssociateMpaTeam.html\">AssociateMpaTeam</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetMpaTeamAssociation.html\">GetMpaTeamAssociation</a> </p> </li> </ul>

        Args:
            action: <p>The protected operation to disassociate from the MPA team. Currently, the only supported value is <code>IMPORT_ROOT_PUBLIC_KEY_CERTIFICATE</code>.</p>
            requester_comment: <p>The comment from the requester explaining the reason for the disassociation.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.disassociate_mpa_team_input.DisassociateMpaTeamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.disassociate_mpa_team_output.DisassociateMpaTeamOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.disassociate_mpa_team

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.disassociate_mpa_team.async_disassociate_mpa_team(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.disassociate_mpa_team_input.DisassociateMpaTeamInput = {}  # type: ignore[typeddict-item]
        input_["action"] = action
        if requester_comment is not None:
            input_["requester_comment"] = requester_comment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_default_key_replication_regions(
        self,
        replication_regions: "aws_sdk_payment_cryptography.types.regions.Regions",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "aws_sdk_payment_cryptography.types.enable_default_key_replication_regions_output.EnableDefaultKeyReplicationRegionsOutput":
        r"""<p>Enables <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html\">Multi-Region key replication</a> settings for your Amazon Web Services account, causing new keys to be automatically replicated to the specified Amazon Web Services Regions when created.</p> <p>When Multi-Region key replication are enabled, any new keys created in your account will automatically be replicated to these regions unless you explicitly override this behavior during key creation. This simplifies key management for applications that operate across multiple regions.</p> <p>Existing keys are not affected by this operation - only keys created after enabling default replication will be automatically replicated.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DisableDefaultKeyReplicationRegions.html\">DisableDefaultKeyReplicationRegions</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetDefaultKeyReplicationRegions.html\">GetDefaultKeyReplicationRegions</a> </p> </li> </ul>

        Args:
            replication_regions: <p>The list of Amazon Web Services Regions to enable as default replication regions for the Amazon Web Services account for <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html\">Multi-Region key replication</a>.</p> <p>New keys created in this account will automatically be replicated to these regions unless explicitly overridden during key creation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.enable_default_key_replication_regions_input.EnableDefaultKeyReplicationRegionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.enable_default_key_replication_regions_output.EnableDefaultKeyReplicationRegionsOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.enable_default_key_replication_regions

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.enable_default_key_replication_regions.async_enable_default_key_replication_regions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.enable_default_key_replication_regions_input.EnableDefaultKeyReplicationRegionsInput = {}  # type: ignore[typeddict-item]
        input_["replication_regions"] = replication_regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def export_key(
        self,
        key_material: "aws_sdk_payment_cryptography.types.export_key_material.ExportKeyMaterial",
        export_key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        export_attributes: Optional[
            "aws_sdk_payment_cryptography.types.export_attributes.ExportAttributes"
        ] = None,
    ) -> "aws_sdk_payment_cryptography.types.export_key_output.ExportKeyOutput":
        r"""<p>Exports a key from Amazon Web Services Payment Cryptography.</p> <p>Amazon Web Services Payment Cryptography simplifies key exchange by replacing the existing paper-based approach with a modern electronic approach. With <code>ExportKey</code> you can export symmetric keys using either symmetric and asymmetric key exchange mechanisms. Using this operation, you can share your Amazon Web Services Payment Cryptography generated keys with other service partners to perform cryptographic operations outside of Amazon Web Services Payment Cryptography </p> <p>For symmetric key exchange, Amazon Web Services Payment Cryptography uses the ANSI X9 TR-31 norm in accordance with PCI PIN guidelines. And for asymmetric key exchange, Amazon Web Services Payment Cryptography supports ANSI X9 TR-34 norm, RSA unwrap, and ECDH (Elliptic Curve Diffie-Hellman) key exchange mechanisms. Asymmetric key exchange methods are typically used to establish bi-directional trust between the two parties exhanging keys and are used for initial key exchange such as Key Encryption Key (KEK). After which you can export working keys using symmetric method to perform various cryptographic operations within Amazon Web Services Payment Cryptography.</p> <p>PCI requires specific minimum key strength of wrapping keys used to protect the keys being exchanged electronically. These requirements can change when PCI standards are revised. The rules specify that wrapping keys used for transport must be at least as strong as the key being protected. For more information on recommended key strength of wrapping keys and key exchange mechanism, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-importexport.html\">Importing and exporting keys</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>You can also use <code>ExportKey</code> functionality to generate and export an IPEK (Initial Pin Encryption Key) from Amazon Web Services Payment Cryptography using either TR-31 or TR-34 export key exchange. IPEK is generated from BDK (Base Derivation Key) and <code>ExportDukptInitialKey</code> attribute KSN (<code>KeySerialNumber</code>). The generated IPEK does not persist within Amazon Web Services Payment Cryptography and has to be re-generated each time during export.</p> <p>For key exchange using TR-31 or TR-34 key blocks, you can also export optional blocks within the key block header which contain additional attribute information about the key. The <code>KeyVersion</code> within <code>KeyBlockHeaders</code> indicates the version of the key within the key block. Furthermore, <code>KeyExportability</code> within <code>KeyBlockHeaders</code> can be used to further restrict exportability of the key after export from Amazon Web Services Payment Cryptography.</p> <p>The <code>OptionalBlocks</code> contain the additional data related to the key. For information on data type that can be included within optional blocks, refer to <a href=\"https://webstore.ansi.org/standards/ascx9/ansix91432022\">ASC X9.143-2022</a>.</p> <note> <p>Data included in key block headers is signed but transmitted in clear text. Sensitive or confidential information should not be included in optional blocks. Refer to ASC X9.143-2022 standard for information on allowed data type.</p> </note> <p> <b>To export initial keys (KEK) or IPEK using TR-34</b> </p> <p>Using this operation, you can export initial key using TR-34 asymmetric key exchange. You can only export KEK generated within Amazon Web Services Payment Cryptography. In TR-34 terminology, the sending party of the key is called Key Distribution Host (KDH) and the receiving party of the key is called Key Receiving Device (KRD). During key export process, KDH is Amazon Web Services Payment Cryptography which initiates key export and KRD is the user receiving the key.</p> <p>To initiate TR-34 key export, the KRD must obtain an export token by calling <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html\">GetParametersForExport</a>. This operation also generates a key pair for the purpose of key export, signs the key and returns back the signing public key certificate (also known as KDH signing certificate) and root certificate chain. The KDH uses the private key to sign the the export payload and the signing public key certificate is provided to KRD to verify the signature. The KRD can import the root certificate into its Hardware Security Module (HSM), as required. The export token and the associated KDH signing certificate expires after 30 days. </p> <p>Next the KRD generates a key pair for the the purpose of encrypting the KDH key and provides the public key cerificate (also known as KRD wrapping certificate) back to KDH. The KRD will also import the root cerificate chain into Amazon Web Services Payment Cryptography by calling <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html\">ImportKey</a> for <code>RootCertificatePublicKey</code>. The KDH, Amazon Web Services Payment Cryptography, will use the KRD wrapping cerificate to encrypt (wrap) the key under export and signs it with signing private key to generate a TR-34 WrappedKeyBlock. For more information on TR-34 key export, see section <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-export.html\">Exporting symmetric keys</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>. </p> <p>Set the following parameters:</p> <ul> <li> <p> <code>ExportAttributes</code>: Specify export attributes in case of IPEK export. This parameter is optional for KEK export.</p> </li> <li> <p> <code>ExportKeyIdentifier</code>: The <code>KeyARN</code> of the KEK or BDK (in case of IPEK) under export.</p> </li> <li> <p> <code>KeyMaterial</code>: Use <code>Tr34KeyBlock</code> parameters.</p> </li> <li> <p> <code>CertificateAuthorityPublicKeyIdentifier</code>: The <code>KeyARN</code> of the certificate chain that signed the KRD wrapping key certificate.</p> </li> <li> <p> <code>ExportToken</code>: Obtained from KDH by calling <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html\">GetParametersForImport</a>.</p> </li> <li> <p> <code>WrappingKeyCertificate</code>: The public key certificate in PEM format (base64 encoded) of the KRD wrapping key Amazon Web Services Payment Cryptography uses for encryption of the TR-34 export payload. This certificate must be signed by the root certificate (CertificateAuthorityPublicKeyIdentifier) imported into Amazon Web Services Payment Cryptography.</p> </li> </ul> <p>When this operation is successful, Amazon Web Services Payment Cryptography returns the KEK or IPEK as a TR-34 WrappedKeyBlock. </p> <p> <b>To export initial keys (KEK) or IPEK using RSA Wrap and Unwrap</b> </p> <p>Using this operation, you can export initial key using asymmetric RSA wrap and unwrap key exchange method. To initiate export, generate an asymmetric key pair on the receiving HSM and obtain the public key certificate in PEM format (base64 encoded) for the purpose of wrapping and the root certifiate chain. Import the root certificate into Amazon Web Services Payment Cryptography by calling <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html\">ImportKey</a> for <code>RootCertificatePublicKey</code>.</p> <p>Next call <code>ExportKey</code> and set the following parameters:</p> <ul> <li> <p> <code>CertificateAuthorityPublicKeyIdentifier</code>: The <code>KeyARN</code> of the certificate chain that signed wrapping key certificate.</p> </li> <li> <p> <code>KeyMaterial</code>: Set to <code>KeyCryptogram</code>.</p> </li> <li> <p> <code>WrappingKeyCertificate</code>: The public key certificate in PEM format (base64 encoded) obtained by the receiving HSM and signed by the root certificate (CertificateAuthorityPublicKeyIdentifier) imported into Amazon Web Services Payment Cryptography. The receiving HSM uses its private key component to unwrap the WrappedKeyCryptogram.</p> </li> </ul> <p>When this operation is successful, Amazon Web Services Payment Cryptography returns the WrappedKeyCryptogram. </p> <p> <b>To export working keys or IPEK using TR-31</b> </p> <p>Using this operation, you can export working keys or IPEK using TR-31 symmetric key exchange. In TR-31, you must use an initial key such as KEK to encrypt or wrap the key under export. To establish a KEK, you can use <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html\">CreateKey</a> or <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html\">ImportKey</a>. </p> <p>Set the following parameters:</p> <ul> <li> <p> <code>ExportAttributes</code>: Specify export attributes in case of IPEK export. This parameter is optional for KEK export.</p> </li> <li> <p> <code>ExportKeyIdentifier</code>: The <code>KeyARN</code> of the KEK or BDK (in case of IPEK) under export.</p> </li> <li> <p> <code>KeyMaterial</code>: Use <code>Tr31KeyBlock</code> parameters.</p> </li> </ul> <p> <b>To export working keys using ECDH</b> </p> <p>You can also use ECDH key agreement to export working keys in a TR-31 keyblock, where the wrapping key is an ECDH derived key.</p> <p>To initiate a TR-31 key export using ECDH, both sides must create an ECC key pair with key usage K3 and exchange public key certificates. In Amazon Web Services Payment Cryptography, you can do this by calling <code>CreateKey</code>. If you have not already done so, you must import the CA chain that issued the receiving public key certificate by calling <code>ImportKey</code> with input <code>RootCertificatePublicKey</code> for root CA or <code>TrustedPublicKey</code> for intermediate CA. You can then complete a TR-31 key export by deriving a shared wrapping key using the service ECC key pair, public certificate of your ECC key pair outside of Amazon Web Services Payment Cryptography, and the key derivation parameters including key derivation function, hash algorithm, derivation data, key algorithm.</p> <ul> <li> <p> <code>KeyMaterial</code>: Use <code>DiffieHellmanTr31KeyBlock</code> parameters.</p> </li> <li> <p> <code>PrivateKeyIdentifier</code>: The <code>KeyArn</code> of the ECC key pair created within Amazon Web Services Payment Cryptography to derive a shared KEK.</p> </li> <li> <p> <code>PublicKeyCertificate</code>: The public key certificate of the receiving ECC key pair in PEM format (base64 encoded) to derive a shared KEK.</p> </li> <li> <p> <code>CertificateAuthorityPublicKeyIdentifier</code>: The <code>keyARN</code> of the CA that signed the public key certificate of the receiving ECC key pair.</p> </li> </ul> <p>When this operation is successful, Amazon Web Services Payment Cryptography returns the working key as a TR-31 WrappedKeyBlock, where the wrapping key is the ECDH derived key.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html\">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html\">GetParametersForExport</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html\">ImportKey</a> </p> </li> </ul>

        Args:
            key_material: <p>The key block format type, for example, TR-34 or TR-31, to use during key material export.</p>
            export_key_identifier: <p>The <code>KeyARN</code> of the key under export from Amazon Web Services Payment Cryptography.</p>
            export_attributes: <p>The attributes for IPEK generation during export.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.export_key_input.ExportKeyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.export_key_output.ExportKeyOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.export_key

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.export_key.async_export_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.export_key_input.ExportKeyInput = {}  # type: ignore[typeddict-item]
        input_["key_material"] = key_material
        input_["export_key_identifier"] = export_key_identifier
        if export_attributes is not None:
            input_["export_attributes"] = export_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_certificate_signing_request(
        self,
        key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        signing_algorithm: "aws_sdk_payment_cryptography.types.signing_algorithm_type.SigningAlgorithmType",
        certificate_subject: "aws_sdk_payment_cryptography.types.certificate_subject_type.CertificateSubjectType",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "aws_sdk_payment_cryptography.types.get_certificate_signing_request_output.GetCertificateSigningRequestOutput":
        """<p>Creates a certificate signing request (CSR) from a key pair.</p>

        Args:
            key_identifier: <p>Asymmetric key used for generating the certificate signing request</p>
            signing_algorithm: <p>The cryptographic algorithm used to sign your CSR.</p>
            certificate_subject: <p>The metadata used to create the CSR.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.get_certificate_signing_request_input.GetCertificateSigningRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.get_certificate_signing_request_output.GetCertificateSigningRequestOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_certificate_signing_request

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_certificate_signing_request.async_get_certificate_signing_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.get_certificate_signing_request_input.GetCertificateSigningRequestInput = {}  # type: ignore[typeddict-item]
        input_["key_identifier"] = key_identifier
        input_["signing_algorithm"] = signing_algorithm
        input_["certificate_subject"] = certificate_subject

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_default_key_replication_regions(
        self, *, config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None
    ) -> "aws_sdk_payment_cryptography.types.get_default_key_replication_regions_output.GetDefaultKeyReplicationRegionsOutput":
        r"""<p>Retrieves the list of Amazon Web Services Regions where <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html\">Multi-Region key replication</a> is currently enabled for your Amazon Web Services account.</p> <p>This operation returns the current Multi-Region key replication configuration. New keys created in your account will be automatically replicated to these regions unless explicitly overridden during key creation.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_EnableDefaultKeyReplicationRegions.html\">EnableDefaultKeyReplicationRegions</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DisableDefaultKeyReplicationRegions.html\">DisableDefaultKeyReplicationRegions</a> </p> </li> </ul>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.get_default_key_replication_regions_input.GetDefaultKeyReplicationRegionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.get_default_key_replication_regions_output.GetDefaultKeyReplicationRegionsOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_default_key_replication_regions

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_default_key_replication_regions.async_get_default_key_replication_regions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.get_default_key_replication_regions_input.GetDefaultKeyReplicationRegionsInput = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_mpa_team_association(
        self,
        action: "aws_sdk_payment_cryptography.types.mpa_operation.MpaOperation",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "aws_sdk_payment_cryptography.types.get_mpa_team_association_output.GetMpaTeamAssociationOutput":
        r"""<p>Returns the Multi-Party Approval (MPA) team association for a protected operation.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_AssociateMpaTeam.html\">AssociateMpaTeam</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DisassociateMpaTeam.html\">DisassociateMpaTeam</a> </p> </li> </ul>

        Args:
            action: <p>The protected operation whose MPA team association you want to retrieve. Currently, the only supported value is <code>IMPORT_ROOT_PUBLIC_KEY_CERTIFICATE</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.get_mpa_team_association_input.GetMpaTeamAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.get_mpa_team_association_output.GetMpaTeamAssociationOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_mpa_team_association

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_mpa_team_association.async_get_mpa_team_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.get_mpa_team_association_input.GetMpaTeamAssociationInput = {}  # type: ignore[typeddict-item]
        input_["action"] = action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_parameters_for_export(
        self,
        key_material_type: "aws_sdk_payment_cryptography.types.key_material_type.KeyMaterialType",
        signing_key_algorithm: "aws_sdk_payment_cryptography.types.key_algorithm.KeyAlgorithm",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        reuse_last_generated_token: Optional[bool] = None,
    ) -> "aws_sdk_payment_cryptography.types.get_parameters_for_export_output.GetParametersForExportOutput":
        r"""<p>Gets the export token and the signing key certificate to initiate a TR-34 key export from Amazon Web Services Payment Cryptography.</p> <p>The signing key certificate signs the wrapped key under export within the TR-34 key payload. The export token and signing key certificate must be in place and operational before calling <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKey.html\">ExportKey</a>. The export token expires in 30 days. You can use the same export token to export multiple keys from your service account.</p> <p>To return a previously generated export token and signing key certificate instead of generating new ones, set <code>ReuseLastGeneratedToken</code> to <code>true</code>.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKey.html\">ExportKey</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html\">GetParametersForImport</a> </p> </li> </ul>

        Args:
            key_material_type: <p>The key block format type (for example, TR-34 or TR-31) to use during key material export. Export token is only required for a TR-34 key export, <code>TR34_KEY_BLOCK</code>. Export token is not required for TR-31 key export.</p>
            signing_key_algorithm: <p>The signing key algorithm to generate a signing key certificate. This certificate signs the wrapped key under export within the TR-34 key block. <code>RSA_2048</code> is the only signing key algorithm allowed.</p>
            reuse_last_generated_token: <p>Specifies whether to reuse the existing export token and signing key certificate. If set to <code>true</code> and a valid export token exists for the same key material type and signing key algorithm with at least 7 days of remaining validity, the existing token and signing key certificate are returned. Otherwise, a new export token and signing key certificate are generated. The default value is <code>false</code>, which generates a new export token and signing key certificate on every call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.get_parameters_for_export_input.GetParametersForExportInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.get_parameters_for_export_output.GetParametersForExportOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_parameters_for_export

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_parameters_for_export.async_get_parameters_for_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.get_parameters_for_export_input.GetParametersForExportInput = {}  # type: ignore[typeddict-item]
        input_["key_material_type"] = key_material_type
        input_["signing_key_algorithm"] = signing_key_algorithm
        if reuse_last_generated_token is not None:
            input_["reuse_last_generated_token"] = reuse_last_generated_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_parameters_for_import(
        self,
        key_material_type: "aws_sdk_payment_cryptography.types.key_material_type.KeyMaterialType",
        wrapping_key_algorithm: "aws_sdk_payment_cryptography.types.key_algorithm.KeyAlgorithm",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        reuse_last_generated_token: Optional[bool] = None,
    ) -> "aws_sdk_payment_cryptography.types.get_parameters_for_import_output.GetParametersForImportOutput":
        r"""<p>Gets the import token and the wrapping key certificate in PEM format (base64 encoded) to initiate a TR-34 WrappedKeyBlock or a RSA WrappedKeyCryptogram import into Amazon Web Services Payment Cryptography.</p> <p>The wrapping key certificate wraps the key under import. The import token and wrapping key certificate must be in place and operational before calling <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html\">ImportKey</a>. The import token expires in 30 days. You can use the same import token to import multiple keys into your service account.</p> <p>To return a previously generated import token and wrapping key certificate instead of generating new ones, set <code>ReuseLastGeneratedToken</code> to <code>true</code>.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html\">GetParametersForExport</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html\">ImportKey</a> </p> </li> </ul>

        Args:
            key_material_type: <p>The method to use for key material import. Import token is only required for TR-34 WrappedKeyBlock (<code>TR34_KEY_BLOCK</code>) and RSA WrappedKeyCryptogram (<code>KEY_CRYPTOGRAM</code>).</p> <p>Import token is not required for TR-31, root public key cerificate or trusted public key certificate.</p>
            wrapping_key_algorithm: <p>The wrapping key algorithm to generate a wrapping key certificate. This certificate wraps the key under import.</p> <p>At this time, <code>RSA_2048</code> is the allowed algorithm for TR-34 WrappedKeyBlock import. Additionally, <code>RSA_2048</code>, <code>RSA_3072</code>, <code>RSA_4096</code> are the allowed algorithms for RSA WrappedKeyCryptogram import.</p>
            reuse_last_generated_token: <p>Specifies whether to reuse the existing import token and wrapping key certificate. If set to <code>true</code> and a valid import token exists for the same key material type and wrapping key algorithm with at least 7 days of remaining validity, the existing token and wrapping key certificate are returned. Otherwise, a new import token and wrapping key certificate are generated. The default value is <code>false</code>, which generates a new import token and wrapping key certificate on every call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.get_parameters_for_import_input.GetParametersForImportInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.get_parameters_for_import_output.GetParametersForImportOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_parameters_for_import

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_parameters_for_import.async_get_parameters_for_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.get_parameters_for_import_input.GetParametersForImportInput = {}  # type: ignore[typeddict-item]
        input_["key_material_type"] = key_material_type
        input_["wrapping_key_algorithm"] = wrapping_key_algorithm
        if reuse_last_generated_token is not None:
            input_["reuse_last_generated_token"] = reuse_last_generated_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_public_key_certificate(
        self,
        key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "aws_sdk_payment_cryptography.types.get_public_key_certificate_output.GetPublicKeyCertificateOutput":
        r"""<p>Gets the public key certificate of the asymmetric key pair that exists within Amazon Web Services Payment Cryptography.</p> <p>Unlike the private key of an asymmetric key, which never leaves Amazon Web Services Payment Cryptography unencrypted, callers with <code>GetPublicKeyCertificate</code> permission can download the public key certificate of the asymmetric key. You can share the public key certificate to allow others to encrypt messages and verify signatures outside of Amazon Web Services Payment Cryptography</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html\">Resource-based policies</a>.</p>

        Args:
            key_identifier: <p>The <code>KeyARN</code> of the asymmetric key pair.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.get_public_key_certificate_input.GetPublicKeyCertificateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.get_public_key_certificate_output.GetPublicKeyCertificateOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_public_key_certificate

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_public_key_certificate.async_get_public_key_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.get_public_key_certificate_input.GetPublicKeyCertificateInput = {}  # type: ignore[typeddict-item]
        input_["key_identifier"] = key_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "aws_sdk_payment_cryptography.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "aws_sdk_payment_cryptography.types.get_resource_policy_output.GetResourcePolicyOutput":
        r"""<p>Returns the resource-based policy attached to an Amazon Web Services Payment Cryptography key.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_PutResourcePolicy.html\">PutResourcePolicy</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteResourcePolicy.html\">DeleteResourcePolicy</a> </p> </li> </ul>

        Args:
            resource_arn: <p>The <code>KeyARN</code> of the key whose resource-based policy you want to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.get_resource_policy_input.GetResourcePolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.get_resource_policy_output.GetResourcePolicyOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.get_resource_policy_input.GetResourcePolicyInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_key(
        self,
        key_material: "aws_sdk_payment_cryptography.types.import_key_material.ImportKeyMaterial",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        key_check_value_algorithm: Optional[
            "aws_sdk_payment_cryptography.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
        ] = None,
        enabled: Optional[bool] = None,
        tags: Optional["aws_sdk_payment_cryptography.types.tags.Tags"] = None,
        replication_regions: Optional[
            "aws_sdk_payment_cryptography.types.regions.Regions"
        ] = None,
        requester_comment: Optional[
            "aws_sdk_payment_cryptography.types.mpa_requester_comment.MpaRequesterComment"
        ] = None,
    ) -> "aws_sdk_payment_cryptography.types.import_key_output.ImportKeyOutput":
        r"""<p>Imports symmetric keys and public key certificates in PEM format (base64 encoded) into Amazon Web Services Payment Cryptography.</p> <p>Amazon Web Services Payment Cryptography simplifies key exchange by replacing the existing paper-based approach with a modern electronic approach. With <code>ImportKey</code> you can import symmetric keys using either symmetric and asymmetric key exchange mechanisms.</p> <p>For symmetric key exchange, Amazon Web Services Payment Cryptography uses the ANSI X9 TR-31 norm in accordance with PCI PIN guidelines. And for asymmetric key exchange, Amazon Web Services Payment Cryptography supports ANSI X9 TR-34 norm, RSA unwrap, and ECDH (Elliptic Curve Diffie-Hellman) key exchange mechanisms. Asymmetric key exchange methods are typically used to establish bi-directional trust between the two parties exhanging keys and are used for initial key exchange such as Key Encryption Key (KEK) or Zone Master Key (ZMK). After which you can import working keys using symmetric method to perform various cryptographic operations within Amazon Web Services Payment Cryptography.</p> <p>PCI requires specific minimum key strength of wrapping keys used to protect the keys being exchanged electronically. These requirements can change when PCI standards are revised. The rules specify that wrapping keys used for transport must be at least as strong as the key being protected. For more information on recommended key strength of wrapping keys and key exchange mechanism, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-importexport.html\">Importing and exporting keys</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>You can also import a <i>root public key certificate</i>, used to sign other public key certificates, or a <i>trusted public key certificate</i> under an already established root public key certificate.</p> <p> <b>To import a public root key certificate</b> </p> <p>Using this operation, you can import the public component (in PEM cerificate format) of your private root key. You can use the imported public root key certificate for digital signatures, for example signing wrapping key or signing key in TR-34, within your Amazon Web Services Payment Cryptography account.</p> <p>Set the following parameters:</p> <ul> <li> <p> <code>KeyMaterial</code>: <code>RootCertificatePublicKey</code> </p> </li> <li> <p> <code>KeyClass</code>: <code>PUBLIC_KEY</code> </p> </li> <li> <p> <code>KeyModesOfUse</code>: <code>Verify</code> </p> </li> <li> <p> <code>KeyUsage</code>: <code>TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE</code> </p> </li> <li> <p> <code>PublicKeyCertificate</code>: The public key certificate in PEM format (base64 encoded) of the private root key under import.</p> </li> </ul> <p> <b>To import a trusted public key certificate</b> </p> <p>The root public key certificate must be in place and operational before you import a trusted public key certificate. Set the following parameters:</p> <ul> <li> <p> <code>KeyMaterial</code>: <code>TrustedCertificatePublicKey</code> </p> </li> <li> <p> <code>CertificateAuthorityPublicKeyIdentifier</code>: <code>KeyArn</code> of the <code>RootCertificatePublicKey</code>.</p> </li> <li> <p> <code>KeyModesOfUse</code> and <code>KeyUsage</code>: Corresponding to the cryptographic operations such as wrap, sign, or encrypt that you will allow the trusted public key certificate to perform.</p> </li> <li> <p> <code>PublicKeyCertificate</code>: The trusted public key certificate in PEM format (base64 encoded) under import.</p> </li> </ul> <p> <b>To import initial keys (KEK or ZMK or similar) using TR-34</b> </p> <p>Using this operation, you can import initial key using TR-34 asymmetric key exchange. In TR-34 terminology, the sending party of the key is called Key Distribution Host (KDH) and the receiving party of the key is called Key Receiving Device (KRD). During the key import process, KDH is the user who initiates the key import and KRD is Amazon Web Services Payment Cryptography who receives the key.</p> <p>To initiate TR-34 key import, the KDH must obtain an import token by calling <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html\">GetParametersForImport</a>. This operation generates an encryption keypair for the purpose of key import, signs the key and returns back the wrapping key certificate (also known as KRD wrapping certificate) and the root certificate chain. The KDH must trust and install the KRD wrapping certificate on its HSM and use it to encrypt (wrap) the KDH key during TR-34 WrappedKeyBlock generation. The import token and associated KRD wrapping certificate expires after 30 days.</p> <p>Next the KDH generates a key pair for the purpose of signing the encrypted KDH key and provides the public certificate of the signing key to Amazon Web Services Payment Cryptography. The KDH will also need to import the root certificate chain of the KDH signing certificate by calling <code>ImportKey</code> for <code>RootCertificatePublicKey</code>. For more information on TR-34 key import, see section <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-import.html\">Importing symmetric keys</a> in the <i>Amazon Web Services Payment Cryptography User Guide</i>.</p> <p>Set the following parameters:</p> <ul> <li> <p> <code>KeyMaterial</code>: Use <code>Tr34KeyBlock</code> parameters.</p> </li> <li> <p> <code>CertificateAuthorityPublicKeyIdentifier</code>: The <code>KeyARN</code> of the certificate chain that signed the KDH signing key certificate.</p> </li> <li> <p> <code>ImportToken</code>: Obtained from KRD by calling <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html\">GetParametersForImport</a>.</p> </li> <li> <p> <code>WrappedKeyBlock</code>: The TR-34 wrapped key material from KDH. It contains the KDH key under import, wrapped with KRD wrapping certificate and signed by KDH signing private key. This TR-34 key block is typically generated by the KDH Hardware Security Module (HSM) outside of Amazon Web Services Payment Cryptography.</p> </li> <li> <p> <code>SigningKeyCertificate</code>: The public key certificate in PEM format (base64 encoded) of the KDH signing key generated under the root certificate (CertificateAuthorityPublicKeyIdentifier) imported in Amazon Web Services Payment Cryptography.</p> </li> </ul> <p> <b>To import initial keys (KEK or ZMK or similar) using RSA Wrap and Unwrap</b> </p> <p>Using this operation, you can import initial key using asymmetric RSA wrap and unwrap key exchange method. To initiate import, call <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html\">GetParametersForImport</a> with <code>KeyMaterial</code> set to <code>KEY_CRYPTOGRAM</code> to generate an import token. This operation also generates an encryption keypair for the purpose of key import, signs the key and returns back the wrapping key certificate in PEM format (base64 encoded) and its root certificate chain. The import token and associated KRD wrapping certificate expires after 30 days. </p> <p>You must trust and install the wrapping certificate and its certificate chain on the sending HSM and use it to wrap the key under export for WrappedKeyCryptogram generation. Next call <code>ImportKey</code> with <code>KeyMaterial</code> set to <code>KEY_CRYPTOGRAM</code> and provide the <code>ImportToken</code> and <code>KeyAttributes</code> for the key under import.</p> <p> <b>To import working keys using TR-31</b> </p> <p>Amazon Web Services Payment Cryptography uses TR-31 symmetric key exchange norm to import working keys. A KEK must be established within Amazon Web Services Payment Cryptography by using TR-34 key import or by using <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html\">CreateKey</a>. To initiate a TR-31 key import, set the following parameters:</p> <ul> <li> <p> <code>KeyMaterial</code>: Use <code>Tr31KeyBlock</code> parameters.</p> </li> <li> <p> <code>WrappedKeyBlock</code>: The TR-31 wrapped key material. It contains the key under import, encrypted using KEK. The TR-31 key block is typically generated by a HSM outside of Amazon Web Services Payment Cryptography. </p> </li> <li> <p> <code>WrappingKeyIdentifier</code>: The <code>KeyArn</code> of the KEK that Amazon Web Services Payment Cryptography uses to decrypt or unwrap the key under import.</p> </li> </ul> <p> <b>To import working keys using ECDH</b> </p> <p>You can also use ECDH key agreement to import working keys as a TR-31 keyblock, where the wrapping key is an ECDH derived key.</p> <p>To initiate a TR-31 key import using ECDH, both sides must create an ECC key pair with key usage K3 and exchange public key certificates. In Amazon Web Services Payment Cryptography, you can do this by calling <code>CreateKey</code> and then <code>GetPublicKeyCertificate</code> to retrieve its public key certificate. Next, you can then generate a TR-31 WrappedKeyBlock using your own ECC key pair, the public certificate of the service's ECC key pair, and the key derivation parameters including key derivation function, hash algorithm, derivation data, and key algorithm. If you have not already done so, you must import the CA chain that issued the receiving public key certificate by calling <code>ImportKey</code> with input <code>RootCertificatePublicKey</code> for root CA or <code>TrustedPublicKey</code> for intermediate CA. To complete the TR-31 key import, you can use the following parameters. It is important that the ECDH key derivation parameters you use should match those used during import to derive the same shared wrapping key within Amazon Web Services Payment Cryptography.</p> <ul> <li> <p> <code>KeyMaterial</code>: Use <code>DiffieHellmanTr31KeyBlock</code> parameters.</p> </li> <li> <p> <code>PrivateKeyIdentifier</code>: The <code>KeyArn</code> of the ECC key pair created within Amazon Web Services Payment Cryptography to derive a shared KEK.</p> </li> <li> <p> <code>PublicKeyCertificate</code>: The public key certificate of the receiving ECC key pair in PEM format (base64 encoded) to derive a shared KEK.</p> </li> <li> <p> <code>CertificateAuthorityPublicKeyIdentifier</code>: The <code>keyARN</code> of the CA that signed the public key certificate of the receiving ECC key pair.</p> </li> </ul> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html\">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKey.html\">ExportKey</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html\">GetParametersForImport</a> </p> </li> </ul>

        Args:
            key_material: <p>The key or public key certificate type to use during key material import, for example TR-34 or RootCertificatePublicKey.</p>
            key_check_value_algorithm: <p>The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.</p> <p>For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.</p>
            enabled: <p>Specifies whether import key is enabled.</p>
            tags: <p>Assigns one or more tags to the Amazon Web Services Payment Cryptography key. Use this parameter to tag a key when it is imported. To tag an existing Amazon Web Services Payment Cryptography key, use the <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html\">TagResource</a> operation.</p> <p>Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You can't have more than one tag on an Amazon Web Services Payment Cryptography key with the same tag key. If you specify an existing tag key with a different tag value, Amazon Web Services Payment Cryptography replaces the current tag value with the specified one.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <note> <p>Tagging or untagging an Amazon Web Services Payment Cryptography key can allow or deny permission to the key.</p> </note>
            requester_comment: <p>The comment from the requester explaining the reason for the import.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.import_key_input.ImportKeyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.import_key_output.ImportKeyOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.import_key

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.import_key.async_import_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.import_key_input.ImportKeyInput = {}  # type: ignore[typeddict-item]
        input_["key_material"] = key_material
        if key_check_value_algorithm is not None:
            input_["key_check_value_algorithm"] = key_check_value_algorithm
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags
        if replication_regions is not None:
            input_["replication_regions"] = replication_regions
        if requester_comment is not None:
            input_["requester_comment"] = requester_comment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_payment_cryptography.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        next_token: Optional[
            "aws_sdk_payment_cryptography.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_payment_cryptography.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_payment_cryptography.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        r"""<p>Lists the tags for an Amazon Web Services resource.</p> <p>This is a paginated operation, which means that each response might contain only a subset of all the tags. When the response contains only a subset of tags, it includes a <code>NextToken</code> value. Use this value in a subsequent <code>ListTagsForResource</code> request to get more tags. When you receive a response with no NextToken (or an empty or null value), that means there are no more tags to get.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html\">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html\">TagResource</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UntagResource.html\">UntagResource</a> </p> </li> </ul>

        Args:
            resource_arn: <p>The <code>KeyARN</code> of the key whose tags you are getting.</p>
            next_token: <p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the truncated response you just received.</p>
            max_results: <p>Use this parameter to specify the maximum number of items to return. When this value is present, Amazon Web Services Payment Cryptography does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_payment_cryptography.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
        next_token: Optional[
            "aws_sdk_payment_cryptography.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_payment_cryptography.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_payment_cryptography.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_resource_policy(
        self,
        resource_arn: "aws_sdk_payment_cryptography.types.resource_arn.ResourceArn",
        policy: "aws_sdk_payment_cryptography.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "aws_sdk_payment_cryptography.types.put_resource_policy_output.PutResourcePolicyOutput":
        r"""<p>Attaches or replaces a resource-based policy on an Amazon Web Services Payment Cryptography key. A resource-based policy can grant cross-account access to your key.</p> <p>If the policy would grant public access, the request fails with a <code>PublicPolicyException</code>.</p> <p>To remove a resource-based policy from a key, use <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteResourcePolicy.html\">DeleteResourcePolicy</a>.</p> <p> <b>Cross-account use:</b> This operation can't be used across different Amazon Web Services accounts.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetResourcePolicy.html\">GetResourcePolicy</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteResourcePolicy.html\">DeleteResourcePolicy</a> </p> </li> </ul>

        Args:
            resource_arn: <p>The <code>KeyARN</code> of the key to attach the resource-based policy to.</p>
            policy: <p>The resource-based policy to attach to the key, in JSON format.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.put_resource_policy_input.PutResourcePolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.put_resource_policy_output.PutResourcePolicyOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.put_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.put_resource_policy_input.PutResourcePolicyInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_payment_cryptography.types.resource_arn.ResourceArn",
        tags: "aws_sdk_payment_cryptography.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "aws_sdk_payment_cryptography.types.tag_resource_output.TagResourceOutput":
        r"""<p>Adds or edits tags on an Amazon Web Services Payment Cryptography key.</p> <note> <p>Tagging or untagging an Amazon Web Services Payment Cryptography key can allow or deny permission to the key.</p> </note> <p>Each tag consists of a tag key and a tag value, both of which are case-sensitive strings. The tag value can be an empty (null) string. To add a tag, specify a new tag key and a tag value. To edit a tag, specify an existing tag key and a new tag value. You can also add tags to an Amazon Web Services Payment Cryptography key when you create it with <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html\">CreateKey</a>.</p> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html\">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListTagsForResource.html\">ListTagsForResource</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UntagResource.html\">UntagResource</a> </p> </li> </ul>

        Args:
            resource_arn: <p>The <code>KeyARN</code> of the key whose tags are being updated.</p>
            tags: <p>One or more tags. Each tag consists of a tag key and a tag value. The tag value can be an empty (null) string. You can't have more than one tag on an Amazon Web Services Payment Cryptography key with the same tag key. If you specify an existing tag key with a different tag value, Amazon Web Services Payment Cryptography replaces the current tag value with the new one.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <p>To use this parameter, you must have <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html\">TagResource</a> permission in an IAM policy.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_payment_cryptography.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_payment_cryptography.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncPaymentCryptographyClientConfig] = None,
    ) -> "aws_sdk_payment_cryptography.types.untag_resource_output.UntagResourceOutput":
        r"""<p>Deletes a tag from an Amazon Web Services Payment Cryptography key.</p> <note> <p>Tagging or untagging an Amazon Web Services Payment Cryptography key can allow or deny permission to the key.</p> </note> <p> <b>Cross-account use:</b> This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html\">Resource-based policies</a>.</p> <p> <b>Related operations:</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListTagsForResource.html\">ListTagsForResource</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html\">TagResource</a> </p> </li> </ul>

        Args:
            resource_arn: <p>The <code>KeyARN</code> of the key whose tags are being removed.</p>
            tag_keys: <p>One or more tag keys. Don't include the tag values.</p> <p>If the Amazon Web Services Payment Cryptography key doesn't have the specified tag key, Amazon Web Services Payment Cryptography doesn't throw an exception or return a response. To confirm that the operation succeeded, use the <a href=\"https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListTagsForResource.html\">ListTagsForResource</a> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_payment_cryptography.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_payment_cryptography.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_payment_cryptography._operations.payment_cryptography_control_plane.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_payment_cryptography.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
