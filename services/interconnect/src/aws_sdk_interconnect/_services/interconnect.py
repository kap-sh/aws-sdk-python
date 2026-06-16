"""Generated from Smithy shape ``com.amazonaws.interconnect#Interconnect``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_interconnect._auth._signers
import aws_sdk_interconnect._auth._sigv4
from aws_sdk_interconnect._auth._identity import Credentials
from aws_sdk_interconnect._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_interconnect._auth._zapros_handler import AuthMiddleware
from aws_sdk_interconnect._pagination import resolve_path as _resolve_path
from aws_sdk_interconnect._resources.interconnect.connection_resource import (
    ConnectionResource,
)
from aws_sdk_interconnect._resources.interconnect.environment_resource import (
    EnvironmentResource,
)
from aws_sdk_interconnect._services._aws_config import aws_config
from aws_sdk_interconnect._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.accept_connection_proposal_request
    import aws_sdk_interconnect.types.accept_connection_proposal_response
    import aws_sdk_interconnect.types.activation_key
    import aws_sdk_interconnect.types.amazon_resource_name
    import aws_sdk_interconnect.types.attach_point
    import aws_sdk_interconnect.types.attach_point_descriptor
    import aws_sdk_interconnect.types.connection_description
    import aws_sdk_interconnect.types.describe_connection_proposal_request
    import aws_sdk_interconnect.types.describe_connection_proposal_response
    import aws_sdk_interconnect.types.environment_id
    import aws_sdk_interconnect.types.list_attach_points_request
    import aws_sdk_interconnect.types.list_attach_points_response
    import aws_sdk_interconnect.types.list_tags_for_resource_request
    import aws_sdk_interconnect.types.list_tags_for_resource_response
    import aws_sdk_interconnect.types.max_results
    import aws_sdk_interconnect.types.next_token
    import aws_sdk_interconnect.types.tag_key_list
    import aws_sdk_interconnect.types.tag_map
    import aws_sdk_interconnect.types.tag_resource_request
    import aws_sdk_interconnect.types.tag_resource_response
    import aws_sdk_interconnect.types.untag_resource_request
    import aws_sdk_interconnect.types.untag_resource_response


class InterconnectClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class InterconnectClient:
    """A client for the ``Interconnect`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = InterconnectClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.connection_resource = ConnectionResource(self)
        self.environment_resource = EnvironmentResource(self)

    def operation_options(
        self, config_overrides: Optional[InterconnectClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: InterconnectClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def accept_connection_proposal(
        self,
        attach_point: "aws_sdk_interconnect.types.attach_point.AttachPoint",
        activation_key: "aws_sdk_interconnect.types.activation_key.ActivationKey",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
        description: Optional[
            "aws_sdk_interconnect.types.connection_description.ConnectionDescription"
        ] = None,
        tags: Optional["aws_sdk_interconnect.types.tag_map.TagMap"] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_interconnect.types.accept_connection_proposal_response.AcceptConnectionProposalResponse":
        """<p>Accepts a connection proposal which was generated at a supported partner's portal.</p> <p>The proposal contains the Environment and bandwidth that were chosen on the partner's portal and cannot be modified.</p> <p>Upon accepting the proposal a connection will be made between the AWS network as accessed via the selected Attach Point and the network previously selected network on the partner's portal.</p>

        Args:
            attach_point: <p>The Attach Point to which the connection should be associated.</p>
            activation_key: <p>An Activation Key that was generated on a supported partner's portal. This key captures the desired parameters from the initial creation request.</p> <p>The details of this request can be described using with <a>DescribeConnectionProposal</a>. </p>
            description: <p>A description to distinguish this <a>Connection</a>.</p>
            tags: <p>The tags to associate with the resulting <a>Connection</a>.</p>
            client_token: <p>Idempotency token used for the request.</p>

        Examples:
            Accept Connection Proposal

            >>> client.accept_connection_proposal(activation_key='<Activation Key Data>', attach_point={'directConnectGateway': '90392BE3-219C-47FD-BBA5-03DF76D2542A'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_interconnect.types.accept_connection_proposal_request.AcceptConnectionProposalRequest]",
        ) -> OperationResponse[
            "aws_sdk_interconnect.types.accept_connection_proposal_response.AcceptConnectionProposalResponse"
        ]:
            import aws_sdk_interconnect._operations.interconnect.accept_connection_proposal

            output, http_response = (
                aws_sdk_interconnect._operations.interconnect.accept_connection_proposal.accept_connection_proposal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_interconnect.types.accept_connection_proposal_request.AcceptConnectionProposalRequest = {}  # type: ignore[typeddict-item]
        input_["attach_point"] = attach_point
        input_["activation_key"] = activation_key
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_connection_proposal(
        self,
        activation_key: "aws_sdk_interconnect.types.activation_key.ActivationKey",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
    ) -> "aws_sdk_interconnect.types.describe_connection_proposal_response.DescribeConnectionProposalResponse":
        """<p>Describes the details of a connection proposal generated at a partner's portal.</p>

        Args:
            activation_key: <p>An Activation Key that was generated on a supported partner's portal. This key captures the desired parameters from the initial creation request.</p>

        Examples:
            Describe Connection Proposal

            >>> client.describe_connection_proposal(activation_key='<Activation Key Data>')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_interconnect.types.describe_connection_proposal_request.DescribeConnectionProposalRequest]",
        ) -> OperationResponse[
            "aws_sdk_interconnect.types.describe_connection_proposal_response.DescribeConnectionProposalResponse"
        ]:
            import aws_sdk_interconnect._operations.interconnect.describe_connection_proposal

            output, http_response = (
                aws_sdk_interconnect._operations.interconnect.describe_connection_proposal.describe_connection_proposal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_interconnect.types.describe_connection_proposal_request.DescribeConnectionProposalRequest = {}  # type: ignore[typeddict-item]
        input_["activation_key"] = activation_key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_attach_points(
        self,
        environment_id: "aws_sdk_interconnect.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_interconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_interconnect.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_interconnect.types.list_attach_points_response.ListAttachPointsResponse":
        """<p>Lists all Attach Points the caller has access to that are valid for the specified <a>Environment</a>.</p>

        Args:
            environment_id: <p>The identifier of the <a>Environment</a> for which to list valid Attach Points.</p>
            max_results: <p>The max number of list results in a single paginated response.</p>
            next_token: <p>A pagination token from a previous paginated response indicating you wish to get the next page.</p>

        Examples:
            List Attach Points

            >>> client.list_attach_points(environment_id='mce-aws-acme-1')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_interconnect.types.list_attach_points_request.ListAttachPointsRequest]",
        ) -> OperationResponse[
            "aws_sdk_interconnect.types.list_attach_points_response.ListAttachPointsResponse"
        ]:
            import aws_sdk_interconnect._operations.interconnect.list_attach_points

            output, http_response = (
                aws_sdk_interconnect._operations.interconnect.list_attach_points.list_attach_points(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_interconnect.types.list_attach_points_request.ListAttachPointsRequest = {}  # type: ignore[typeddict-item]
        input_["environment_id"] = environment_id
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

    def iter_list_attach_points(
        self,
        environment_id: "aws_sdk_interconnect.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_interconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_interconnect.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_interconnect.types.attach_point_descriptor.AttachPointDescriptor]":
        _token = next_token
        while True:
            _response = self.list_attach_points(
                environment_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("attach_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        arn: "aws_sdk_interconnect.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
    ) -> "aws_sdk_interconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all current tags on the specified resource. Currently this supports <a>Connection</a> resources. </p>

        Args:
            arn: <p>The resource ARN for which to list tags. </p>

        Examples:
            List Tags

            >>> client.list_tags_for_resource(arn='arn:aws:interconnect:us-east-1:000000000000:connection/mcc-abc12345')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_interconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_interconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_interconnect._operations.interconnect.list_tags_for_resource

            output, http_response = (
                aws_sdk_interconnect._operations.interconnect.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_interconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        arn: "aws_sdk_interconnect.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_interconnect.types.tag_map.TagMap",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
    ) -> "aws_sdk_interconnect.types.tag_resource_response.TagResourceResponse":
        """<p>Add new tags to the specified resource.</p>

        Args:
            arn: <p>The ARN of the resource that should receive the new tags.</p>
            tags: <p>A map of tags to apply to the specified resource.</p>

        Examples:
            Apply Tags

            >>> client.tag_resource(arn='arn:aws:interconnect:us-east-1:000000000000:connection/mcc-abc12345', tags={'TagKey1': 'TagValue1', 'TagKey2': 'TagValue2'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_interconnect.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_interconnect.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_interconnect._operations.interconnect.tag_resource

            output, http_response = (
                aws_sdk_interconnect._operations.interconnect.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_interconnect.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        arn: "aws_sdk_interconnect.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_interconnect.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
    ) -> "aws_sdk_interconnect.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the specified resource.</p>

        Args:
            arn: <p>The ARN of the resource from which the specified tags should be removed.</p>
            tag_keys: <p>The list of tag keys that should be removed from the resource.</p>

        Examples:
            Remove Tags

            >>> client.untag_resource(arn='arn:aws:interconnect:us-east-1:000000000000:connection/mcc-abc12345', tag_keys=['TagKey1', 'TagKey2'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_interconnect.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_interconnect.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_interconnect._operations.interconnect.untag_resource

            output, http_response = (
                aws_sdk_interconnect._operations.interconnect.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_interconnect.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
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
