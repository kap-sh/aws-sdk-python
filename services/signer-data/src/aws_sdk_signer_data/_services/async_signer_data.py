"""Generated from Smithy shape ``com.amazonaws.signerdata#SignerDataPlane``."""

import datetime
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_signer_data._auth._signers
import aws_sdk_signer_data._auth._sigv4
from aws_sdk_signer_data._auth._identity import Credentials
from aws_sdk_signer_data._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_signer_data._auth._zapros_handler import AuthMiddleware
from aws_sdk_signer_data._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_signer_data.types.arn
    import aws_sdk_signer_data.types.certificate_hashes
    import aws_sdk_signer_data.types.get_revocation_status_request
    import aws_sdk_signer_data.types.get_revocation_status_response
    import aws_sdk_signer_data.types.platform_id


class AsyncSignerDataClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_fips: bool | None
    use_dual_stack: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncSignerDataClient:
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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_fips: bool | None = None,
        use_dual_stack: bool | None = None,
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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncSignerDataClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "use_dual_stack": use_dual_stack,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSignerDataClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSignerDataClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    async def get_revocation_status(
        self,
        signature_timestamp: datetime.datetime,
        platform_id: "aws_sdk_signer_data.types.platform_id.PlatformId",
        profile_version_arn: "aws_sdk_signer_data.types.arn.Arn",
        job_arn: "aws_sdk_signer_data.types.arn.Arn",
        certificate_hashes: "aws_sdk_signer_data.types.certificate_hashes.CertificateHashes",
        *,
        config_overrides: Optional[AsyncSignerDataClientConfig] = None,
    ) -> "aws_sdk_signer_data.types.get_revocation_status_response.GetRevocationStatusResponse":
        """<p>Retrieves the revocation status for a signed artifact by checking if the signing profile, job, or certificate has been revoked.</p>

        Args:
            signature_timestamp: <p>The timestamp when the artifact was signed, in ISO 8601 format.</p>
            platform_id: <p>The platform identifier for the signing platform used.</p>
            profile_version_arn: <p>The ARN of the signing profile version used to sign the artifact.</p>
            job_arn: <p>The ARN of the signing job that produced the signature.</p>
            certificate_hashes: <p>List of certificate hashes to check for revocation.</p>

        Examples:
            Check revocation status for a signed artifact
            Checks if a signing profile, job, or certificate has been revoked for a given artifact.

            >>> await client.get_revocation_status(signature_timestamp=1700000000, platform_id='Notation-OCI-SHA384-ECDSA', profile_version_arn='arn:aws:signer:us-east-1:123456789012:/signing-profiles/my-profile/v1', job_arn='arn:aws:signer:us-east-1:123456789012:/signing-jobs/my-job-id', certificate_hashes=['e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_signer_data.types.get_revocation_status_request.GetRevocationStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_signer_data.types.get_revocation_status_response.GetRevocationStatusResponse"
        ]:
            import aws_sdk_signer_data._operations.signer_data_plane.get_revocation_status

            (
                output,
                http_response,
            ) = await aws_sdk_signer_data._operations.signer_data_plane.get_revocation_status.async_get_revocation_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_signer_data.types.get_revocation_status_request.GetRevocationStatusRequest = {}  # type: ignore[typeddict-item]
        input_["signature_timestamp"] = signature_timestamp
        input_["platform_id"] = platform_id
        input_["profile_version_arn"] = profile_version_arn
        input_["job_arn"] = job_arn
        input_["certificate_hashes"] = certificate_hashes

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
