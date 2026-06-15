"""Generated from Smithy shape ``com.amazonaws.acm#CertificateManager``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_acm._auth._signers
import aws_sdk_acm._auth._sigv4
from aws_sdk_acm._auth._identity import Credentials
from aws_sdk_acm._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_acm._auth._zapros_handler import AuthMiddleware
from aws_sdk_acm._pagination import resolve_path as _resolve_path
from aws_sdk_acm._services._aws_config import aws_config
from aws_sdk_acm._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_acm.types.add_tags_to_certificate_request
    import aws_sdk_acm.types.arn
    import aws_sdk_acm.types.certificate_body_blob
    import aws_sdk_acm.types.certificate_chain_blob
    import aws_sdk_acm.types.certificate_filter_statement
    import aws_sdk_acm.types.certificate_managed_by
    import aws_sdk_acm.types.certificate_options
    import aws_sdk_acm.types.certificate_search_result
    import aws_sdk_acm.types.certificate_statuses
    import aws_sdk_acm.types.certificate_summary
    import aws_sdk_acm.types.delete_certificate_request
    import aws_sdk_acm.types.describe_certificate_request
    import aws_sdk_acm.types.describe_certificate_response
    import aws_sdk_acm.types.domain_list
    import aws_sdk_acm.types.domain_name_string
    import aws_sdk_acm.types.domain_validation_option_list
    import aws_sdk_acm.types.expiry_events_configuration
    import aws_sdk_acm.types.export_certificate_request
    import aws_sdk_acm.types.export_certificate_response
    import aws_sdk_acm.types.filters
    import aws_sdk_acm.types.get_account_configuration_response
    import aws_sdk_acm.types.get_certificate_request
    import aws_sdk_acm.types.get_certificate_response
    import aws_sdk_acm.types.idempotency_token
    import aws_sdk_acm.types.import_certificate_request
    import aws_sdk_acm.types.import_certificate_response
    import aws_sdk_acm.types.key_algorithm
    import aws_sdk_acm.types.list_certificates_request
    import aws_sdk_acm.types.list_certificates_response
    import aws_sdk_acm.types.list_tags_for_certificate_request
    import aws_sdk_acm.types.list_tags_for_certificate_response
    import aws_sdk_acm.types.max_items
    import aws_sdk_acm.types.next_token
    import aws_sdk_acm.types.passphrase_blob
    import aws_sdk_acm.types.pca_arn
    import aws_sdk_acm.types.private_key_blob
    import aws_sdk_acm.types.put_account_configuration_request
    import aws_sdk_acm.types.remove_tags_from_certificate_request
    import aws_sdk_acm.types.renew_certificate_request
    import aws_sdk_acm.types.request_certificate_request
    import aws_sdk_acm.types.request_certificate_response
    import aws_sdk_acm.types.resend_validation_email_request
    import aws_sdk_acm.types.revocation_reason
    import aws_sdk_acm.types.revoke_certificate_request
    import aws_sdk_acm.types.revoke_certificate_response
    import aws_sdk_acm.types.search_certificates_request
    import aws_sdk_acm.types.search_certificates_response
    import aws_sdk_acm.types.search_certificates_sort_by
    import aws_sdk_acm.types.search_certificates_sort_order
    import aws_sdk_acm.types.search_max_results
    import aws_sdk_acm.types.sort_by
    import aws_sdk_acm.types.sort_order
    import aws_sdk_acm.types.tag_list
    import aws_sdk_acm.types.update_certificate_options_request
    import aws_sdk_acm.types.validation_method


class ACMClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class ACMClient:
    """A client for the ``ACM`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = ACMClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[ACMClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ACMClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def add_tags_to_certificate(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        tags: "aws_sdk_acm.types.tag_list.TagList",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> None:
        r"""<p>Adds one or more tags to an ACM certificate. Tags are labels that you can use to identify and organize your Amazon Web Services resources. Each tag consists of a <code>key</code> and an optional <code>value</code>. You specify the certificate on input by its Amazon Resource Name (ARN). You specify the tag by using a key-value pair. </p> <p>You can apply a tag to just one certificate if you want to identify a specific characteristic of that certificate, or you can apply the same tag to multiple certificates if you want to filter for a common relationship among those certificates. Similarly, you can apply the same tag to multiple resources if you want to specify a relationship among those resources. For example, you can add the same tag to an ACM certificate and an Elastic Load Balancing load balancer to indicate that they are both used by the same website. For more information, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/tags.html\">Tagging ACM certificates</a>. </p> <p>To remove one or more tags, use the <a>RemoveTagsFromCertificate</a> action. To view all of the tags that have been applied to the certificate, use the <a>ListTagsForCertificate</a> action. </p>

        Args:
            certificate_arn: <p>String that contains the ARN of the ACM certificate to which the tag is to be applied. This must be of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a>.</p>
            tags: <p>The key-value pair that defines the tag. The tag value is optional.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.add_tags_to_certificate_request.AddTagsToCertificateRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_acm._operations.certificate_manager.add_tags_to_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.add_tags_to_certificate.add_tags_to_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.add_tags_to_certificate_request.AddTagsToCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_certificate(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> None:
        r"""<p>Deletes a certificate and its associated private key. If this action succeeds, the certificate is not available for use by Amazon Web Services services integrated with ACM. Deleting a certificate is eventually consistent. The may be a short delay before the certificate no longer appears in the list that can be displayed by calling the <a>ListCertificates</a> action or be retrieved by calling the <a>GetCertificate</a> action.</p> <note> <p>You cannot delete an ACM certificate that is being used by another Amazon Web Services service. To delete a certificate that is in use, you must first remove the certificate association using the console or the CLI for the associated service.</p> <p>Deleting a certificate issued by a private certificate authority (CA) has no effect on the CA. You will continue to be charged for the CA until it is deleted. For more information, see <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/PCADeleteCA.html\"> Deleting Your Private CA</a> in the <i>Private Certificate Authority User Guide</i>.</p> </note> <p>Deleting a certificate issued by a private certificate authority (CA) has no effect on the CA. You will continue to be charged for the CA until it is deleted. For more information, see <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/PCADeleteCA.html\">Deleting your private CA</a> in the <i>Amazon Web Services Private Certificate Authority User Guide</i>.</p>

        Args:
            certificate_arn: <p>String that contains the ARN of the ACM certificate to be deleted. This must be of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.delete_certificate_request.DeleteCertificateRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_acm._operations.certificate_manager.delete_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.delete_certificate.delete_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.delete_certificate_request.DeleteCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_certificate(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> "aws_sdk_acm.types.describe_certificate_response.DescribeCertificateResponse":
        r"""<p>Returns detailed metadata about the specified ACM certificate.</p> <p>If you have just created a certificate using the <code>RequestCertificate</code> action, there is a delay of several seconds before you can retrieve information about it.</p>

        Args:
            certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate. The ARN must have the following form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.describe_certificate_request.DescribeCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_acm.types.describe_certificate_response.DescribeCertificateResponse"
        ]:
            import aws_sdk_acm._operations.certificate_manager.describe_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.describe_certificate.describe_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.describe_certificate_request.DescribeCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def export_certificate(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        passphrase: "aws_sdk_acm.types.passphrase_blob.PassphraseBlob",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> "aws_sdk_acm.types.export_certificate_response.ExportCertificateResponse":
        r"""<p>Exports a private certificate issued by a private certificate authority (CA) or a public certificate for use anywhere. The exported file contains the certificate, the certificate chain, and the encrypted private key associated with the public key that is embedded in the certificate. For security, you must assign a passphrase for the private key when exporting it. </p> <p>For information about exporting and formatting a certificate using the ACM console or CLI, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/export-private.html\">Export a private certificate</a> and <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/export-public-certificate\">Export a public certificate</a>.</p> <note> <p>ACM public certificates created prior to June 17, 2025 cannot be exported.</p> </note>

        Args:
            certificate_arn: <p>An Amazon Resource Name (ARN) of the issued certificate. This must be of the form:</p> <p> <code>arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012</code> </p>
            passphrase: <p>Passphrase to associate with the encrypted exported private key. </p> <note> <p>When creating your passphrase, you can use any ASCII character except #, $, or %.</p> </note> <p>If you want to later decrypt the private key, you must have the passphrase. You can use the following OpenSSL command to decrypt a private key. After entering the command, you are prompted for the passphrase.</p> <p> <code>openssl rsa -in encrypted_key.pem -out decrypted_key.pem</code> </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.export_certificate_request.ExportCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_acm.types.export_certificate_response.ExportCertificateResponse"
        ]:
            import aws_sdk_acm._operations.certificate_manager.export_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.export_certificate.export_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.export_certificate_request.ExportCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn
        input_["passphrase"] = passphrase

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_account_configuration(
        self, *, config_overrides: Optional[ACMClientConfig] = None
    ) -> "aws_sdk_acm.types.get_account_configuration_response.GetAccountConfigurationResponse":
        """<p>Returns the account configuration options associated with an Amazon Web Services account.</p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_acm.types.get_account_configuration_response.GetAccountConfigurationResponse"
        ]:
            import aws_sdk_acm._operations.certificate_manager.get_account_configuration

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.get_account_configuration.get_account_configuration(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_certificate(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> "aws_sdk_acm.types.get_certificate_response.GetCertificateResponse":
        r"""<p>Retrieves a certificate and its certificate chain. The certificate may be either a public or private certificate issued using the ACM <code>RequestCertificate</code> action, or a certificate imported into ACM using the <code>ImportCertificate</code> action. The chain consists of the certificate of the issuing CA and the intermediate certificates of any other subordinate CAs. All of the certificates are base64 encoded. You can use <a href=\"https://wiki.openssl.org/index.php/Command_Line_Utilities\">OpenSSL</a> to decode the certificates and inspect individual fields.</p>

        Args:
            certificate_arn: <p>String that contains a certificate ARN in the following format:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.get_certificate_request.GetCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_acm.types.get_certificate_response.GetCertificateResponse"
        ]:
            import aws_sdk_acm._operations.certificate_manager.get_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.get_certificate.get_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.get_certificate_request.GetCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_certificate(
        self,
        certificate: "aws_sdk_acm.types.certificate_body_blob.CertificateBodyBlob",
        private_key: "aws_sdk_acm.types.private_key_blob.PrivateKeyBlob",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
        certificate_arn: Optional["aws_sdk_acm.types.arn.Arn"] = None,
        certificate_chain: Optional[
            "aws_sdk_acm.types.certificate_chain_blob.CertificateChainBlob"
        ] = None,
        tags: Optional["aws_sdk_acm.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_acm.types.import_certificate_response.ImportCertificateResponse":
        r"""<p>Imports a certificate into Certificate Manager (ACM) to use with services that are integrated with ACM. Note that <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html\">integrated services</a> allow only certificate types and keys they support to be associated with their resources. Further, their support differs depending on whether the certificate is imported into IAM or into ACM. For more information, see the documentation for each service. For more information about importing certificates into ACM, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html\">Importing Certificates</a> in the <i>Certificate Manager User Guide</i>. </p> <note> <p>ACM does not provide <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html\">managed renewal</a> for certificates that you import.</p> </note> <p>Note the following guidelines when importing third party certificates:</p> <ul> <li> <p>You must enter the private key that matches the certificate you are importing.</p> </li> <li> <p>The private key must be unencrypted. You cannot import a private key that is protected by a password or a passphrase.</p> </li> <li> <p>The private key must be no larger than 5 KB (5,120 bytes).</p> </li> <li> <p>The certificate, private key, and certificate chain must be PEM-encoded.</p> </li> <li> <p>The current time must be between the <code>Not Before</code> and <code>Not After</code> certificate fields.</p> </li> <li> <p>The <code>Issuer</code> field must not be empty.</p> </li> <li> <p>The OCSP authority URL, if present, must not exceed 1000 characters.</p> </li> <li> <p>To import a new certificate, omit the <code>CertificateArn</code> argument. Include this argument only when you want to replace a previously imported certificate.</p> </li> <li> <p>When you import a certificate by using the CLI, you must specify the certificate, the certificate chain, and the private key by their file names preceded by <code>fileb://</code>. For example, you can specify a certificate saved in the <code>C:\temp</code> folder as <code>fileb://C:\temp\certificate_to_import.pem</code>. If you are making an HTTP or HTTPS Query request, include these arguments as BLOBs. </p> </li> <li> <p>When you import a certificate by using an SDK, you must specify the certificate, the certificate chain, and the private key files in the manner required by the programming language you're using. </p> </li> <li> <p>The cryptographic algorithm of an imported certificate must match the algorithm of the signing CA. For example, if the signing CA key type is RSA, then the certificate key type must also be RSA.</p> </li> </ul> <p>This operation returns the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the imported certificate.</p>

        Args:
            certificate_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of an imported certificate to replace. To import a new certificate, omit this field. </p>
            certificate: <p>The certificate to import.</p>
            private_key: <p>The private key that matches the public key in the certificate.</p>
            certificate_chain: <p>The PEM encoded certificate chain.</p>
            tags: <p>One or more resource tags to associate with the imported certificate. </p> <p>Note: You cannot apply tags when reimporting a certificate.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.import_certificate_request.ImportCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_acm.types.import_certificate_response.ImportCertificateResponse"
        ]:
            import aws_sdk_acm._operations.certificate_manager.import_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.import_certificate.import_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.import_certificate_request.ImportCertificateRequest = {}  # type: ignore[typeddict-item]
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        input_["certificate"] = certificate
        input_["private_key"] = private_key
        if certificate_chain is not None:
            input_["certificate_chain"] = certificate_chain
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_certificates(
        self,
        *,
        config_overrides: Optional[ACMClientConfig] = None,
        certificate_statuses: Optional[
            "aws_sdk_acm.types.certificate_statuses.CertificateStatuses"
        ] = None,
        includes: Optional["aws_sdk_acm.types.filters.Filters"] = None,
        next_token: Optional["aws_sdk_acm.types.next_token.NextToken"] = None,
        max_items: Optional["aws_sdk_acm.types.max_items.MaxItems"] = None,
        sort_by: Optional["aws_sdk_acm.types.sort_by.SortBy"] = None,
        sort_order: Optional["aws_sdk_acm.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_acm.types.list_certificates_response.ListCertificatesResponse":
        """<p>Retrieves a list of certificate ARNs and domain names. You can request that only certificates that match a specific status be listed. You can also filter by specific attributes of the certificate. Default filtering returns only <code>RSA_2048</code> certificates. For more information, see <a>Filters</a>.</p>

        Args:
            certificate_statuses: <p>Filter the certificate list by status value.</p>
            includes: <p>Filter the certificate list. For more information, see the <a>Filters</a> structure.</p>
            next_token: <p>Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the response you just received.</p>
            max_items: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            sort_by: <p>Specifies the field to sort results by. If you specify <code>SortBy</code>, you must also specify <code>SortOrder</code>.</p>
            sort_order: <p>Specifies the order of sorted results. If you specify <code>SortOrder</code>, you must also specify <code>SortBy</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.list_certificates_request.ListCertificatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_acm.types.list_certificates_response.ListCertificatesResponse"
        ]:
            import aws_sdk_acm._operations.certificate_manager.list_certificates

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.list_certificates.list_certificates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.list_certificates_request.ListCertificatesRequest = {}  # type: ignore[typeddict-item]
        if certificate_statuses is not None:
            input_["certificate_statuses"] = certificate_statuses
        if includes is not None:
            input_["includes"] = includes
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_certificates(
        self,
        *,
        config_overrides: Optional[ACMClientConfig] = None,
        certificate_statuses: Optional[
            "aws_sdk_acm.types.certificate_statuses.CertificateStatuses"
        ] = None,
        includes: Optional["aws_sdk_acm.types.filters.Filters"] = None,
        next_token: Optional["aws_sdk_acm.types.next_token.NextToken"] = None,
        max_items: Optional["aws_sdk_acm.types.max_items.MaxItems"] = None,
        sort_by: Optional["aws_sdk_acm.types.sort_by.SortBy"] = None,
        sort_order: Optional["aws_sdk_acm.types.sort_order.SortOrder"] = None,
    ) -> "Iterator[aws_sdk_acm.types.certificate_summary.CertificateSummary]":
        _token = next_token
        while True:
            _response = self.list_certificates(
                config_overrides=config_overrides,
                certificate_statuses=certificate_statuses,
                includes=includes,
                next_token=_token,
                max_items=max_items,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("certificate_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_certificate(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> "aws_sdk_acm.types.list_tags_for_certificate_response.ListTagsForCertificateResponse":
        r"""<p>Lists the tags that have been applied to the ACM certificate. Use the certificate's Amazon Resource Name (ARN) to specify the certificate. To add a tag to an ACM certificate, use the <a>AddTagsToCertificate</a> action. To delete a tag, use the <a>RemoveTagsFromCertificate</a> action. </p>

        Args:
            certificate_arn: <p>String that contains the ARN of the ACM certificate for which you want to list the tags. This must have the following form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.list_tags_for_certificate_request.ListTagsForCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_acm.types.list_tags_for_certificate_response.ListTagsForCertificateResponse"
        ]:
            import aws_sdk_acm._operations.certificate_manager.list_tags_for_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.list_tags_for_certificate.list_tags_for_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.list_tags_for_certificate_request.ListTagsForCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_account_configuration(
        self,
        idempotency_token: "aws_sdk_acm.types.idempotency_token.IdempotencyToken",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
        expiry_events: Optional[
            "aws_sdk_acm.types.expiry_events_configuration.ExpiryEventsConfiguration"
        ] = None,
    ) -> None:
        """<p>Adds or modifies account-level configurations in ACM. </p> <p>The supported configuration option is <code>DaysBeforeExpiry</code>. This option specifies the number of days prior to certificate expiration when ACM starts generating <code>EventBridge</code> events. ACM sends one event per day per certificate until the certificate expires. By default, accounts receive events starting 45 days before certificate expiration.</p>

        Args:
            expiry_events: <p>Specifies expiration events associated with an account.</p>
            idempotency_token: <p>Customer-chosen string used to distinguish between calls to <code>PutAccountConfiguration</code>. Idempotency tokens time out after one hour. If you call <code>PutAccountConfiguration</code> multiple times with the same unexpired idempotency token, ACM treats it as the same request and returns the original result. If you change the idempotency token for each call, ACM treats each call as a new request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.put_account_configuration_request.PutAccountConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_acm._operations.certificate_manager.put_account_configuration

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.put_account_configuration.put_account_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.put_account_configuration_request.PutAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
        if expiry_events is not None:
            input_["expiry_events"] = expiry_events
        input_["idempotency_token"] = idempotency_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_tags_from_certificate(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        tags: "aws_sdk_acm.types.tag_list.TagList",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> None:
        r"""<p>Remove one or more tags from an ACM certificate. A tag consists of a key-value pair. If you do not specify the value portion of the tag when calling this function, the tag will be removed regardless of value. If you specify a value, the tag is removed only if it is associated with the specified value. </p> <p>To add tags to a certificate, use the <a>AddTagsToCertificate</a> action. To view all of the tags that have been applied to a specific ACM certificate, use the <a>ListTagsForCertificate</a> action. </p>

        Args:
            certificate_arn: <p>String that contains the ARN of the ACM Certificate with one or more tags that you want to remove. This must be of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a>.</p>
            tags: <p>The key-value pair that defines the tag to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.remove_tags_from_certificate_request.RemoveTagsFromCertificateRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_acm._operations.certificate_manager.remove_tags_from_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.remove_tags_from_certificate.remove_tags_from_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.remove_tags_from_certificate_request.RemoveTagsFromCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def renew_certificate(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> None:
        r"""<p>Renews an <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html\">eligible ACM certificate</a>. In order to renew your Amazon Web Services Private CA certificates with ACM, you must first <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/assign-permissions.html#PcaPermissions\">grant the ACM service principal permission to do so</a>. For more information, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html\">Testing Managed Renewal</a> in the ACM User Guide.</p>

        Args:
            certificate_arn: <p>String that contains the ARN of the ACM certificate to be renewed. This must be of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.renew_certificate_request.RenewCertificateRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_acm._operations.certificate_manager.renew_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.renew_certificate.renew_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.renew_certificate_request.RenewCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def request_certificate(
        self,
        domain_name: "aws_sdk_acm.types.domain_name_string.DomainNameString",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
        validation_method: Optional[
            "aws_sdk_acm.types.validation_method.ValidationMethod"
        ] = None,
        subject_alternative_names: Optional[
            "aws_sdk_acm.types.domain_list.DomainList"
        ] = None,
        idempotency_token: Optional[
            "aws_sdk_acm.types.idempotency_token.IdempotencyToken"
        ] = None,
        domain_validation_options: Optional[
            "aws_sdk_acm.types.domain_validation_option_list.DomainValidationOptionList"
        ] = None,
        options: Optional[
            "aws_sdk_acm.types.certificate_options.CertificateOptions"
        ] = None,
        certificate_authority_arn: Optional["aws_sdk_acm.types.pca_arn.PcaArn"] = None,
        tags: Optional["aws_sdk_acm.types.tag_list.TagList"] = None,
        key_algorithm: Optional["aws_sdk_acm.types.key_algorithm.KeyAlgorithm"] = None,
        managed_by: Optional[
            "aws_sdk_acm.types.certificate_managed_by.CertificateManagedBy"
        ] = None,
    ) -> "aws_sdk_acm.types.request_certificate_response.RequestCertificateResponse":
        r"""<p>Requests an ACM certificate for use with other Amazon Web Services services. To request an ACM certificate, you must specify a fully qualified domain name (FQDN) in the <code>DomainName</code> parameter. You can also specify additional FQDNs in the <code>SubjectAlternativeNames</code> parameter. </p> <p>If you are requesting a private certificate, domain validation is not required. If you are requesting a public certificate, each domain name that you specify must be validated to verify that you own or control the domain. You can use <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html\">DNS validation</a> or <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html\">email validation</a>. We recommend that you use DNS validation.</p> <note> <p>ACM behavior differs from the <a href=\"https://datatracker.ietf.org/doc/html/rfc6125#appendix-B.2\">RFC 6125</a> specification of the certificate validation process. ACM first checks for a Subject Alternative Name, and, if it finds one, ignores the common name (CN).</p> </note> <p>After successful completion of the <code>RequestCertificate</code> action, there is a delay of several seconds before you can retrieve information about the new certificate.</p>

        Args:
            domain_name: <p>Fully qualified domain name (FQDN), such as www.example.com, that you want to secure with an ACM certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, *.example.com protects www.example.com, site.example.com, and images.example.com. </p> <p>In compliance with <a href=\"https://datatracker.ietf.org/doc/html/rfc5280\">RFC 5280</a>, the length of the domain name (technically, the Common Name) that you provide cannot exceed 64 octets (characters), including periods. To add a longer domain name, specify it in the Subject Alternative Name field, which supports names up to 253 octets in length. </p>
            validation_method: <p>The method you want to use if you are requesting a public certificate to validate that you own or control domain. You can <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html\">validate with DNS</a> or <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html\">validate with email</a>. We recommend that you use DNS validation. </p>
            subject_alternative_names: <p>Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate. For example, add the name www.example.net to a certificate for which the <code>DomainName</code> field is www.example.com if users can reach your site by using either name. The maximum number of domain names that you can add to an ACM certificate is 100. However, the initial quota is 10 domain names. If you need more than 10 names, you must request a quota increase. For more information, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html\">Quotas</a>.</p> <p> The maximum length of a SAN DNS name is 253 octets. The name is made up of multiple labels separated by periods. No label can be longer than 63 octets. Consider the following examples: </p> <ul> <li> <p> <code>(63 octets).(63 octets).(63 octets).(61 octets)</code> is legal because the total length is 253 octets (63+1+63+1+63+1+61) and no label exceeds 63 octets.</p> </li> <li> <p> <code>(64 octets).(63 octets).(63 octets).(61 octets)</code> is not legal because the total length exceeds 253 octets (64+1+63+1+63+1+61) and the first label exceeds 63 octets.</p> </li> <li> <p> <code>(63 octets).(63 octets).(63 octets).(62 octets)</code> is not legal because the total length of the DNS name (63+1+63+1+63+1+62) exceeds 253 octets.</p> </li> </ul>
            idempotency_token: <p>Customer chosen string that can be used to distinguish between calls to <code>RequestCertificate</code>. Idempotency tokens time out after one hour. Therefore, if you call <code>RequestCertificate</code> multiple times with the same idempotency token within one hour, ACM recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, ACM recognizes that you are requesting multiple certificates.</p>
            domain_validation_options: <p>The domain name that you want ACM to use to send you emails so that you can validate domain ownership.</p>
            options: <p>You can use this parameter to specify whether to add the certificate to a certificate transparency log and export your certificate.</p> <p>Certificate transparency makes it possible to detect SSL/TLS certificates that have been mistakenly or maliciously issued. Certificates that have not been logged typically produce an error message in a browser. For more information, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency\">Opting Out of Certificate Transparency Logging</a>.</p> <p>You can export public ACM certificates to use with Amazon Web Services services as well as outside the Amazon Web Services Cloud. For more information, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-exportable-certificates.html\">Certificate Manager exportable public certificate</a>.</p>
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) of the private certificate authority (CA) that will be used to issue the certificate. If you do not provide an ARN and you are trying to request a private certificate, ACM will attempt to issue a public certificate. For more information about private CAs, see the <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html\">Amazon Web Services Private Certificate Authority</a> user guide. The ARN must have the following form: </p> <p> <code>arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012</code> </p>
            tags: <p>One or more resource tags to associate with the certificate.</p>
            key_algorithm: <p>Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. RSA is the default key algorithm for ACM certificates. Elliptic Curve Digital Signature Algorithm (ECDSA) keys are smaller, offering security comparable to RSA keys but with greater computing efficiency. However, ECDSA is not supported by all network clients. Some Amazon Web Services services may require RSA keys, or only support ECDSA keys of a particular size, while others allow the use of either RSA and ECDSA keys to ensure that compatibility is not broken. Check the requirements for the Amazon Web Services service where you plan to deploy your certificate. For more information about selecting an algorithm, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate-characteristics.html#algorithms-term\">Key algorithms</a>.</p> <note> <p>Algorithms supported for an ACM certificate request include: </p> <ul> <li> <p> <code>RSA_2048</code> </p> </li> <li> <p> <code>EC_prime256v1</code> </p> </li> <li> <p> <code>EC_secp384r1</code> </p> </li> </ul> <p>Other listed algorithms are for imported certificates only. </p> </note> <note> <p>When you request a private PKI certificate signed by a CA from Amazon Web Services Private CA, the specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.</p> </note> <p>Default: RSA_2048</p>
            managed_by: <p>Identifies the Amazon Web Services service that manages the certificate issued by ACM.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.request_certificate_request.RequestCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_acm.types.request_certificate_response.RequestCertificateResponse"
        ]:
            import aws_sdk_acm._operations.certificate_manager.request_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.request_certificate.request_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.request_certificate_request.RequestCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if validation_method is not None:
            input_["validation_method"] = validation_method
        if subject_alternative_names is not None:
            input_["subject_alternative_names"] = subject_alternative_names
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token
        if domain_validation_options is not None:
            input_["domain_validation_options"] = domain_validation_options
        if options is not None:
            input_["options"] = options
        if certificate_authority_arn is not None:
            input_["certificate_authority_arn"] = certificate_authority_arn
        if tags is not None:
            input_["tags"] = tags
        if key_algorithm is not None:
            input_["key_algorithm"] = key_algorithm
        if managed_by is not None:
            input_["managed_by"] = managed_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def resend_validation_email(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        domain: "aws_sdk_acm.types.domain_name_string.DomainNameString",
        validation_domain: "aws_sdk_acm.types.domain_name_string.DomainNameString",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> None:
        r"""<p>Resends the email that requests domain ownership validation. The domain owner or an authorized representative must approve the ACM certificate before it can be issued. The certificate can be approved by clicking a link in the mail to navigate to the Amazon certificate approval website and then clicking <b>I Approve</b>. However, the validation email can be blocked by spam filters. Therefore, if you do not receive the original mail, you can request that the mail be resent within 72 hours of requesting the ACM certificate. If more than 72 hours have elapsed since your original request or since your last attempt to resend validation mail, you must request a new certificate. For more information about setting up your contact email addresses, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/setup-email.html\">Configure Email for your Domain</a>. </p>

        Args:
            certificate_arn: <p>String that contains the ARN of the requested certificate. The certificate ARN is generated and returned by the <a>RequestCertificate</a> action as soon as the request is made. By default, using this parameter causes email to be sent to all top-level domains you specified in the certificate request. The ARN must be of the form: </p> <p> <code>arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p>
            domain: <p>The fully qualified domain name (FQDN) of the certificate that needs to be validated.</p>
            validation_domain: <p>The base validation domain that will act as the suffix of the email addresses that are used to send the emails. This must be the same as the <code>Domain</code> value or a superdomain of the <code>Domain</code> value. For example, if you requested a certificate for <code>site.subdomain.example.com</code> and specify a <b>ValidationDomain</b> of <code>subdomain.example.com</code>, ACM sends email to the the following five addresses:</p> <ul> <li> <p>admin@subdomain.example.com</p> </li> <li> <p>administrator@subdomain.example.com</p> </li> <li> <p>hostmaster@subdomain.example.com</p> </li> <li> <p>postmaster@subdomain.example.com</p> </li> <li> <p>webmaster@subdomain.example.com</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.resend_validation_email_request.ResendValidationEmailRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_acm._operations.certificate_manager.resend_validation_email

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.resend_validation_email.resend_validation_email(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.resend_validation_email_request.ResendValidationEmailRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn
        input_["domain"] = domain
        input_["validation_domain"] = validation_domain

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def revoke_certificate(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        revocation_reason: "aws_sdk_acm.types.revocation_reason.RevocationReason",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> "aws_sdk_acm.types.revoke_certificate_response.RevokeCertificateResponse":
        """<p>Revokes a public ACM certificate. You can only revoke certificates that have been previously exported.</p> <important> <p>Once a certificate is revoked, you cannot reuse the certificate. Revoking a certificate is permanent.</p> </important>

        Args:
            certificate_arn: <p>The Amazon Resource Name (ARN) of the public or private certificate that will be revoked. The ARN must have the following form: </p> <p> <code>arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012</code> </p>
            revocation_reason: <p>Specifies why you revoked the certificate.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.revoke_certificate_request.RevokeCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_acm.types.revoke_certificate_response.RevokeCertificateResponse"
        ]:
            import aws_sdk_acm._operations.certificate_manager.revoke_certificate

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.revoke_certificate.revoke_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.revoke_certificate_request.RevokeCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn
        input_["revocation_reason"] = revocation_reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_certificates(
        self,
        *,
        config_overrides: Optional[ACMClientConfig] = None,
        filter_statement: Optional[
            "aws_sdk_acm.types.certificate_filter_statement.CertificateFilterStatement"
        ] = None,
        max_results: Optional[
            "aws_sdk_acm.types.search_max_results.SearchMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_acm.types.next_token.NextToken"] = None,
        sort_by: Optional[
            "aws_sdk_acm.types.search_certificates_sort_by.SearchCertificatesSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_acm.types.search_certificates_sort_order.SearchCertificatesSortOrder"
        ] = None,
    ) -> "aws_sdk_acm.types.search_certificates_response.SearchCertificatesResponse":
        """<p>Retrieves a list of certificates matching search criteria. You can filter certificates by X.509 attributes and ACM specific properties like certificate status, type and renewal eligibility. This operation provides more flexible filtering than <a>ListCertificates</a> by supporting complex filter statements.</p>

        Args:
            filter_statement: <p>A filter statement that defines the search criteria. You can combine multiple filters using AND, OR, and NOT logical operators to create complex queries.</p>
            max_results: <p>The maximum number of results to return in the response. Default is 100.</p>
            next_token: <p>Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the response you just received.</p>
            sort_by: <p>Specifies the field to sort results by. Valid values are CREATED_AT, NOT_AFTER, STATUS, RENEWAL_STATUS, EXPORTED, IN_USE, NOT_BEFORE, KEY_ALGORITHM, TYPE, CERTIFICATE_ARN, COMMON_NAME, REVOKED_AT, RENEWAL_ELIGIBILITY, ISSUED_AT, MANAGED_BY, EXPORT_OPTION, VALIDATION_METHOD, and IMPORTED_AT.</p>
            sort_order: <p>Specifies the order of sorted results. Valid values are ASCENDING or DESCENDING.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.search_certificates_request.SearchCertificatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_acm.types.search_certificates_response.SearchCertificatesResponse"
        ]:
            import aws_sdk_acm._operations.certificate_manager.search_certificates

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.search_certificates.search_certificates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.search_certificates_request.SearchCertificatesRequest = {}  # type: ignore[typeddict-item]
        if filter_statement is not None:
            input_["filter_statement"] = filter_statement
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_search_certificates(
        self,
        *,
        config_overrides: Optional[ACMClientConfig] = None,
        filter_statement: Optional[
            "aws_sdk_acm.types.certificate_filter_statement.CertificateFilterStatement"
        ] = None,
        max_results: Optional[
            "aws_sdk_acm.types.search_max_results.SearchMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_acm.types.next_token.NextToken"] = None,
        sort_by: Optional[
            "aws_sdk_acm.types.search_certificates_sort_by.SearchCertificatesSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_acm.types.search_certificates_sort_order.SearchCertificatesSortOrder"
        ] = None,
    ) -> (
        "Iterator[aws_sdk_acm.types.certificate_search_result.CertificateSearchResult]"
    ):
        _token = next_token
        while True:
            _response = self.search_certificates(
                config_overrides=config_overrides,
                filter_statement=filter_statement,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_certificate_options(
        self,
        certificate_arn: "aws_sdk_acm.types.arn.Arn",
        options: "aws_sdk_acm.types.certificate_options.CertificateOptions",
        *,
        config_overrides: Optional[ACMClientConfig] = None,
    ) -> None:
        r"""<p>Updates a certificate. You can use this function to specify whether to opt in to or out of recording your certificate in a certificate transparency log and exporting. For more information, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency\"> Opting Out of Certificate Transparency Logging</a> and <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-exportable-certificates.html\">Certificate Manager Exportable Managed Certificates</a>.</p>

        Args:
            certificate_arn: <p>ARN of the requested certificate to update. This must be of the form:</p> <p> <code>arn:aws:acm:us-east-1:<i>account</i>:certificate/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>
            options: <p>Use to update the options for your certificate. Currently, you can specify whether to add your certificate to a transparency log or export your certificate. Certificate transparency makes it possible to detect SSL/TLS certificates that have been mistakenly or maliciously issued. Certificates that have not been logged typically produce an error message in a browser. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_acm.types.update_certificate_options_request.UpdateCertificateOptionsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_acm._operations.certificate_manager.update_certificate_options

            output, http_response = (
                aws_sdk_acm._operations.certificate_manager.update_certificate_options.update_certificate_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_acm.types.update_certificate_options_request.UpdateCertificateOptionsRequest = {}  # type: ignore[typeddict-item]
        input_["certificate_arn"] = certificate_arn
        input_["options"] = options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
