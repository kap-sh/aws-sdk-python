"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#TrustedAdvisor``."""

import datetime
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_trustedadvisor._auth._signers
import aws_sdk_trustedadvisor._auth._sigv4
from aws_sdk_trustedadvisor._auth._identity import Credentials
from aws_sdk_trustedadvisor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_trustedadvisor._auth._zapros_handler import AuthMiddleware
from aws_sdk_trustedadvisor._pagination import resolve_path as _resolve_path
from aws_sdk_trustedadvisor._services._aws_config import aws_config
from aws_sdk_trustedadvisor._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.account_id
    import aws_sdk_trustedadvisor.types.account_recommendation_identifier
    import aws_sdk_trustedadvisor.types.account_recommendation_lifecycle_summary
    import aws_sdk_trustedadvisor.types.batch_update_recommendation_resource_exclusion_request
    import aws_sdk_trustedadvisor.types.batch_update_recommendation_resource_exclusion_response
    import aws_sdk_trustedadvisor.types.check_identifier
    import aws_sdk_trustedadvisor.types.check_summary
    import aws_sdk_trustedadvisor.types.exclusion_status
    import aws_sdk_trustedadvisor.types.get_organization_recommendation_request
    import aws_sdk_trustedadvisor.types.get_organization_recommendation_response
    import aws_sdk_trustedadvisor.types.get_recommendation_request
    import aws_sdk_trustedadvisor.types.get_recommendation_response
    import aws_sdk_trustedadvisor.types.list_checks_request
    import aws_sdk_trustedadvisor.types.list_checks_response
    import aws_sdk_trustedadvisor.types.list_organization_recommendation_accounts_request
    import aws_sdk_trustedadvisor.types.list_organization_recommendation_accounts_response
    import aws_sdk_trustedadvisor.types.list_organization_recommendation_resources_request
    import aws_sdk_trustedadvisor.types.list_organization_recommendation_resources_response
    import aws_sdk_trustedadvisor.types.list_organization_recommendations_request
    import aws_sdk_trustedadvisor.types.list_organization_recommendations_response
    import aws_sdk_trustedadvisor.types.list_recommendation_resources_request
    import aws_sdk_trustedadvisor.types.list_recommendation_resources_response
    import aws_sdk_trustedadvisor.types.list_recommendations_request
    import aws_sdk_trustedadvisor.types.list_recommendations_response
    import aws_sdk_trustedadvisor.types.organization_recommendation_identifier
    import aws_sdk_trustedadvisor.types.organization_recommendation_resource_summary
    import aws_sdk_trustedadvisor.types.organization_recommendation_summary
    import aws_sdk_trustedadvisor.types.recommendation_aws_service
    import aws_sdk_trustedadvisor.types.recommendation_language
    import aws_sdk_trustedadvisor.types.recommendation_pillar
    import aws_sdk_trustedadvisor.types.recommendation_resource_exclusion_list
    import aws_sdk_trustedadvisor.types.recommendation_resource_summary
    import aws_sdk_trustedadvisor.types.recommendation_source
    import aws_sdk_trustedadvisor.types.recommendation_status
    import aws_sdk_trustedadvisor.types.recommendation_summary
    import aws_sdk_trustedadvisor.types.recommendation_type
    import aws_sdk_trustedadvisor.types.recommendation_update_reason
    import aws_sdk_trustedadvisor.types.resource_status
    import aws_sdk_trustedadvisor.types.update_organization_recommendation_lifecycle_request
    import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_request
    import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage
    import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code


class TrustedAdvisorClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class TrustedAdvisorClient:
    """A client for the ``TrustedAdvisor`` service.

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
        self._config = TrustedAdvisorClientConfig(
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
        self, config_overrides: Optional[TrustedAdvisorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: TrustedAdvisorClientConfig = config_overrides or {}
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

    def batch_update_recommendation_resource_exclusion(
        self,
        recommendation_resource_exclusions: "aws_sdk_trustedadvisor.types.recommendation_resource_exclusion_list.RecommendationResourceExclusionList",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
    ) -> "aws_sdk_trustedadvisor.types.batch_update_recommendation_resource_exclusion_response.BatchUpdateRecommendationResourceExclusionResponse":
        """<p>Update one or more exclusion statuses for a list of recommendation resources. This API supports up to 25 unique recommendation resource ARNs per request. This API currently doesn't support prioritized recommendation resources. This API updates global recommendations, eliminating the need to call the API in each AWS Region. After submitting an exclusion update, note that it might take a few minutes for the changes to be reflected in the system.</p>

        Args:
            recommendation_resource_exclusions: <p>A list of recommendation resource ARNs and exclusion status to update</p>

        Examples:
            Batch updates the exclusion status for a list of recommendation resources

            >>> client.batch_update_recommendation_resource_exclusion(recommendation_resource_exclusions=[{'arn': 'arn:aws:trustedadvisor::000000000000:recommendation-resource/55fa4d2e-bbb7-491a-833b-5773e9589578/18959a1f1973cff8e706e9d9bde28bba36cd602a6b2cb86c8b61252835236010', 'isExcluded': True}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.batch_update_recommendation_resource_exclusion_request.BatchUpdateRecommendationResourceExclusionRequest]",
        ) -> OperationResponse[
            "aws_sdk_trustedadvisor.types.batch_update_recommendation_resource_exclusion_response.BatchUpdateRecommendationResourceExclusionResponse"
        ]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.batch_update_recommendation_resource_exclusion

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.batch_update_recommendation_resource_exclusion.batch_update_recommendation_resource_exclusion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.batch_update_recommendation_resource_exclusion_request.BatchUpdateRecommendationResourceExclusionRequest = {}  # type: ignore[typeddict-item]
        input_["recommendation_resource_exclusions"] = (
            recommendation_resource_exclusions
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_organization_recommendation(
        self,
        organization_recommendation_identifier: "aws_sdk_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
    ) -> "aws_sdk_trustedadvisor.types.get_organization_recommendation_response.GetOrganizationRecommendationResponse":
        """<p>Get a specific recommendation within an AWS Organizations organization. This API supports only prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region. </p>

        Args:
            organization_recommendation_identifier: <p>The Recommendation identifier</p>

        Examples:
            Get an AWS Organization's Recommendation by ARN

            >>> client.get_organization_recommendation(organization_recommendation_identifier='arn:aws:trustedadvisor:::organization-recommendation/9534ec9b-bf3a-44e8-8213-2ed68b39d9d5')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.get_organization_recommendation_request.GetOrganizationRecommendationRequest]",
        ) -> OperationResponse[
            "aws_sdk_trustedadvisor.types.get_organization_recommendation_response.GetOrganizationRecommendationResponse"
        ]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.get_organization_recommendation

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.get_organization_recommendation.get_organization_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.get_organization_recommendation_request.GetOrganizationRecommendationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_recommendation_identifier"] = (
            organization_recommendation_identifier
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_recommendation(
        self,
        recommendation_identifier: "aws_sdk_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        language: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "aws_sdk_trustedadvisor.types.get_recommendation_response.GetRecommendationResponse":
        """<p>Get a specific Recommendation. This API provides global recommendations, eliminating the need to call the API in each AWS Region.</p>

        Args:
            recommendation_identifier: <p>The Recommendation identifier</p>
            language: <p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>

        Examples:
            Get a Recommendation by ARN

            >>> client.get_recommendation(recommendation_identifier='arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.get_recommendation_request.GetRecommendationRequest]",
        ) -> OperationResponse[
            "aws_sdk_trustedadvisor.types.get_recommendation_response.GetRecommendationResponse"
        ]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.get_recommendation

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.get_recommendation.get_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.get_recommendation_request.GetRecommendationRequest = {}  # type: ignore[typeddict-item]
        input_["recommendation_identifier"] = recommendation_identifier
        if language is not None:
            input_["language"] = language

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_checks(
        self,
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        pillar: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        language: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "aws_sdk_trustedadvisor.types.list_checks_response.ListChecksResponse":
        """<p>List a filterable set of Checks. This API provides global recommendations, eliminating the need to call the API in each AWS Region.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            pillar: <p>The pillar of the check</p>
            aws_service: <p>The aws service associated with the check</p>
            source: <p>The source of the check</p>
            language: <p>The ISO 639-1 code for the language that you want your checks to appear in.</p>

        Examples:
            List all AWS Trusted Advisor Checks

            >>> client.list_checks()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.list_checks_request.ListChecksRequest]",
        ) -> OperationResponse[
            "aws_sdk_trustedadvisor.types.list_checks_response.ListChecksResponse"
        ]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.list_checks

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.list_checks.list_checks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.list_checks_request.ListChecksRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if pillar is not None:
            input_["pillar"] = pillar
        if aws_service is not None:
            input_["aws_service"] = aws_service
        if source is not None:
            input_["source"] = source
        if language is not None:
            input_["language"] = language

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_checks(
        self,
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        pillar: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        language: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "Iterator[aws_sdk_trustedadvisor.types.check_summary.CheckSummary]":
        _token = next_token
        while True:
            _response = self.list_checks(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                pillar=pillar,
                aws_service=aws_service,
                source=source,
                language=language,
            )
            _page = _resolve_path(_response, ("check_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_organization_recommendation_accounts(
        self,
        organization_recommendation_identifier: "aws_sdk_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        affected_account_id: Optional[
            "aws_sdk_trustedadvisor.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_trustedadvisor.types.list_organization_recommendation_accounts_response.ListOrganizationRecommendationAccountsResponse":
        """<p>Lists the accounts that own the resources for an organization aggregate recommendation. This API only supports prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region. </p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            organization_recommendation_identifier: <p>The Recommendation identifier</p>
            affected_account_id: <p>An account affected by this organization recommendation</p>

        Examples:
            List all Accounts for an AWS Organization's Recommendation

            >>> client.list_organization_recommendation_accounts(organization_recommendation_identifier='arn:aws:trustedadvisor:::organization-recommendation/9534ec9b-bf3a-44e8-8213-2ed68b39d9d5')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.list_organization_recommendation_accounts_request.ListOrganizationRecommendationAccountsRequest]",
        ) -> OperationResponse[
            "aws_sdk_trustedadvisor.types.list_organization_recommendation_accounts_response.ListOrganizationRecommendationAccountsResponse"
        ]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.list_organization_recommendation_accounts

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.list_organization_recommendation_accounts.list_organization_recommendation_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.list_organization_recommendation_accounts_request.ListOrganizationRecommendationAccountsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["organization_recommendation_identifier"] = (
            organization_recommendation_identifier
        )
        if affected_account_id is not None:
            input_["affected_account_id"] = affected_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_organization_recommendation_accounts(
        self,
        organization_recommendation_identifier: "aws_sdk_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        affected_account_id: Optional[
            "aws_sdk_trustedadvisor.types.account_id.AccountId"
        ] = None,
    ) -> "Iterator[aws_sdk_trustedadvisor.types.account_recommendation_lifecycle_summary.AccountRecommendationLifecycleSummary]":
        _token = next_token
        while True:
            _response = self.list_organization_recommendation_accounts(
                organization_recommendation_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                affected_account_id=affected_account_id,
            )
            _page = _resolve_path(
                _response, ("account_recommendation_lifecycle_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_organization_recommendation_resources(
        self,
        organization_recommendation_identifier: "aws_sdk_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        status: Optional[
            "aws_sdk_trustedadvisor.types.resource_status.ResourceStatus"
        ] = None,
        exclusion_status: Optional[
            "aws_sdk_trustedadvisor.types.exclusion_status.ExclusionStatus"
        ] = None,
        region_code: Optional[str] = None,
        affected_account_id: Optional[
            "aws_sdk_trustedadvisor.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_trustedadvisor.types.list_organization_recommendation_resources_response.ListOrganizationRecommendationResourcesResponse":
        """<p>List Resources of a Recommendation within an Organization. This API only supports prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region. </p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            status: <p>The status of the resource</p>
            exclusion_status: <p>The exclusion status of the resource</p>
            region_code: <p>The AWS Region code of the resource</p>
            organization_recommendation_identifier: <p>The AWS Organization organization's Recommendation identifier</p>
            affected_account_id: <p>An account affected by this organization recommendation</p>

        Examples:
            List all Resources for an AWS Organization's Recommendation

            >>> client.list_organization_recommendation_resources(organization_recommendation_identifier='arn:aws:trustedadvisor:::organization-recommendation/5a694939-2e54-45a2-ae72-730598fa89d0')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.list_organization_recommendation_resources_request.ListOrganizationRecommendationResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_trustedadvisor.types.list_organization_recommendation_resources_response.ListOrganizationRecommendationResourcesResponse"
        ]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.list_organization_recommendation_resources

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.list_organization_recommendation_resources.list_organization_recommendation_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.list_organization_recommendation_resources_request.ListOrganizationRecommendationResourcesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if exclusion_status is not None:
            input_["exclusion_status"] = exclusion_status
        if region_code is not None:
            input_["region_code"] = region_code
        input_["organization_recommendation_identifier"] = (
            organization_recommendation_identifier
        )
        if affected_account_id is not None:
            input_["affected_account_id"] = affected_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_organization_recommendation_resources(
        self,
        organization_recommendation_identifier: "aws_sdk_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        status: Optional[
            "aws_sdk_trustedadvisor.types.resource_status.ResourceStatus"
        ] = None,
        exclusion_status: Optional[
            "aws_sdk_trustedadvisor.types.exclusion_status.ExclusionStatus"
        ] = None,
        region_code: Optional[str] = None,
        affected_account_id: Optional[
            "aws_sdk_trustedadvisor.types.account_id.AccountId"
        ] = None,
    ) -> "Iterator[aws_sdk_trustedadvisor.types.organization_recommendation_resource_summary.OrganizationRecommendationResourceSummary]":
        _token = next_token
        while True:
            _response = self.list_organization_recommendation_resources(
                organization_recommendation_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
                exclusion_status=exclusion_status,
                region_code=region_code,
                affected_account_id=affected_account_id,
            )
            _page = _resolve_path(
                _response, ("organization_recommendation_resource_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_organization_recommendations(
        self,
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        type: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_type.RecommendationType"
        ] = None,
        status: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_status.RecommendationStatus"
        ] = None,
        pillar: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        check_identifier: Optional[
            "aws_sdk_trustedadvisor.types.check_identifier.CheckIdentifier"
        ] = None,
        after_last_updated_at: Optional[datetime.datetime] = None,
        before_last_updated_at: Optional[datetime.datetime] = None,
    ) -> "aws_sdk_trustedadvisor.types.list_organization_recommendations_response.ListOrganizationRecommendationsResponse":
        """<p>List a filterable set of Recommendations within an Organization. This API only supports prioritized recommendations and provides global priority recommendations, eliminating the need to call the API in each AWS Region. </p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            type: <p>The type of the Recommendation</p>
            status: <p>The status of the Recommendation</p>
            pillar: <p>The pillar of the Recommendation</p>
            aws_service: <p>The aws service associated with the Recommendation</p>
            source: <p>The source of the Recommendation</p>
            check_identifier: <p>The check identifier of the Recommendation</p>
            after_last_updated_at: <p>After the last update of the Recommendation</p>
            before_last_updated_at: <p>Before the last update of the Recommendation</p>

        Examples:
            List all of an AWS Organization's Recommendations

            >>> client.list_organization_recommendations()
            Filter and return a max of one AWS Organization Recommendation that is a part of the "security" pillar

            >>> client.list_organization_recommendations(pillar='security', max_results=100)
            Use the "nextToken" returned from a previous request to fetch the next page of filtered AWS Organization Recommendations that are a part of the "security" pillar

            >>> client.list_organization_recommendations(next_token='<REDACTED>', pillar='security', max_results=100)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.list_organization_recommendations_request.ListOrganizationRecommendationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_trustedadvisor.types.list_organization_recommendations_response.ListOrganizationRecommendationsResponse"
        ]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.list_organization_recommendations

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.list_organization_recommendations.list_organization_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.list_organization_recommendations_request.ListOrganizationRecommendationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type is not None:
            input_["type"] = type
        if status is not None:
            input_["status"] = status
        if pillar is not None:
            input_["pillar"] = pillar
        if aws_service is not None:
            input_["aws_service"] = aws_service
        if source is not None:
            input_["source"] = source
        if check_identifier is not None:
            input_["check_identifier"] = check_identifier
        if after_last_updated_at is not None:
            input_["after_last_updated_at"] = after_last_updated_at
        if before_last_updated_at is not None:
            input_["before_last_updated_at"] = before_last_updated_at

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_organization_recommendations(
        self,
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        type: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_type.RecommendationType"
        ] = None,
        status: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_status.RecommendationStatus"
        ] = None,
        pillar: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        check_identifier: Optional[
            "aws_sdk_trustedadvisor.types.check_identifier.CheckIdentifier"
        ] = None,
        after_last_updated_at: Optional[datetime.datetime] = None,
        before_last_updated_at: Optional[datetime.datetime] = None,
    ) -> "Iterator[aws_sdk_trustedadvisor.types.organization_recommendation_summary.OrganizationRecommendationSummary]":
        _token = next_token
        while True:
            _response = self.list_organization_recommendations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                type=type,
                status=status,
                pillar=pillar,
                aws_service=aws_service,
                source=source,
                check_identifier=check_identifier,
                after_last_updated_at=after_last_updated_at,
                before_last_updated_at=before_last_updated_at,
            )
            _page = _resolve_path(_response, ("organization_recommendation_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recommendation_resources(
        self,
        recommendation_identifier: "aws_sdk_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        status: Optional[
            "aws_sdk_trustedadvisor.types.resource_status.ResourceStatus"
        ] = None,
        exclusion_status: Optional[
            "aws_sdk_trustedadvisor.types.exclusion_status.ExclusionStatus"
        ] = None,
        region_code: Optional[str] = None,
        language: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "aws_sdk_trustedadvisor.types.list_recommendation_resources_response.ListRecommendationResourcesResponse":
        """<p>List Resources of a Recommendation. This API provides global recommendations, eliminating the need to call the API in each AWS Region.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            status: <p>The status of the resource</p>
            exclusion_status: <p>The exclusion status of the resource</p>
            region_code: <p>The AWS Region code of the resource</p>
            recommendation_identifier: <p>The Recommendation identifier</p>
            language: <p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>

        Examples:
            List all Resources for a Recommendation

            >>> client.list_recommendation_resources(recommendation_identifier='arn:aws:trustedadvisor::000000000000:recommendation/55fa4d2e-bbb7-491a-833b-5773e9589578')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.list_recommendation_resources_request.ListRecommendationResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_trustedadvisor.types.list_recommendation_resources_response.ListRecommendationResourcesResponse"
        ]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.list_recommendation_resources

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.list_recommendation_resources.list_recommendation_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.list_recommendation_resources_request.ListRecommendationResourcesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if exclusion_status is not None:
            input_["exclusion_status"] = exclusion_status
        if region_code is not None:
            input_["region_code"] = region_code
        input_["recommendation_identifier"] = recommendation_identifier
        if language is not None:
            input_["language"] = language

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_recommendation_resources(
        self,
        recommendation_identifier: "aws_sdk_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        status: Optional[
            "aws_sdk_trustedadvisor.types.resource_status.ResourceStatus"
        ] = None,
        exclusion_status: Optional[
            "aws_sdk_trustedadvisor.types.exclusion_status.ExclusionStatus"
        ] = None,
        region_code: Optional[str] = None,
        language: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "Iterator[aws_sdk_trustedadvisor.types.recommendation_resource_summary.RecommendationResourceSummary]":
        _token = next_token
        while True:
            _response = self.list_recommendation_resources(
                recommendation_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
                exclusion_status=exclusion_status,
                region_code=region_code,
                language=language,
            )
            _page = _resolve_path(_response, ("recommendation_resource_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recommendations(
        self,
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        type: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_type.RecommendationType"
        ] = None,
        status: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_status.RecommendationStatus"
        ] = None,
        pillar: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        check_identifier: Optional[
            "aws_sdk_trustedadvisor.types.check_identifier.CheckIdentifier"
        ] = None,
        after_last_updated_at: Optional[datetime.datetime] = None,
        before_last_updated_at: Optional[datetime.datetime] = None,
        language: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "aws_sdk_trustedadvisor.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>List a filterable set of Recommendations. This API provides global recommendations, eliminating the need to call the API in each AWS Region.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            type: <p>The type of the Recommendation</p>
            status: <p>The status of the Recommendation</p>
            pillar: <p>The pillar of the Recommendation</p>
            aws_service: <p>The aws service associated with the Recommendation</p>
            source: <p>The source of the Recommendation</p>
            check_identifier: <p>The check identifier of the Recommendation</p>
            after_last_updated_at: <p>After the last update of the Recommendation</p>
            before_last_updated_at: <p>Before the last update of the Recommendation</p>
            language: <p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>

        Examples:
            List all Recommendations

            >>> client.list_recommendations()
            Filter and return a max of one Recommendation that is a part of AWS IAM

            >>> client.list_recommendations(aws_service='iam', max_results=100)
            Use the "nextToken" returned from a previous request to fetch the next page of filtered Recommendations

            >>> client.list_recommendations(next_token='<REDACTED>', aws_service='rds', max_results=100)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_trustedadvisor.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.list_recommendations

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.list_recommendations.list_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.list_recommendations_request.ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type is not None:
            input_["type"] = type
        if status is not None:
            input_["status"] = status
        if pillar is not None:
            input_["pillar"] = pillar
        if aws_service is not None:
            input_["aws_service"] = aws_service
        if source is not None:
            input_["source"] = source
        if check_identifier is not None:
            input_["check_identifier"] = check_identifier
        if after_last_updated_at is not None:
            input_["after_last_updated_at"] = after_last_updated_at
        if before_last_updated_at is not None:
            input_["before_last_updated_at"] = before_last_updated_at
        if language is not None:
            input_["language"] = language

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_recommendations(
        self,
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        type: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_type.RecommendationType"
        ] = None,
        status: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_status.RecommendationStatus"
        ] = None,
        pillar: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
        ] = None,
        aws_service: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
        ] = None,
        source: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_source.RecommendationSource"
        ] = None,
        check_identifier: Optional[
            "aws_sdk_trustedadvisor.types.check_identifier.CheckIdentifier"
        ] = None,
        after_last_updated_at: Optional[datetime.datetime] = None,
        before_last_updated_at: Optional[datetime.datetime] = None,
        language: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_language.RecommendationLanguage"
        ] = None,
    ) -> "Iterator[aws_sdk_trustedadvisor.types.recommendation_summary.RecommendationSummary]":
        _token = next_token
        while True:
            _response = self.list_recommendations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                type=type,
                status=status,
                pillar=pillar,
                aws_service=aws_service,
                source=source,
                check_identifier=check_identifier,
                after_last_updated_at=after_last_updated_at,
                before_last_updated_at=before_last_updated_at,
                language=language,
            )
            _page = _resolve_path(_response, ("recommendation_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_organization_recommendation_lifecycle(
        self,
        lifecycle_stage: "aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage.UpdateRecommendationLifecycleStage",
        organization_recommendation_identifier: "aws_sdk_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        update_reason: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_update_reason.RecommendationUpdateReason"
        ] = None,
        update_reason_code: Optional[
            "aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.UpdateRecommendationLifecycleStageReasonCode"
        ] = None,
    ) -> None:
        """<p>Update the lifecycle of a Recommendation within an Organization. This API only supports prioritized recommendations and updates global priority recommendations, eliminating the need to call the API in each AWS Region. </p>

        Args:
            lifecycle_stage: <p>The new lifecycle stage</p>
            update_reason: <p>Reason for the lifecycle stage change</p>
            update_reason_code: <p>Reason code for the lifecycle state change</p>
            organization_recommendation_identifier: <p>The Recommendation identifier for AWS Trusted Advisor Priority recommendations</p>

        Examples:
            Update the lifecycle stage of an AWS Organization's Recommendation that is managed by AWS Trusted Advisor Priority

            >>> client.update_organization_recommendation_lifecycle(organization_recommendation_identifier='arn:aws:trustedadvisor:::organization-recommendation/96b5e5ca-7930-444c-90c6-06d386128100', lifecycle_stage='dismissed', update_reason_code='not_applicable', update_reason='Does not apply to this resource')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.update_organization_recommendation_lifecycle_request.UpdateOrganizationRecommendationLifecycleRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.update_organization_recommendation_lifecycle

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.update_organization_recommendation_lifecycle.update_organization_recommendation_lifecycle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.update_organization_recommendation_lifecycle_request.UpdateOrganizationRecommendationLifecycleRequest = {}  # type: ignore[typeddict-item]
        input_["lifecycle_stage"] = lifecycle_stage
        if update_reason is not None:
            input_["update_reason"] = update_reason
        if update_reason_code is not None:
            input_["update_reason_code"] = update_reason_code
        input_["organization_recommendation_identifier"] = (
            organization_recommendation_identifier
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_recommendation_lifecycle(
        self,
        lifecycle_stage: "aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage.UpdateRecommendationLifecycleStage",
        recommendation_identifier: "aws_sdk_trustedadvisor.types.account_recommendation_identifier.AccountRecommendationIdentifier",
        *,
        config_overrides: Optional[TrustedAdvisorClientConfig] = None,
        update_reason: Optional[
            "aws_sdk_trustedadvisor.types.recommendation_update_reason.RecommendationUpdateReason"
        ] = None,
        update_reason_code: Optional[
            "aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.UpdateRecommendationLifecycleStageReasonCode"
        ] = None,
    ) -> None:
        """<p>Update the lifecyle of a Recommendation. This API only supports prioritized recommendations and updates global priority recommendations, eliminating the need to call the API in each AWS Region.</p>

        Args:
            lifecycle_stage: <p>The new lifecycle stage</p>
            update_reason: <p>Reason for the lifecycle stage change</p>
            update_reason_code: <p>Reason code for the lifecycle state change</p>
            recommendation_identifier: <p>The Recommendation identifier for AWS Trusted Advisor Priority recommendations</p>

        Examples:
            Update the lifecycle stage of a Recommendation managed by AWS Trusted Advisor Priority

            >>> client.update_recommendation_lifecycle(recommendation_identifier='arn:aws:trustedadvisor::000000000000:recommendation/861c9c6e-f169-405a-8b59-537a8caccd7a', lifecycle_stage='resolved', update_reason_code='valid_business_case', update_reason='Resolved the recommendation')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_request.UpdateRecommendationLifecycleRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_trustedadvisor._operations.trusted_advisor.update_recommendation_lifecycle

            output, http_response = (
                aws_sdk_trustedadvisor._operations.trusted_advisor.update_recommendation_lifecycle.update_recommendation_lifecycle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_request.UpdateRecommendationLifecycleRequest = {}  # type: ignore[typeddict-item]
        input_["lifecycle_stage"] = lifecycle_stage
        if update_reason is not None:
            input_["update_reason"] = update_reason
        if update_reason_code is not None:
            input_["update_reason_code"] = update_reason_code
        input_["recommendation_identifier"] = recommendation_identifier

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
