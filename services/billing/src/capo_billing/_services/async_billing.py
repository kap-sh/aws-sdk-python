"""Generated from Smithy shape ``com.amazonaws.billing#AWSBilling``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_billing._auth._signers
import capo_billing._auth._sigv4
from capo_billing._auth._identity import Credentials
from capo_billing._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_billing._auth._zapros_handler import AuthMiddleware
from capo_billing._pagination import resolve_path as _resolve_path
from capo_billing._services._aws_config import aaws_config
from capo_billing._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_billing.types.account_id
    import capo_billing.types.active_time_range
    import capo_billing.types.associate_source_views_request
    import capo_billing.types.associate_source_views_response
    import capo_billing.types.billing_view_arn
    import capo_billing.types.billing_view_arn_list
    import capo_billing.types.billing_view_description
    import capo_billing.types.billing_view_list_element
    import capo_billing.types.billing_view_name
    import capo_billing.types.billing_view_source_views_list
    import capo_billing.types.billing_view_type_list
    import capo_billing.types.billing_views_max_results
    import capo_billing.types.client_token
    import capo_billing.types.create_billing_view_request
    import capo_billing.types.create_billing_view_response
    import capo_billing.types.delete_billing_view_request
    import capo_billing.types.delete_billing_view_response
    import capo_billing.types.disassociate_source_views_request
    import capo_billing.types.disassociate_source_views_response
    import capo_billing.types.expression
    import capo_billing.types.get_billing_view_request
    import capo_billing.types.get_billing_view_response
    import capo_billing.types.get_resource_policy_request
    import capo_billing.types.get_resource_policy_response
    import capo_billing.types.list_billing_views_request
    import capo_billing.types.list_billing_views_response
    import capo_billing.types.list_source_views_for_billing_view_request
    import capo_billing.types.list_source_views_for_billing_view_response
    import capo_billing.types.list_tags_for_resource_request
    import capo_billing.types.list_tags_for_resource_response
    import capo_billing.types.page_token
    import capo_billing.types.resource_arn
    import capo_billing.types.resource_tag_key_list
    import capo_billing.types.resource_tag_list
    import capo_billing.types.string_searches
    import capo_billing.types.tag_resource_request
    import capo_billing.types.tag_resource_response
    import capo_billing.types.untag_resource_request
    import capo_billing.types.untag_resource_response
    import capo_billing.types.update_billing_view_request
    import capo_billing.types.update_billing_view_response


class AsyncBillingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncBillingClient:
    """A client for the ``Billing`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncBillingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncBillingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBillingClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_source_views(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        source_views: "capo_billing.types.billing_view_source_views_list.BillingViewSourceViewsList",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
    ) -> "capo_billing.types.associate_source_views_response.AssociateSourceViewsResponse":
        """<p> Associates one or more source billing views with an existing billing view. This allows creating aggregate billing views that combine data from multiple sources. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the billing view to associate source views with. </p>
            source_views: <p> A list of ARNs of the source billing views to associate. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than <code>HEALTHY</code>.</p>
            capo_billing.errors.conflict_exception.ConflictException: <p> The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You've reached the limit of resources you can create, or exceeded the size of an individual resource. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke AssociateSourceViews

            >>> await client.associate_source_views(arn='arn:aws:billing::123456789012:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899', source_views=['arn:aws:billing::123456789012:billingview/primary', 'arn:aws:billing::123456789012:billingview/custom-d3f9c7e4-8b2f-4a6e-9d3b-2f7c8a1e5f6d'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.associate_source_views_request.AssociateSourceViewsRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.associate_source_views_response.AssociateSourceViewsResponse"
        ]:
            import capo_billing._operations.aws_billing.associate_source_views

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.associate_source_views.async_associate_source_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.associate_source_views_request.AssociateSourceViewsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["source_views"] = source_views

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_billing_view(
        self,
        name: "capo_billing.types.billing_view_name.BillingViewName",
        source_views: "capo_billing.types.billing_view_source_views_list.BillingViewSourceViewsList",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
        description: Optional[
            "capo_billing.types.billing_view_description.BillingViewDescription"
        ] = None,
        data_filter_expression: Optional[
            "capo_billing.types.expression.Expression"
        ] = None,
        client_token: Optional["capo_billing.types.client_token.ClientToken"] = None,
        resource_tags: Optional[
            "capo_billing.types.resource_tag_list.ResourceTagList"
        ] = None,
    ) -> "capo_billing.types.create_billing_view_response.CreateBillingViewResponse":
        r"""<p> Creates a billing view with the specified billing view attributes. </p>

        Args:
            name: <p> The name of the billing view. </p>
            description: <p> The description of the billing view. </p>
            source_views: <p>A list of billing views used as the data source for the custom billing view.</p>
            data_filter_expression: <p> See <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html\">Expression</a>. Billing view only supports <code>LINKED_ACCOUNT</code>, <code>Tags</code>, and <code>CostCategories</code>. </p>
            client_token: <p>A unique, case-sensitive identifier you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. If the original request completes successfully, any subsequent retries complete successfully without performing any further actions with an idempotent request. </p>
            resource_tags: <p>A list of key value map specifying tags associated to the billing view being created. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than <code>HEALTHY</code>.</p>
            capo_billing.errors.conflict_exception.ConflictException: <p> The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You've reached the limit of resources you can create, or exceeded the size of an individual resource. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CreateBillingView

            >>> await client.create_billing_view(name='Example Custom Billing View', source_views=['arn:aws:billing::123456789101:billingview/primary'], description='Custom Billing View Example', data_filter_expression={'dimensions': {'key': 'LINKED_ACCOUNT', 'values': ['000000000000']}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.create_billing_view_request.CreateBillingViewRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.create_billing_view_response.CreateBillingViewResponse"
        ]:
            import capo_billing._operations.aws_billing.create_billing_view

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.create_billing_view.async_create_billing_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.create_billing_view_request.CreateBillingViewRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["source_views"] = source_views
        if data_filter_expression is not None:
            input_["data_filter_expression"] = data_filter_expression
        if client_token is not None:
            input_["client_token"] = client_token
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_billing_view(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_billing.types.delete_billing_view_response.DeleteBillingViewResponse":
        """<p>Deletes the specified billing view.</p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>
            force: <p> If set to true, forces deletion of the billing view even if it has derived resources (e.g. other billing views or budgets). Use with caution as this may break dependent resources. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.conflict_exception.ConflictException: <p> The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke DeleteBillingView

            >>> await client.delete_billing_view(arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.delete_billing_view_request.DeleteBillingViewRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.delete_billing_view_response.DeleteBillingViewResponse"
        ]:
            import capo_billing._operations.aws_billing.delete_billing_view

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.delete_billing_view.async_delete_billing_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.delete_billing_view_request.DeleteBillingViewRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_source_views(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        source_views: "capo_billing.types.billing_view_source_views_list.BillingViewSourceViewsList",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
    ) -> "capo_billing.types.disassociate_source_views_response.DisassociateSourceViewsResponse":
        """<p> Removes the association between one or more source billing views and an existing billing view. This allows modifying the composition of aggregate billing views. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the billing view to disassociate source views from. </p>
            source_views: <p> A list of ARNs of the source billing views to disassociate. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than <code>HEALTHY</code>.</p>
            capo_billing.errors.conflict_exception.ConflictException: <p> The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke DisassociateSourceViews

            >>> await client.disassociate_source_views(arn='arn:aws:billing::123456789012:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899', source_views=['arn:aws:billing::123456789012:billingview/primary', 'arn:aws:billing::123456789012:billingview/custom-d3f9c7e4-8b2f-4a6e-9d3b-2f7c8a1e5f6d'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.disassociate_source_views_request.DisassociateSourceViewsRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.disassociate_source_views_response.DisassociateSourceViewsResponse"
        ]:
            import capo_billing._operations.aws_billing.disassociate_source_views

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.disassociate_source_views.async_disassociate_source_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.disassociate_source_views_request.DisassociateSourceViewsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["source_views"] = source_views

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_billing_view(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
    ) -> "capo_billing.types.get_billing_view_response.GetBillingViewResponse":
        """<p>Returns the metadata associated to the specified billing view ARN. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetBillingView

            >>> await client.get_billing_view(arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.get_billing_view_request.GetBillingViewRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.get_billing_view_response.GetBillingViewResponse"
        ]:
            import capo_billing._operations.aws_billing.get_billing_view

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.get_billing_view.async_get_billing_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.get_billing_view_request.GetBillingViewRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_billing.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
    ) -> "capo_billing.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Returns the resource-based policy document attached to the resource in <code>JSON</code> format. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the billing view resource to which the policy is attached to. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetResourcePolicy

            >>> await client.get_resource_policy(resource_arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_billing._operations.aws_billing.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_billing_views(
        self,
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
        active_time_range: Optional[
            "capo_billing.types.active_time_range.ActiveTimeRange"
        ] = None,
        arns: Optional[
            "capo_billing.types.billing_view_arn_list.BillingViewArnList"
        ] = None,
        billing_view_types: Optional[
            "capo_billing.types.billing_view_type_list.BillingViewTypeList"
        ] = None,
        names: Optional["capo_billing.types.string_searches.StringSearches"] = None,
        owner_account_id: Optional["capo_billing.types.account_id.AccountId"] = None,
        source_account_id: Optional["capo_billing.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
        ] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "capo_billing.types.list_billing_views_response.ListBillingViewsResponse":
        """<p>Lists the billing views available for a given time period. </p> <p>Every Amazon Web Services account has a unique <code>PRIMARY</code> billing view that represents the billing data available by default. Accounts that use Billing Conductor also have <code>BILLING_GROUP</code> billing views representing pro forma costs associated with each created billing group.</p>

        Args:
            active_time_range: <p> The time range for the billing views listed. <code>PRIMARY</code> billing view is always listed. <code>BILLING_GROUP</code> billing views are listed for time ranges when the associated billing group resource in Billing Conductor is active. The time range must be within one calendar month. </p>
            arns: <p>The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>
            billing_view_types: <p>The type of billing view.</p>
            names: <p> Filters the list of billing views by name. You can specify search criteria to match billing view names based on the search option provided. </p>
            owner_account_id: <p> The list of owners of the billing view. </p>
            source_account_id: <p> Filters the results to include only billing views that use the specified account as a source. </p>
            max_results: <p>The maximum number of billing views to retrieve. Default is 100. </p>
            next_token: <p>The pagination token that is used on subsequent calls to list billing views.</p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListBillingViews

            >>> await client.list_billing_views(active_time_range={'activeAfterInclusive': 1719792000, 'activeBeforeInclusive': 1722470399.999})
            Error example for ListBillingViews

            >>> await client.list_billing_views(active_time_range={'activeAfterInclusive': 1719792001, 'activeBeforeInclusive': 1719792000})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.list_billing_views_request.ListBillingViewsRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.list_billing_views_response.ListBillingViewsResponse"
        ]:
            import capo_billing._operations.aws_billing.list_billing_views

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.list_billing_views.async_list_billing_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.list_billing_views_request.ListBillingViewsRequest = {}  # type: ignore[typeddict-item]
        if active_time_range is not None:
            input_["active_time_range"] = active_time_range
        if arns is not None:
            input_["arns"] = arns
        if billing_view_types is not None:
            input_["billing_view_types"] = billing_view_types
        if names is not None:
            input_["names"] = names
        if owner_account_id is not None:
            input_["owner_account_id"] = owner_account_id
        if source_account_id is not None:
            input_["source_account_id"] = source_account_id
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

    async def iter_list_billing_views(
        self,
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
        active_time_range: Optional[
            "capo_billing.types.active_time_range.ActiveTimeRange"
        ] = None,
        arns: Optional[
            "capo_billing.types.billing_view_arn_list.BillingViewArnList"
        ] = None,
        billing_view_types: Optional[
            "capo_billing.types.billing_view_type_list.BillingViewTypeList"
        ] = None,
        names: Optional["capo_billing.types.string_searches.StringSearches"] = None,
        owner_account_id: Optional["capo_billing.types.account_id.AccountId"] = None,
        source_account_id: Optional["capo_billing.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
        ] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_billing.types.billing_view_list_element.BillingViewListElement]":
        _token = next_token
        while True:
            _response = await self.list_billing_views(
                config_overrides=config_overrides,
                active_time_range=active_time_range,
                arns=arns,
                billing_view_types=billing_view_types,
                names=names,
                owner_account_id=owner_account_id,
                source_account_id=source_account_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("billing_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_source_views_for_billing_view(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
        max_results: Optional[
            "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
        ] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "capo_billing.types.list_source_views_for_billing_view_response.ListSourceViewsForBillingViewResponse":
        """<p>Lists the source views (managed Amazon Web Services billing views) associated with the billing view. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>
            max_results: <p> The number of entries a paginated response contains. </p>
            next_token: <p> The pagination token that is used on subsequent calls to list billing views. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListSourceViewsForBillingView

            >>> await client.list_source_views_for_billing_view(arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.list_source_views_for_billing_view_request.ListSourceViewsForBillingViewRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.list_source_views_for_billing_view_response.ListSourceViewsForBillingViewResponse"
        ]:
            import capo_billing._operations.aws_billing.list_source_views_for_billing_view

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.list_source_views_for_billing_view.async_list_source_views_for_billing_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.list_source_views_for_billing_view_request.ListSourceViewsForBillingViewRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
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

    async def iter_list_source_views_for_billing_view(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
        max_results: Optional[
            "capo_billing.types.billing_views_max_results.BillingViewsMaxResults"
        ] = None,
        next_token: Optional["capo_billing.types.page_token.PageToken"] = None,
    ) -> "AsyncIterator[capo_billing.types.billing_view_arn.BillingViewArn]":
        _token = next_token
        while True:
            _response = await self.list_source_views_for_billing_view(
                arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("source_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_billing.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
    ) -> (
        "capo_billing.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Lists tags associated with the billing view resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListTagsForResource

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_billing._operations.aws_billing.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_billing.types.resource_arn.ResourceArn",
        resource_tags: "capo_billing.types.resource_tag_list.ResourceTagList",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
    ) -> "capo_billing.types.tag_resource_response.TagResourceResponse":
        """<p> An API operation for adding one or more tags (key-value pairs) to a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource. </p>
            resource_tags: <p> A list of tag key value pairs that are associated with the resource. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke TagResource

            >>> await client.tag_resource(resource_arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899', resource_tags=[{'key': 'ExampleTagKey', 'value': 'ExampleTagValue'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_billing._operations.aws_billing.tag_resource

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["resource_tags"] = resource_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_billing.types.resource_arn.ResourceArn",
        resource_tag_keys: "capo_billing.types.resource_tag_key_list.ResourceTagKeyList",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
    ) -> "capo_billing.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes one or more tags from a resource. Specify only tag keys in your request. Don't specify the value. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource. </p>
            resource_tag_keys: <p> A list of tag key value pairs that are associated with the resource. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UntagResource

            >>> await client.untag_resource(resource_arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899', resource_tag_keys=['ExampleTagKey'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_billing._operations.aws_billing.untag_resource

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["resource_tag_keys"] = resource_tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_billing_view(
        self,
        arn: "capo_billing.types.billing_view_arn.BillingViewArn",
        *,
        config_overrides: Optional[AsyncBillingClientConfig] = None,
        name: Optional["capo_billing.types.billing_view_name.BillingViewName"] = None,
        description: Optional[
            "capo_billing.types.billing_view_description.BillingViewDescription"
        ] = None,
        data_filter_expression: Optional[
            "capo_billing.types.expression.Expression"
        ] = None,
    ) -> "capo_billing.types.update_billing_view_response.UpdateBillingViewResponse":
        r"""<p>An API to update the attributes of the billing view. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>
            name: <p> The name of the billing view. </p>
            description: <p> The description of the billing view. </p>
            data_filter_expression: <p>See <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html\">Expression</a>. Billing view only supports <code>LINKED_ACCOUNT</code>, <code>Tags</code>, and <code>CostCategories</code>. </p>

        Raises:
            capo_billing.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_billing.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than <code>HEALTHY</code>.</p>
            capo_billing.errors.conflict_exception.ConflictException: <p> The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_billing.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an unknown error, exception, or failure. </p>
            capo_billing.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_billing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You've reached the limit of resources you can create, or exceeded the size of an individual resource. </p>
            capo_billing.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billing.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_billing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateBillingView

            >>> await client.update_billing_view(name='Example Custom Billing View', arn='arn:aws:billing::123456789101:billingview/custom-46f47cb2-a11d-43f3-983d-470b5708a899', description='Custom Billing View Example -- updated description', data_filter_expression={'dimensions': {'key': 'LINKED_ACCOUNT', 'values': ['000000000000']}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billing.types.update_billing_view_request.UpdateBillingViewRequest]",
        ) -> AsyncOperationResponse[
            "capo_billing.types.update_billing_view_response.UpdateBillingViewResponse"
        ]:
            import capo_billing._operations.aws_billing.update_billing_view

            (
                output,
                http_response,
            ) = await capo_billing._operations.aws_billing.update_billing_view.async_update_billing_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billing.types.update_billing_view_request.UpdateBillingViewRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if data_filter_expression is not None:
            input_["data_filter_expression"] = data_filter_expression

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
