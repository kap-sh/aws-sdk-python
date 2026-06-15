"""Generated from Smithy shape ``com.amazonaws.inspectorscan#InspectorScan``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_inspector_scan._auth._signers
import aws_sdk_inspector_scan._auth._sigv4
from aws_sdk_inspector_scan._auth._identity import Credentials
from aws_sdk_inspector_scan._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_inspector_scan._auth._zapros_handler import AuthMiddleware
from aws_sdk_inspector_scan._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_inspector_scan.types.output_format
    import aws_sdk_inspector_scan.types.sbom
    import aws_sdk_inspector_scan.types.scan_sbom_request
    import aws_sdk_inspector_scan.types.scan_sbom_response


class AsyncInspectorScanClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
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


class AsyncInspectorScanClient:
    """A client for the ``InspectorScan`` service.

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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncInspectorScanClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncInspectorScanClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncInspectorScanClientConfig = config_overrides or {}
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

    async def scan_sbom(
        self,
        sbom: "aws_sdk_inspector_scan.types.sbom.Sbom",
        *,
        config_overrides: Optional[AsyncInspectorScanClientConfig] = None,
        output_format: Optional[
            "aws_sdk_inspector_scan.types.output_format.OutputFormat"
        ] = None,
    ) -> "aws_sdk_inspector_scan.types.scan_sbom_response.ScanSbomResponse":
        r"""<p>Scans a provided CycloneDX 1.5 SBOM and reports on any vulnerabilities discovered in that SBOM. You can generate compatible SBOMs for your resources using the <a href=\"https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html\">Amazon Inspector SBOM generator</a>.</p> <note> <p> The output of this action reports NVD and CVSS scores when NVD and CVSS scores are available. Because the output reports both scores, you might notice a discrepency between them. However, you can triage the severity of either score depending on the vendor of your choosing. </p> </note>

        Args:
            sbom: <p>The JSON file for the SBOM you want to scan. The SBOM must be in CycloneDX 1.5 format. This format limits you to passing 2000 components before throwing a <code>ValidException</code> error.</p>
            output_format: <p>The output format for the vulnerability report.</p>

        Examples:
            Sample ScanSbom Call

            >>> await client.scan_sbom(output_format='CYCLONE_DX_1_5', sbom={'bomFormat': 'CycloneDX', 'specVersion': '1.5', 'components': [{'type': 'library', 'name': 'log4j-core', 'purl': 'pkg:maven/org.apache.logging.log4j/log4j-core@2.17.0'}]})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_inspector_scan.types.scan_sbom_request.ScanSbomRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_inspector_scan.types.scan_sbom_response.ScanSbomResponse"
        ]:
            import aws_sdk_inspector_scan._operations.inspector_scan.scan_sbom

            (
                output,
                http_response,
            ) = await aws_sdk_inspector_scan._operations.inspector_scan.scan_sbom.async_scan_sbom(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector_scan.types.scan_sbom_request.ScanSbomRequest = {}  # type: ignore[typeddict-item]
        input_["sbom"] = sbom
        if output_format is not None:
            input_["output_format"] = output_format

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
