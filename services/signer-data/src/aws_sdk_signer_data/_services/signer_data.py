"""Generated from Smithy shape ``com.amazonaws.signerdata#SignerDataPlane``."""

import datetime
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_signer_data._auth._signers
import aws_sdk_signer_data._auth._sigv4
from aws_sdk_signer_data._auth._identity import Credentials
from aws_sdk_signer_data._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_signer_data._auth._zapros_handler import AuthMiddleware
from aws_sdk_signer_data._services._aws_config import aws_config
from aws_sdk_signer_data._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_signer_data.types.arn
    import aws_sdk_signer_data.types.certificate_hashes
    import aws_sdk_signer_data.types.get_revocation_status_request
    import aws_sdk_signer_data.types.get_revocation_status_response
    import aws_sdk_signer_data.types.platform_id


class SignerDataClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_fips: bool | None
    use_dual_stack: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SignerDataClient:
    """A client for the ``SignerData`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
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
        use_fips: bool | None = None,
        use_dual_stack: bool | None = None,
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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = SignerDataClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "use_dual_stack": use_dual_stack,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[SignerDataClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SignerDataClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def get_revocation_status(
        self,
        signature_timestamp: datetime.datetime,
        platform_id: "aws_sdk_signer_data.types.platform_id.PlatformId",
        profile_version_arn: "aws_sdk_signer_data.types.arn.Arn",
        job_arn: "aws_sdk_signer_data.types.arn.Arn",
        certificate_hashes: "aws_sdk_signer_data.types.certificate_hashes.CertificateHashes",
        *,
        config_overrides: Optional[SignerDataClientConfig] = None,
    ) -> "aws_sdk_signer_data.types.get_revocation_status_response.GetRevocationStatusResponse":
        """<p>Retrieves the revocation status for a signed artifact by checking if the signing profile, job, or certificate has been revoked.</p>

        Args:
            signature_timestamp: <p>The timestamp when the artifact was signed, in ISO 8601 format.</p>
            platform_id: <p>The platform identifier for the signing platform used.</p>
            profile_version_arn: <p>The ARN of the signing profile version used to sign the artifact.</p>
            job_arn: <p>The ARN of the signing job that produced the signature.</p>
            certificate_hashes: <p>List of certificate hashes to check for revocation.</p>

        Raises:
            aws_sdk_signer_data.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            aws_sdk_signer_data.errors.internal_service_error_exception.InternalServiceErrorException: <p>An internal service error occurred.</p>
            aws_sdk_signer_data.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            aws_sdk_signer_data.errors.validation_exception.ValidationException: <p>The request contains invalid parameters or is malformed.</p>
            aws_sdk_signer_data.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Check revocation status for a signed artifact
            Checks if a signing profile, job, or certificate has been revoked for a given artifact.

            >>> client.get_revocation_status(signature_timestamp=1700000000, platform_id='Notation-OCI-SHA384-ECDSA', profile_version_arn='arn:aws:signer:us-east-1:123456789012:/signing-profiles/my-profile/v1', job_arn='arn:aws:signer:us-east-1:123456789012:/signing-jobs/my-job-id', certificate_hashes=['e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_signer_data.types.get_revocation_status_request.GetRevocationStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_signer_data.types.get_revocation_status_response.GetRevocationStatusResponse"
        ]:
            import aws_sdk_signer_data._operations.signer_data_plane.get_revocation_status

            output, http_response = (
                aws_sdk_signer_data._operations.signer_data_plane.get_revocation_status.get_revocation_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer_data.types.get_revocation_status_request.GetRevocationStatusRequest = {}  # type: ignore[typeddict-item]
        input_["signature_timestamp"] = signature_timestamp
        input_["platform_id"] = platform_id
        input_["profile_version_arn"] = profile_version_arn
        input_["job_arn"] = job_arn
        input_["certificate_hashes"] = certificate_hashes

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
