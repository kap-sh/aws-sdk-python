"""Generated from Smithy shape ``com.amazonaws.uxc#AWSAccountUXSetting``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_uxc._auth._signers
import aws_sdk_uxc._auth._sigv4
from aws_sdk_uxc._auth._identity import Credentials
from aws_sdk_uxc._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_uxc._auth._zapros_handler import AuthMiddleware
from aws_sdk_uxc._pagination import resolve_path as _resolve_path
from aws_sdk_uxc._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_uxc.types.account_color
    import aws_sdk_uxc.types.get_account_customizations_input
    import aws_sdk_uxc.types.get_account_customizations_output
    import aws_sdk_uxc.types.list_services_input
    import aws_sdk_uxc.types.list_services_output
    import aws_sdk_uxc.types.max_results
    import aws_sdk_uxc.types.next_token
    import aws_sdk_uxc.types.regions_list
    import aws_sdk_uxc.types.service
    import aws_sdk_uxc.types.service_list
    import aws_sdk_uxc.types.update_account_customizations_input
    import aws_sdk_uxc.types.update_account_customizations_output


class AsyncuxcClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
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


class AsyncuxcClient:
    """A client for the ``uxc`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
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
        self.config = AsyncuxcClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncuxcClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncuxcClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def get_account_customizations(
        self, *, config_overrides: Optional[AsyncuxcClientConfig] = None
    ) -> "aws_sdk_uxc.types.get_account_customizations_output.GetAccountCustomizationsOutput":
        """<p>Returns the current account customization settings, including account color, visible services, and visible Regions. Settings that you have not configured return their default values: visible Regions and visible services return `null`, and account color returns `none`.</p> <note> <p>The <code>visibleServices</code> and <code>visibleRegions</code> settings control only the appearance of services and Regions in the Amazon Web Services Management Console. They do not restrict access through the CLI, SDKs, or other APIs.</p> </note>

        Examples:
            Get account customizations
            Retrieves all account customization settings

            >>> await client.get_account_customizations()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_uxc.types.get_account_customizations_input.GetAccountCustomizationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_uxc.types.get_account_customizations_output.GetAccountCustomizationsOutput"
        ]:
            import aws_sdk_uxc._operations.aws_account_ux_setting.get_account_customizations

            (
                output,
                http_response,
            ) = await aws_sdk_uxc._operations.aws_account_ux_setting.get_account_customizations.async_get_account_customizations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_uxc.types.get_account_customizations_input.GetAccountCustomizationsInput = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_services(
        self,
        *,
        config_overrides: Optional[AsyncuxcClientConfig] = None,
        next_token: Optional["aws_sdk_uxc.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_uxc.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_uxc.types.list_services_output.ListServicesOutput":
        """<p>Returns a paginated list of Amazon Web Services service identifiers that you can use as values for the <code>visibleServices</code> setting in <a href=\"https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_UpdateAccountCustomizations.html\">UpdateAccountCustomizations</a>. The available services vary by Amazon Web Services partition. Use pagination to retrieve all results.</p> <note> <p>The <code>visibleServices</code> setting controls only the appearance of services in the Amazon Web Services Management Console. It does not restrict access through the CLI, SDKs, or other APIs.</p> </note>

        Args:
            next_token: <p>The token for retrieving the next page of results. Use the <code>nextToken</code> value from a previous response.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Examples:
            List available services
            Retrieves a paginated list of available AWS services

            >>> await client.list_services()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_uxc.types.list_services_input.ListServicesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_uxc.types.list_services_output.ListServicesOutput"
        ]:
            import aws_sdk_uxc._operations.aws_account_ux_setting.list_services

            (
                output,
                http_response,
            ) = await aws_sdk_uxc._operations.aws_account_ux_setting.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_uxc.types.list_services_input.ListServicesInput = {}  # type: ignore[typeddict-item]
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

    async def iter_list_services(
        self,
        *,
        config_overrides: Optional[AsyncuxcClientConfig] = None,
        next_token: Optional["aws_sdk_uxc.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_uxc.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_uxc.types.service.Service]":
        _token = next_token
        while True:
            _response = await self.list_services(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_account_customizations(
        self,
        *,
        config_overrides: Optional[AsyncuxcClientConfig] = None,
        account_color: Optional["aws_sdk_uxc.types.account_color.AccountColor"] = None,
        visible_services: Optional["aws_sdk_uxc.types.service_list.ServiceList"] = None,
        visible_regions: Optional["aws_sdk_uxc.types.regions_list.RegionsList"] = None,
    ) -> "aws_sdk_uxc.types.update_account_customizations_output.UpdateAccountCustomizationsOutput":
        """<p>Updates one or more account customization settings. You can update account color, visible services, and visible Regions in a single request. Only the settings that you include in the request body are modified. Omitted settings remain unchanged. To reset a setting to its default behavior, set the value to <code>null</code> for visible Regions and visible services, or <code>none</code> for account color. This operation is idempotent.</p> <note> <p>The <code>visibleServices</code> and <code>visibleRegions</code> settings control only the appearance of services and Regions in the Amazon Web Services Management Console. They do not restrict access through the CLI, SDKs, or other APIs.</p> </note>

        Args:
            account_color: <p>The account color preference to set. Set to <code>none</code> to reset to the default (no color).</p>
            visible_services: <p>The list of Amazon Web Services service identifiers to make visible in the Amazon Web Services Management Console. Set to <code>null</code> to reset to the default, which makes all services visible. For valid service identifiers, call <a href=\"https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_ListServices.html\">ListServices</a>.</p>
            visible_regions: <p>The list of Amazon Web Services Region codes to make visible in the Amazon Web Services Management Console. Set to <code>null</code> to reset to the default, which makes all Regions visible. For a list of valid Region codes, see <a href=\"https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html\">Amazon Web Services Regions</a>.</p>

        Examples:
            Update account customizations
            Updates account customization settings with new values

            >>> await client.update_account_customizations(account_color='green', visible_services=['s3', 'ec2', 'lambda'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_uxc.types.update_account_customizations_input.UpdateAccountCustomizationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_uxc.types.update_account_customizations_output.UpdateAccountCustomizationsOutput"
        ]:
            import aws_sdk_uxc._operations.aws_account_ux_setting.update_account_customizations

            (
                output,
                http_response,
            ) = await aws_sdk_uxc._operations.aws_account_ux_setting.update_account_customizations.async_update_account_customizations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_uxc.types.update_account_customizations_input.UpdateAccountCustomizationsInput = {}  # type: ignore[typeddict-item]
        if account_color is not None:
            input_["account_color"] = account_color
        if visible_services is not None:
            input_["visible_services"] = visible_services
        if visible_regions is not None:
            input_["visible_regions"] = visible_regions

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
