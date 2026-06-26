"""Generated from Smithy shape ``com.amazonaws.mpa#AWSFluffyCoreService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_mpa._auth._signers
import aws_sdk_mpa._auth._sigv4
from aws_sdk_mpa._auth._identity import Credentials
from aws_sdk_mpa._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_mpa._auth._zapros_handler import AuthMiddleware
from aws_sdk_mpa._pagination import resolve_path as _resolve_path
from aws_sdk_mpa._resources.aws_fluffy_core_service.approval_team import (
    AsyncApprovalTeam,
)
from aws_sdk_mpa._resources.aws_fluffy_core_service.identity_source import (
    AsyncIdentitySource,
)
from aws_sdk_mpa._resources.aws_fluffy_core_service.session import AsyncSession
from aws_sdk_mpa._services._aws_config import aaws_config
from aws_sdk_mpa._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_mpa.types.get_policy_version_request
    import aws_sdk_mpa.types.get_policy_version_response
    import aws_sdk_mpa.types.get_resource_policy_request
    import aws_sdk_mpa.types.get_resource_policy_response
    import aws_sdk_mpa.types.list_policies_request
    import aws_sdk_mpa.types.list_policies_response
    import aws_sdk_mpa.types.list_policy_versions_request
    import aws_sdk_mpa.types.list_policy_versions_response
    import aws_sdk_mpa.types.list_resource_policies_request
    import aws_sdk_mpa.types.list_resource_policies_response
    import aws_sdk_mpa.types.list_resource_policies_response_resource_policy
    import aws_sdk_mpa.types.list_tags_for_resource_request
    import aws_sdk_mpa.types.list_tags_for_resource_response
    import aws_sdk_mpa.types.max_results
    import aws_sdk_mpa.types.policy
    import aws_sdk_mpa.types.policy_type
    import aws_sdk_mpa.types.policy_version_summary
    import aws_sdk_mpa.types.qualified_policy_arn
    import aws_sdk_mpa.types.string
    import aws_sdk_mpa.types.tag_key_list
    import aws_sdk_mpa.types.tag_resource_request
    import aws_sdk_mpa.types.tag_resource_response
    import aws_sdk_mpa.types.tags
    import aws_sdk_mpa.types.token
    import aws_sdk_mpa.types.unqualified_policy_arn
    import aws_sdk_mpa.types.untag_resource_request
    import aws_sdk_mpa.types.untag_resource_response


class AsyncMPAClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncMPAClient:
    """A client for the ``MPA`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncMPAClientConfig(
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
        self.approval_team = AsyncApprovalTeam(self)
        self.identity_source = AsyncIdentitySource(self)
        self.session = AsyncSession(self)

    def operation_options(
        self, config_overrides: Optional[AsyncMPAClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMPAClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def get_policy_version(
        self,
        policy_version_arn: "aws_sdk_mpa.types.qualified_policy_arn.QualifiedPolicyArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "aws_sdk_mpa.types.get_policy_version_response.GetPolicyVersionResponse":
        """<p>Returns details for the version of a policy. Policies define the permissions for team resources.</p>

        Args:
            policy_version_arn: <p>Amazon Resource Name (ARN) for the policy.</p>

        Raises:
            aws_sdk_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            aws_sdk_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            aws_sdk_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            aws_sdk_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.get_policy_version_request.GetPolicyVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.get_policy_version_response.GetPolicyVersionResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.get_policy_version

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.get_policy_version.async_get_policy_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.get_policy_version_request.GetPolicyVersionRequest = {}  # type: ignore[typeddict-item]
        input_["policy_version_arn"] = policy_version_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "aws_sdk_mpa.types.string.String",
        policy_name: "aws_sdk_mpa.types.string.String",
        policy_type: "aws_sdk_mpa.types.policy_type.PolicyType",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "aws_sdk_mpa.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Returns details about a policy for a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>
            policy_name: <p>Name of the policy.</p>
            policy_type: <p>The type of policy.</p>

        Raises:
            aws_sdk_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            aws_sdk_mpa.errors.invalid_parameter_exception.InvalidParameterException: <p>The request contains an invalid parameter value.</p>
            aws_sdk_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            aws_sdk_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["policy_name"] = policy_name
        input_["policy_type"] = policy_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_policies(
        self,
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["aws_sdk_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
    ) -> "aws_sdk_mpa.types.list_policies_response.ListPoliciesResponse":
        """<p>Returns a list of policies. Policies define the permissions for team resources.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>

        Raises:
            aws_sdk_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            aws_sdk_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            aws_sdk_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.list_policies_request.ListPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.list_policies_response.ListPoliciesResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.list_policies

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.list_policies.async_list_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.list_policies_request.ListPoliciesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_policies(
        self,
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["aws_sdk_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
    ) -> "AsyncIterator[aws_sdk_mpa.types.policy.Policy]":
        _token = next_token
        while True:
            _response = await self.list_policies(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_policy_versions(
        self,
        policy_arn: "aws_sdk_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["aws_sdk_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
    ) -> "aws_sdk_mpa.types.list_policy_versions_response.ListPolicyVersionsResponse":
        """<p>Returns a list of the versions for policies. Policies define the permissions for team resources.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>
            policy_arn: <p>Amazon Resource Name (ARN) for the policy.</p>

        Raises:
            aws_sdk_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            aws_sdk_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            aws_sdk_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            aws_sdk_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.list_policy_versions_request.ListPolicyVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.list_policy_versions_response.ListPolicyVersionsResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.list_policy_versions

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.list_policy_versions.async_list_policy_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.list_policy_versions_request.ListPolicyVersionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["policy_arn"] = policy_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_policy_versions(
        self,
        policy_arn: "aws_sdk_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["aws_sdk_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
    ) -> "AsyncIterator[aws_sdk_mpa.types.policy_version_summary.PolicyVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_policy_versions(
                policy_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("policy_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_policies(
        self,
        resource_arn: "aws_sdk_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["aws_sdk_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
    ) -> (
        "aws_sdk_mpa.types.list_resource_policies_response.ListResourcePoliciesResponse"
    ):
        """<p>Returns a list of policies for a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>

        Raises:
            aws_sdk_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            aws_sdk_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            aws_sdk_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            aws_sdk_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.list_resource_policies_request.ListResourcePoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.list_resource_policies_response.ListResourcePoliciesResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.list_resource_policies

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.list_resource_policies.async_list_resource_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.list_resource_policies_request.ListResourcePoliciesRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_resource_policies(
        self,
        resource_arn: "aws_sdk_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["aws_sdk_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
    ) -> "AsyncIterator[aws_sdk_mpa.types.list_resource_policies_response_resource_policy.ListResourcePoliciesResponseResourcePolicy]":
        _token = next_token
        while True:
            _response = await self.list_resource_policies(
                resource_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> (
        "aws_sdk_mpa.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Returns a list of the tags for a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>

        Raises:
            aws_sdk_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            aws_sdk_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            aws_sdk_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            aws_sdk_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_mpa.types.string.String",
        tags: "aws_sdk_mpa.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "aws_sdk_mpa.types.tag_resource_response.TagResourceResponse":
        """<p>Creates or updates a resource tag. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource you want to tag.</p>
            tags: <p>Tags that you have added to the specified resource.</p>

        Raises:
            aws_sdk_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            aws_sdk_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            aws_sdk_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            aws_sdk_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_mpa.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeds the maximum number of tags allowed for this resource. Remove some tags, and try again.</p>
            aws_sdk_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_mpa.types.string.String",
        tag_keys: "aws_sdk_mpa.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "aws_sdk_mpa.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a resource tag. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. </p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource you want to untag.</p>
            tag_keys: <p>Array of tag key-value pairs that you want to untag.</p>

        Raises:
            aws_sdk_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            aws_sdk_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            aws_sdk_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            aws_sdk_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
