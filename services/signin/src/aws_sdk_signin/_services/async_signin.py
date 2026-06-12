"""Generated from Smithy shape ``com.amazonaws.signin#Signin``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_signin._auth._signers
import aws_sdk_signin._auth._sigv4
from aws_sdk_signin._auth._identity import Credentials
from aws_sdk_signin._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_signin._auth._zapros_handler import AuthMiddleware
from aws_sdk_signin._pagination import resolve_path as _resolve_path
from aws_sdk_signin._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_signin.types.client_token
    import aws_sdk_signin.types.console_permission_max_results
    import aws_sdk_signin.types.create_o_auth2_token_request
    import aws_sdk_signin.types.create_o_auth2_token_request_body
    import aws_sdk_signin.types.create_o_auth2_token_response
    import aws_sdk_signin.types.delete_console_authorization_configuration_input
    import aws_sdk_signin.types.delete_console_authorization_configuration_output
    import aws_sdk_signin.types.delete_resource_permission_statement_input
    import aws_sdk_signin.types.delete_resource_permission_statement_output
    import aws_sdk_signin.types.excluded_principal
    import aws_sdk_signin.types.get_console_authorization_configuration_input
    import aws_sdk_signin.types.get_console_authorization_configuration_output
    import aws_sdk_signin.types.get_resource_policy_input
    import aws_sdk_signin.types.get_resource_policy_output
    import aws_sdk_signin.types.list_resource_permission_statements_input
    import aws_sdk_signin.types.list_resource_permission_statements_output
    import aws_sdk_signin.types.next_token
    import aws_sdk_signin.types.permission_statement_summary
    import aws_sdk_signin.types.put_console_authorization_configuration_input
    import aws_sdk_signin.types.put_console_authorization_configuration_output
    import aws_sdk_signin.types.put_resource_permission_statement_input
    import aws_sdk_signin.types.put_resource_permission_statement_output
    import aws_sdk_signin.types.requested_region
    import aws_sdk_signin.types.source_ip
    import aws_sdk_signin.types.source_vpc
    import aws_sdk_signin.types.source_vpce
    import aws_sdk_signin.types.statement_id
    import aws_sdk_signin.types.target_id
    import aws_sdk_signin.types.vpc_source_ip


class AsyncSigninClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
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


class AsyncSigninClient:
    """A client for the ``Signin`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self.config = AsyncSigninClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSigninClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSigninClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def create_o_auth2_token(
        self,
        token_input: "aws_sdk_signin.types.create_o_auth2_token_request_body.CreateOAuth2TokenRequestBody",
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
    ) -> "aws_sdk_signin.types.create_o_auth2_token_response.CreateOAuth2TokenResponse":
        """CreateOAuth2Token API Path: /v1/token Request Method: POST Content-Type: application/json or application/x-www-form-urlencoded This API implements OAuth 2.0 flows for AWS Sign-In CLI clients, supporting both: 1. Authorization code redemption (grant_type=authorization_code) - NOT idempotent 2. Token refresh (grant_type=refresh_token) - Idempotent within token validity window The operation behavior is determined by the grant_type parameter in the request body: **Authorization Code Flow (NOT Idempotent):** - JSON or form-encoded body with client_id, grant_type=authorization_code, code, redirect_uri, code_verifier - Returns access_token, token_type, expires_in, refresh_token, and id_token - Each authorization code can only be used ONCE for security (prevents replay attacks) **Token Refresh Flow (Idempotent):** - JSON or form-encoded body with client_id, grant_type=refresh_token, refresh_token - Returns access_token, token_type, expires_in, and refresh_token (no id_token) - Multiple calls with same refresh_token return consistent results within validity window Authentication and authorization: - Confidential clients: sigv4 signing required with signin:ExchangeToken permissions - CLI clients (public): authn/authz skipped based on client_id & grant_type Note: This operation cannot be marked as @idempotent because it handles both idempotent (token refresh) and non-idempotent (auth code redemption) flows in a single endpoint.

        Args:
            token_input: Flattened token operation inputs The specific operation is determined by grant_type in the request body
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_signin.types.create_o_auth2_token_request.CreateOAuth2TokenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_signin.types.create_o_auth2_token_response.CreateOAuth2TokenResponse"
        ]:
            import aws_sdk_signin._operations.signin.create_o_auth2_token

            (
                output,
                http_response,
            ) = await aws_sdk_signin._operations.signin.create_o_auth2_token.async_create_o_auth2_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_signin.types.create_o_auth2_token_request.CreateOAuth2TokenRequest = {}  # type: ignore[typeddict-item]
        input["token_input"] = token_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_console_authorization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        target_id: Optional["aws_sdk_signin.types.target_id.TargetId"] = None,
    ) -> "aws_sdk_signin.types.delete_console_authorization_configuration_output.DeleteConsoleAuthorizationConfigurationOutput":
        """Delete console authorization configuration with automatic scope detection

        Args:
            target_id: Target account identifier
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_signin.types.delete_console_authorization_configuration_input.DeleteConsoleAuthorizationConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_signin.types.delete_console_authorization_configuration_output.DeleteConsoleAuthorizationConfigurationOutput"
        ]:
            import aws_sdk_signin._operations.signin.delete_console_authorization_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_signin._operations.signin.delete_console_authorization_configuration.async_delete_console_authorization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_signin.types.delete_console_authorization_configuration_input.DeleteConsoleAuthorizationConfigurationInput = {}  # type: ignore[typeddict-item]
        if target_id is not None:
            input["target_id"] = target_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource_permission_statement(
        self,
        statement_id: "aws_sdk_signin.types.statement_id.StatementId",
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        client_token: Optional["aws_sdk_signin.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_signin.types.delete_resource_permission_statement_output.DeleteResourcePermissionStatementOutput":
        """Remove a permission statement from the account's SignIn resource-based policy

        Args:
            statement_id: Unique identifier of the permission statement to delete
            client_token: Idempotency token for the request
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_signin.types.delete_resource_permission_statement_input.DeleteResourcePermissionStatementInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_signin.types.delete_resource_permission_statement_output.DeleteResourcePermissionStatementOutput"
        ]:
            import aws_sdk_signin._operations.signin.delete_resource_permission_statement

            (
                output,
                http_response,
            ) = await aws_sdk_signin._operations.signin.delete_resource_permission_statement.async_delete_resource_permission_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_signin.types.delete_resource_permission_statement_input.DeleteResourcePermissionStatementInput = {}  # type: ignore[typeddict-item]
        input["statement_id"] = statement_id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_console_authorization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        target_id: Optional["aws_sdk_signin.types.target_id.TargetId"] = None,
    ) -> "aws_sdk_signin.types.get_console_authorization_configuration_output.GetConsoleAuthorizationConfigurationOutput":
        """Get console authorization configuration with automatic scope detection

        Args:
            target_id: Target account identifier
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_signin.types.get_console_authorization_configuration_input.GetConsoleAuthorizationConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_signin.types.get_console_authorization_configuration_output.GetConsoleAuthorizationConfigurationOutput"
        ]:
            import aws_sdk_signin._operations.signin.get_console_authorization_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_signin._operations.signin.get_console_authorization_configuration.async_get_console_authorization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_signin.types.get_console_authorization_configuration_input.GetConsoleAuthorizationConfigurationInput = {}  # type: ignore[typeddict-item]
        if target_id is not None:
            input["target_id"] = target_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self, *, config_overrides: Optional[AsyncSigninClientConfig] = None
    ) -> "aws_sdk_signin.types.get_resource_policy_output.GetResourcePolicyOutput":
        """Retrieve the account's consolidated SignIn resource-based policy"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_signin.types.get_resource_policy_input.GetResourcePolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_signin.types.get_resource_policy_output.GetResourcePolicyOutput"
        ]:
            import aws_sdk_signin._operations.signin.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_signin._operations.signin.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_signin.types.get_resource_policy_input.GetResourcePolicyInput = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_resource_permission_statements(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        max_results: Optional[
            "aws_sdk_signin.types.console_permission_max_results.ConsolePermissionMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_signin.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_signin.types.list_resource_permission_statements_output.ListResourcePermissionStatementsOutput":
        """Retrieve all permission statements in the account's SignIn resource-based policy

        Args:
            max_results: Maximum number of results to return
            next_token: Token for pagination
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_signin.types.list_resource_permission_statements_input.ListResourcePermissionStatementsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_signin.types.list_resource_permission_statements_output.ListResourcePermissionStatementsOutput"
        ]:
            import aws_sdk_signin._operations.signin.list_resource_permission_statements

            (
                output,
                http_response,
            ) = await aws_sdk_signin._operations.signin.list_resource_permission_statements.async_list_resource_permission_statements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_signin.types.list_resource_permission_statements_input.ListResourcePermissionStatementsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_resource_permission_statements(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        max_results: Optional[
            "aws_sdk_signin.types.console_permission_max_results.ConsolePermissionMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_signin.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_signin.types.permission_statement_summary.PermissionStatementSummary]":
        _token = next_token
        while True:
            _response = await self.list_resource_permission_statements(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("permission_statements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_console_authorization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        target_id: Optional["aws_sdk_signin.types.target_id.TargetId"] = None,
    ) -> "aws_sdk_signin.types.put_console_authorization_configuration_output.PutConsoleAuthorizationConfigurationOutput":
        """Enable console authorization configuration with automatic scope detection

        Args:
            target_id: Target account identifier
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_signin.types.put_console_authorization_configuration_input.PutConsoleAuthorizationConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_signin.types.put_console_authorization_configuration_output.PutConsoleAuthorizationConfigurationOutput"
        ]:
            import aws_sdk_signin._operations.signin.put_console_authorization_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_signin._operations.signin.put_console_authorization_configuration.async_put_console_authorization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_signin.types.put_console_authorization_configuration_input.PutConsoleAuthorizationConfigurationInput = {}  # type: ignore[typeddict-item]
        if target_id is not None:
            input["target_id"] = target_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_resource_permission_statement(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        source_vpc: Optional["aws_sdk_signin.types.source_vpc.SourceVpc"] = None,
        signin_source_vpce: Optional[
            "aws_sdk_signin.types.source_vpce.SourceVpce"
        ] = None,
        console_source_vpce: Optional[
            "aws_sdk_signin.types.source_vpce.SourceVpce"
        ] = None,
        vpc_source_ip: Optional[
            "aws_sdk_signin.types.vpc_source_ip.VpcSourceIp"
        ] = None,
        source_ip: Optional["aws_sdk_signin.types.source_ip.SourceIp"] = None,
        requested_region: Optional[
            "aws_sdk_signin.types.requested_region.RequestedRegion"
        ] = None,
        excluded_principal: Optional[
            "aws_sdk_signin.types.excluded_principal.ExcludedPrincipal"
        ] = None,
        client_token: Optional["aws_sdk_signin.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_signin.types.put_resource_permission_statement_output.PutResourcePermissionStatementOutput":
        """Create a permission statement in the account's SignIn resource-based policy

        Args:
            source_vpc: VPC identifier to restrict console access
            signin_source_vpce: SignIn VPC endpoint identifier
            console_source_vpce: Console VPC endpoint identifier
            vpc_source_ip: Source IP address within VPC
            source_ip: Source IP address
            requested_region: AWS region where the VPC and VPC endpoint reside Required when sourceVpc or signinSourceVpce/consoleSourceVpce is provided
            excluded_principal: Principal to exclude from the permission statement
            client_token: Idempotency token for the request
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_signin.types.put_resource_permission_statement_input.PutResourcePermissionStatementInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_signin.types.put_resource_permission_statement_output.PutResourcePermissionStatementOutput"
        ]:
            import aws_sdk_signin._operations.signin.put_resource_permission_statement

            (
                output,
                http_response,
            ) = await aws_sdk_signin._operations.signin.put_resource_permission_statement.async_put_resource_permission_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_signin.types.put_resource_permission_statement_input.PutResourcePermissionStatementInput = {}  # type: ignore[typeddict-item]
        if source_vpc is not None:
            input["source_vpc"] = source_vpc
        if signin_source_vpce is not None:
            input["signin_source_vpce"] = signin_source_vpce
        if console_source_vpce is not None:
            input["console_source_vpce"] = console_source_vpce
        if vpc_source_ip is not None:
            input["vpc_source_ip"] = vpc_source_ip
        if source_ip is not None:
            input["source_ip"] = source_ip
        if requested_region is not None:
            input["requested_region"] = requested_region
        if excluded_principal is not None:
            input["excluded_principal"] = excluded_principal
        if client_token is not None:
            input["client_token"] = client_token

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
