"""Generated from Smithy shape ``com.amazonaws.eksauth#EKSAuthFrontend``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_eks_auth._auth._signers
import aws_sdk_eks_auth._auth._sigv4
from aws_sdk_eks_auth._auth._identity import Credentials
from aws_sdk_eks_auth._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_eks_auth._auth._zapros_handler import AuthMiddleware
from aws_sdk_eks_auth._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_eks_auth.types.assume_role_for_pod_identity_request
    import aws_sdk_eks_auth.types.assume_role_for_pod_identity_response
    import aws_sdk_eks_auth.types.cluster_name
    import aws_sdk_eks_auth.types.jwt_token


class AsyncEKSAuthClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncEKSAuthClient:
    """A client for the ``EKSAuth`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncEKSAuthClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncEKSAuthClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncEKSAuthClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def assume_role_for_pod_identity(
        self,
        cluster_name: "aws_sdk_eks_auth.types.cluster_name.ClusterName",
        token: "aws_sdk_eks_auth.types.jwt_token.JwtToken",
        *,
        config_overrides: Optional[AsyncEKSAuthClientConfig] = None,
    ) -> "aws_sdk_eks_auth.types.assume_role_for_pod_identity_response.AssumeRoleForPodIdentityResponse":
        """<p>The Amazon EKS Auth API and the <code>AssumeRoleForPodIdentity</code> action are only used by the EKS Pod Identity Agent.</p> <p>We recommend that applications use the Amazon Web Services SDKs to connect to Amazon Web Services services; if credentials from an EKS Pod Identity association are available in the pod, the latest versions of the SDKs use them automatically.</p>

        Args:
            cluster_name: <p>The name of the cluster for the request.</p>
            token: <p>The token of the Kubernetes service account for the pod.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_eks_auth.types.assume_role_for_pod_identity_request.AssumeRoleForPodIdentityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_eks_auth.types.assume_role_for_pod_identity_response.AssumeRoleForPodIdentityResponse"
        ]:
            import aws_sdk_eks_auth._operations.eks_auth_frontend.assume_role_for_pod_identity

            (
                output,
                http_response,
            ) = await aws_sdk_eks_auth._operations.eks_auth_frontend.assume_role_for_pod_identity.async_assume_role_for_pod_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_eks_auth.types.assume_role_for_pod_identity_request.AssumeRoleForPodIdentityRequest = {}  # type: ignore[typeddict-item]
        input["cluster_name"] = cluster_name
        input["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
