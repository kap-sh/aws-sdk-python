"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#AWSMigrationHubMultiAccountService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_migrationhub_config._auth._signers
import aws_sdk_migrationhub_config._auth._sigv4
from aws_sdk_migrationhub_config._auth._identity import Credentials
from aws_sdk_migrationhub_config._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_migrationhub_config._auth._zapros_handler import AuthMiddleware
from aws_sdk_migrationhub_config._services._aws_config import aws_config
from aws_sdk_migrationhub_config._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_migrationhub_config.types.control_id
    import aws_sdk_migrationhub_config.types.create_home_region_control_request
    import aws_sdk_migrationhub_config.types.create_home_region_control_result
    import aws_sdk_migrationhub_config.types.delete_home_region_control_request
    import aws_sdk_migrationhub_config.types.delete_home_region_control_result
    import aws_sdk_migrationhub_config.types.describe_home_region_controls_max_results
    import aws_sdk_migrationhub_config.types.describe_home_region_controls_request
    import aws_sdk_migrationhub_config.types.describe_home_region_controls_result
    import aws_sdk_migrationhub_config.types.dry_run
    import aws_sdk_migrationhub_config.types.get_home_region_request
    import aws_sdk_migrationhub_config.types.get_home_region_result
    import aws_sdk_migrationhub_config.types.home_region
    import aws_sdk_migrationhub_config.types.target
    import aws_sdk_migrationhub_config.types.token


class MigrationHubConfigClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class MigrationHubConfigClient:
    """A client for the ``MigrationHubConfig`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = MigrationHubConfigClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[MigrationHubConfigClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MigrationHubConfigClientConfig = config_overrides or {}
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

    def create_home_region_control(
        self,
        home_region: "aws_sdk_migrationhub_config.types.home_region.HomeRegion",
        target: "aws_sdk_migrationhub_config.types.target.Target",
        *,
        config_overrides: Optional[MigrationHubConfigClientConfig] = None,
        dry_run: Optional["aws_sdk_migrationhub_config.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migrationhub_config.types.create_home_region_control_result.CreateHomeRegionControlResult":
        """<p>This API sets up the home region for the calling account only.</p>

        Args:
            home_region: <p>The name of the home region of the calling account.</p>
            target: <p>The account for which this command sets up a home region control. The <code>Target</code> is always of type <code>ACCOUNT</code>.</p>
            dry_run: <p>Optional Boolean flag to indicate whether any effect should take place. It tests whether the caller has permission to make the call.</p>

        Raises:
            aws_sdk_migrationhub_config.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhub_config.errors.dry_run_operation.DryRunOperation: <p>Exception raised to indicate that authorization of an action was successful, when the <code>DryRun</code> flag is set to true.</p>
            aws_sdk_migrationhub_config.errors.internal_server_error.InternalServerError: <p>Exception raised when an internal, configuration, or dependency error is encountered.</p>
            aws_sdk_migrationhub_config.errors.invalid_input_exception.InvalidInputException: <p>Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type.</p>
            aws_sdk_migrationhub_config.errors.service_unavailable_exception.ServiceUnavailableException: <p>Exception raised when a request fails due to temporary unavailability of the service.</p>
            aws_sdk_migrationhub_config.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhub_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhub_config.types.create_home_region_control_request.CreateHomeRegionControlRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhub_config.types.create_home_region_control_result.CreateHomeRegionControlResult"
        ]:
            import aws_sdk_migrationhub_config._operations.aws_migration_hub_multi_account_service.create_home_region_control

            output, http_response = (
                aws_sdk_migrationhub_config._operations.aws_migration_hub_multi_account_service.create_home_region_control.create_home_region_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migrationhub_config.types.create_home_region_control_request.CreateHomeRegionControlRequest = {}  # type: ignore[typeddict-item]
        input_["home_region"] = home_region
        input_["target"] = target
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_home_region_control(
        self,
        control_id: "aws_sdk_migrationhub_config.types.control_id.ControlId",
        *,
        config_overrides: Optional[MigrationHubConfigClientConfig] = None,
    ) -> "aws_sdk_migrationhub_config.types.delete_home_region_control_result.DeleteHomeRegionControlResult":
        r"""<p>This operation deletes the home region configuration for the calling account. The operation does not delete discovery or migration tracking data in the home region.</p>

        Args:
            control_id: <p>A unique identifier that's generated for each home region control. It's always a string that begins with \"hrc-\" followed by 12 lowercase letters and numbers.</p>

        Raises:
            aws_sdk_migrationhub_config.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhub_config.errors.internal_server_error.InternalServerError: <p>Exception raised when an internal, configuration, or dependency error is encountered.</p>
            aws_sdk_migrationhub_config.errors.invalid_input_exception.InvalidInputException: <p>Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type.</p>
            aws_sdk_migrationhub_config.errors.service_unavailable_exception.ServiceUnavailableException: <p>Exception raised when a request fails due to temporary unavailability of the service.</p>
            aws_sdk_migrationhub_config.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhub_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhub_config.types.delete_home_region_control_request.DeleteHomeRegionControlRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhub_config.types.delete_home_region_control_result.DeleteHomeRegionControlResult"
        ]:
            import aws_sdk_migrationhub_config._operations.aws_migration_hub_multi_account_service.delete_home_region_control

            output, http_response = (
                aws_sdk_migrationhub_config._operations.aws_migration_hub_multi_account_service.delete_home_region_control.delete_home_region_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migrationhub_config.types.delete_home_region_control_request.DeleteHomeRegionControlRequest = {}  # type: ignore[typeddict-item]
        input_["control_id"] = control_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_home_region_controls(
        self,
        *,
        config_overrides: Optional[MigrationHubConfigClientConfig] = None,
        control_id: Optional[
            "aws_sdk_migrationhub_config.types.control_id.ControlId"
        ] = None,
        home_region: Optional[
            "aws_sdk_migrationhub_config.types.home_region.HomeRegion"
        ] = None,
        target: Optional["aws_sdk_migrationhub_config.types.target.Target"] = None,
        max_results: Optional[
            "aws_sdk_migrationhub_config.types.describe_home_region_controls_max_results.DescribeHomeRegionControlsMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_migrationhub_config.types.token.Token"] = None,
    ) -> "aws_sdk_migrationhub_config.types.describe_home_region_controls_result.DescribeHomeRegionControlsResult":
        """<p>This API permits filtering on the <code>ControlId</code> and <code>HomeRegion</code> fields.</p>

        Args:
            control_id: <p>The <code>ControlID</code> is a unique identifier string of your <code>HomeRegionControl</code> object.</p>
            home_region: <p>The name of the home region you'd like to view.</p>
            target: <p>The target parameter specifies the identifier to which the home region is applied, which is always of type <code>ACCOUNT</code>. It applies the home region to the current <code>ACCOUNT</code>.</p>
            max_results: <p>The maximum number of filtering results to display per page. </p>
            next_token: <p>If a <code>NextToken</code> was returned by a previous call, more results are available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>

        Raises:
            aws_sdk_migrationhub_config.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhub_config.errors.internal_server_error.InternalServerError: <p>Exception raised when an internal, configuration, or dependency error is encountered.</p>
            aws_sdk_migrationhub_config.errors.invalid_input_exception.InvalidInputException: <p>Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type.</p>
            aws_sdk_migrationhub_config.errors.service_unavailable_exception.ServiceUnavailableException: <p>Exception raised when a request fails due to temporary unavailability of the service.</p>
            aws_sdk_migrationhub_config.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhub_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhub_config.types.describe_home_region_controls_request.DescribeHomeRegionControlsRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhub_config.types.describe_home_region_controls_result.DescribeHomeRegionControlsResult"
        ]:
            import aws_sdk_migrationhub_config._operations.aws_migration_hub_multi_account_service.describe_home_region_controls

            output, http_response = (
                aws_sdk_migrationhub_config._operations.aws_migration_hub_multi_account_service.describe_home_region_controls.describe_home_region_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migrationhub_config.types.describe_home_region_controls_request.DescribeHomeRegionControlsRequest = {}  # type: ignore[typeddict-item]
        if control_id is not None:
            input_["control_id"] = control_id
        if home_region is not None:
            input_["home_region"] = home_region
        if target is not None:
            input_["target"] = target
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_home_region(
        self, *, config_overrides: Optional[MigrationHubConfigClientConfig] = None
    ) -> "aws_sdk_migrationhub_config.types.get_home_region_result.GetHomeRegionResult":
        """<p>Returns the calling account’s home region, if configured. This API is used by other AWS services to determine the regional endpoint for calling AWS Application Discovery Service and Migration Hub. You must call <code>GetHomeRegion</code> at least once before you call any other AWS Application Discovery Service and AWS Migration Hub APIs, to obtain the account's Migration Hub home region.</p>

        Raises:
            aws_sdk_migrationhub_config.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_migrationhub_config.errors.internal_server_error.InternalServerError: <p>Exception raised when an internal, configuration, or dependency error is encountered.</p>
            aws_sdk_migrationhub_config.errors.invalid_input_exception.InvalidInputException: <p>Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type.</p>
            aws_sdk_migrationhub_config.errors.service_unavailable_exception.ServiceUnavailableException: <p>Exception raised when a request fails due to temporary unavailability of the service.</p>
            aws_sdk_migrationhub_config.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_migrationhub_config.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhub_config.types.get_home_region_request.GetHomeRegionRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhub_config.types.get_home_region_result.GetHomeRegionResult"
        ]:
            import aws_sdk_migrationhub_config._operations.aws_migration_hub_multi_account_service.get_home_region

            output, http_response = (
                aws_sdk_migrationhub_config._operations.aws_migration_hub_multi_account_service.get_home_region.get_home_region(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migrationhub_config.types.get_home_region_request.GetHomeRegionRequest = {}  # type: ignore[typeddict-item]

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
