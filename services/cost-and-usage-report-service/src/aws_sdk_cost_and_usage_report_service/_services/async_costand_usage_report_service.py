"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#AWSOrigamiServiceGatewayService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_cost_and_usage_report_service._auth._signers
import aws_sdk_cost_and_usage_report_service._auth._sigv4
from aws_sdk_cost_and_usage_report_service._auth._identity import Credentials
from aws_sdk_cost_and_usage_report_service._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_cost_and_usage_report_service._auth._zapros_handler import AuthMiddleware
from aws_sdk_cost_and_usage_report_service._services._aws_config import aaws_config
from aws_sdk_cost_and_usage_report_service._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_cost_and_usage_report_service.types.delete_report_definition_request
    import aws_sdk_cost_and_usage_report_service.types.delete_report_definition_response
    import aws_sdk_cost_and_usage_report_service.types.describe_report_definitions_request
    import aws_sdk_cost_and_usage_report_service.types.describe_report_definitions_response
    import aws_sdk_cost_and_usage_report_service.types.generic_string
    import aws_sdk_cost_and_usage_report_service.types.list_tags_for_resource_request
    import aws_sdk_cost_and_usage_report_service.types.list_tags_for_resource_response
    import aws_sdk_cost_and_usage_report_service.types.max_results
    import aws_sdk_cost_and_usage_report_service.types.modify_report_definition_request
    import aws_sdk_cost_and_usage_report_service.types.modify_report_definition_response
    import aws_sdk_cost_and_usage_report_service.types.put_report_definition_request
    import aws_sdk_cost_and_usage_report_service.types.put_report_definition_response
    import aws_sdk_cost_and_usage_report_service.types.report_definition
    import aws_sdk_cost_and_usage_report_service.types.report_name
    import aws_sdk_cost_and_usage_report_service.types.tag_key_list
    import aws_sdk_cost_and_usage_report_service.types.tag_list
    import aws_sdk_cost_and_usage_report_service.types.tag_resource_request
    import aws_sdk_cost_and_usage_report_service.types.tag_resource_response
    import aws_sdk_cost_and_usage_report_service.types.untag_resource_request
    import aws_sdk_cost_and_usage_report_service.types.untag_resource_response


class AsyncCostandUsageReportServiceClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncCostandUsageReportServiceClient:
    """A client for the ``CostandUsageReportService`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncCostandUsageReportServiceClientConfig(
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
        self,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCostandUsageReportServiceClientConfig = config_overrides or {}
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

    async def delete_report_definition(
        self,
        report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> "aws_sdk_cost_and_usage_report_service.types.delete_report_definition_response.DeleteReportDefinitionResponse":
        """<p>Deletes the specified report. Any tags associated with the report are also deleted.</p>

        Args:
            report_name: <p>The name of the report that you want to delete. The name must be unique, is case sensitive, and can't include spaces.</p>

        Examples:
            To delete the AWS Cost and Usage report named ExampleReport.
            The following example deletes the AWS Cost and Usage report named ExampleReport.

            >>> await client.delete_report_definition(report_name='ExampleReport')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cost_and_usage_report_service.types.delete_report_definition_request.DeleteReportDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cost_and_usage_report_service.types.delete_report_definition_response.DeleteReportDefinitionResponse"
        ]:
            import aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.delete_report_definition

            (
                output,
                http_response,
            ) = await aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.delete_report_definition.async_delete_report_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cost_and_usage_report_service.types.delete_report_definition_request.DeleteReportDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["report_name"] = report_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_report_definitions(
        self,
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
        max_results: Optional[
            "aws_sdk_cost_and_usage_report_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_cost_and_usage_report_service.types.generic_string.GenericString"
        ] = None,
    ) -> "aws_sdk_cost_and_usage_report_service.types.describe_report_definitions_response.DescribeReportDefinitionsResponse":
        """<p>Lists the Amazon Web Services Cost and Usage Report available to this account.</p>

        Examples:
            To list the AWS Cost and Usage reports for the account.
            The following example lists the AWS Cost and Usage reports for the account.

            >>> await client.describe_report_definitions(max_results=5)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cost_and_usage_report_service.types.describe_report_definitions_request.DescribeReportDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cost_and_usage_report_service.types.describe_report_definitions_response.DescribeReportDefinitionsResponse"
        ]:
            import aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.describe_report_definitions

            (
                output,
                http_response,
            ) = await aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.describe_report_definitions.async_describe_report_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cost_and_usage_report_service.types.describe_report_definitions_request.DescribeReportDefinitionsRequest = {}  # type: ignore[typeddict-item]
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

    async def list_tags_for_resource(
        self,
        report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> "aws_sdk_cost_and_usage_report_service.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with the specified report definition.</p>

        Args:
            report_name: <p>The report name of the report definition that tags are to be returned for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cost_and_usage_report_service.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cost_and_usage_report_service.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cost_and_usage_report_service.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["report_name"] = report_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def modify_report_definition(
        self,
        report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName",
        report_definition: "aws_sdk_cost_and_usage_report_service.types.report_definition.ReportDefinition",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> "aws_sdk_cost_and_usage_report_service.types.modify_report_definition_response.ModifyReportDefinitionResponse":
        """<p>Allows you to programmatically update your report preferences.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cost_and_usage_report_service.types.modify_report_definition_request.ModifyReportDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cost_and_usage_report_service.types.modify_report_definition_response.ModifyReportDefinitionResponse"
        ]:
            import aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.modify_report_definition

            (
                output,
                http_response,
            ) = await aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.modify_report_definition.async_modify_report_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cost_and_usage_report_service.types.modify_report_definition_request.ModifyReportDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["report_name"] = report_name
        input_["report_definition"] = report_definition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_report_definition(
        self,
        report_definition: "aws_sdk_cost_and_usage_report_service.types.report_definition.ReportDefinition",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
        tags: Optional[
            "aws_sdk_cost_and_usage_report_service.types.tag_list.TagList"
        ] = None,
    ) -> "aws_sdk_cost_and_usage_report_service.types.put_report_definition_response.PutReportDefinitionResponse":
        """<p>Creates a new report using the description that you provide.</p>

        Args:
            report_definition: <p>Represents the output of the PutReportDefinition operation. The content consists of the detailed metadata and data file information. </p>
            tags: <p>The tags to be assigned to the report definition resource.</p>

        Examples:
            To create a report named ExampleReport.
            The following example creates a AWS Cost and Usage report named ExampleReport.

            >>> await client.put_report_definition(report_definition={'ReportName': 'ExampleReport', 'TimeUnit': 'DAILY', 'Format': 'textORcsv', 'Compression': 'ZIP', 'AdditionalSchemaElements': ['RESOURCES'], 'S3Bucket': 'example-s3-bucket', 'S3Prefix': 'exampleprefix', 'S3Region': 'us-east-1', 'AdditionalArtifacts': ['REDSHIFT', 'QUICKSIGHT']})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cost_and_usage_report_service.types.put_report_definition_request.PutReportDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cost_and_usage_report_service.types.put_report_definition_response.PutReportDefinitionResponse"
        ]:
            import aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.put_report_definition

            (
                output,
                http_response,
            ) = await aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.put_report_definition.async_put_report_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cost_and_usage_report_service.types.put_report_definition_request.PutReportDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["report_definition"] = report_definition
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName",
        tags: "aws_sdk_cost_and_usage_report_service.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> "aws_sdk_cost_and_usage_report_service.types.tag_resource_response.TagResourceResponse":
        """<p>Associates a set of tags with a report definition.</p>

        Args:
            report_name: <p>The report name of the report definition that tags are to be associated with.</p>
            tags: <p>The tags to be assigned to the report definition resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cost_and_usage_report_service.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cost_and_usage_report_service.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cost_and_usage_report_service.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["report_name"] = report_name
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        report_name: "aws_sdk_cost_and_usage_report_service.types.report_name.ReportName",
        tag_keys: "aws_sdk_cost_and_usage_report_service.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncCostandUsageReportServiceClientConfig] = None,
    ) -> "aws_sdk_cost_and_usage_report_service.types.untag_resource_response.UntagResourceResponse":
        """<p>Disassociates a set of tags from a report definition.</p>

        Args:
            report_name: <p>The report name of the report definition that tags are to be disassociated from.</p>
            tag_keys: <p>The tags to be disassociated from the report definition resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cost_and_usage_report_service.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cost_and_usage_report_service.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cost_and_usage_report_service._operations.aws_origami_service_gateway_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cost_and_usage_report_service.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["report_name"] = report_name
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
