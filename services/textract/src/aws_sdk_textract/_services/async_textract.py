"""Generated from Smithy shape ``com.amazonaws.textract#Textract``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_textract._auth._signers
import aws_sdk_textract._auth._sigv4
from aws_sdk_textract._auth._identity import Credentials
from aws_sdk_textract._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_textract._auth._zapros_handler import AuthMiddleware
from aws_sdk_textract._pagination import resolve_path as _resolve_path
from aws_sdk_textract._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_description
    import aws_sdk_textract.types.adapter_id
    import aws_sdk_textract.types.adapter_name
    import aws_sdk_textract.types.adapter_overview
    import aws_sdk_textract.types.adapter_version
    import aws_sdk_textract.types.adapter_version_dataset_config
    import aws_sdk_textract.types.adapter_version_overview
    import aws_sdk_textract.types.adapters_config
    import aws_sdk_textract.types.amazon_resource_name
    import aws_sdk_textract.types.analyze_document_request
    import aws_sdk_textract.types.analyze_document_response
    import aws_sdk_textract.types.analyze_expense_request
    import aws_sdk_textract.types.analyze_expense_response
    import aws_sdk_textract.types.analyze_id_request
    import aws_sdk_textract.types.analyze_id_response
    import aws_sdk_textract.types.auto_update
    import aws_sdk_textract.types.client_request_token
    import aws_sdk_textract.types.create_adapter_request
    import aws_sdk_textract.types.create_adapter_response
    import aws_sdk_textract.types.create_adapter_version_request
    import aws_sdk_textract.types.create_adapter_version_response
    import aws_sdk_textract.types.date_time
    import aws_sdk_textract.types.delete_adapter_request
    import aws_sdk_textract.types.delete_adapter_response
    import aws_sdk_textract.types.delete_adapter_version_request
    import aws_sdk_textract.types.delete_adapter_version_response
    import aws_sdk_textract.types.detect_document_text_request
    import aws_sdk_textract.types.detect_document_text_response
    import aws_sdk_textract.types.document
    import aws_sdk_textract.types.document_location
    import aws_sdk_textract.types.document_pages
    import aws_sdk_textract.types.feature_types
    import aws_sdk_textract.types.get_adapter_request
    import aws_sdk_textract.types.get_adapter_response
    import aws_sdk_textract.types.get_adapter_version_request
    import aws_sdk_textract.types.get_adapter_version_response
    import aws_sdk_textract.types.get_document_analysis_request
    import aws_sdk_textract.types.get_document_analysis_response
    import aws_sdk_textract.types.get_document_text_detection_request
    import aws_sdk_textract.types.get_document_text_detection_response
    import aws_sdk_textract.types.get_expense_analysis_request
    import aws_sdk_textract.types.get_expense_analysis_response
    import aws_sdk_textract.types.get_lending_analysis_request
    import aws_sdk_textract.types.get_lending_analysis_response
    import aws_sdk_textract.types.get_lending_analysis_summary_request
    import aws_sdk_textract.types.get_lending_analysis_summary_response
    import aws_sdk_textract.types.human_loop_config
    import aws_sdk_textract.types.job_id
    import aws_sdk_textract.types.job_tag
    import aws_sdk_textract.types.kms_key_id
    import aws_sdk_textract.types.list_adapter_versions_request
    import aws_sdk_textract.types.list_adapter_versions_response
    import aws_sdk_textract.types.list_adapters_request
    import aws_sdk_textract.types.list_adapters_response
    import aws_sdk_textract.types.list_tags_for_resource_request
    import aws_sdk_textract.types.list_tags_for_resource_response
    import aws_sdk_textract.types.max_results
    import aws_sdk_textract.types.notification_channel
    import aws_sdk_textract.types.output_config
    import aws_sdk_textract.types.pagination_token
    import aws_sdk_textract.types.queries_config
    import aws_sdk_textract.types.start_document_analysis_request
    import aws_sdk_textract.types.start_document_analysis_response
    import aws_sdk_textract.types.start_document_text_detection_request
    import aws_sdk_textract.types.start_document_text_detection_response
    import aws_sdk_textract.types.start_expense_analysis_request
    import aws_sdk_textract.types.start_expense_analysis_response
    import aws_sdk_textract.types.start_lending_analysis_request
    import aws_sdk_textract.types.start_lending_analysis_response
    import aws_sdk_textract.types.tag_key_list
    import aws_sdk_textract.types.tag_map
    import aws_sdk_textract.types.tag_resource_request
    import aws_sdk_textract.types.tag_resource_response
    import aws_sdk_textract.types.untag_resource_request
    import aws_sdk_textract.types.untag_resource_response
    import aws_sdk_textract.types.update_adapter_request
    import aws_sdk_textract.types.update_adapter_response


class AsyncTextractClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncTextractClient:
    """A client for the ``Textract`` service.

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
        self._config = AsyncTextractClientConfig(
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
        self, config_overrides: Optional[AsyncTextractClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTextractClientConfig = config_overrides or {}
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

    async def analyze_document(
        self,
        document: "aws_sdk_textract.types.document.Document",
        feature_types: "aws_sdk_textract.types.feature_types.FeatureTypes",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        human_loop_config: Optional[
            "aws_sdk_textract.types.human_loop_config.HumanLoopConfig"
        ] = None,
        queries_config: Optional[
            "aws_sdk_textract.types.queries_config.QueriesConfig"
        ] = None,
        adapters_config: Optional[
            "aws_sdk_textract.types.adapters_config.AdaptersConfig"
        ] = None,
    ) -> "aws_sdk_textract.types.analyze_document_response.AnalyzeDocumentResponse":
        r"""<p>Analyzes an input document for relationships between detected items. </p> <p>The types of information returned are as follows: </p> <ul> <li> <p>Form data (key-value pairs). The related information is returned in two <a>Block</a> objects, each of type <code>KEY_VALUE_SET</code>: a KEY <code>Block</code> object and a VALUE <code>Block</code> object. For example, <i>Name: Ana Silva Carolina</i> contains a key and value. <i>Name:</i> is the key. <i>Ana Silva Carolina</i> is the value.</p> </li> <li> <p>Table and table cell data. A TABLE <code>Block</code> object contains information about a detected table. A CELL <code>Block</code> object is returned for each cell in a table.</p> </li> <li> <p>Lines and words of text. A LINE <code>Block</code> object contains one or more WORD <code>Block</code> objects. All lines and words that are detected in the document are returned (including text that doesn't have a relationship with the value of <code>FeatureTypes</code>). </p> </li> <li> <p>Signatures. A SIGNATURE <code>Block</code> object contains the location information of a signature in a document. If used in conjunction with forms or tables, a signature can be given a Key-Value pairing or be detected in the cell of a table.</p> </li> <li> <p>Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.</p> </li> <li> <p>Query Result. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.</p> </li> </ul> <p>Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT <code>Block</code> object contains information about a selection element, including the selection status.</p> <p>You can choose which type of analysis to perform by specifying the <code>FeatureTypes</code> list. </p> <p>The output is returned in a list of <code>Block</code> objects.</p> <p> <code>AnalyzeDocument</code> is a synchronous operation. To analyze documents asynchronously, use <a>StartDocumentAnalysis</a>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\">Document Text Analysis</a>.</p>

        Args:
            document: <p>The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can't pass image bytes. The document must be an image in JPEG, PNG, PDF, or TIFF format.</p> <p>If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes that are passed using the <code>Bytes</code> field. </p>
            feature_types: <p>A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. Add SIGNATURES to return the locations of detected signatures. Add LAYOUT to the list to return information about the layout of the document. All lines and words detected in the document are included in the response (including text that isn't related to the value of <code>FeatureTypes</code>). </p>
            human_loop_config: <p>Sets the configuration for the human in the loop workflow for analyzing documents.</p>
            queries_config: <p>Contains Queries and the alias for those Queries, as determined by the input. </p>
            adapters_config: <p>Specifies the adapter to be used when analyzing a document.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.analyze_document_request.AnalyzeDocumentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.analyze_document_response.AnalyzeDocumentResponse"
        ]:
            import aws_sdk_textract._operations.textract.analyze_document

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.analyze_document.async_analyze_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.analyze_document_request.AnalyzeDocumentRequest = {}  # type: ignore[typeddict-item]
        input_["document"] = document
        input_["feature_types"] = feature_types
        if human_loop_config is not None:
            input_["human_loop_config"] = human_loop_config
        if queries_config is not None:
            input_["queries_config"] = queries_config
        if adapters_config is not None:
            input_["adapters_config"] = adapters_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def analyze_expense(
        self,
        document: "aws_sdk_textract.types.document.Document",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> "aws_sdk_textract.types.analyze_expense_response.AnalyzeExpenseResponse":
        """<p> <code>AnalyzeExpense</code> synchronously analyzes an input document for financially related relationships between text.</p> <p>Information is returned as <code>ExpenseDocuments</code> and seperated as follows:</p> <ul> <li> <p> <code>LineItemGroups</code>- A data set containing <code>LineItems</code> which store information about the lines of text, such as an item purchased and its price on a receipt.</p> </li> <li> <p> <code>SummaryFields</code>- Contains all other information a receipt, such as header information or the vendors name.</p> </li> </ul>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.analyze_expense_request.AnalyzeExpenseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.analyze_expense_response.AnalyzeExpenseResponse"
        ]:
            import aws_sdk_textract._operations.textract.analyze_expense

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.analyze_expense.async_analyze_expense(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.analyze_expense_request.AnalyzeExpenseRequest = {}  # type: ignore[typeddict-item]
        input_["document"] = document

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def analyze_id(
        self,
        document_pages: "aws_sdk_textract.types.document_pages.DocumentPages",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> "aws_sdk_textract.types.analyze_id_response.AnalyzeIDResponse":
        """<p>Analyzes identity documents for relevant information. This information is extracted and returned as <code>IdentityDocumentFields</code>, which records both the normalized field and value of the extracted text. Unlike other Amazon Textract operations, <code>AnalyzeID</code> doesn't return any Geometry data.</p>

        Args:
            document_pages: <p>The document being passed to AnalyzeID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.analyze_id_request.AnalyzeIDRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.analyze_id_response.AnalyzeIDResponse"
        ]:
            import aws_sdk_textract._operations.textract.analyze_id

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.analyze_id.async_analyze_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.analyze_id_request.AnalyzeIDRequest = {}  # type: ignore[typeddict-item]
        input_["document_pages"] = document_pages

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_adapter(
        self,
        adapter_name: "aws_sdk_textract.types.adapter_name.AdapterName",
        feature_types: "aws_sdk_textract.types.feature_types.FeatureTypes",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        description: Optional[
            "aws_sdk_textract.types.adapter_description.AdapterDescription"
        ] = None,
        auto_update: Optional["aws_sdk_textract.types.auto_update.AutoUpdate"] = None,
        tags: Optional["aws_sdk_textract.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_textract.types.create_adapter_response.CreateAdapterResponse":
        """<p>Creates an adapter, which can be fine-tuned for enhanced performance on user provided documents. Takes an AdapterName and FeatureType. Currently the only supported feature type is <code>QUERIES</code>. You can also provide a Description, Tags, and a ClientRequestToken. You can choose whether or not the adapter should be AutoUpdated with the AutoUpdate argument. By default, AutoUpdate is set to DISABLED.</p>

        Args:
            adapter_name: <p>The name to be assigned to the adapter being created.</p>
            client_request_token: <p>Idempotent token is used to recognize the request. If the same token is used with multiple CreateAdapter requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.</p>
            description: <p>The description to be assigned to the adapter being created.</p>
            feature_types: <p>The type of feature that the adapter is being trained on. Currrenly, supported feature types are: <code>QUERIES</code> </p>
            auto_update: <p>Controls whether or not the adapter should automatically update.</p>
            tags: <p>A list of tags to be added to the adapter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.create_adapter_request.CreateAdapterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.create_adapter_response.CreateAdapterResponse"
        ]:
            import aws_sdk_textract._operations.textract.create_adapter

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.create_adapter.async_create_adapter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.create_adapter_request.CreateAdapterRequest = {}  # type: ignore[typeddict-item]
        input_["adapter_name"] = adapter_name
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if description is not None:
            input_["description"] = description
        input_["feature_types"] = feature_types
        if auto_update is not None:
            input_["auto_update"] = auto_update
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_adapter_version(
        self,
        adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId",
        dataset_config: "aws_sdk_textract.types.adapter_version_dataset_config.AdapterVersionDatasetConfig",
        output_config: "aws_sdk_textract.types.output_config.OutputConfig",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        kms_key_id: Optional["aws_sdk_textract.types.kms_key_id.KMSKeyId"] = None,
        tags: Optional["aws_sdk_textract.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_textract.types.create_adapter_version_response.CreateAdapterVersionResponse":
        """<p>Creates a new version of an adapter. Operates on a provided AdapterId and a specified dataset provided via the DatasetConfig argument. Requires that you specify an Amazon S3 bucket with the OutputConfig argument. You can provide an optional KMSKeyId, an optional ClientRequestToken, and optional tags.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter that will receive a new version.</p>
            client_request_token: <p>Idempotent token is used to recognize the request. If the same token is used with multiple CreateAdapterVersion requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.</p>
            dataset_config: <p>Specifies a dataset used to train a new adapter version. Takes a ManifestS3Object as the value.</p>
            kms_key_id: <p>The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt your documents.</p>
            tags: <p>A set of tags (key-value pairs) that you want to attach to the adapter version. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.create_adapter_version_request.CreateAdapterVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.create_adapter_version_response.CreateAdapterVersionResponse"
        ]:
            import aws_sdk_textract._operations.textract.create_adapter_version

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.create_adapter_version.async_create_adapter_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.create_adapter_version_request.CreateAdapterVersionRequest = {}  # type: ignore[typeddict-item]
        input_["adapter_id"] = adapter_id
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        input_["dataset_config"] = dataset_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        input_["output_config"] = output_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_adapter(
        self,
        adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> "aws_sdk_textract.types.delete_adapter_response.DeleteAdapterResponse":
        """<p>Deletes an Amazon Textract adapter. Takes an AdapterId and deletes the adapter specified by the ID.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.delete_adapter_request.DeleteAdapterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.delete_adapter_response.DeleteAdapterResponse"
        ]:
            import aws_sdk_textract._operations.textract.delete_adapter

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.delete_adapter.async_delete_adapter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.delete_adapter_request.DeleteAdapterRequest = {}  # type: ignore[typeddict-item]
        input_["adapter_id"] = adapter_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_adapter_version(
        self,
        adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId",
        adapter_version: "aws_sdk_textract.types.adapter_version.AdapterVersion",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> "aws_sdk_textract.types.delete_adapter_version_response.DeleteAdapterVersionResponse":
        """<p>Deletes an Amazon Textract adapter version. Requires that you specify both an AdapterId and a AdapterVersion. Deletes the adapter version specified by the AdapterId and the AdapterVersion.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter version that will be deleted.</p>
            adapter_version: <p>Specifies the adapter version to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.delete_adapter_version_request.DeleteAdapterVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.delete_adapter_version_response.DeleteAdapterVersionResponse"
        ]:
            import aws_sdk_textract._operations.textract.delete_adapter_version

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.delete_adapter_version.async_delete_adapter_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.delete_adapter_version_request.DeleteAdapterVersionRequest = {}  # type: ignore[typeddict-item]
        input_["adapter_id"] = adapter_id
        input_["adapter_version"] = adapter_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def detect_document_text(
        self,
        document: "aws_sdk_textract.types.document.Document",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> "aws_sdk_textract.types.detect_document_text_response.DetectDocumentTextResponse":
        r"""<p>Detects text in the input document. Amazon Textract can detect lines of text and the words that make up a line of text. The input document must be in one of the following image formats: JPEG, PNG, PDF, or TIFF. <code>DetectDocumentText</code> returns the detected text in an array of <a>Block</a> objects. </p> <p>Each document page has as an associated <code>Block</code> of type PAGE. Each PAGE <code>Block</code> object is the parent of LINE <code>Block</code> objects that represent the lines of detected text on a page. A LINE <code>Block</code> object is a parent for each word that makes up the line. Words are represented by <code>Block</code> objects of type WORD.</p> <p> <code>DetectDocumentText</code> is a synchronous operation. To analyze documents asynchronously, use <a>StartDocumentTextDetection</a>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\">Document Text Detection</a>.</p>

        Args:
            document: <p>The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can't pass image bytes. The document must be an image in JPEG or PNG format.</p> <p>If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes that are passed using the <code>Bytes</code> field. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.detect_document_text_request.DetectDocumentTextRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.detect_document_text_response.DetectDocumentTextResponse"
        ]:
            import aws_sdk_textract._operations.textract.detect_document_text

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.detect_document_text.async_detect_document_text(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.detect_document_text_request.DetectDocumentTextRequest = {}  # type: ignore[typeddict-item]
        input_["document"] = document

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_adapter(
        self,
        adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> "aws_sdk_textract.types.get_adapter_response.GetAdapterResponse":
        """<p>Gets configuration information for an adapter specified by an AdapterId, returning information on AdapterName, Description, CreationTime, AutoUpdate status, and FeatureTypes.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.get_adapter_request.GetAdapterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.get_adapter_response.GetAdapterResponse"
        ]:
            import aws_sdk_textract._operations.textract.get_adapter

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.get_adapter.async_get_adapter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.get_adapter_request.GetAdapterRequest = {}  # type: ignore[typeddict-item]
        input_["adapter_id"] = adapter_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_adapter_version(
        self,
        adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId",
        adapter_version: "aws_sdk_textract.types.adapter_version.AdapterVersion",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> (
        "aws_sdk_textract.types.get_adapter_version_response.GetAdapterVersionResponse"
    ):
        """<p>Gets configuration information for the specified adapter version, including: AdapterId, AdapterVersion, FeatureTypes, Status, StatusMessage, DatasetConfig, KMSKeyId, OutputConfig, Tags and EvaluationMetrics.</p>

        Args:
            adapter_id: <p>A string specifying a unique ID for the adapter version you want to retrieve information for.</p>
            adapter_version: <p>A string specifying the adapter version you want to retrieve information for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.get_adapter_version_request.GetAdapterVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.get_adapter_version_response.GetAdapterVersionResponse"
        ]:
            import aws_sdk_textract._operations.textract.get_adapter_version

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.get_adapter_version.async_get_adapter_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.get_adapter_version_request.GetAdapterVersionRequest = {}  # type: ignore[typeddict-item]
        input_["adapter_id"] = adapter_id
        input_["adapter_version"] = adapter_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_document_analysis(
        self,
        job_id: "aws_sdk_textract.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        max_results: Optional["aws_sdk_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_textract.types.get_document_analysis_response.GetDocumentAnalysisResponse":
        r"""<p>Gets the results for an Amazon Textract asynchronous operation that analyzes text in a document.</p> <p>You start asynchronous text analysis by calling <a>StartDocumentAnalysis</a>, which returns a job identifier (<code>JobId</code>). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that's registered in the initial call to <code>StartDocumentAnalysis</code>. To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <code>GetDocumentAnalysis</code>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartDocumentAnalysis</code>.</p> <p> <code>GetDocumentAnalysis</code> returns an array of <a>Block</a> objects. The following types of information are returned: </p> <ul> <li> <p>Form data (key-value pairs). The related information is returned in two <a>Block</a> objects, each of type <code>KEY_VALUE_SET</code>: a KEY <code>Block</code> object and a VALUE <code>Block</code> object. For example, <i>Name: Ana Silva Carolina</i> contains a key and value. <i>Name:</i> is the key. <i>Ana Silva Carolina</i> is the value.</p> </li> <li> <p>Table and table cell data. A TABLE <code>Block</code> object contains information about a detected table. A CELL <code>Block</code> object is returned for each cell in a table.</p> </li> <li> <p>Lines and words of text. A LINE <code>Block</code> object contains one or more WORD <code>Block</code> objects. All lines and words that are detected in the document are returned (including text that doesn't have a relationship with the value of the <code>StartDocumentAnalysis</code> <code>FeatureTypes</code> input parameter). </p> </li> <li> <p>Query. A QUERY Block object contains the query text, alias and link to the associated Query results block object.</p> </li> <li> <p>Query Results. A QUERY_RESULT Block object contains the answer to the query and an ID that connects it to the query asked. This Block also contains a confidence score.</p> </li> </ul> <note> <p>While processing a document with queries, look out for <code>INVALID_REQUEST_PARAMETERS</code> output. This indicates that either the per page query limit has been exceeded or that the operation is trying to query a page in the document which doesn’t exist. </p> </note> <p>Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT <code>Block</code> object contains information about a selection element, including the selection status.</p> <p>Use the <code>MaxResults</code> parameter to limit the number of blocks that are returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetDocumentAnalysis</code>, and populate the <code>NextToken</code> request parameter with the token value that's returned from the previous call to <code>GetDocumentAnalysis</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\">Document Text Analysis</a>.</p>

        Args:
            job_id: <p>A unique identifier for the text-detection job. The <code>JobId</code> is returned from <code>StartDocumentAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value that you can specify is 1,000. If you specify a value greater than 1,000, a maximum of 1,000 results is returned. The default value is 1,000.</p>
            next_token: <p>If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.get_document_analysis_request.GetDocumentAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.get_document_analysis_response.GetDocumentAnalysisResponse"
        ]:
            import aws_sdk_textract._operations.textract.get_document_analysis

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.get_document_analysis.async_get_document_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.get_document_analysis_request.GetDocumentAnalysisRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
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

    async def get_document_text_detection(
        self,
        job_id: "aws_sdk_textract.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        max_results: Optional["aws_sdk_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_textract.types.get_document_text_detection_response.GetDocumentTextDetectionResponse":
        r"""<p>Gets the results for an Amazon Textract asynchronous operation that detects text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.</p> <p>You start asynchronous text detection by calling <a>StartDocumentTextDetection</a>, which returns a job identifier (<code>JobId</code>). When the text detection operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that's registered in the initial call to <code>StartDocumentTextDetection</code>. To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <code>GetDocumentTextDetection</code>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartDocumentTextDetection</code>.</p> <p> <code>GetDocumentTextDetection</code> returns an array of <a>Block</a> objects. </p> <p>Each document page has as an associated <code>Block</code> of type PAGE. Each PAGE <code>Block</code> object is the parent of LINE <code>Block</code> objects that represent the lines of detected text on a page. A LINE <code>Block</code> object is a parent for each word that makes up the line. Words are represented by <code>Block</code> objects of type WORD.</p> <p>Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetDocumentTextDetection</code>, and populate the <code>NextToken</code> request parameter with the token value that's returned from the previous call to <code>GetDocumentTextDetection</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\">Document Text Detection</a>.</p>

        Args:
            job_id: <p>A unique identifier for the text detection job. The <code>JobId</code> is returned from <code>StartDocumentTextDetection</code>. A <code>JobId</code> value is only valid for 7 days.</p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value you can specify is 1,000. If you specify a value greater than 1,000, a maximum of 1,000 results is returned. The default value is 1,000.</p>
            next_token: <p>If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.get_document_text_detection_request.GetDocumentTextDetectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.get_document_text_detection_response.GetDocumentTextDetectionResponse"
        ]:
            import aws_sdk_textract._operations.textract.get_document_text_detection

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.get_document_text_detection.async_get_document_text_detection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.get_document_text_detection_request.GetDocumentTextDetectionRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
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

    async def get_expense_analysis(
        self,
        job_id: "aws_sdk_textract.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        max_results: Optional["aws_sdk_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_textract.types.get_expense_analysis_response.GetExpenseAnalysisResponse":
        r"""<p>Gets the results for an Amazon Textract asynchronous operation that analyzes invoices and receipts. Amazon Textract finds contact information, items purchased, and vendor name, from input invoices and receipts.</p> <p>You start asynchronous invoice/receipt analysis by calling <a>StartExpenseAnalysis</a>, which returns a job identifier (<code>JobId</code>). Upon completion of the invoice/receipt analysis, Amazon Textract publishes the completion status to the Amazon Simple Notification Service (Amazon SNS) topic. This topic must be registered in the initial call to <code>StartExpenseAnalysis</code>. To get the results of the invoice/receipt analysis operation, first ensure that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <code>GetExpenseAnalysis</code>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartExpenseAnalysis</code>.</p> <p>Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in <code>MaxResults</code>, the value of <code>NextToken</code> in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call <code>GetExpenseAnalysis</code>, and populate the <code>NextToken</code> request parameter with the token value that's returned from the previous call to <code>GetExpenseAnalysis</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/invoices-receipts.html\">Analyzing Invoices and Receipts</a>.</p>

        Args:
            job_id: <p>A unique identifier for the text detection job. The <code>JobId</code> is returned from <code>StartExpenseAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value you can specify is 20. If you specify a value greater than 20, a maximum of 20 results is returned. The default value is 20.</p>
            next_token: <p>If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.get_expense_analysis_request.GetExpenseAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.get_expense_analysis_response.GetExpenseAnalysisResponse"
        ]:
            import aws_sdk_textract._operations.textract.get_expense_analysis

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.get_expense_analysis.async_get_expense_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.get_expense_analysis_request.GetExpenseAnalysisRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
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

    async def get_lending_analysis(
        self,
        job_id: "aws_sdk_textract.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        max_results: Optional["aws_sdk_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_textract.types.get_lending_analysis_response.GetLendingAnalysisResponse":
        """<p>Gets the results for an Amazon Textract asynchronous operation that analyzes text in a lending document. </p> <p>You start asynchronous text analysis by calling <code>StartLendingAnalysis</code>, which returns a job identifier (<code>JobId</code>). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that's registered in the initial call to <code>StartLendingAnalysis</code>. </p> <p>To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call GetLendingAnalysis, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartLendingAnalysis</code>.</p>

        Args:
            job_id: <p>A unique identifier for the lending or text-detection job. The <code>JobId</code> is returned from <code>StartLendingAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>
            max_results: <p>The maximum number of results to return per paginated call. The largest value that you can specify is 30. If you specify a value greater than 30, a maximum of 30 results is returned. The default value is 30.</p>
            next_token: <p>If the previous response was incomplete, Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of lending results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.get_lending_analysis_request.GetLendingAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.get_lending_analysis_response.GetLendingAnalysisResponse"
        ]:
            import aws_sdk_textract._operations.textract.get_lending_analysis

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.get_lending_analysis.async_get_lending_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.get_lending_analysis_request.GetLendingAnalysisRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
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

    async def get_lending_analysis_summary(
        self,
        job_id: "aws_sdk_textract.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> "aws_sdk_textract.types.get_lending_analysis_summary_response.GetLendingAnalysisSummaryResponse":
        """<p>Gets summarized results for the <code>StartLendingAnalysis</code> operation, which analyzes text in a lending document. The returned summary consists of information about documents grouped together by a common document type. Information like detected signatures, page numbers, and split documents is returned with respect to the type of grouped document. </p> <p>You start asynchronous text analysis by calling <code>StartLendingAnalysis</code>, which returns a job identifier (<code>JobId</code>). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that's registered in the initial call to <code>StartLendingAnalysis</code>. </p> <p>To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If so, call <code>GetLendingAnalysisSummary</code>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartLendingAnalysis</code>.</p>

        Args:
            job_id: <p> A unique identifier for the lending or text-detection job. The <code>JobId</code> is returned from StartLendingAnalysis. A <code>JobId</code> value is only valid for 7 days.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.get_lending_analysis_summary_request.GetLendingAnalysisSummaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.get_lending_analysis_summary_response.GetLendingAnalysisSummaryResponse"
        ]:
            import aws_sdk_textract._operations.textract.get_lending_analysis_summary

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.get_lending_analysis_summary.async_get_lending_analysis_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.get_lending_analysis_summary_request.GetLendingAnalysisSummaryRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_adapters(
        self,
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        after_creation_time: Optional[
            "aws_sdk_textract.types.date_time.DateTime"
        ] = None,
        before_creation_time: Optional[
            "aws_sdk_textract.types.date_time.DateTime"
        ] = None,
        max_results: Optional["aws_sdk_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_textract.types.list_adapters_response.ListAdaptersResponse":
        """<p>Lists all adapters that match the specified filtration criteria.</p>

        Args:
            after_creation_time: <p>Specifies the lower bound for the ListAdapters operation. Ensures ListAdapters returns only adapters created after the specified creation time.</p>
            before_creation_time: <p>Specifies the upper bound for the ListAdapters operation. Ensures ListAdapters returns only adapters created before the specified creation time.</p>
            max_results: <p>The maximum number of results to return when listing adapters.</p>
            next_token: <p>Identifies the next page of results to return when listing adapters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.list_adapters_request.ListAdaptersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.list_adapters_response.ListAdaptersResponse"
        ]:
            import aws_sdk_textract._operations.textract.list_adapters

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.list_adapters.async_list_adapters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.list_adapters_request.ListAdaptersRequest = {}  # type: ignore[typeddict-item]
        if after_creation_time is not None:
            input_["after_creation_time"] = after_creation_time
        if before_creation_time is not None:
            input_["before_creation_time"] = before_creation_time
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

    async def iter_list_adapters(
        self,
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        after_creation_time: Optional[
            "aws_sdk_textract.types.date_time.DateTime"
        ] = None,
        before_creation_time: Optional[
            "aws_sdk_textract.types.date_time.DateTime"
        ] = None,
        max_results: Optional["aws_sdk_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_textract.types.adapter_overview.AdapterOverview]":
        _token = next_token
        while True:
            _response = await self.list_adapters(
                config_overrides=config_overrides,
                after_creation_time=after_creation_time,
                before_creation_time=before_creation_time,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("adapters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_adapter_versions(
        self,
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        adapter_id: Optional["aws_sdk_textract.types.adapter_id.AdapterId"] = None,
        after_creation_time: Optional[
            "aws_sdk_textract.types.date_time.DateTime"
        ] = None,
        before_creation_time: Optional[
            "aws_sdk_textract.types.date_time.DateTime"
        ] = None,
        max_results: Optional["aws_sdk_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_textract.types.list_adapter_versions_response.ListAdapterVersionsResponse":
        """<p>List all version of an adapter that meet the specified filtration criteria.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter to match for when listing adapter versions.</p>
            after_creation_time: <p>Specifies the lower bound for the ListAdapterVersions operation. Ensures ListAdapterVersions returns only adapter versions created after the specified creation time.</p>
            before_creation_time: <p>Specifies the upper bound for the ListAdapterVersions operation. Ensures ListAdapterVersions returns only adapter versions created after the specified creation time.</p>
            max_results: <p>The maximum number of results to return when listing adapter versions.</p>
            next_token: <p>Identifies the next page of results to return when listing adapter versions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.list_adapter_versions_request.ListAdapterVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.list_adapter_versions_response.ListAdapterVersionsResponse"
        ]:
            import aws_sdk_textract._operations.textract.list_adapter_versions

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.list_adapter_versions.async_list_adapter_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.list_adapter_versions_request.ListAdapterVersionsRequest = {}  # type: ignore[typeddict-item]
        if adapter_id is not None:
            input_["adapter_id"] = adapter_id
        if after_creation_time is not None:
            input_["after_creation_time"] = after_creation_time
        if before_creation_time is not None:
            input_["before_creation_time"] = before_creation_time
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

    async def iter_list_adapter_versions(
        self,
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        adapter_id: Optional["aws_sdk_textract.types.adapter_id.AdapterId"] = None,
        after_creation_time: Optional[
            "aws_sdk_textract.types.date_time.DateTime"
        ] = None,
        before_creation_time: Optional[
            "aws_sdk_textract.types.date_time.DateTime"
        ] = None,
        max_results: Optional["aws_sdk_textract.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_textract.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_textract.types.adapter_version_overview.AdapterVersionOverview]":
        _token = next_token
        while True:
            _response = await self.list_adapter_versions(
                config_overrides=config_overrides,
                adapter_id=adapter_id,
                after_creation_time=after_creation_time,
                before_creation_time=before_creation_time,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("adapter_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_textract.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> "aws_sdk_textract.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags for an Amazon Textract resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that specifies the resource to list tags for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_textract._operations.textract.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_document_analysis(
        self,
        document_location: "aws_sdk_textract.types.document_location.DocumentLocation",
        feature_types: "aws_sdk_textract.types.feature_types.FeatureTypes",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        job_tag: Optional["aws_sdk_textract.types.job_tag.JobTag"] = None,
        notification_channel: Optional[
            "aws_sdk_textract.types.notification_channel.NotificationChannel"
        ] = None,
        output_config: Optional[
            "aws_sdk_textract.types.output_config.OutputConfig"
        ] = None,
        kms_key_id: Optional["aws_sdk_textract.types.kms_key_id.KMSKeyId"] = None,
        queries_config: Optional[
            "aws_sdk_textract.types.queries_config.QueriesConfig"
        ] = None,
        adapters_config: Optional[
            "aws_sdk_textract.types.adapters_config.AdaptersConfig"
        ] = None,
    ) -> "aws_sdk_textract.types.start_document_analysis_response.StartDocumentAnalysisResponse":
        r"""<p>Starts the asynchronous analysis of an input document for relationships between detected items such as key-value pairs, tables, and selection elements.</p> <p> <code>StartDocumentAnalysis</code> can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use <a>DocumentLocation</a> to specify the bucket name and file name of the document. </p> <p> <code>StartDocumentAnalysis</code> returns a job identifier (<code>JobId</code>) that you use to get the results of the operation. When text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in <code>NotificationChannel</code>. To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetDocumentAnalysis</a>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartDocumentAnalysis</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html\">Document Text Analysis</a>.</p>

        Args:
            document_location: <p>The location of the document to be processed.</p>
            feature_types: <p>A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. To perform both types of analysis, add TABLES and FORMS to <code>FeatureTypes</code>. All lines and words detected in the document are included in the response (including text that isn't related to the value of <code>FeatureTypes</code>). </p>
            client_request_token: <p>The idempotent token that you use to identify the start request. If you use the same token with multiple <code>StartDocumentAnalysis</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentally started more than once. For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/api-async.html\">Calling Amazon Textract Asynchronous Operations</a>.</p>
            job_tag: <p>An identifier that you specify that's included in the completion notification published to the Amazon SNS topic. For example, you can use <code>JobTag</code> to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).</p>
            notification_channel: <p>The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to. </p>
            output_config: <p>Sets if the output will go to a customer defined bucket. By default, Amazon Textract will save the results internally to be accessed by the GetDocumentAnalysis operation.</p>
            kms_key_id: <p>The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side,using SSE-S3.</p>
            adapters_config: <p>Specifies the adapter to be used when analyzing a document.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.start_document_analysis_request.StartDocumentAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.start_document_analysis_response.StartDocumentAnalysisResponse"
        ]:
            import aws_sdk_textract._operations.textract.start_document_analysis

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.start_document_analysis.async_start_document_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.start_document_analysis_request.StartDocumentAnalysisRequest = {}  # type: ignore[typeddict-item]
        input_["document_location"] = document_location
        input_["feature_types"] = feature_types
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if output_config is not None:
            input_["output_config"] = output_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if queries_config is not None:
            input_["queries_config"] = queries_config
        if adapters_config is not None:
            input_["adapters_config"] = adapters_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_document_text_detection(
        self,
        document_location: "aws_sdk_textract.types.document_location.DocumentLocation",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        job_tag: Optional["aws_sdk_textract.types.job_tag.JobTag"] = None,
        notification_channel: Optional[
            "aws_sdk_textract.types.notification_channel.NotificationChannel"
        ] = None,
        output_config: Optional[
            "aws_sdk_textract.types.output_config.OutputConfig"
        ] = None,
        kms_key_id: Optional["aws_sdk_textract.types.kms_key_id.KMSKeyId"] = None,
    ) -> "aws_sdk_textract.types.start_document_text_detection_response.StartDocumentTextDetectionResponse":
        r"""<p>Starts the asynchronous detection of text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.</p> <p> <code>StartDocumentTextDetection</code> can analyze text in documents that are in JPEG, PNG, TIFF, and PDF format. The documents are stored in an Amazon S3 bucket. Use <a>DocumentLocation</a> to specify the bucket name and file name of the document. </p> <p> <code>StartDocumentTextDetection</code> returns a job identifier (<code>JobId</code>) that you use to get the results of the operation. When text detection is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in <code>NotificationChannel</code>. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetDocumentTextDetection</a>, and pass the job identifier (<code>JobId</code>) from the initial call to <code>StartDocumentTextDetection</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html\">Document Text Detection</a>.</p>

        Args:
            document_location: <p>The location of the document to be processed.</p>
            client_request_token: <p>The idempotent token that's used to identify the start request. If you use the same token with multiple <code>StartDocumentTextDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentally started more than once. For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/api-async.html\">Calling Amazon Textract Asynchronous Operations</a>.</p>
            job_tag: <p>An identifier that you specify that's included in the completion notification published to the Amazon SNS topic. For example, you can use <code>JobTag</code> to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).</p>
            notification_channel: <p>The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to. </p>
            output_config: <p>Sets if the output will go to a customer defined bucket. By default Amazon Textract will save the results internally to be accessed with the GetDocumentTextDetection operation.</p>
            kms_key_id: <p>The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side,using SSE-S3.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.start_document_text_detection_request.StartDocumentTextDetectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.start_document_text_detection_response.StartDocumentTextDetectionResponse"
        ]:
            import aws_sdk_textract._operations.textract.start_document_text_detection

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.start_document_text_detection.async_start_document_text_detection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.start_document_text_detection_request.StartDocumentTextDetectionRequest = {}  # type: ignore[typeddict-item]
        input_["document_location"] = document_location
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if output_config is not None:
            input_["output_config"] = output_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_expense_analysis(
        self,
        document_location: "aws_sdk_textract.types.document_location.DocumentLocation",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        job_tag: Optional["aws_sdk_textract.types.job_tag.JobTag"] = None,
        notification_channel: Optional[
            "aws_sdk_textract.types.notification_channel.NotificationChannel"
        ] = None,
        output_config: Optional[
            "aws_sdk_textract.types.output_config.OutputConfig"
        ] = None,
        kms_key_id: Optional["aws_sdk_textract.types.kms_key_id.KMSKeyId"] = None,
    ) -> "aws_sdk_textract.types.start_expense_analysis_response.StartExpenseAnalysisResponse":
        r"""<p>Starts the asynchronous analysis of invoices or receipts for data like contact information, items purchased, and vendor names.</p> <p> <code>StartExpenseAnalysis</code> can analyze text in documents that are in JPEG, PNG, and PDF format. The documents must be stored in an Amazon S3 bucket. Use the <a>DocumentLocation</a> parameter to specify the name of your S3 bucket and the name of the document in that bucket. </p> <p> <code>StartExpenseAnalysis</code> returns a job identifier (<code>JobId</code>) that you will provide to <code>GetExpenseAnalysis</code> to retrieve the results of the operation. When the analysis of the input invoices/receipts is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you provide to the <code>NotificationChannel</code>. To obtain the results of the invoice and receipt analysis operation, ensure that the status value published to the Amazon SNS topic is <code>SUCCEEDED</code>. If so, call <a>GetExpenseAnalysis</a>, and pass the job identifier (<code>JobId</code>) that was returned by your call to <code>StartExpenseAnalysis</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/invoice-receipts.html\">Analyzing Invoices and Receipts</a>.</p>

        Args:
            document_location: <p>The location of the document to be processed.</p>
            client_request_token: <p>The idempotent token that's used to identify the start request. If you use the same token with multiple <code>StartDocumentTextDetection</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentally started more than once. For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/api-async.html\">Calling Amazon Textract Asynchronous Operations</a> </p>
            job_tag: <p>An identifier you specify that's included in the completion notification published to the Amazon SNS topic. For example, you can use <code>JobTag</code> to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).</p>
            notification_channel: <p>The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to. </p>
            output_config: <p>Sets if the output will go to a customer defined bucket. By default, Amazon Textract will save the results internally to be accessed by the <code>GetExpenseAnalysis</code> operation.</p>
            kms_key_id: <p>The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side,using SSE-S3.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.start_expense_analysis_request.StartExpenseAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.start_expense_analysis_response.StartExpenseAnalysisResponse"
        ]:
            import aws_sdk_textract._operations.textract.start_expense_analysis

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.start_expense_analysis.async_start_expense_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.start_expense_analysis_request.StartExpenseAnalysisRequest = {}  # type: ignore[typeddict-item]
        input_["document_location"] = document_location
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if output_config is not None:
            input_["output_config"] = output_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_lending_analysis(
        self,
        document_location: "aws_sdk_textract.types.document_location.DocumentLocation",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_textract.types.client_request_token.ClientRequestToken"
        ] = None,
        job_tag: Optional["aws_sdk_textract.types.job_tag.JobTag"] = None,
        notification_channel: Optional[
            "aws_sdk_textract.types.notification_channel.NotificationChannel"
        ] = None,
        output_config: Optional[
            "aws_sdk_textract.types.output_config.OutputConfig"
        ] = None,
        kms_key_id: Optional["aws_sdk_textract.types.kms_key_id.KMSKeyId"] = None,
    ) -> "aws_sdk_textract.types.start_lending_analysis_response.StartLendingAnalysisResponse":
        r"""<p>Starts the classification and analysis of an input document. <code>StartLendingAnalysis</code> initiates the classification and analysis of a packet of lending documents. <code>StartLendingAnalysis</code> operates on a document file located in an Amazon S3 bucket.</p> <p> <code>StartLendingAnalysis</code> can analyze text in documents that are in one of the following formats: JPEG, PNG, TIFF, PDF. Use <code>DocumentLocation</code> to specify the bucket name and the file name of the document. </p> <p> <code>StartLendingAnalysis</code> returns a job identifier (<code>JobId</code>) that you use to get the results of the operation. When the text analysis is finished, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that you specify in <code>NotificationChannel</code>. To get the results of the text analysis operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED. If the status is SUCCEEDED you can call either <code>GetLendingAnalysis</code> or <code>GetLendingAnalysisSummary</code> and provide the <code>JobId</code> to obtain the results of the analysis.</p> <p>If using <code>OutputConfig</code> to specify an Amazon S3 bucket, the output will be contained within the specified prefix in a directory labeled with the job-id. In the directory there are 3 sub-directories: </p> <ul> <li> <p>detailedResponse (contains the GetLendingAnalysis response)</p> </li> <li> <p>summaryResponse (for the GetLendingAnalysisSummary response)</p> </li> <li> <p>splitDocuments (documents split across logical boundaries)</p> </li> </ul>

        Args:
            client_request_token: <p>The idempotent token that you use to identify the start request. If you use the same token with multiple <code>StartLendingAnalysis</code> requests, the same <code>JobId</code> is returned. Use <code>ClientRequestToken</code> to prevent the same job from being accidentally started more than once. For more information, see <a href=\"https://docs.aws.amazon.com/textract/latest/dg/api-sync.html\">Calling Amazon Textract Asynchronous Operations</a>.</p>
            job_tag: <p>An identifier that you specify to be included in the completion notification published to the Amazon SNS topic. For example, you can use <code>JobTag</code> to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).</p>
            kms_key_id: <p>The KMS key used to encrypt the inference results. This can be in either Key ID or Key Alias format. When a KMS key is provided, the KMS key will be used for server-side encryption of the objects in the customer bucket. When this parameter is not enabled, the result will be encrypted server side, using SSE-S3. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.start_lending_analysis_request.StartLendingAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.start_lending_analysis_response.StartLendingAnalysisResponse"
        ]:
            import aws_sdk_textract._operations.textract.start_lending_analysis

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.start_lending_analysis.async_start_lending_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.start_lending_analysis_request.StartLendingAnalysisRequest = {}  # type: ignore[typeddict-item]
        input_["document_location"] = document_location
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if job_tag is not None:
            input_["job_tag"] = job_tag
        if notification_channel is not None:
            input_["notification_channel"] = notification_channel
        if output_config is not None:
            input_["output_config"] = output_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_textract.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_textract.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> "aws_sdk_textract.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that specifies the resource to be tagged.</p>
            tags: <p>A set of tags (key-value pairs) that you want to assign to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_textract._operations.textract.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_textract.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_textract.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
    ) -> "aws_sdk_textract.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes any tags with the specified keys from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that specifies the resource to be untagged.</p>
            tag_keys: <p>Specifies the tags to be removed from the resource specified by the ResourceARN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_textract._operations.textract.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_adapter(
        self,
        adapter_id: "aws_sdk_textract.types.adapter_id.AdapterId",
        *,
        config_overrides: Optional[AsyncTextractClientConfig] = None,
        description: Optional[
            "aws_sdk_textract.types.adapter_description.AdapterDescription"
        ] = None,
        adapter_name: Optional[
            "aws_sdk_textract.types.adapter_name.AdapterName"
        ] = None,
        auto_update: Optional["aws_sdk_textract.types.auto_update.AutoUpdate"] = None,
    ) -> "aws_sdk_textract.types.update_adapter_response.UpdateAdapterResponse":
        """<p>Update the configuration for an adapter. FeatureTypes configurations cannot be updated. At least one new parameter must be specified as an argument.</p>

        Args:
            adapter_id: <p>A string containing a unique ID for the adapter that will be updated.</p>
            description: <p>The new description to be applied to the adapter.</p>
            adapter_name: <p>The new name to be applied to the adapter.</p>
            auto_update: <p>The new auto-update status to be applied to the adapter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_textract.types.update_adapter_request.UpdateAdapterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_textract.types.update_adapter_response.UpdateAdapterResponse"
        ]:
            import aws_sdk_textract._operations.textract.update_adapter

            (
                output,
                http_response,
            ) = await aws_sdk_textract._operations.textract.update_adapter.async_update_adapter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_textract.types.update_adapter_request.UpdateAdapterRequest = {}  # type: ignore[typeddict-item]
        input_["adapter_id"] = adapter_id
        if description is not None:
            input_["description"] = description
        if adapter_name is not None:
            input_["adapter_name"] = adapter_name
        if auto_update is not None:
            input_["auto_update"] = auto_update

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
