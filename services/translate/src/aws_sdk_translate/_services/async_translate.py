"""Generated from Smithy shape ``com.amazonaws.translate#AWSShineFrontendService_20170701``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_translate._auth._signers
import aws_sdk_translate._auth._sigv4
from aws_sdk_translate._auth._identity import Credentials
from aws_sdk_translate._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_translate._auth._zapros_handler import AuthMiddleware
from aws_sdk_translate._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_translate.types.bounded_length_string
    import aws_sdk_translate.types.client_token_string
    import aws_sdk_translate.types.create_parallel_data_request
    import aws_sdk_translate.types.create_parallel_data_response
    import aws_sdk_translate.types.delete_parallel_data_request
    import aws_sdk_translate.types.delete_parallel_data_response
    import aws_sdk_translate.types.delete_terminology_request
    import aws_sdk_translate.types.describe_text_translation_job_request
    import aws_sdk_translate.types.describe_text_translation_job_response
    import aws_sdk_translate.types.description
    import aws_sdk_translate.types.display_language_code
    import aws_sdk_translate.types.document
    import aws_sdk_translate.types.encryption_key
    import aws_sdk_translate.types.get_parallel_data_request
    import aws_sdk_translate.types.get_parallel_data_response
    import aws_sdk_translate.types.get_terminology_request
    import aws_sdk_translate.types.get_terminology_response
    import aws_sdk_translate.types.iam_role_arn
    import aws_sdk_translate.types.import_terminology_request
    import aws_sdk_translate.types.import_terminology_response
    import aws_sdk_translate.types.input_data_config
    import aws_sdk_translate.types.job_id
    import aws_sdk_translate.types.job_name
    import aws_sdk_translate.types.language_code_string
    import aws_sdk_translate.types.list_languages_request
    import aws_sdk_translate.types.list_languages_response
    import aws_sdk_translate.types.list_parallel_data_request
    import aws_sdk_translate.types.list_parallel_data_response
    import aws_sdk_translate.types.list_tags_for_resource_request
    import aws_sdk_translate.types.list_tags_for_resource_response
    import aws_sdk_translate.types.list_terminologies_request
    import aws_sdk_translate.types.list_terminologies_response
    import aws_sdk_translate.types.list_text_translation_jobs_request
    import aws_sdk_translate.types.list_text_translation_jobs_response
    import aws_sdk_translate.types.max_results_integer
    import aws_sdk_translate.types.merge_strategy
    import aws_sdk_translate.types.next_token
    import aws_sdk_translate.types.output_data_config
    import aws_sdk_translate.types.parallel_data_config
    import aws_sdk_translate.types.resource_arn
    import aws_sdk_translate.types.resource_name
    import aws_sdk_translate.types.resource_name_list
    import aws_sdk_translate.types.start_text_translation_job_request
    import aws_sdk_translate.types.start_text_translation_job_response
    import aws_sdk_translate.types.stop_text_translation_job_request
    import aws_sdk_translate.types.stop_text_translation_job_response
    import aws_sdk_translate.types.tag_key_list
    import aws_sdk_translate.types.tag_list
    import aws_sdk_translate.types.tag_resource_request
    import aws_sdk_translate.types.tag_resource_response
    import aws_sdk_translate.types.target_language_code_string_list
    import aws_sdk_translate.types.terminology_data
    import aws_sdk_translate.types.terminology_data_format
    import aws_sdk_translate.types.text_translation_job_filter
    import aws_sdk_translate.types.translate_document_request
    import aws_sdk_translate.types.translate_document_response
    import aws_sdk_translate.types.translate_text_request
    import aws_sdk_translate.types.translate_text_response
    import aws_sdk_translate.types.translation_settings
    import aws_sdk_translate.types.untag_resource_request
    import aws_sdk_translate.types.untag_resource_response
    import aws_sdk_translate.types.update_parallel_data_request
    import aws_sdk_translate.types.update_parallel_data_response


class AsyncTranslateClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncTranslateClient:
    """A client for the ``Translate`` service.

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
        self._config = AsyncTranslateClientConfig(
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
        self, config_overrides: Optional[AsyncTranslateClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTranslateClientConfig = config_overrides or {}
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

    async def create_parallel_data(
        self,
        name: "aws_sdk_translate.types.resource_name.ResourceName",
        parallel_data_config: "aws_sdk_translate.types.parallel_data_config.ParallelDataConfig",
        client_token: "aws_sdk_translate.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        description: Optional["aws_sdk_translate.types.description.Description"] = None,
        encryption_key: Optional[
            "aws_sdk_translate.types.encryption_key.EncryptionKey"
        ] = None,
        tags: Optional["aws_sdk_translate.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_translate.types.create_parallel_data_response.CreateParallelDataResponse":
        r"""<p>Creates a parallel data resource in Amazon Translate by importing an input file from Amazon S3. Parallel data files contain examples that show how you want segments of text to be translated. By adding parallel data, you can influence the style, tone, and word choice in your translation output.</p>

        Args:
            name: <p>A custom name for the parallel data resource in Amazon Translate. You must assign a name that is unique in the account and region.</p>
            description: <p>A custom description for the parallel data resource in Amazon Translate.</p>
            parallel_data_config: <p>Specifies the format and S3 location of the parallel data input file.</p>
            client_token: <p>A unique identifier for the request. This token is automatically generated when you use Amazon Translate through an AWS SDK.</p>
            tags: <p>Tags to be associated with this resource. A tag is a key-value pair that adds metadata to a resource. Each tag key for the resource must be unique. For more information, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/tagging.html\"> Tagging your resources</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.create_parallel_data_request.CreateParallelDataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.create_parallel_data_response.CreateParallelDataResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.create_parallel_data

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.create_parallel_data.async_create_parallel_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.create_parallel_data_request.CreateParallelDataRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["parallel_data_config"] = parallel_data_config
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_parallel_data(
        self,
        name: "aws_sdk_translate.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
    ) -> "aws_sdk_translate.types.delete_parallel_data_response.DeleteParallelDataResponse":
        """<p>Deletes a parallel data resource in Amazon Translate.</p>

        Args:
            name: <p>The name of the parallel data resource that is being deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.delete_parallel_data_request.DeleteParallelDataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.delete_parallel_data_response.DeleteParallelDataResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.delete_parallel_data

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.delete_parallel_data.async_delete_parallel_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.delete_parallel_data_request.DeleteParallelDataRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_terminology(
        self,
        name: "aws_sdk_translate.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
    ) -> None:
        """<p>A synchronous action that deletes a custom terminology.</p>

        Args:
            name: <p>The name of the custom terminology being deleted. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.delete_terminology_request.DeleteTerminologyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.delete_terminology

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.delete_terminology.async_delete_terminology(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.delete_terminology_request.DeleteTerminologyRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_text_translation_job(
        self,
        job_id: "aws_sdk_translate.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
    ) -> "aws_sdk_translate.types.describe_text_translation_job_response.DescribeTextTranslationJobResponse":
        """<p>Gets the properties associated with an asynchronous batch translation job including name, ID, status, source and target languages, input/output S3 buckets, and so on.</p>

        Args:
            job_id: <p>The identifier that Amazon Translate generated for the job. The <a>StartTextTranslationJob</a> operation returns this identifier in its response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.describe_text_translation_job_request.DescribeTextTranslationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.describe_text_translation_job_response.DescribeTextTranslationJobResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.describe_text_translation_job

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.describe_text_translation_job.async_describe_text_translation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.describe_text_translation_job_request.DescribeTextTranslationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_parallel_data(
        self,
        name: "aws_sdk_translate.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
    ) -> "aws_sdk_translate.types.get_parallel_data_response.GetParallelDataResponse":
        """<p>Provides information about a parallel data resource.</p>

        Args:
            name: <p>The name of the parallel data resource that is being retrieved.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.get_parallel_data_request.GetParallelDataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.get_parallel_data_response.GetParallelDataResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.get_parallel_data

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.get_parallel_data.async_get_parallel_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.get_parallel_data_request.GetParallelDataRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_terminology(
        self,
        name: "aws_sdk_translate.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        terminology_data_format: Optional[
            "aws_sdk_translate.types.terminology_data_format.TerminologyDataFormat"
        ] = None,
    ) -> "aws_sdk_translate.types.get_terminology_response.GetTerminologyResponse":
        """<p>Retrieves a custom terminology.</p>

        Args:
            name: <p>The name of the custom terminology being retrieved.</p>
            terminology_data_format: <p>The data format of the custom terminology being retrieved.</p> <p>If you don't specify this parameter, Amazon Translate returns a file with the same format as the file that was imported to create the terminology. </p> <p>If you specify this parameter when you retrieve a multi-directional terminology resource, you must specify the same format as the input file that was imported to create it. Otherwise, Amazon Translate throws an error.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.get_terminology_request.GetTerminologyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.get_terminology_response.GetTerminologyResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.get_terminology

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.get_terminology.async_get_terminology(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.get_terminology_request.GetTerminologyRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if terminology_data_format is not None:
            input_["terminology_data_format"] = terminology_data_format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_terminology(
        self,
        name: "aws_sdk_translate.types.resource_name.ResourceName",
        merge_strategy: "aws_sdk_translate.types.merge_strategy.MergeStrategy",
        terminology_data: "aws_sdk_translate.types.terminology_data.TerminologyData",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        description: Optional["aws_sdk_translate.types.description.Description"] = None,
        encryption_key: Optional[
            "aws_sdk_translate.types.encryption_key.EncryptionKey"
        ] = None,
        tags: Optional["aws_sdk_translate.types.tag_list.TagList"] = None,
    ) -> (
        "aws_sdk_translate.types.import_terminology_response.ImportTerminologyResponse"
    ):
        r"""<p>Creates or updates a custom terminology, depending on whether one already exists for the given terminology name. Importing a terminology with the same name as an existing one will merge the terminologies based on the chosen merge strategy. The only supported merge strategy is OVERWRITE, where the imported terminology overwrites the existing terminology of the same name.</p> <p>If you import a terminology that overwrites an existing one, the new terminology takes up to 10 minutes to fully propagate. After that, translations have access to the new terminology.</p>

        Args:
            name: <p>The name of the custom terminology being imported.</p>
            merge_strategy: <p>The merge strategy of the custom terminology being imported. Currently, only the OVERWRITE merge strategy is supported. In this case, the imported terminology will overwrite an existing terminology of the same name.</p>
            description: <p>The description of the custom terminology being imported.</p>
            terminology_data: <p>The terminology data for the custom terminology being imported.</p>
            encryption_key: <p>The encryption key for the custom terminology being imported.</p>
            tags: <p>Tags to be associated with this resource. A tag is a key-value pair that adds metadata to a resource. Each tag key for the resource must be unique. For more information, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/tagging.html\"> Tagging your resources</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.import_terminology_request.ImportTerminologyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.import_terminology_response.ImportTerminologyResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.import_terminology

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.import_terminology.async_import_terminology(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.import_terminology_request.ImportTerminologyRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["merge_strategy"] = merge_strategy
        if description is not None:
            input_["description"] = description
        input_["terminology_data"] = terminology_data
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_languages(
        self,
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        display_language_code: Optional[
            "aws_sdk_translate.types.display_language_code.DisplayLanguageCode"
        ] = None,
        next_token: Optional["aws_sdk_translate.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_translate.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "aws_sdk_translate.types.list_languages_response.ListLanguagesResponse":
        """<p>Provides a list of languages (RFC-5646 codes and names) that Amazon Translate supports.</p>

        Args:
            display_language_code: <p>The language code for the language to use to display the language names in the response. The language code is <code>en</code> by default. </p>
            next_token: <p>Include the NextToken value to fetch the next group of supported languages. </p>
            max_results: <p>The maximum number of results to return in each response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.list_languages_request.ListLanguagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.list_languages_response.ListLanguagesResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.list_languages

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.list_languages.async_list_languages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.list_languages_request.ListLanguagesRequest = {}  # type: ignore[typeddict-item]
        if display_language_code is not None:
            input_["display_language_code"] = display_language_code
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_parallel_data(
        self,
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        next_token: Optional["aws_sdk_translate.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_translate.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "aws_sdk_translate.types.list_parallel_data_response.ListParallelDataResponse":
        """<p>Provides a list of your parallel data resources in Amazon Translate.</p>

        Args:
            next_token: <p>A string that specifies the next page of results to return in a paginated response.</p>
            max_results: <p>The maximum number of parallel data resources returned for each request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.list_parallel_data_request.ListParallelDataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.list_parallel_data_response.ListParallelDataResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.list_parallel_data

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.list_parallel_data.async_list_parallel_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.list_parallel_data_request.ListParallelDataRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_translate.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
    ) -> "aws_sdk_translate.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        r"""<p>Lists all tags associated with a given Amazon Translate resource. For more information, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/tagging.html\"> Tagging your resources</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the given Amazon Translate resource you are querying. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_terminologies(
        self,
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        next_token: Optional["aws_sdk_translate.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_translate.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> (
        "aws_sdk_translate.types.list_terminologies_response.ListTerminologiesResponse"
    ):
        """<p>Provides a list of custom terminologies associated with your account.</p>

        Args:
            next_token: <p>If the result of the request to ListTerminologies was truncated, include the NextToken to fetch the next group of custom terminologies. </p>
            max_results: <p>The maximum number of custom terminologies returned per list request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.list_terminologies_request.ListTerminologiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.list_terminologies_response.ListTerminologiesResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.list_terminologies

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.list_terminologies.async_list_terminologies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.list_terminologies_request.ListTerminologiesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_text_translation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        filter: Optional[
            "aws_sdk_translate.types.text_translation_job_filter.TextTranslationJobFilter"
        ] = None,
        next_token: Optional["aws_sdk_translate.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_translate.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "aws_sdk_translate.types.list_text_translation_jobs_response.ListTextTranslationJobsResponse":
        """<p>Gets a list of the batch translation jobs that you have submitted.</p>

        Args:
            filter: <p>The parameters that specify which batch translation jobs to retrieve. Filters include job name, job status, and submission time. You can only set one filter at a time.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of results to return in each page. The default value is 100.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.list_text_translation_jobs_request.ListTextTranslationJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.list_text_translation_jobs_response.ListTextTranslationJobsResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.list_text_translation_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.list_text_translation_jobs.async_list_text_translation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.list_text_translation_jobs_request.ListTextTranslationJobsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_text_translation_job(
        self,
        input_data_config: "aws_sdk_translate.types.input_data_config.InputDataConfig",
        output_data_config: "aws_sdk_translate.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "aws_sdk_translate.types.iam_role_arn.IamRoleArn",
        source_language_code: "aws_sdk_translate.types.language_code_string.LanguageCodeString",
        target_language_codes: "aws_sdk_translate.types.target_language_code_string_list.TargetLanguageCodeStringList",
        client_token: "aws_sdk_translate.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        job_name: Optional["aws_sdk_translate.types.job_name.JobName"] = None,
        terminology_names: Optional[
            "aws_sdk_translate.types.resource_name_list.ResourceNameList"
        ] = None,
        parallel_data_names: Optional[
            "aws_sdk_translate.types.resource_name_list.ResourceNameList"
        ] = None,
        settings: Optional[
            "aws_sdk_translate.types.translation_settings.TranslationSettings"
        ] = None,
    ) -> "aws_sdk_translate.types.start_text_translation_job_response.StartTextTranslationJobResponse":
        r"""<p>Starts an asynchronous batch translation job. Use batch translation jobs to translate large volumes of text across multiple documents at once. For batch translation, you can input documents with different source languages (specify <code>auto</code> as the source language). You can specify one or more target languages. Batch translation translates each input document into each of the target languages. For more information, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/async.html\">Asynchronous batch processing</a>.</p> <p>Batch translation jobs can be described with the <a>DescribeTextTranslationJob</a> operation, listed with the <a>ListTextTranslationJobs</a> operation, and stopped with the <a>StopTextTranslationJob</a> operation.</p>

        Args:
            job_name: <p>The name of the batch translation job to be performed.</p>
            input_data_config: <p>Specifies the format and location of the input documents for the translation job.</p>
            output_data_config: <p>Specifies the S3 folder to which your job output will be saved. </p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of an AWS Identity Access and Management (IAM) role that grants Amazon Translate read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/identity-and-access-management.html\">Identity and access management </a>.</p>
            source_language_code: <p>The language code of the input language. Specify the language if all input documents share the same language. If you don't know the language of the source files, or your input documents contains different source languages, select <code>auto</code>. Amazon Translate auto detects the source language for each input document. For a list of supported language codes, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html\">Supported languages</a>.</p>
            target_language_codes: <p>The target languages of the translation job. Enter up to 10 language codes. Each input file is translated into each target language.</p> <p>Each language code is 2 or 5 characters long. For a list of language codes, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html\">Supported languages</a>.</p>
            terminology_names: <p>The name of a custom terminology resource to add to the translation job. This resource lists examples source terms and the desired translation for each term.</p> <p>This parameter accepts only one custom terminology resource.</p> <p>If you specify multiple target languages for the job, translate uses the designated terminology for each requested target language that has an entry for the source term in the terminology file.</p> <p>For a list of available custom terminology resources, use the <a>ListTerminologies</a> operation.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html\">Custom terminology</a>.</p>
            parallel_data_names: <p>The name of a parallel data resource to add to the translation job. This resource consists of examples that show how you want segments of text to be translated. If you specify multiple target languages for the job, the parallel data file must include translations for all the target languages.</p> <p>When you add parallel data to a translation job, you create an <i>Active Custom Translation</i> job. </p> <p>This parameter accepts only one parallel data resource.</p> <note> <p>Active Custom Translation jobs are priced at a higher rate than other jobs that don't use parallel data. For more information, see <a href=\"http://aws.amazon.com/translate/pricing/\">Amazon Translate pricing</a>.</p> </note> <p>For a list of available parallel data resources, use the <a>ListParallelData</a> operation.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-parallel-data.html\"> Customizing your translations with parallel data</a>.</p>
            client_token: <p>A unique identifier for the request. This token is generated for you when using the Amazon Translate SDK.</p>
            settings: <p>Settings to configure your translation output. You can configure the following options:</p> <ul> <li> <p>Brevity: not supported.</p> </li> <li> <p>Formality: sets the formality level of the output text.</p> </li> <li> <p>Profanity: masks profane words and phrases in your translation output.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.start_text_translation_job_request.StartTextTranslationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.start_text_translation_job_response.StartTextTranslationJobResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.start_text_translation_job

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.start_text_translation_job.async_start_text_translation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.start_text_translation_job_request.StartTextTranslationJobRequest = {}  # type: ignore[typeddict-item]
        if job_name is not None:
            input_["job_name"] = job_name
        input_["input_data_config"] = input_data_config
        input_["output_data_config"] = output_data_config
        input_["data_access_role_arn"] = data_access_role_arn
        input_["source_language_code"] = source_language_code
        input_["target_language_codes"] = target_language_codes
        if terminology_names is not None:
            input_["terminology_names"] = terminology_names
        if parallel_data_names is not None:
            input_["parallel_data_names"] = parallel_data_names
        input_["client_token"] = client_token
        if settings is not None:
            input_["settings"] = settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_text_translation_job(
        self,
        job_id: "aws_sdk_translate.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
    ) -> "aws_sdk_translate.types.stop_text_translation_job_response.StopTextTranslationJobResponse":
        """<p>Stops an asynchronous batch translation job that is in progress.</p> <p>If the job's state is <code>IN_PROGRESS</code>, the job will be marked for termination and put into the <code>STOP_REQUESTED</code> state. If the job completes before it can be stopped, it is put into the <code>COMPLETED</code> state. Otherwise, the job is put into the <code>STOPPED</code> state.</p> <p>Asynchronous batch translation jobs are started with the <a>StartTextTranslationJob</a> operation. You can use the <a>DescribeTextTranslationJob</a> or <a>ListTextTranslationJobs</a> operations to get a batch translation job's <code>JobId</code>.</p>

        Args:
            job_id: <p>The job ID of the job to be stopped.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.stop_text_translation_job_request.StopTextTranslationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.stop_text_translation_job_response.StopTextTranslationJobResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.stop_text_translation_job

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.stop_text_translation_job.async_stop_text_translation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.stop_text_translation_job_request.StopTextTranslationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_translate.types.resource_arn.ResourceArn",
        tags: "aws_sdk_translate.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
    ) -> "aws_sdk_translate.types.tag_resource_response.TagResourceResponse":
        r"""<p>Associates a specific tag with a resource. A tag is a key-value pair that adds as a metadata to a resource. For more information, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/tagging.html\"> Tagging your resources</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the given Amazon Translate resource to which you want to associate the tags. </p>
            tags: <p>Tags being associated with a specific Amazon Translate resource. There can be a maximum of 50 tags (both existing and pending) associated with a specific resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def translate_document(
        self,
        document: "aws_sdk_translate.types.document.Document",
        source_language_code: "aws_sdk_translate.types.language_code_string.LanguageCodeString",
        target_language_code: "aws_sdk_translate.types.language_code_string.LanguageCodeString",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        terminology_names: Optional[
            "aws_sdk_translate.types.resource_name_list.ResourceNameList"
        ] = None,
        settings: Optional[
            "aws_sdk_translate.types.translation_settings.TranslationSettings"
        ] = None,
    ) -> (
        "aws_sdk_translate.types.translate_document_response.TranslateDocumentResponse"
    ):
        r"""<p>Translates the input document from the source language to the target language. This synchronous operation supports text, HTML, or Word documents as the input document. <code>TranslateDocument</code> supports translations from English to any supported language, and from any supported language to English. Therefore, specify either the source language code or the target language code as “en” (English). </p> <p> If you set the <code>Formality</code> parameter, the request will fail if the target language does not support formality. For a list of target languages that support formality, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-formality.html\">Setting formality</a>. </p>

        Args:
            document: <p>The content and content type for the document to be translated. The document size must not exceed 100 KB.</p>
            terminology_names: <p>The name of a terminology list file to add to the translation job. This file provides source terms and the desired translation for each term. A terminology list can contain a maximum of 256 terms. You can use one custom terminology resource in your translation request.</p> <p>Use the <a>ListTerminologies</a> operation to get the available terminology lists.</p> <p>For more information about custom terminology lists, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html\">Custom terminology</a>.</p>
            source_language_code: <p>The language code for the language of the source text. For a list of supported language codes, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html\">Supported languages</a>.</p> <p>To have Amazon Translate determine the source language of your text, you can specify <code>auto</code> in the <code>SourceLanguageCode</code> field. If you specify <code>auto</code>, Amazon Translate will call <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-general.html\">Amazon Comprehend</a> to determine the source language.</p> <note> <p>If you specify <code>auto</code>, you must send the <code>TranslateDocument</code> request in a region that supports Amazon Comprehend. Otherwise, the request returns an error indicating that autodetect is not supported. </p> </note>
            target_language_code: <p>The language code requested for the translated document. For a list of supported language codes, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html\">Supported languages</a>.</p>
            settings: <p>Settings to configure your translation output. You can configure the following options:</p> <ul> <li> <p>Brevity: not supported.</p> </li> <li> <p>Formality: sets the formality level of the output text.</p> </li> <li> <p>Profanity: masks profane words and phrases in your translation output.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.translate_document_request.TranslateDocumentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.translate_document_response.TranslateDocumentResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.translate_document

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.translate_document.async_translate_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.translate_document_request.TranslateDocumentRequest = {}  # type: ignore[typeddict-item]
        input_["document"] = document
        if terminology_names is not None:
            input_["terminology_names"] = terminology_names
        input_["source_language_code"] = source_language_code
        input_["target_language_code"] = target_language_code
        if settings is not None:
            input_["settings"] = settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def translate_text(
        self,
        text: "aws_sdk_translate.types.bounded_length_string.BoundedLengthString",
        source_language_code: "aws_sdk_translate.types.language_code_string.LanguageCodeString",
        target_language_code: "aws_sdk_translate.types.language_code_string.LanguageCodeString",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        terminology_names: Optional[
            "aws_sdk_translate.types.resource_name_list.ResourceNameList"
        ] = None,
        settings: Optional[
            "aws_sdk_translate.types.translation_settings.TranslationSettings"
        ] = None,
    ) -> "aws_sdk_translate.types.translate_text_response.TranslateTextResponse":
        r"""<p>Translates input text from the source language to the target language. For a list of available languages and language codes, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html\">Supported languages</a>.</p>

        Args:
            text: <p>The text to translate. The text string can be a maximum of 10,000 bytes long. Depending on your character set, this may be fewer than 10,000 characters.</p>
            terminology_names: <p>The name of a terminology list file to add to the translation job. This file provides source terms and the desired translation for each term. A terminology list can contain a maximum of 256 terms. You can use one custom terminology resource in your translation request.</p> <p>Use the <a>ListTerminologies</a> operation to get the available terminology lists.</p> <p>For more information about custom terminology lists, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html\">Custom terminology</a>.</p>
            source_language_code: <p>The language code for the language of the source text. For a list of language codes, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html\">Supported languages</a>.</p> <p>To have Amazon Translate determine the source language of your text, you can specify <code>auto</code> in the <code>SourceLanguageCode</code> field. If you specify <code>auto</code>, Amazon Translate will call <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-general.html\">Amazon Comprehend</a> to determine the source language.</p> <note> <p>If you specify <code>auto</code>, you must send the <code>TranslateText</code> request in a region that supports Amazon Comprehend. Otherwise, the request returns an error indicating that autodetect is not supported. </p> </note>
            target_language_code: <p>The language code requested for the language of the target text. For a list of language codes, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html\">Supported languages</a>.</p>
            settings: <p>Settings to configure your translation output. You can configure the following options:</p> <ul> <li> <p>Brevity: reduces the length of the translated output for most translations.</p> </li> <li> <p>Formality: sets the formality level of the output text.</p> </li> <li> <p>Profanity: masks profane words and phrases in your translation output.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.translate_text_request.TranslateTextRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.translate_text_response.TranslateTextResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.translate_text

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.translate_text.async_translate_text(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.translate_text_request.TranslateTextRequest = {}  # type: ignore[typeddict-item]
        input_["text"] = text
        if terminology_names is not None:
            input_["terminology_names"] = terminology_names
        input_["source_language_code"] = source_language_code
        input_["target_language_code"] = target_language_code
        if settings is not None:
            input_["settings"] = settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_translate.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_translate.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
    ) -> "aws_sdk_translate.types.untag_resource_response.UntagResourceResponse":
        r"""<p>Removes a specific tag associated with an Amazon Translate resource. For more information, see <a href=\"https://docs.aws.amazon.com/translate/latest/dg/tagging.html\"> Tagging your resources</a>.</p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the given Amazon Translate resource from which you want to remove the tags. </p>
            tag_keys: <p>The initial part of a key-value pair that forms a tag being removed from a given resource. Keys must be unique and cannot be duplicated for a particular resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_parallel_data(
        self,
        name: "aws_sdk_translate.types.resource_name.ResourceName",
        parallel_data_config: "aws_sdk_translate.types.parallel_data_config.ParallelDataConfig",
        client_token: "aws_sdk_translate.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[AsyncTranslateClientConfig] = None,
        description: Optional["aws_sdk_translate.types.description.Description"] = None,
    ) -> "aws_sdk_translate.types.update_parallel_data_response.UpdateParallelDataResponse":
        """<p>Updates a previously created parallel data resource by importing a new input file from Amazon S3.</p>

        Args:
            name: <p>The name of the parallel data resource being updated.</p>
            description: <p>A custom description for the parallel data resource in Amazon Translate.</p>
            parallel_data_config: <p>Specifies the format and S3 location of the parallel data input file.</p>
            client_token: <p>A unique identifier for the request. This token is automatically generated when you use Amazon Translate through an AWS SDK.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_translate.types.update_parallel_data_request.UpdateParallelDataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_translate.types.update_parallel_data_response.UpdateParallelDataResponse"
        ]:
            import aws_sdk_translate._operations.aws_shine_frontend_service_20170701.update_parallel_data

            (
                output,
                http_response,
            ) = await aws_sdk_translate._operations.aws_shine_frontend_service_20170701.update_parallel_data.async_update_parallel_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_translate.types.update_parallel_data_request.UpdateParallelDataRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["parallel_data_config"] = parallel_data_config
        input_["client_token"] = client_token

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
