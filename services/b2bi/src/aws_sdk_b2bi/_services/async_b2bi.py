"""Generated from Smithy shape ``com.amazonaws.b2bi#B2BI``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

from aws_sdk_b2bi._auth._identity import Credentials
from aws_sdk_b2bi._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_b2bi._auth._zapros_handler import AuthMiddleware
from aws_sdk_b2bi._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.advanced_options
    import aws_sdk_b2bi.types.amazon_resource_name
    import aws_sdk_b2bi.types.conversion_source
    import aws_sdk_b2bi.types.conversion_target
    import aws_sdk_b2bi.types.create_starter_mapping_template_request
    import aws_sdk_b2bi.types.create_starter_mapping_template_response
    import aws_sdk_b2bi.types.edi_type
    import aws_sdk_b2bi.types.file_format
    import aws_sdk_b2bi.types.generate_mapping_input_file_content
    import aws_sdk_b2bi.types.generate_mapping_output_file_content
    import aws_sdk_b2bi.types.generate_mapping_request
    import aws_sdk_b2bi.types.generate_mapping_response
    import aws_sdk_b2bi.types.get_transformer_job_request
    import aws_sdk_b2bi.types.get_transformer_job_response
    import aws_sdk_b2bi.types.list_tags_for_resource_request
    import aws_sdk_b2bi.types.list_tags_for_resource_response
    import aws_sdk_b2bi.types.mapping_template
    import aws_sdk_b2bi.types.mapping_type
    import aws_sdk_b2bi.types.s3_location
    import aws_sdk_b2bi.types.start_transformer_job_request
    import aws_sdk_b2bi.types.start_transformer_job_response
    import aws_sdk_b2bi.types.tag_key_list
    import aws_sdk_b2bi.types.tag_list
    import aws_sdk_b2bi.types.tag_resource_request
    import aws_sdk_b2bi.types.template_details
    import aws_sdk_b2bi.types.test_conversion_request
    import aws_sdk_b2bi.types.test_conversion_response
    import aws_sdk_b2bi.types.test_mapping_input_file_content
    import aws_sdk_b2bi.types.test_mapping_request
    import aws_sdk_b2bi.types.test_mapping_response
    import aws_sdk_b2bi.types.test_parsing_request
    import aws_sdk_b2bi.types.test_parsing_response
    import aws_sdk_b2bi.types.transformer_id
    import aws_sdk_b2bi.types.transformer_job_id
    import aws_sdk_b2bi.types.untag_resource_request


class Asyncb2biClientConfig(TypedDict, total=False):
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


class Asyncb2biClient:
    """A client for the ``b2bi`` service.

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
        self.config = Asyncb2biClientConfig(
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
        self, config_overrides: Optional[Asyncb2biClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: Asyncb2biClientConfig = config_overrides or {}
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

    async def create_starter_mapping_template(
        self,
        mapping_type: "aws_sdk_b2bi.types.mapping_type.MappingType",
        template_details: "aws_sdk_b2bi.types.template_details.TemplateDetails",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        output_sample_location: Optional[
            "aws_sdk_b2bi.types.s3_location.S3Location"
        ] = None,
    ) -> "aws_sdk_b2bi.types.create_starter_mapping_template_response.CreateStarterMappingTemplateResponse":
        """<p>Amazon Web Services B2B Data Interchange uses a mapping template in JSONata or XSLT format to transform a customer input file into a JSON or XML file that can be converted to EDI.</p> <p>If you provide a sample EDI file with the same structure as the EDI files that you wish to generate, then the service can generate a mapping template. The starter template contains placeholder values which you can replace with JSONata or XSLT expressions to take data from your input file and insert it into the JSON or XML file that is used to generate the EDI.</p> <p>If you do not provide a sample EDI file, then the service can generate a mapping template based on the EDI settings in the <code>templateDetails</code> parameter. </p> <p> Currently, we only support generating a template that can generate the input to produce an Outbound X12 EDI file.</p>

        Args:
            output_sample_location: <p>Specify the location of the sample EDI file that is used to generate the mapping template.</p>
            mapping_type: <p>Specify the format for the mapping template: either JSONATA or XSLT.</p>
            template_details: <p> Describes the details needed for generating the template. Specify the X12 transaction set and version for which the template is used: currently, we only support X12. </p>

        Examples:
            Sample CreateStarterMappingTemplate call

            >>> await client.create_starter_mapping_template(mapping_type='JSONATA', template_details={'x12': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, output_sample_location={'bucketName': 'output-sample-bucket', 'key': 'output-sample-key'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.create_starter_mapping_template_request.CreateStarterMappingTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.create_starter_mapping_template_response.CreateStarterMappingTemplateResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.create_starter_mapping_template

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.create_starter_mapping_template.async_create_starter_mapping_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_b2bi.types.create_starter_mapping_template_request.CreateStarterMappingTemplateRequest = {}  # type: ignore[typeddict-item]
        if output_sample_location is not None:
            input["output_sample_location"] = output_sample_location
        input["mapping_type"] = mapping_type
        input["template_details"] = template_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def generate_mapping(
        self,
        input_file_content: "aws_sdk_b2bi.types.generate_mapping_input_file_content.GenerateMappingInputFileContent",
        output_file_content: "aws_sdk_b2bi.types.generate_mapping_output_file_content.GenerateMappingOutputFileContent",
        mapping_type: "aws_sdk_b2bi.types.mapping_type.MappingType",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "aws_sdk_b2bi.types.generate_mapping_response.GenerateMappingResponse":
        """<p>Takes sample input and output documents and uses Amazon Bedrock to generate a mapping automatically. Depending on the accuracy and other factors, you can then edit the mapping for your needs.</p> <note> <p>Before you can use the AI-assisted feature for Amazon Web Services B2B Data Interchange you must enable models in Amazon Bedrock. For details, see <a href=\"https://docs.aws.amazon.com/b2bi/latest/userguide/ai-assisted-mapping.html#ai-assist-prereq\">AI-assisted template mapping prerequisites</a> in the <i>Amazon Web Services B2B Data Interchange User guide</i>.</p> </note> <p>To generate a mapping, perform the following steps:</p> <ol> <li> <p>Start with an X12 EDI document to use as the input.</p> </li> <li> <p>Call <code>TestMapping</code> using your EDI document.</p> </li> <li> <p>Use the output from the <code>TestMapping</code> operation as either input or output for your GenerateMapping call, along with your sample file.</p> </li> </ol>

        Args:
            input_file_content: <p>Provide the contents of a sample X12 EDI file, either in JSON or XML format, to use as a starting point for the mapping.</p>
            output_file_content: <p>Provide the contents of a sample X12 EDI file, either in JSON or XML format, to use as a target for the mapping.</p>
            mapping_type: <p>Specify the mapping type: either <code>JSONATA</code> or <code>XSLT.</code> </p>

        Examples:
            Sample GenerateMapping call

            >>> await client.generate_mapping(input_file_content='Sample input file content', output_file_content='Sample output file content', mapping_type='JSONATA')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.generate_mapping_request.GenerateMappingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.generate_mapping_response.GenerateMappingResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.generate_mapping

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.generate_mapping.async_generate_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_b2bi.types.generate_mapping_request.GenerateMappingRequest = {}  # type: ignore[typeddict-item]
        input["input_file_content"] = input_file_content
        input["output_file_content"] = output_file_content
        input["mapping_type"] = mapping_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_transformer_job(
        self,
        transformer_job_id: "aws_sdk_b2bi.types.transformer_job_id.TransformerJobId",
        transformer_id: "aws_sdk_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "aws_sdk_b2bi.types.get_transformer_job_response.GetTransformerJobResponse":
        """<p>Returns the details of the transformer run, based on the Transformer job ID.</p> <note> <p>If 30 days have elapsed since your transformer job was started, the system deletes it. So, if you run <code>GetTransformerJob</code> and supply a <code>transformerId</code> and <code>transformerJobId</code> for a job that was started more than 30 days previously, you receive a 404 response.</p> </note>

        Args:
            transformer_job_id: <p>Specifies the unique, system-generated identifier for a transformer run.</p>
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>

        Examples:
            Sample GetTransformerJob call

            >>> await client.get_transformer_job(transformer_id='tr-974c129999f84d8c9', transformer_job_id='tj-vpYxfV7yQOqjMSYllEslLw')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.get_transformer_job_request.GetTransformerJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.get_transformer_job_response.GetTransformerJobResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.get_transformer_job

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.get_transformer_job.async_get_transformer_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_b2bi.types.get_transformer_job_request.GetTransformerJobRequest = {}  # type: ignore[typeddict-item]
        input["transformer_job_id"] = transformer_job_id
        input["transformer_id"] = transformer_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_b2bi.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> (
        "aws_sdk_b2bi.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify. The resource can be a capability, partnership, profile, or transformer.</p>

        Args:
            resource_arn: <p>Requests the tags associated with a particular Amazon Resource Name (ARN). An ARN is an identifier for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>

        Examples:
            Sample ListTagsForResources call

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:b2bi:us-west-2:123456789012:profile/p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_b2bi.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_transformer_job(
        self,
        input_file: "aws_sdk_b2bi.types.s3_location.S3Location",
        output_location: "aws_sdk_b2bi.types.s3_location.S3Location",
        transformer_id: "aws_sdk_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "aws_sdk_b2bi.types.start_transformer_job_response.StartTransformerJobResponse"
    ):
        """<p>Runs a job, using a transformer, to parse input EDI (electronic data interchange) file into the output structures used by Amazon Web Services B2B Data Interchange.</p> <p>If you only want to transform EDI (electronic data interchange) documents, you don't need to create profiles, partnerships or capabilities. Just create and configure a transformer, and then run the <code>StartTransformerJob</code> API to process your files.</p> <note> <p>The system stores transformer jobs for 30 days. During that period, you can run <a href=\"https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetTransformerJob.html\">GetTransformerJob</a> and supply its <code>transformerId</code> and <code>transformerJobId</code> to return details of the job.</p> </note>

        Args:
            input_file: <p>Specifies the location of the input file for the transformation. The location consists of an Amazon S3 bucket and prefix.</p>
            output_location: <p>Specifies the location of the output file for the transformation. The location consists of an Amazon S3 bucket and prefix.</p>
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>
            client_token: <p>Reserved for future use.</p>

        Examples:
            Sample StartTransformerJob call

            >>> await client.start_transformer_job(client_token='foo', input_file={'bucketName': 'test-bucket', 'key': 'input/inputFile.txt'}, output_location={'bucketName': 'test-bucket', 'key': 'output/'}, transformer_id='tr-974c129999f84d8c9')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.start_transformer_job_request.StartTransformerJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.start_transformer_job_response.StartTransformerJobResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.start_transformer_job

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.start_transformer_job.async_start_transformer_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_b2bi.types.start_transformer_job_request.StartTransformerJobRequest = {}  # type: ignore[typeddict-item]
        input["input_file"] = input_file
        input["output_location"] = output_location
        input["transformer_id"] = transformer_id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_b2bi.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_b2bi.types.tag_list.TagList",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN). Resources are capability, partnership, profile, transformers and other entities.</p> <p>There is no response returned from this call.</p>

        Args:
            resource_arn: <p>Specifies an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Examples:
            Sample TagResource call

            >>> await client.tag_resource(resource_arn='arn:aws:b2bi:us-west-2:123456789012:profile/p-60fbc37c87f04fce9', tags=[{'Key': 'sampleKey', 'Value': 'SampleValue'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_b2bi._operations.b2_bi.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_b2bi.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_conversion(
        self,
        source: "aws_sdk_b2bi.types.conversion_source.ConversionSource",
        target: "aws_sdk_b2bi.types.conversion_target.ConversionTarget",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "aws_sdk_b2bi.types.test_conversion_response.TestConversionResponse":
        """<p>This operation mimics the latter half of a typical Outbound EDI request. It takes an input JSON/XML in the B2Bi shape as input, converts it to an X12 EDI string, and return that string.</p>

        Args:
            source: <p>Specify the source file for an outbound EDI request.</p>
            target: <p>Specify the format (X12 is the only currently supported format), and other details for the conversion target.</p>

        Examples:
            Sample TestConversion call

            >>> await client.test_conversion(source={'fileFormat': 'JSON', 'inputFile': {'fileContent': 'Sample file content'}}, target={'fileFormat': 'X12', 'formatDetails': {'x12': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'advancedOptions': {'x12': {'validationOptions': {'validationRules': [{'codeListValidationRule': {'elementId': '1280', 'codesToAdd': ['X', 'Y', 'Z'], 'codesToRemove': ['A', 'B', 'C']}}, {'elementRequirementValidationRule': {'elementPosition': 'NM1-01', 'requirement': 'OPTIONAL'}}, {'elementLengthValidationRule': {'elementId': '0803', 'maxLength': 30, 'minLength': 5}}]}}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.test_conversion_request.TestConversionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.test_conversion_response.TestConversionResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.test_conversion

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.test_conversion.async_test_conversion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_b2bi.types.test_conversion_request.TestConversionRequest = {}  # type: ignore[typeddict-item]
        input["source"] = source
        input["target"] = target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_mapping(
        self,
        input_file_content: "aws_sdk_b2bi.types.test_mapping_input_file_content.TestMappingInputFileContent",
        mapping_template: "aws_sdk_b2bi.types.mapping_template.MappingTemplate",
        file_format: "aws_sdk_b2bi.types.file_format.FileFormat",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "aws_sdk_b2bi.types.test_mapping_response.TestMappingResponse":
        """<p>Maps the input file according to the provided template file. The API call downloads the file contents from the Amazon S3 location, and passes the contents in as a string, to the <code>inputFileContent</code> parameter.</p>

        Args:
            input_file_content: <p>Specify the contents of the EDI (electronic data interchange) XML or JSON file that is used as input for the transform.</p>
            mapping_template: <p>Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p> <note> <p>This parameter is available for backwards compatibility. Use the <a href=\"https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html\">Mapping</a> data type instead.</p> </note>
            file_format: <p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>

        Examples:
            Sample TestMapping call

            >>> await client.test_mapping(file_format='JSON', input_file_content='Sample file content', mapping_template='$')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.test_mapping_request.TestMappingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.test_mapping_response.TestMappingResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.test_mapping

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.test_mapping.async_test_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_b2bi.types.test_mapping_request.TestMappingRequest = {}  # type: ignore[typeddict-item]
        input["input_file_content"] = input_file_content
        input["mapping_template"] = mapping_template
        input["file_format"] = file_format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_parsing(
        self,
        input_file: "aws_sdk_b2bi.types.s3_location.S3Location",
        file_format: "aws_sdk_b2bi.types.file_format.FileFormat",
        edi_type: "aws_sdk_b2bi.types.edi_type.EdiType",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        advanced_options: Optional[
            "aws_sdk_b2bi.types.advanced_options.AdvancedOptions"
        ] = None,
    ) -> "aws_sdk_b2bi.types.test_parsing_response.TestParsingResponse":
        """<p>Parses the input EDI (electronic data interchange) file. The input file has a file size limit of 250 KB.</p>

        Args:
            input_file: <p>Specifies an <code>S3Location</code> object, which contains the Amazon S3 bucket and prefix for the location of the input file.</p>
            file_format: <p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>
            edi_type: <p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>
            advanced_options: <p>Specifies advanced options for parsing the input EDI file. These options allow for more granular control over the parsing process, including split options for X12 files.</p>

        Examples:
            Sample TestParsing call

            >>> await client.test_parsing(edi_type={'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, file_format='JSON', input_file={'bucketName': 'test-bucket', 'key': 'sampleFile.txt'})
            Sample TestParsing call without EDI Splitting

            >>> await client.test_parsing(edi_type={'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, file_format='JSON', advanced_options={'x12': {'splitOptions': {'splitBy': 'NONE'}}}, input_file={'bucketName': 'test-bucket', 'key': 'sampleFile.txt'})
            Sample TestParsing call with EDI Splitting by Transaction

            >>> await client.test_parsing(edi_type={'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, file_format='JSON', advanced_options={'x12': {'splitOptions': {'splitBy': 'TRANSACTION'}}}, input_file={'bucketName': 'test-bucket', 'key': 'sampleFile.txt'})
            Sample TestParsing call with Validation Options

            >>> await client.test_parsing(edi_type={'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, file_format='JSON', advanced_options={'x12': {'validationOptions': {'validationRules': [{'codeListValidationRule': {'elementId': '1280', 'codesToAdd': ['X', 'Y', 'Z'], 'codesToRemove': ['A', 'B', 'C']}}, {'elementRequirementValidationRule': {'elementPosition': 'NM1-01', 'requirement': 'OPTIONAL'}}, {'elementLengthValidationRule': {'elementId': '0803', 'maxLength': 30, 'minLength': 5}}]}}}, input_file={'bucketName': 'test-bucket', 'key': 'sampleFile.txt'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.test_parsing_request.TestParsingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.test_parsing_response.TestParsingResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.test_parsing

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.test_parsing.async_test_parsing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_b2bi.types.test_parsing_request.TestParsingRequest = {}  # type: ignore[typeddict-item]
        input["input_file"] = input_file
        input["file_format"] = file_format
        input["edi_type"] = edi_type
        if advanced_options is not None:
            input["advanced_options"] = advanced_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_b2bi.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_b2bi.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Detaches a key-value pair from the specified resource, as identified by its Amazon Resource Name (ARN). Resources are capability, partnership, profile, transformers and other entities.</p>

        Args:
            resource_arn: <p>Specifies an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>
            tag_keys: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Examples:
            Sample UntagResource call

            >>> await client.untag_resource(resource_arn='arn:aws:b2bi:us-west-2:123456789012:profile/p-60fbc37c87f04fce9', tag_keys=['sampleKey'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_b2bi._operations.b2_bi.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_b2bi.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

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
