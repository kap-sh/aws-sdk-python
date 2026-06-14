"""Generated from Smithy shape ``com.amazonaws.eksauth#EKSAuthFrontend``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_eks_auth._auth._signers
import aws_sdk_eks_auth._auth._sigv4
from aws_sdk_eks_auth._auth._identity import Credentials
from aws_sdk_eks_auth._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_eks_auth._auth._zapros_handler import AuthMiddleware
from aws_sdk_eks_auth._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_eks_auth.types.assume_role_for_pod_identity_request
    import aws_sdk_eks_auth.types.assume_role_for_pod_identity_response
    import aws_sdk_eks_auth.types.cluster_name
    import aws_sdk_eks_auth.types.jwt_token


class EKSAuthClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class EKSAuthClient:
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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
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
        self.config = EKSAuthClientConfig(
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
        self, config_overrides: Optional[EKSAuthClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: EKSAuthClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def assume_role_for_pod_identity(
        self,
        cluster_name: "aws_sdk_eks_auth.types.cluster_name.ClusterName",
        token: "aws_sdk_eks_auth.types.jwt_token.JwtToken",
        *,
        config_overrides: Optional[EKSAuthClientConfig] = None,
    ) -> "aws_sdk_eks_auth.types.assume_role_for_pod_identity_response.AssumeRoleForPodIdentityResponse":
        """<p>The Amazon EKS Auth API and the <code>AssumeRoleForPodIdentity</code> action are only used by the EKS Pod Identity Agent.</p> <p>We recommend that applications use the Amazon Web Services SDKs to connect to Amazon Web Services services; if credentials from an EKS Pod Identity association are available in the pod, the latest versions of the SDKs use them automatically.</p>

        Args:
            cluster_name: <p>The name of the cluster for the request.</p>
            token: <p>The token of the Kubernetes service account for the pod.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_eks_auth.types.assume_role_for_pod_identity_request.AssumeRoleForPodIdentityRequest]",
        ) -> OperationResponse[
            "aws_sdk_eks_auth.types.assume_role_for_pod_identity_response.AssumeRoleForPodIdentityResponse"
        ]:
            import aws_sdk_eks_auth._operations.eks_auth_frontend.assume_role_for_pod_identity

            output, http_response = (
                aws_sdk_eks_auth._operations.eks_auth_frontend.assume_role_for_pod_identity.assume_role_for_pod_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_eks_auth.types.assume_role_for_pod_identity_request.AssumeRoleForPodIdentityRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_name"] = cluster_name
        input_["token"] = token

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
