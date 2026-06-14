"""Generated from Smithy shape ``com.amazonaws.securityir#SecurityIncidentResponse``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_security_ir._auth._signers
import aws_sdk_security_ir._auth._sigv4
from aws_sdk_security_ir._auth._identity import Credentials
from aws_sdk_security_ir._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_security_ir._auth._zapros_handler import AuthMiddleware
from aws_sdk_security_ir._resources.security_incident_response.case import Case
from aws_sdk_security_ir._resources.security_incident_response.membership import (
    Membership,
)
from aws_sdk_security_ir._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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


class SecurityIRClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class SecurityIRClient:
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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self.config = SecurityIRClientConfig(
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
        self.case = Case(self)
        self.membership = Membership(self)

    def operation_options(
        self, config_overrides: Optional[SecurityIRClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SecurityIRClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_security_ir.types.arn.Arn",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "aws_sdk_security_ir.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns currently configured tags on a resource.</p>

        Args:
            resource_arn: <p>Required element for ListTagsForResource to provide the ARN to identify a specific resource.</p>

        Examples:
            Invoke ListTagsForResource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:security-ir:us-west-1:123456789012:membership/m-abcd1234efgh')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_security_ir.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_security_ir.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_security_ir._operations.security_incident_response.list_tags_for_resource

            output, http_response = (
                aws_sdk_security_ir._operations.security_incident_response.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_security_ir.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_security_ir.types.arn.Arn",
        tags: "aws_sdk_security_ir.types.tag_map.TagMap",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "aws_sdk_security_ir.types.tag_resource_output.TagResourceOutput":
        """<p>Adds a tag(s) to a designated resource.</p>

        Args:
            resource_arn: <p>Required element for TagResource to identify the ARN for the resource to add a tag to.</p>
            tags: <p>Required element for ListTagsForResource to provide the content for a tag.</p>

        Examples:
            Invoke TagResource

            >>> client.tag_resource(resource_arn='arn:aws:security-ir:us-west-1:123456789012:membership/m-abcd1234efgh', tags={'key': 'example-tag-key', 'value': 'example-tag-value'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_security_ir.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_security_ir.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_security_ir._operations.security_incident_response.tag_resource

            output, http_response = (
                aws_sdk_security_ir._operations.security_incident_response.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_security_ir.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_security_ir.types.arn.Arn",
        tag_keys: "aws_sdk_security_ir.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[SecurityIRClientConfig] = None,
    ) -> "aws_sdk_security_ir.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a tag(s) from a designate resource.</p>

        Args:
            resource_arn: <p>Required element for UnTagResource to identify the ARN for the resource to remove a tag from.</p>
            tag_keys: <p>Required element for UnTagResource to identify tag to remove.</p>

        Examples:
            Invoke UntagResource

            >>> client.untag_resource(resource_arn='arn:aws:security-ir:us-west-1:123456789012:membership/m-abcd1234efgh', tag_keys=['example-tag-key'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_security_ir.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_security_ir.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_security_ir._operations.security_incident_response.untag_resource

            output, http_response = (
                aws_sdk_security_ir._operations.security_incident_response.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_security_ir.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
