"""Generated from Smithy shape ``com.amazonaws.cloudsearch#A9SearchCloudConfigService2013``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

from aws_sdk_cloudsearch._auth._identity import Credentials
from aws_sdk_cloudsearch._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_cloudsearch._auth._zapros_handler import AuthMiddleware
from aws_sdk_cloudsearch._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.analysis_scheme
    import aws_sdk_cloudsearch.types.boolean
    import aws_sdk_cloudsearch.types.build_suggesters_request
    import aws_sdk_cloudsearch.types.build_suggesters_response
    import aws_sdk_cloudsearch.types.create_domain_request
    import aws_sdk_cloudsearch.types.create_domain_response
    import aws_sdk_cloudsearch.types.define_analysis_scheme_request
    import aws_sdk_cloudsearch.types.define_analysis_scheme_response
    import aws_sdk_cloudsearch.types.define_expression_request
    import aws_sdk_cloudsearch.types.define_expression_response
    import aws_sdk_cloudsearch.types.define_index_field_request
    import aws_sdk_cloudsearch.types.define_index_field_response
    import aws_sdk_cloudsearch.types.define_suggester_request
    import aws_sdk_cloudsearch.types.define_suggester_response
    import aws_sdk_cloudsearch.types.delete_analysis_scheme_request
    import aws_sdk_cloudsearch.types.delete_analysis_scheme_response
    import aws_sdk_cloudsearch.types.delete_domain_request
    import aws_sdk_cloudsearch.types.delete_domain_response
    import aws_sdk_cloudsearch.types.delete_expression_request
    import aws_sdk_cloudsearch.types.delete_expression_response
    import aws_sdk_cloudsearch.types.delete_index_field_request
    import aws_sdk_cloudsearch.types.delete_index_field_response
    import aws_sdk_cloudsearch.types.delete_suggester_request
    import aws_sdk_cloudsearch.types.delete_suggester_response
    import aws_sdk_cloudsearch.types.describe_analysis_schemes_request
    import aws_sdk_cloudsearch.types.describe_analysis_schemes_response
    import aws_sdk_cloudsearch.types.describe_availability_options_request
    import aws_sdk_cloudsearch.types.describe_availability_options_response
    import aws_sdk_cloudsearch.types.describe_domain_endpoint_options_request
    import aws_sdk_cloudsearch.types.describe_domain_endpoint_options_response
    import aws_sdk_cloudsearch.types.describe_domains_request
    import aws_sdk_cloudsearch.types.describe_domains_response
    import aws_sdk_cloudsearch.types.describe_expressions_request
    import aws_sdk_cloudsearch.types.describe_expressions_response
    import aws_sdk_cloudsearch.types.describe_index_fields_request
    import aws_sdk_cloudsearch.types.describe_index_fields_response
    import aws_sdk_cloudsearch.types.describe_scaling_parameters_request
    import aws_sdk_cloudsearch.types.describe_scaling_parameters_response
    import aws_sdk_cloudsearch.types.describe_service_access_policies_request
    import aws_sdk_cloudsearch.types.describe_service_access_policies_response
    import aws_sdk_cloudsearch.types.describe_suggesters_request
    import aws_sdk_cloudsearch.types.describe_suggesters_response
    import aws_sdk_cloudsearch.types.domain_endpoint_options
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.domain_name_list
    import aws_sdk_cloudsearch.types.dynamic_field_name
    import aws_sdk_cloudsearch.types.dynamic_field_name_list
    import aws_sdk_cloudsearch.types.expression
    import aws_sdk_cloudsearch.types.index_documents_request
    import aws_sdk_cloudsearch.types.index_documents_response
    import aws_sdk_cloudsearch.types.index_field
    import aws_sdk_cloudsearch.types.list_domain_names_response
    import aws_sdk_cloudsearch.types.policy_document
    import aws_sdk_cloudsearch.types.scaling_parameters
    import aws_sdk_cloudsearch.types.standard_name
    import aws_sdk_cloudsearch.types.standard_name_list
    import aws_sdk_cloudsearch.types.suggester
    import aws_sdk_cloudsearch.types.update_availability_options_request
    import aws_sdk_cloudsearch.types.update_availability_options_response
    import aws_sdk_cloudsearch.types.update_domain_endpoint_options_request
    import aws_sdk_cloudsearch.types.update_domain_endpoint_options_response
    import aws_sdk_cloudsearch.types.update_scaling_parameters_request
    import aws_sdk_cloudsearch.types.update_scaling_parameters_response
    import aws_sdk_cloudsearch.types.update_service_access_policies_request
    import aws_sdk_cloudsearch.types.update_service_access_policies_response


class AsyncCloudSearchClientConfig(TypedDict, total=False):
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


class AsyncCloudSearchClient:
    """A client for the ``CloudSearch`` service.

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
        self.config = AsyncCloudSearchClientConfig(
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
        self, config_overrides: Optional[AsyncCloudSearchClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCloudSearchClientConfig = config_overrides or {}
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
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def build_suggesters(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.build_suggesters_response.BuildSuggestersResponse":
        """<p>Indexes the search suggestions. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html#configuring-suggesters\">Configuring Suggesters</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.build_suggesters_request.BuildSuggestersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.build_suggesters_response.BuildSuggestersResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.build_suggesters

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.build_suggesters.async_build_suggesters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.build_suggesters_request.BuildSuggestersRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_domain(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a new search domain. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-domains.html\" target=\"_blank\">Creating a Search Domain</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>A name for the domain you are creating. Allowed characters are a-z (lower-case letters), 0-9, and hyphen (-). Domain names must start with a letter or number and be at least 3 and no more than 28 characters long.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.create_domain_request.CreateDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.create_domain_response.CreateDomainResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.create_domain

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.create_domain_request.CreateDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def define_analysis_scheme(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        analysis_scheme: "aws_sdk_cloudsearch.types.analysis_scheme.AnalysisScheme",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.define_analysis_scheme_response.DefineAnalysisSchemeResponse":
        """<p>Configures an analysis scheme that can be applied to a <code>text</code> or <code>text-array</code> field to define language-specific text processing options. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html\" target=\"_blank\">Configuring Analysis Schemes</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.define_analysis_scheme_request.DefineAnalysisSchemeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.define_analysis_scheme_response.DefineAnalysisSchemeResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.define_analysis_scheme

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.define_analysis_scheme.async_define_analysis_scheme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.define_analysis_scheme_request.DefineAnalysisSchemeRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["analysis_scheme"] = analysis_scheme

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def define_expression(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        expression: "aws_sdk_cloudsearch.types.expression.Expression",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> (
        "aws_sdk_cloudsearch.types.define_expression_response.DefineExpressionResponse"
    ):
        """<p>Configures an <code><a>Expression</a></code> for the search domain. Used to create new expressions and modify existing ones. If the expression exists, the new configuration replaces the old one. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html\" target=\"_blank\">Configuring Expressions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.define_expression_request.DefineExpressionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.define_expression_response.DefineExpressionResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.define_expression

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.define_expression.async_define_expression(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.define_expression_request.DefineExpressionRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["expression"] = expression

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def define_index_field(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        index_field: "aws_sdk_cloudsearch.types.index_field.IndexField",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> (
        "aws_sdk_cloudsearch.types.define_index_field_response.DefineIndexFieldResponse"
    ):
        """<p>Configures an <code><a>IndexField</a></code> for the search domain. Used to create new fields and modify existing ones. You must specify the name of the domain you are configuring and an index field configuration. The index field configuration specifies a unique name, the index field type, and the options you want to configure for the field. The options you can specify depend on the <code><a>IndexFieldType</a></code>. If the field exists, the new configuration replaces the old one. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html\" target=\"_blank\">Configuring Index Fields</a> in the <i>Amazon CloudSearch Developer Guide</i>. </p>

        Args:
            index_field: <p>The index field and field options you want to configure. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.define_index_field_request.DefineIndexFieldRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.define_index_field_response.DefineIndexFieldResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.define_index_field

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.define_index_field.async_define_index_field(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.define_index_field_request.DefineIndexFieldRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["index_field"] = index_field

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def define_suggester(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        suggester: "aws_sdk_cloudsearch.types.suggester.Suggester",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.define_suggester_response.DefineSuggesterResponse":
        """<p>Configures a suggester for a domain. A suggester enables you to display possible matches before users finish typing their queries. When you configure a suggester, you must specify the name of the text field you want to search for possible matches and a unique name for the suggester. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html\" target=\"_blank\">Getting Search Suggestions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.define_suggester_request.DefineSuggesterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.define_suggester_response.DefineSuggesterResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.define_suggester

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.define_suggester.async_define_suggester(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.define_suggester_request.DefineSuggesterRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["suggester"] = suggester

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_analysis_scheme(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        analysis_scheme_name: "aws_sdk_cloudsearch.types.standard_name.StandardName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.delete_analysis_scheme_response.DeleteAnalysisSchemeResponse":
        """<p>Deletes an analysis scheme. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html\" target=\"_blank\">Configuring Analysis Schemes</a> in the <i>Amazon CloudSearch Developer Guide</i>. </p>

        Args:
            analysis_scheme_name: <p>The name of the analysis scheme you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.delete_analysis_scheme_request.DeleteAnalysisSchemeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.delete_analysis_scheme_response.DeleteAnalysisSchemeResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.delete_analysis_scheme

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.delete_analysis_scheme.async_delete_analysis_scheme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.delete_analysis_scheme_request.DeleteAnalysisSchemeRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["analysis_scheme_name"] = analysis_scheme_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_domain(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.delete_domain_response.DeleteDomainResponse":
        """<p>Permanently deletes a search domain and all of its data. Once a domain has been deleted, it cannot be recovered. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/deleting-domains.html\" target=\"_blank\">Deleting a Search Domain</a> in the <i>Amazon CloudSearch Developer Guide</i>. </p>

        Args:
            domain_name: <p>The name of the domain you want to permanently delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.delete_domain_request.DeleteDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.delete_domain

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.delete_domain_request.DeleteDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_expression(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        expression_name: "aws_sdk_cloudsearch.types.standard_name.StandardName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> (
        "aws_sdk_cloudsearch.types.delete_expression_response.DeleteExpressionResponse"
    ):
        """<p>Removes an <code><a>Expression</a></code> from the search domain. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html\" target=\"_blank\">Configuring Expressions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            expression_name: <p>The name of the <code><a>Expression</a></code> to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.delete_expression_request.DeleteExpressionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.delete_expression_response.DeleteExpressionResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.delete_expression

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.delete_expression.async_delete_expression(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.delete_expression_request.DeleteExpressionRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["expression_name"] = expression_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_index_field(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        index_field_name: "aws_sdk_cloudsearch.types.dynamic_field_name.DynamicFieldName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> (
        "aws_sdk_cloudsearch.types.delete_index_field_response.DeleteIndexFieldResponse"
    ):
        """<p>Removes an <code><a>IndexField</a></code> from the search domain. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html\" target=\"_blank\">Configuring Index Fields</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            index_field_name: <p>The name of the index field your want to remove from the domain's indexing options.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.delete_index_field_request.DeleteIndexFieldRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.delete_index_field_response.DeleteIndexFieldResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.delete_index_field

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.delete_index_field.async_delete_index_field(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.delete_index_field_request.DeleteIndexFieldRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["index_field_name"] = index_field_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_suggester(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        suggester_name: "aws_sdk_cloudsearch.types.standard_name.StandardName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.delete_suggester_response.DeleteSuggesterResponse":
        """<p>Deletes a suggester. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html\" target=\"_blank\">Getting Search Suggestions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            suggester_name: <p>Specifies the name of the suggester you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.delete_suggester_request.DeleteSuggesterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.delete_suggester_response.DeleteSuggesterResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.delete_suggester

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.delete_suggester.async_delete_suggester(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.delete_suggester_request.DeleteSuggesterRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["suggester_name"] = suggester_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_analysis_schemes(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
        analysis_scheme_names: Optional[
            "aws_sdk_cloudsearch.types.standard_name_list.StandardNameList"
        ] = None,
        deployed: Optional["aws_sdk_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_cloudsearch.types.describe_analysis_schemes_response.DescribeAnalysisSchemesResponse":
        """<p>Gets the analysis schemes configured for a domain. An analysis scheme defines language-specific text processing options for a <code>text</code> field. Can be limited to specific analysis schemes by name. By default, shows all analysis schemes and includes any pending changes to the configuration. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html\" target=\"_blank\">Configuring Analysis Schemes</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            analysis_scheme_names: <p>The analysis schemes you want to describe.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.describe_analysis_schemes_request.DescribeAnalysisSchemesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.describe_analysis_schemes_response.DescribeAnalysisSchemesResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_analysis_schemes

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_analysis_schemes.async_describe_analysis_schemes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.describe_analysis_schemes_request.DescribeAnalysisSchemesRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if analysis_scheme_names is not None:
            input["analysis_scheme_names"] = analysis_scheme_names
        if deployed is not None:
            input["deployed"] = deployed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_availability_options(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
        deployed: Optional["aws_sdk_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_cloudsearch.types.describe_availability_options_response.DescribeAvailabilityOptionsResponse":
        """<p>Gets the availability options configured for a domain. By default, shows the configuration with any pending changes. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-availability-options.html\" target=\"_blank\">Configuring Availability Options</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.describe_availability_options_request.DescribeAvailabilityOptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.describe_availability_options_response.DescribeAvailabilityOptionsResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_availability_options

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_availability_options.async_describe_availability_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.describe_availability_options_request.DescribeAvailabilityOptionsRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if deployed is not None:
            input["deployed"] = deployed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_domain_endpoint_options(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
        deployed: Optional["aws_sdk_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_cloudsearch.types.describe_domain_endpoint_options_response.DescribeDomainEndpointOptionsResponse":
        """<p>Returns the domain's endpoint options, specifically whether all requests to the domain must arrive over HTTPS. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-domain-endpoint-options.html\" target=\"_blank\">Configuring Domain Endpoint Options</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>A string that represents the name of a domain.</p>
            deployed: <p>Whether to retrieve the latest configuration (which might be in a Processing state) or the current, active configuration. Defaults to <code>false</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.describe_domain_endpoint_options_request.DescribeDomainEndpointOptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.describe_domain_endpoint_options_response.DescribeDomainEndpointOptionsResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_domain_endpoint_options

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_domain_endpoint_options.async_describe_domain_endpoint_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.describe_domain_endpoint_options_request.DescribeDomainEndpointOptionsRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if deployed is not None:
            input["deployed"] = deployed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_domains(
        self,
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
        domain_names: Optional[
            "aws_sdk_cloudsearch.types.domain_name_list.DomainNameList"
        ] = None,
    ) -> "aws_sdk_cloudsearch.types.describe_domains_response.DescribeDomainsResponse":
        """<p>Gets information about the search domains owned by this account. Can be limited to specific domains. Shows all domains by default. To get the number of searchable documents in a domain, use the console or submit a <code>matchall</code> request to your domain's search endpoint: <code>q=matchall&amp;q.parser=structured&amp;size=0</code>. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-domain-info.html\" target=\"_blank\">Getting Information about a Search Domain</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_names: <p>The names of the domains you want to include in the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.describe_domains_request.DescribeDomainsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.describe_domains_response.DescribeDomainsResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_domains

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_domains.async_describe_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.describe_domains_request.DescribeDomainsRequest = {}  # type: ignore[typeddict-item]
        if domain_names is not None:
            input["domain_names"] = domain_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_expressions(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
        expression_names: Optional[
            "aws_sdk_cloudsearch.types.standard_name_list.StandardNameList"
        ] = None,
        deployed: Optional["aws_sdk_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_cloudsearch.types.describe_expressions_response.DescribeExpressionsResponse":
        """<p>Gets the expressions configured for the search domain. Can be limited to specific expressions by name. By default, shows all expressions and includes any pending changes to the configuration. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html\" target=\"_blank\">Configuring Expressions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            expression_names: <p>Limits the <code><a>DescribeExpressions</a></code> response to the specified expressions. If not specified, all expressions are shown.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.describe_expressions_request.DescribeExpressionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.describe_expressions_response.DescribeExpressionsResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_expressions

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_expressions.async_describe_expressions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.describe_expressions_request.DescribeExpressionsRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if expression_names is not None:
            input["expression_names"] = expression_names
        if deployed is not None:
            input["deployed"] = deployed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_index_fields(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
        field_names: Optional[
            "aws_sdk_cloudsearch.types.dynamic_field_name_list.DynamicFieldNameList"
        ] = None,
        deployed: Optional["aws_sdk_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_cloudsearch.types.describe_index_fields_response.DescribeIndexFieldsResponse":
        """<p>Gets information about the index fields configured for the search domain. Can be limited to specific fields by name. By default, shows all fields and includes any pending changes to the configuration. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-domain-info.html\" target=\"_blank\">Getting Domain Information</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            field_names: <p>A list of the index fields you want to describe. If not specified, information is returned for all configured index fields.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.describe_index_fields_request.DescribeIndexFieldsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.describe_index_fields_response.DescribeIndexFieldsResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_index_fields

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_index_fields.async_describe_index_fields(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.describe_index_fields_request.DescribeIndexFieldsRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if field_names is not None:
            input["field_names"] = field_names
        if deployed is not None:
            input["deployed"] = deployed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_scaling_parameters(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.describe_scaling_parameters_response.DescribeScalingParametersResponse":
        """<p>Gets the scaling parameters configured for a domain. A domain's scaling parameters specify the desired search instance type and replication count. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-scaling-options.html\" target=\"_blank\">Configuring Scaling Options</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.describe_scaling_parameters_request.DescribeScalingParametersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.describe_scaling_parameters_response.DescribeScalingParametersResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_scaling_parameters

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_scaling_parameters.async_describe_scaling_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.describe_scaling_parameters_request.DescribeScalingParametersRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_service_access_policies(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
        deployed: Optional["aws_sdk_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_cloudsearch.types.describe_service_access_policies_response.DescribeServiceAccessPoliciesResponse":
        """<p>Gets information about the access policies that control access to the domain's document and search endpoints. By default, shows the configuration with any pending changes. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html\" target=\"_blank\">Configuring Access for a Search Domain</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.describe_service_access_policies_request.DescribeServiceAccessPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.describe_service_access_policies_response.DescribeServiceAccessPoliciesResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_service_access_policies

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_service_access_policies.async_describe_service_access_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.describe_service_access_policies_request.DescribeServiceAccessPoliciesRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if deployed is not None:
            input["deployed"] = deployed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_suggesters(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
        suggester_names: Optional[
            "aws_sdk_cloudsearch.types.standard_name_list.StandardNameList"
        ] = None,
        deployed: Optional["aws_sdk_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_cloudsearch.types.describe_suggesters_response.DescribeSuggestersResponse":
        """<p>Gets the suggesters configured for a domain. A suggester enables you to display possible matches before users finish typing their queries. Can be limited to specific suggesters by name. By default, shows all suggesters and includes any pending changes to the configuration. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html\" target=\"_blank\">Getting Search Suggestions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            suggester_names: <p>The suggesters you want to describe.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.describe_suggesters_request.DescribeSuggestersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.describe_suggesters_response.DescribeSuggestersResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_suggesters

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.describe_suggesters.async_describe_suggesters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.describe_suggesters_request.DescribeSuggestersRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if suggester_names is not None:
            input["suggester_names"] = suggester_names
        if deployed is not None:
            input["deployed"] = deployed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def index_documents(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.index_documents_response.IndexDocumentsResponse":
        """<p>Tells the search domain to start indexing its documents using the latest indexing options. This operation must be invoked to activate options whose <a>OptionStatus</a> is <code>RequiresIndexDocuments</code>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.index_documents_request.IndexDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.index_documents_response.IndexDocumentsResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.index_documents

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.index_documents.async_index_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.index_documents_request.IndexDocumentsRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_domain_names(
        self, *, config_overrides: Optional[AsyncCloudSearchClientConfig] = None
    ) -> "aws_sdk_cloudsearch.types.list_domain_names_response.ListDomainNamesResponse":
        """<p>Lists all search domains owned by an account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.list_domain_names_response.ListDomainNamesResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.list_domain_names

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.list_domain_names.async_list_domain_names(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_availability_options(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        multi_az: "aws_sdk_cloudsearch.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.update_availability_options_response.UpdateAvailabilityOptionsResponse":
        """<p>Configures the availability options for a domain. Enabling the Multi-AZ option expands an Amazon CloudSearch domain to an additional Availability Zone in the same Region to increase fault tolerance in the event of a service disruption. Changes to the Multi-AZ option can take about half an hour to become active. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-availability-options.html\" target=\"_blank\">Configuring Availability Options</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            multi_az: <p>You expand an existing search domain to a second Availability Zone by setting the Multi-AZ option to true. Similarly, you can turn off the Multi-AZ option to downgrade the domain to a single Availability Zone by setting the Multi-AZ option to <code>false</code>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.update_availability_options_request.UpdateAvailabilityOptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.update_availability_options_response.UpdateAvailabilityOptionsResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.update_availability_options

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.update_availability_options.async_update_availability_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.update_availability_options_request.UpdateAvailabilityOptionsRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["multi_az"] = multi_az

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_domain_endpoint_options(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        domain_endpoint_options: "aws_sdk_cloudsearch.types.domain_endpoint_options.DomainEndpointOptions",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.update_domain_endpoint_options_response.UpdateDomainEndpointOptionsResponse":
        """<p>Updates the domain's endpoint options, specifically whether all requests to the domain must arrive over HTTPS. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-domain-endpoint-options.html\" target=\"_blank\">Configuring Domain Endpoint Options</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>A string that represents the name of a domain.</p>
            domain_endpoint_options: <p>Whether to require that all requests to the domain arrive over HTTPS. We recommend Policy-Min-TLS-1-2-2019-07 for TLSSecurityPolicy. For compatibility with older clients, the default is Policy-Min-TLS-1-0-2019-07. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.update_domain_endpoint_options_request.UpdateDomainEndpointOptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.update_domain_endpoint_options_response.UpdateDomainEndpointOptionsResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.update_domain_endpoint_options

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.update_domain_endpoint_options.async_update_domain_endpoint_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.update_domain_endpoint_options_request.UpdateDomainEndpointOptionsRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["domain_endpoint_options"] = domain_endpoint_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_scaling_parameters(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        scaling_parameters: "aws_sdk_cloudsearch.types.scaling_parameters.ScalingParameters",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.update_scaling_parameters_response.UpdateScalingParametersResponse":
        """<p>Configures scaling parameters for a domain. A domain's scaling parameters specify the desired search instance type and replication count. Amazon CloudSearch will still automatically scale your domain based on the volume of data and traffic, but not below the desired instance type and replication count. If the Multi-AZ option is enabled, these values control the resources used per Availability Zone. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-scaling-options.html\" target=\"_blank\">Configuring Scaling Options</a> in the <i>Amazon CloudSearch Developer Guide</i>. </p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.update_scaling_parameters_request.UpdateScalingParametersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.update_scaling_parameters_response.UpdateScalingParametersResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.update_scaling_parameters

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.update_scaling_parameters.async_update_scaling_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.update_scaling_parameters_request.UpdateScalingParametersRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["scaling_parameters"] = scaling_parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_service_access_policies(
        self,
        domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName",
        access_policies: "aws_sdk_cloudsearch.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[AsyncCloudSearchClientConfig] = None,
    ) -> "aws_sdk_cloudsearch.types.update_service_access_policies_response.UpdateServiceAccessPoliciesResponse":
        """<p>Configures the access rules that control access to the domain's document and search endpoints. For more information, see <a href=\"http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html\" target=\"_blank\"> Configuring Access for an Amazon CloudSearch Domain</a>.</p>

        Args:
            access_policies: <p>The access rules you want to configure. These rules replace any existing rules. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudsearch.types.update_service_access_policies_request.UpdateServiceAccessPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudsearch.types.update_service_access_policies_response.UpdateServiceAccessPoliciesResponse"
        ]:
            import aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.update_service_access_policies

            (
                output,
                http_response,
            ) = await aws_sdk_cloudsearch._operations.a9_search_cloud_config_service2013.update_service_access_policies.async_update_service_access_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_cloudsearch.types.update_service_access_policies_request.UpdateServiceAccessPoliciesRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["access_policies"] = access_policies

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
