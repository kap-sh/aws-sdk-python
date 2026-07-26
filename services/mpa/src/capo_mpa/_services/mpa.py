"""Generated from Smithy shape ``com.amazonaws.mpa#AWSFluffyCoreService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_mpa._auth._signers
import capo_mpa._auth._sigv4
from capo_mpa._auth._identity import Credentials
from capo_mpa._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mpa._auth._zapros_handler import AuthMiddleware
from capo_mpa._pagination import resolve_path as _resolve_path
from capo_mpa._resources.aws_fluffy_core_service.approval_team import ApprovalTeam
from capo_mpa._resources.aws_fluffy_core_service.identity_source import IdentitySource
from capo_mpa._resources.aws_fluffy_core_service.session import Session
from capo_mpa._services._aws_config import aws_config
from capo_mpa._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_mpa.types.get_policy_version_request
    import capo_mpa.types.get_policy_version_response
    import capo_mpa.types.get_resource_policy_request
    import capo_mpa.types.get_resource_policy_response
    import capo_mpa.types.list_policies_request
    import capo_mpa.types.list_policies_response
    import capo_mpa.types.list_policy_versions_request
    import capo_mpa.types.list_policy_versions_response
    import capo_mpa.types.list_resource_policies_request
    import capo_mpa.types.list_resource_policies_response
    import capo_mpa.types.list_resource_policies_response_resource_policy
    import capo_mpa.types.list_tags_for_resource_request
    import capo_mpa.types.list_tags_for_resource_response
    import capo_mpa.types.max_results
    import capo_mpa.types.policy
    import capo_mpa.types.policy_type
    import capo_mpa.types.policy_version_summary
    import capo_mpa.types.qualified_policy_arn
    import capo_mpa.types.string
    import capo_mpa.types.tag_key_list
    import capo_mpa.types.tag_resource_request
    import capo_mpa.types.tag_resource_response
    import capo_mpa.types.tags
    import capo_mpa.types.token
    import capo_mpa.types.unqualified_policy_arn
    import capo_mpa.types.untag_resource_request
    import capo_mpa.types.untag_resource_response


class MPAClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class MPAClient:
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
        self._config = MPAClientConfig(
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
        self.approval_team = ApprovalTeam(self)
        self.identity_source = IdentitySource(self)
        self.session = Session(self)

    def operation_options(
        self, config_overrides: Optional[MPAClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MPAClientConfig = config_overrides or {}
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

    def get_policy_version(
        self,
        policy_version_arn: "capo_mpa.types.qualified_policy_arn.QualifiedPolicyArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "capo_mpa.types.get_policy_version_response.GetPolicyVersionResponse":
        """<p>Returns details for the version of a policy. Policies define the permissions for team resources.</p>

        Args:
            policy_version_arn: <p>Amazon Resource Name (ARN) for the policy.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.get_policy_version_request.GetPolicyVersionRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.get_policy_version_response.GetPolicyVersionResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_policy_version

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.get_policy_version.get_policy_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.get_policy_version_request.GetPolicyVersionRequest = {}  # type: ignore[typeddict-item]
        input_["policy_version_arn"] = policy_version_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "capo_mpa.types.string.String",
        policy_name: "capo_mpa.types.string.String",
        policy_type: "capo_mpa.types.policy_type.PolicyType",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "capo_mpa.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Returns details about a policy for a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>
            policy_name: <p>Name of the policy.</p>
            policy_type: <p>The type of policy.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.invalid_parameter_exception.InvalidParameterException: <p>The request contains an invalid parameter value.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.get_resource_policy

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["policy_name"] = policy_name
        input_["policy_type"] = policy_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_policies(
        self,
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "capo_mpa.types.list_policies_response.ListPoliciesResponse":
        """<p>Returns a list of policies. Policies define the permissions for team resources.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.list_policies_request.ListPoliciesRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.list_policies_response.ListPoliciesResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_policies

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.list_policies.list_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_policies_request.ListPoliciesRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_policies(
        self,
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "Iterator[capo_mpa.types.policy.Policy]":
        _token = next_token
        while True:
            _response = self.list_policies(
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

    def list_policy_versions(
        self,
        policy_arn: "capo_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "capo_mpa.types.list_policy_versions_response.ListPolicyVersionsResponse":
        """<p>Returns a list of the versions for policies. Policies define the permissions for team resources.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>
            policy_arn: <p>Amazon Resource Name (ARN) for the policy.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.list_policy_versions_request.ListPolicyVersionsRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.list_policy_versions_response.ListPolicyVersionsResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_policy_versions

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.list_policy_versions.list_policy_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_policy_versions_request.ListPolicyVersionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["policy_arn"] = policy_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_policy_versions(
        self,
        policy_arn: "capo_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "Iterator[capo_mpa.types.policy_version_summary.PolicyVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_policy_versions(
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

    def list_resource_policies(
        self,
        resource_arn: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "capo_mpa.types.list_resource_policies_response.ListResourcePoliciesResponse":
        """<p>Returns a list of policies for a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.list_resource_policies_request.ListResourcePoliciesRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.list_resource_policies_response.ListResourcePoliciesResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_resource_policies

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.list_resource_policies.list_resource_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_resource_policies_request.ListResourcePoliciesRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
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

    def iter_list_resource_policies(
        self,
        resource_arn: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        max_results: Optional["capo_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mpa.types.token.Token"] = None,
    ) -> "Iterator[capo_mpa.types.list_resource_policies_response_resource_policy.ListResourcePoliciesResponseResourcePolicy]":
        _token = next_token
        while True:
            _response = self.list_resource_policies(
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_mpa.types.string.String",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "capo_mpa.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of the tags for a resource.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.list_tags_for_resource

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_mpa.types.string.String",
        tags: "capo_mpa.types.tags.Tags",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "capo_mpa.types.tag_resource_response.TagResourceResponse":
        """<p>Creates or updates a resource tag. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource you want to tag.</p>
            tags: <p>Tags that you have added to the specified resource.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeds the maximum number of tags allowed for this resource. Remove some tags, and try again.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.tag_resource

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "capo_mpa.types.string.String",
        tag_keys: "capo_mpa.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "capo_mpa.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a resource tag. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. </p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) for the resource you want to untag.</p>
            tag_keys: <p>Array of tag key-value pairs that you want to untag.</p>

        Raises:
            capo_mpa.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Check your permissions, and try again.</p>
            capo_mpa.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again. If the problem persists, contact Amazon Web Services Support.</p>
            capo_mpa.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the resource ID, and try again.</p>
            capo_mpa.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_mpa.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_mpa.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mpa.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_mpa.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_mpa._operations.aws_fluffy_core_service.untag_resource

            output, http_response = (
                capo_mpa._operations.aws_fluffy_core_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mpa.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
