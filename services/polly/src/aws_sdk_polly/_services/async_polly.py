"""Generated from Smithy shape ``com.amazonaws.polly#Parrot_v1``."""

import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_polly._auth._signers
import aws_sdk_polly._auth._sigv4
from aws_sdk_polly._auth._identity import Credentials
from aws_sdk_polly._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_polly._auth._zapros_handler import AuthMiddleware
from aws_sdk_polly._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_polly.types.delete_lexicon_input
    import aws_sdk_polly.types.delete_lexicon_output
    import aws_sdk_polly.types.describe_voices_input
    import aws_sdk_polly.types.describe_voices_output
    import aws_sdk_polly.types.engine
    import aws_sdk_polly.types.get_lexicon_input
    import aws_sdk_polly.types.get_lexicon_output
    import aws_sdk_polly.types.get_speech_synthesis_task_input
    import aws_sdk_polly.types.get_speech_synthesis_task_output
    import aws_sdk_polly.types.include_additional_language_codes
    import aws_sdk_polly.types.language_code
    import aws_sdk_polly.types.lexicon_content
    import aws_sdk_polly.types.lexicon_name
    import aws_sdk_polly.types.lexicon_name_list
    import aws_sdk_polly.types.list_lexicons_input
    import aws_sdk_polly.types.list_lexicons_output
    import aws_sdk_polly.types.list_speech_synthesis_tasks_input
    import aws_sdk_polly.types.list_speech_synthesis_tasks_output
    import aws_sdk_polly.types.max_results
    import aws_sdk_polly.types.next_token
    import aws_sdk_polly.types.output_format
    import aws_sdk_polly.types.output_s3_bucket_name
    import aws_sdk_polly.types.output_s3_key_prefix
    import aws_sdk_polly.types.put_lexicon_input
    import aws_sdk_polly.types.put_lexicon_output
    import aws_sdk_polly.types.sample_rate
    import aws_sdk_polly.types.sns_topic_arn
    import aws_sdk_polly.types.speech_mark_type_list
    import aws_sdk_polly.types.start_speech_synthesis_stream_action_stream
    import aws_sdk_polly.types.start_speech_synthesis_stream_input
    import aws_sdk_polly.types.start_speech_synthesis_stream_output
    import aws_sdk_polly.types.start_speech_synthesis_task_input
    import aws_sdk_polly.types.start_speech_synthesis_task_output
    import aws_sdk_polly.types.synthesize_speech_input
    import aws_sdk_polly.types.synthesize_speech_output
    import aws_sdk_polly.types.task_id
    import aws_sdk_polly.types.task_status
    import aws_sdk_polly.types.text
    import aws_sdk_polly.types.text_type
    import aws_sdk_polly.types.voice_id


class AsyncPollyClientConfig(TypedDict, total=False):
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


class AsyncPollyClient:
    """A client for the ``Polly`` service.

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
        self.config = AsyncPollyClientConfig(
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
        self, config_overrides: Optional[AsyncPollyClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPollyClientConfig = config_overrides or {}
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

    async def delete_lexicon(
        self,
        name: "aws_sdk_polly.types.lexicon_name.LexiconName",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
    ) -> "aws_sdk_polly.types.delete_lexicon_output.DeleteLexiconOutput":
        """<p>Deletes the specified pronunciation lexicon stored in an Amazon Web Services Region. A lexicon which has been deleted is not available for speech synthesis, nor is it possible to retrieve it using either the <code>GetLexicon</code> or <code>ListLexicon</code> APIs.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\">Managing Lexicons</a>.</p>

        Args:
            name: <p>The name of the lexicon to delete. Must be an existing lexicon in the region.</p>

        Examples:
            To delete a lexicon
            Deletes a specified pronunciation lexicon stored in an AWS Region.

            >>> await client.delete_lexicon(name='example')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_polly.types.delete_lexicon_input.DeleteLexiconInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_polly.types.delete_lexicon_output.DeleteLexiconOutput"
        ]:
            import aws_sdk_polly._operations.parrot_v1.delete_lexicon

            (
                output,
                http_response,
            ) = await aws_sdk_polly._operations.parrot_v1.delete_lexicon.async_delete_lexicon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_polly.types.delete_lexicon_input.DeleteLexiconInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_voices(
        self,
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        engine: Optional["aws_sdk_polly.types.engine.Engine"] = None,
        language_code: Optional[
            "aws_sdk_polly.types.language_code.LanguageCode"
        ] = None,
        include_additional_language_codes: Optional[
            "aws_sdk_polly.types.include_additional_language_codes.IncludeAdditionalLanguageCodes"
        ] = None,
        next_token: Optional["aws_sdk_polly.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_polly.types.describe_voices_output.DescribeVoicesOutput":
        """<p>Returns the list of voices that are available for use when requesting speech synthesis. Each voice speaks a specified language, is either male or female, and is identified by an ID, which is the ASCII version of the voice name. </p> <p>When synthesizing speech ( <code>SynthesizeSpeech</code> ), you provide the voice ID for the voice you want from the list of voices returned by <code>DescribeVoices</code>.</p> <p>For example, you want your news reader application to read news in a specific language, but giving a user the option to choose the voice. Using the <code>DescribeVoices</code> operation you can provide the user with a list of available voices to select from.</p> <p> You can optionally specify a language code to filter the available voices. For example, if you specify <code>en-US</code>, the operation returns a list of all available US English voices. </p> <p>This operation requires permissions to perform the <code>polly:DescribeVoices</code> action.</p>

        Args:
            engine: <p>Specifies the engine (<code>standard</code>, <code>neural</code>, <code>long-form</code> or <code>generative</code>) used by Amazon Polly when processing input text for speech synthesis. </p>
            language_code: <p> The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don't specify this optional parameter, all available voices are returned. </p>
            include_additional_language_codes: <p>Boolean value indicating whether to return any bilingual voices that use the specified language as an additional language. For instance, if you request all languages that use US English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US English, that voice will be included if you specify <code>yes</code> but not if you specify <code>no</code>.</p>
            next_token: <p>An opaque pagination token returned from the previous <code>DescribeVoices</code> operation. If present, this indicates where to continue the listing.</p>

        Examples:
            To describe available voices
            Returns the list of voices that are available for use when requesting speech synthesis. Displayed languages are those within the specified language code. If no language code is specified, voices for all available languages are displayed.

            >>> await client.describe_voices(language_code='en-GB')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_polly.types.describe_voices_input.DescribeVoicesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_polly.types.describe_voices_output.DescribeVoicesOutput"
        ]:
            import aws_sdk_polly._operations.parrot_v1.describe_voices

            (
                output,
                http_response,
            ) = await aws_sdk_polly._operations.parrot_v1.describe_voices.async_describe_voices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_polly.types.describe_voices_input.DescribeVoicesInput = {}  # type: ignore[typeddict-item]
        if engine is not None:
            input_["engine"] = engine
        if language_code is not None:
            input_["language_code"] = language_code
        if include_additional_language_codes is not None:
            input_["include_additional_language_codes"] = (
                include_additional_language_codes
            )
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_lexicon(
        self,
        name: "aws_sdk_polly.types.lexicon_name.LexiconName",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
    ) -> "aws_sdk_polly.types.get_lexicon_output.GetLexiconOutput":
        """<p>Returns the content of the specified pronunciation lexicon stored in an Amazon Web Services Region. For more information, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\">Managing Lexicons</a>.</p>

        Args:
            name: <p>Name of the lexicon.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_polly.types.get_lexicon_input.GetLexiconInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_polly.types.get_lexicon_output.GetLexiconOutput"
        ]:
            import aws_sdk_polly._operations.parrot_v1.get_lexicon

            (
                output,
                http_response,
            ) = await aws_sdk_polly._operations.parrot_v1.get_lexicon.async_get_lexicon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_polly.types.get_lexicon_input.GetLexiconInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_speech_synthesis_task(
        self,
        task_id: "aws_sdk_polly.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
    ) -> "aws_sdk_polly.types.get_speech_synthesis_task_output.GetSpeechSynthesisTaskOutput":
        """<p>Retrieves a specific SpeechSynthesisTask object based on its TaskID. This object contains information about the given speech synthesis task, including the status of the task, and a link to the S3 bucket containing the output of the task.</p>

        Args:
            task_id: <p>The Amazon Polly generated identifier for a speech synthesis task.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_polly.types.get_speech_synthesis_task_input.GetSpeechSynthesisTaskInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_polly.types.get_speech_synthesis_task_output.GetSpeechSynthesisTaskOutput"
        ]:
            import aws_sdk_polly._operations.parrot_v1.get_speech_synthesis_task

            (
                output,
                http_response,
            ) = await aws_sdk_polly._operations.parrot_v1.get_speech_synthesis_task.async_get_speech_synthesis_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_polly.types.get_speech_synthesis_task_input.GetSpeechSynthesisTaskInput = {}  # type: ignore[typeddict-item]
        input_["task_id"] = task_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_lexicons(
        self,
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        next_token: Optional["aws_sdk_polly.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_polly.types.list_lexicons_output.ListLexiconsOutput":
        """<p>Returns a list of pronunciation lexicons stored in an Amazon Web Services Region. For more information, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\">Managing Lexicons</a>.</p>

        Args:
            next_token: <p>An opaque pagination token returned from previous <code>ListLexicons</code> operation. If present, indicates where to continue the list of lexicons.</p>

        Examples:
            To list all lexicons in a region
            Returns a list of pronunciation lexicons stored in an AWS Region.

            >>> await client.list_lexicons()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_polly.types.list_lexicons_input.ListLexiconsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_polly.types.list_lexicons_output.ListLexiconsOutput"
        ]:
            import aws_sdk_polly._operations.parrot_v1.list_lexicons

            (
                output,
                http_response,
            ) = await aws_sdk_polly._operations.parrot_v1.list_lexicons.async_list_lexicons(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_polly.types.list_lexicons_input.ListLexiconsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_speech_synthesis_tasks(
        self,
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        max_results: Optional["aws_sdk_polly.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_polly.types.next_token.NextToken"] = None,
        status: Optional["aws_sdk_polly.types.task_status.TaskStatus"] = None,
    ) -> "aws_sdk_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput":
        """<p>Returns a list of SpeechSynthesisTask objects ordered by their creation date. This operation can filter the tasks by their status, for example, allowing users to list only tasks that are completed.</p>

        Args:
            max_results: <p>Maximum number of speech synthesis tasks returned in a List operation.</p>
            next_token: <p>The pagination token to use in the next request to continue the listing of speech synthesis tasks. </p>
            status: <p>Status of the speech synthesis tasks returned in a List operation</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_polly.types.list_speech_synthesis_tasks_input.ListSpeechSynthesisTasksInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_polly.types.list_speech_synthesis_tasks_output.ListSpeechSynthesisTasksOutput"
        ]:
            import aws_sdk_polly._operations.parrot_v1.list_speech_synthesis_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_polly._operations.parrot_v1.list_speech_synthesis_tasks.async_list_speech_synthesis_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_polly.types.list_speech_synthesis_tasks_input.ListSpeechSynthesisTasksInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_lexicon(
        self,
        name: "aws_sdk_polly.types.lexicon_name.LexiconName",
        content: "aws_sdk_polly.types.lexicon_content.LexiconContent",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
    ) -> "aws_sdk_polly.types.put_lexicon_output.PutLexiconOutput":
        """<p>Stores a pronunciation lexicon in an Amazon Web Services Region. If a lexicon with the same name already exists in the region, it is overwritten by the new lexicon. Lexicon operations have eventual consistency, therefore, it might take some time before the lexicon is available to the SynthesizeSpeech operation.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\">Managing Lexicons</a>.</p>

        Args:
            name: <p>Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long. </p>
            content: <p>Content of the PLS lexicon as string data.</p>

        Examples:
            To save a lexicon
            Stores a pronunciation lexicon in an AWS Region.

            >>> await client.put_lexicon(name='W3C', content='<Lexicon Content>')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_polly.types.put_lexicon_input.PutLexiconInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_polly.types.put_lexicon_output.PutLexiconOutput"
        ]:
            import aws_sdk_polly._operations.parrot_v1.put_lexicon

            (
                output,
                http_response,
            ) = await aws_sdk_polly._operations.parrot_v1.put_lexicon.async_put_lexicon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_polly.types.put_lexicon_input.PutLexiconInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["content"] = content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_speech_synthesis_stream(
        self,
        engine: "aws_sdk_polly.types.engine.Engine",
        output_format: "aws_sdk_polly.types.output_format.OutputFormat",
        voice_id: "aws_sdk_polly.types.voice_id.VoiceId",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        language_code: Optional[
            "aws_sdk_polly.types.language_code.LanguageCode"
        ] = None,
        lexicon_names: Optional[
            "aws_sdk_polly.types.lexicon_name_list.LexiconNameList"
        ] = None,
        sample_rate: Optional["aws_sdk_polly.types.sample_rate.SampleRate"] = None,
        action_stream: Optional[AsyncIterator[bytes] | bytes] = None,
    ) -> "aws_sdk_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput":
        """<p>Synthesizes UTF-8 input, plain text, or SSML over a bidirectional streaming connection. Specify synthesis parameters in HTTP/2 headers, send text incrementally as events on the input stream, and receive synthesized audio as it becomes available.</p> <p>This operation serves as a bidirectional counterpart to <code>SynthesizeSpeech</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/polly/latest/API/API_SynthesizeSpeech.html\">SynthesizeSpeech</a> </p> </li> </ul>

        Args:
            engine: <p>Specifies the engine for Amazon Polly to use when processing input text for speech synthesis. Currently, only the <code>generative</code> engine is supported. If you specify a voice that the selected engine doesn't support, Amazon Polly returns an error.</p>
            language_code: <p>An optional parameter that sets the language code for the speech synthesis request. Specify this parameter only when using a bilingual voice. If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice.</p>
            lexicon_names: <p>The names of one or more pronunciation lexicons for the service to apply during synthesis. Amazon Polly applies lexicons only when the lexicon language matches the voice language.</p>
            output_format: <p>The audio format for the synthesized speech. Currently, Amazon Polly does not support JSON speech marks.</p>
            sample_rate: <p>The audio frequency, specified in Hz.</p>
            voice_id: <p>The voice to use in synthesis. To get a list of available voice IDs, use the <a href=\"https://docs.aws.amazon.com/polly/latest/API/API_DescribeVoices.html\">DescribeVoices</a> operation.</p>
            action_stream: <p>The input event stream that contains text events and stream control events.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_polly.types.start_speech_synthesis_stream_input.StartSpeechSynthesisStreamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_polly.types.start_speech_synthesis_stream_output.StartSpeechSynthesisStreamOutput"
        ]:
            import aws_sdk_polly._operations.parrot_v1.start_speech_synthesis_stream

            (
                output,
                http_response,
            ) = await aws_sdk_polly._operations.parrot_v1.start_speech_synthesis_stream.async_start_speech_synthesis_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_polly.types.start_speech_synthesis_stream_input.StartSpeechSynthesisStreamInput = {}  # type: ignore[typeddict-item]
        input_["engine"] = engine
        if language_code is not None:
            input_["language_code"] = language_code
        if lexicon_names is not None:
            input_["lexicon_names"] = lexicon_names
        input_["output_format"] = output_format
        if sample_rate is not None:
            input_["sample_rate"] = sample_rate
        input_["voice_id"] = voice_id
        if action_stream is not None:
            input_["action_stream"] = ensure_async_iterator(action_stream)  # type: ignore

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_speech_synthesis_task(
        self,
        output_format: "aws_sdk_polly.types.output_format.OutputFormat",
        output_s3_bucket_name: "aws_sdk_polly.types.output_s3_bucket_name.OutputS3BucketName",
        text: "aws_sdk_polly.types.text.Text",
        voice_id: "aws_sdk_polly.types.voice_id.VoiceId",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        engine: Optional["aws_sdk_polly.types.engine.Engine"] = None,
        language_code: Optional[
            "aws_sdk_polly.types.language_code.LanguageCode"
        ] = None,
        lexicon_names: Optional[
            "aws_sdk_polly.types.lexicon_name_list.LexiconNameList"
        ] = None,
        output_s3_key_prefix: Optional[
            "aws_sdk_polly.types.output_s3_key_prefix.OutputS3KeyPrefix"
        ] = None,
        sample_rate: Optional["aws_sdk_polly.types.sample_rate.SampleRate"] = None,
        sns_topic_arn: Optional["aws_sdk_polly.types.sns_topic_arn.SnsTopicArn"] = None,
        speech_mark_types: Optional[
            "aws_sdk_polly.types.speech_mark_type_list.SpeechMarkTypeList"
        ] = None,
        text_type: Optional["aws_sdk_polly.types.text_type.TextType"] = None,
    ) -> "aws_sdk_polly.types.start_speech_synthesis_task_output.StartSpeechSynthesisTaskOutput":
        """<p>Allows the creation of an asynchronous synthesis task, by starting a new <code>SpeechSynthesisTask</code>. This operation requires all the standard information needed for speech synthesis, plus the name of an Amazon S3 bucket for the service to store the output of the synthesis task and two optional parameters (<code>OutputS3KeyPrefix</code> and <code>SnsTopicArn</code>). Once the synthesis task is created, this operation will return a <code>SpeechSynthesisTask</code> object, which will include an identifier of this task as well as the current status. The <code>SpeechSynthesisTask</code> object is available for 72 hours after starting the asynchronous synthesis task.</p>

        Args:
            engine: <p>Specifies the engine (<code>standard</code>, <code>neural</code>, <code>long-form</code> or <code>generative</code>) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.</p>
            language_code: <p>Optional language code for the Speech Synthesis request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). </p> <p>If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the <a href=\"https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html\">DescribeVoices</a> operation for the <code>LanguageCode</code> parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.</p>
            lexicon_names: <p>List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. </p>
            output_format: <p>The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, ogg_opus, mu-law, a-law, or pcm. For speech marks, this will be json. </p>
            output_s3_bucket_name: <p>Amazon S3 bucket name to which the output file will be saved.</p>
            output_s3_key_prefix: <p>The Amazon S3 key prefix for the output speech file.</p>
            sample_rate: <p>The audio frequency specified in Hz.</p> <p>The valid values for mp3 and ogg_vorbis are \"8000\", \"16000\", \"22050\", and \"24000\". The default value for standard voices is \"22050\". The default value for neural voices is \"24000\". The default value for long-form voices is \"24000\". The default value for generative voices is \"24000\".</p> <p>Valid values for pcm are \"8000\" and \"16000\" The default value is \"16000\". </p> <p>Valid value for ogg_opus is \"48000\". </p> <p>Valid value for mu-law and a-law is \"8000\". </p>
            sns_topic_arn: <p>ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.</p>
            speech_mark_types: <p>The type of speech marks returned for the input text.</p>
            text: <p>The input text to synthesize. If you specify ssml as the TextType, follow the SSML format for the input text. </p>
            text_type: <p>Specifies whether the input text is plain text or SSML. The default value is plain text. </p>
            voice_id: <p>Voice ID to use for the synthesis. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_polly.types.start_speech_synthesis_task_input.StartSpeechSynthesisTaskInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_polly.types.start_speech_synthesis_task_output.StartSpeechSynthesisTaskOutput"
        ]:
            import aws_sdk_polly._operations.parrot_v1.start_speech_synthesis_task

            (
                output,
                http_response,
            ) = await aws_sdk_polly._operations.parrot_v1.start_speech_synthesis_task.async_start_speech_synthesis_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_polly.types.start_speech_synthesis_task_input.StartSpeechSynthesisTaskInput = {}  # type: ignore[typeddict-item]
        if engine is not None:
            input_["engine"] = engine
        if language_code is not None:
            input_["language_code"] = language_code
        if lexicon_names is not None:
            input_["lexicon_names"] = lexicon_names
        input_["output_format"] = output_format
        input_["output_s3_bucket_name"] = output_s3_bucket_name
        if output_s3_key_prefix is not None:
            input_["output_s3_key_prefix"] = output_s3_key_prefix
        if sample_rate is not None:
            input_["sample_rate"] = sample_rate
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if speech_mark_types is not None:
            input_["speech_mark_types"] = speech_mark_types
        input_["text"] = text
        if text_type is not None:
            input_["text_type"] = text_type
        input_["voice_id"] = voice_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    @asynccontextmanager
    async def synthesize_speech(
        self,
        output_format: "aws_sdk_polly.types.output_format.OutputFormat",
        text: "aws_sdk_polly.types.text.Text",
        voice_id: "aws_sdk_polly.types.voice_id.VoiceId",
        *,
        config_overrides: Optional[AsyncPollyClientConfig] = None,
        engine: Optional["aws_sdk_polly.types.engine.Engine"] = None,
        language_code: Optional[
            "aws_sdk_polly.types.language_code.LanguageCode"
        ] = None,
        lexicon_names: Optional[
            "aws_sdk_polly.types.lexicon_name_list.LexiconNameList"
        ] = None,
        sample_rate: Optional["aws_sdk_polly.types.sample_rate.SampleRate"] = None,
        speech_mark_types: Optional[
            "aws_sdk_polly.types.speech_mark_type_list.SpeechMarkTypeList"
        ] = None,
        text_type: Optional["aws_sdk_polly.types.text_type.TextType"] = None,
    ) -> "AsyncGenerator[aws_sdk_polly.types.synthesize_speech_output.SynthesizeSpeechOutput]":
        """<p>Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid, well-formed SSML. Some alphabets might not be available with all the voices (for example, Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For more information, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-works.html\">How it Works</a>.</p>

        Args:
            engine: <p>Specifies the engine (<code>standard</code>, <code>neural</code>, <code>long-form</code>, or <code>generative</code>) for Amazon Polly to use when processing input text for speech synthesis. Provide an engine that is supported by the voice you select. If you don't provide an engine, the standard engine is selected by default. If a chosen voice isn't supported by the standard engine, this will result in an error. For information on Amazon Polly voices and which voices are available for each engine, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/voicelist.html\">Available Voices</a>.</p>
            language_code: <p>Optional language code for the Synthesize Speech request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN). </p> <p>If a bilingual voice is used and no language code is specified, Amazon Polly uses the default language of the bilingual voice. The default language for any voice is the one returned by the <a href=\"https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html\">DescribeVoices</a> operation for the <code>LanguageCode</code> parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.</p>
            lexicon_names: <p>List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html\">PutLexicon</a>.</p>
            output_format: <p> The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, ogg_opus, mu-law, a-law or pcm. For speech marks, this will be json. </p> <p>When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format. </p>
            sample_rate: <p>The audio frequency specified in Hz.</p> <p>The valid values for mp3 and ogg_vorbis are \"8000\", \"16000\", \"22050\", \"24000\", \"44100\" and \"48000\". The default value for standard voices is \"22050\". The default value for neural voices is \"24000\". The default value for long-form voices is \"24000\". The default value for generative voices is \"24000\".</p> <p>Valid values for pcm are \"8000\" and \"16000\" The default value is \"16000\". </p> <p>Valid value for ogg_opus is \"48000\". </p> <p>Valid value for mu-law and a-law is \"8000\". </p>
            speech_mark_types: <p>The type of speech marks returned for the input text.</p>
            text: <p> Input text to synthesize. If you specify <code>ssml</code> as the <code>TextType</code>, follow the SSML format for the input text. </p>
            text_type: <p> Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see <a href=\"https://docs.aws.amazon.com/polly/latest/dg/ssml.html\">Using SSML</a>.</p>
            voice_id: <p> Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the <a href=\"https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html\">DescribeVoices</a> operation. </p>

        Examples:
            To synthesize speech
            Synthesizes plain text or SSML into a file of human-like speech.

            >>> await client.synthesize_speech(lexicon_names=['example'], output_format='mp3', sample_rate='8000', text='All Gaul is divided into three parts', text_type='text', voice_id='Joanna')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_polly.types.synthesize_speech_input.SynthesizeSpeechInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_polly.types.synthesize_speech_output.SynthesizeSpeechOutput"
        ]:
            import aws_sdk_polly._operations.parrot_v1.synthesize_speech

            (
                output,
                http_response,
            ) = await aws_sdk_polly._operations.parrot_v1.synthesize_speech.async_synthesize_speech(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_polly.types.synthesize_speech_input.SynthesizeSpeechInput = {}  # type: ignore[typeddict-item]
        if engine is not None:
            input_["engine"] = engine
        if language_code is not None:
            input_["language_code"] = language_code
        if lexicon_names is not None:
            input_["lexicon_names"] = lexicon_names
        input_["output_format"] = output_format
        if sample_rate is not None:
            input_["sample_rate"] = sample_rate
        if speech_mark_types is not None:
            input_["speech_mark_types"] = speech_mark_types
        input_["text"] = text
        if text_type is not None:
            input_["text_type"] = text_type
        input_["voice_id"] = voice_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
