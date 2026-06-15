"""Generated from Smithy shape ``com.amazonaws.securityir#SecurityIncidentResponse``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_security_ir._auth._signers
import aws_sdk_security_ir._auth._sigv4
from aws_sdk_security_ir._auth._identity import Credentials
from aws_sdk_security_ir._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_security_ir._auth._zapros_handler import AuthMiddleware
from aws_sdk_security_ir._resources.security_incident_response.case import AsyncCase
from aws_sdk_security_ir._resources.security_incident_response.membership import (
    AsyncMembership,
)
from aws_sdk_security_ir._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.arn
    import aws_sdk_security_ir.types.list_tags_for_resource_input
    import aws_sdk_security_ir.types.list_tags_for_resource_output
    import aws_sdk_security_ir.types.tag_keys
    import aws_sdk_security_ir.types.tag_map
    import aws_sdk_security_ir.types.tag_resource_input
    import aws_sdk_security_ir.types.tag_resource_output
    import aws_sdk_security_ir.types.untag_resource_input
    import aws_sdk_security_ir.types.untag_resource_output


class AsyncSecurityIRClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncSecurityIRClient:
    """A client for the ``SecurityIR`` service.

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
        self._config = AsyncSecurityIRClientConfig(
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

        # resources
        self.case = AsyncCase(self)
        self.membership = AsyncMembership(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSecurityIRClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSecurityIRClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_security_ir.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "aws_sdk_security_ir.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns currently configured tags on a resource.</p>

        Args:
            resource_arn: <p>Required element for ListTagsForResource to provide the ARN to identify a specific resource.</p>

        Examples:
            Invoke ListTagsForResource

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:security-ir:us-west-1:123456789012:membership/m-abcd1234efgh')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_security_ir.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_security_ir.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_security_ir._operations.security_incident_response.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_security_ir._operations.security_incident_response.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_security_ir.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_security_ir.types.arn.Arn",
        tags: "aws_sdk_security_ir.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "aws_sdk_security_ir.types.tag_resource_output.TagResourceOutput":
        """<p>Adds a tag(s) to a designated resource.</p>

        Args:
            resource_arn: <p>Required element for TagResource to identify the ARN for the resource to add a tag to.</p>
            tags: <p>Required element for ListTagsForResource to provide the content for a tag.</p>

        Examples:
            Invoke TagResource

            >>> await client.tag_resource(resource_arn='arn:aws:security-ir:us-west-1:123456789012:membership/m-abcd1234efgh', tags={'key': 'example-tag-key', 'value': 'example-tag-value'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_security_ir.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_security_ir.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_security_ir._operations.security_incident_response.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_security_ir._operations.security_incident_response.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_security_ir.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_security_ir.types.arn.Arn",
        tag_keys: "aws_sdk_security_ir.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncSecurityIRClientConfig] = None,
    ) -> "aws_sdk_security_ir.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a tag(s) from a designate resource.</p>

        Args:
            resource_arn: <p>Required element for UnTagResource to identify the ARN for the resource to remove a tag from.</p>
            tag_keys: <p>Required element for UnTagResource to identify tag to remove.</p>

        Examples:
            Invoke UntagResource

            >>> await client.untag_resource(resource_arn='arn:aws:security-ir:us-west-1:123456789012:membership/m-abcd1234efgh', tag_keys=['example-tag-key'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_security_ir.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_security_ir.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_security_ir._operations.security_incident_response.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_security_ir._operations.security_incident_response.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_security_ir.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
