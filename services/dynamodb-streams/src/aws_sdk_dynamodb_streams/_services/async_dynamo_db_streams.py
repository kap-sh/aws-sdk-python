"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#DynamoDBStreams_20120810``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_dynamodb_streams._auth._signers
import aws_sdk_dynamodb_streams._auth._sigv4
from aws_sdk_dynamodb_streams._auth._identity import Credentials
from aws_sdk_dynamodb_streams._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_dynamodb_streams._auth._zapros_handler import AuthMiddleware
from aws_sdk_dynamodb_streams._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.describe_stream_input
    import aws_sdk_dynamodb_streams.types.describe_stream_output
    import aws_sdk_dynamodb_streams.types.get_records_input
    import aws_sdk_dynamodb_streams.types.get_records_output
    import aws_sdk_dynamodb_streams.types.get_shard_iterator_input
    import aws_sdk_dynamodb_streams.types.get_shard_iterator_output
    import aws_sdk_dynamodb_streams.types.list_streams_input
    import aws_sdk_dynamodb_streams.types.list_streams_output
    import aws_sdk_dynamodb_streams.types.positive_integer_object
    import aws_sdk_dynamodb_streams.types.sequence_number
    import aws_sdk_dynamodb_streams.types.shard_filter
    import aws_sdk_dynamodb_streams.types.shard_id
    import aws_sdk_dynamodb_streams.types.shard_iterator
    import aws_sdk_dynamodb_streams.types.shard_iterator_type
    import aws_sdk_dynamodb_streams.types.stream_arn
    import aws_sdk_dynamodb_streams.types.table_name


class AsyncDynamoDBStreamsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
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


class AsyncDynamoDBStreamsClient:
    """A client for the ``DynamoDBStreams`` service.

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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncDynamoDBStreamsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncDynamoDBStreamsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDynamoDBStreamsClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def describe_stream(
        self,
        stream_arn: "aws_sdk_dynamodb_streams.types.stream_arn.StreamArn",
        *,
        config_overrides: Optional[AsyncDynamoDBStreamsClientConfig] = None,
        limit: Optional[
            "aws_sdk_dynamodb_streams.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        exclusive_start_shard_id: Optional[
            "aws_sdk_dynamodb_streams.types.shard_id.ShardId"
        ] = None,
        shard_filter: Optional[
            "aws_sdk_dynamodb_streams.types.shard_filter.ShardFilter"
        ] = None,
    ) -> "aws_sdk_dynamodb_streams.types.describe_stream_output.DescribeStreamOutput":
        """<p>Returns information about a stream, including the current status of the stream, its Amazon Resource Name (ARN), the composition of its shards, and its corresponding DynamoDB table.</p> <note> <p>You can call <code>DescribeStream</code> at a maximum rate of 10 times per second.</p> </note> <p>Each shard in the stream has a <code>SequenceNumberRange</code> associated with it. If the <code>SequenceNumberRange</code> has a <code>StartingSequenceNumber</code> but no <code>EndingSequenceNumber</code>, then the shard is still open (able to receive more stream records). If both <code>StartingSequenceNumber</code> and <code>EndingSequenceNumber</code> are present, then that shard is closed and can no longer receive more data.</p>

        Args:
            stream_arn: <p>The Amazon Resource Name (ARN) for the stream.</p>
            limit: <p>The maximum number of shard objects to return. The upper limit is 100.</p>
            exclusive_start_shard_id: <p>The shard ID of the first item that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedShardId</code> in the previous operation. </p>
            shard_filter: <p>This optional field contains the filter definition for the <code>DescribeStream</code> API.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dynamodb_streams.types.describe_stream_input.DescribeStreamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dynamodb_streams.types.describe_stream_output.DescribeStreamOutput"
        ]:
            import aws_sdk_dynamodb_streams._operations.dynamo_db_streams_20120810.describe_stream

            (
                output,
                http_response,
            ) = await aws_sdk_dynamodb_streams._operations.dynamo_db_streams_20120810.describe_stream.async_describe_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dynamodb_streams.types.describe_stream_input.DescribeStreamInput = {}  # type: ignore[typeddict-item]
        input_["stream_arn"] = stream_arn
        if limit is not None:
            input_["limit"] = limit
        if exclusive_start_shard_id is not None:
            input_["exclusive_start_shard_id"] = exclusive_start_shard_id
        if shard_filter is not None:
            input_["shard_filter"] = shard_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_records(
        self,
        shard_iterator: "aws_sdk_dynamodb_streams.types.shard_iterator.ShardIterator",
        *,
        config_overrides: Optional[AsyncDynamoDBStreamsClientConfig] = None,
        limit: Optional[
            "aws_sdk_dynamodb_streams.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
    ) -> "aws_sdk_dynamodb_streams.types.get_records_output.GetRecordsOutput":
        """<p>Retrieves the stream records from a given shard.</p> <p>Specify a shard iterator using the <code>ShardIterator</code> parameter. The shard iterator specifies the position in the shard from which you want to start reading stream records sequentially. If there are no stream records available in the portion of the shard that the iterator points to, <code>GetRecords</code> returns an empty list. Note that it might take multiple calls to get to a portion of the shard that contains stream records.</p> <note> <p> <code>GetRecords</code> can retrieve a maximum of 1 MB of data or 1000 stream records, whichever comes first.</p> </note>

        Args:
            shard_iterator: <p>A shard iterator that was retrieved from a previous GetShardIterator operation. This iterator can be used to access the stream records in this shard.</p>
            limit: <p>The maximum number of records to return from the shard. The upper limit is 1000.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dynamodb_streams.types.get_records_input.GetRecordsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dynamodb_streams.types.get_records_output.GetRecordsOutput"
        ]:
            import aws_sdk_dynamodb_streams._operations.dynamo_db_streams_20120810.get_records

            (
                output,
                http_response,
            ) = await aws_sdk_dynamodb_streams._operations.dynamo_db_streams_20120810.get_records.async_get_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dynamodb_streams.types.get_records_input.GetRecordsInput = {}  # type: ignore[typeddict-item]
        input_["shard_iterator"] = shard_iterator
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_shard_iterator(
        self,
        stream_arn: "aws_sdk_dynamodb_streams.types.stream_arn.StreamArn",
        shard_id: "aws_sdk_dynamodb_streams.types.shard_id.ShardId",
        shard_iterator_type: "aws_sdk_dynamodb_streams.types.shard_iterator_type.ShardIteratorType",
        *,
        config_overrides: Optional[AsyncDynamoDBStreamsClientConfig] = None,
        sequence_number: Optional[
            "aws_sdk_dynamodb_streams.types.sequence_number.SequenceNumber"
        ] = None,
    ) -> "aws_sdk_dynamodb_streams.types.get_shard_iterator_output.GetShardIteratorOutput":
        """<p>Returns a shard iterator. A shard iterator provides information about how to retrieve the stream records from within a shard. Use the shard iterator in a subsequent <code>GetRecords</code> request to read the stream records from the shard.</p> <note> <p>A shard iterator expires 15 minutes after it is returned to the requester.</p> </note>

        Args:
            stream_arn: <p>The Amazon Resource Name (ARN) for the stream.</p>
            shard_id: <p>The identifier of the shard. The iterator will be returned for this shard ID.</p>
            shard_iterator_type: <p>Determines how the shard iterator is used to start reading stream records from the shard:</p> <ul> <li> <p> <code>AT_SEQUENCE_NUMBER</code> - Start reading exactly from the position denoted by a specific sequence number.</p> </li> <li> <p> <code>AFTER_SEQUENCE_NUMBER</code> - Start reading right after the position denoted by a specific sequence number.</p> </li> <li> <p> <code>TRIM_HORIZON</code> - Start reading at the last (untrimmed) stream record, which is the oldest record in the shard. In DynamoDB Streams, there is a 24 hour limit on data retention. Stream records whose age exceeds this limit are subject to removal (trimming) from the stream.</p> </li> <li> <p> <code>LATEST</code> - Start reading just after the most recent stream record in the shard, so that you always read the most recent data in the shard.</p> </li> </ul>
            sequence_number: <p>The sequence number of a stream record in the shard from which to start reading.</p>

        Examples:
            To obtain a shard iterator for the provided stream ARN and shard ID
            The following example returns a shard iterator for the provided stream ARN and shard ID.

            >>> await client.get_shard_iterator(stream_arn='arn:aws:dynamodb:us-west-2:111122223333:table/Forum/stream/2015-05-20T20:51:10.252', shard_id='00000001414576573621-f55eea83', shard_iterator_type='TRIM_HORIZON')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dynamodb_streams.types.get_shard_iterator_input.GetShardIteratorInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dynamodb_streams.types.get_shard_iterator_output.GetShardIteratorOutput"
        ]:
            import aws_sdk_dynamodb_streams._operations.dynamo_db_streams_20120810.get_shard_iterator

            (
                output,
                http_response,
            ) = await aws_sdk_dynamodb_streams._operations.dynamo_db_streams_20120810.get_shard_iterator.async_get_shard_iterator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dynamodb_streams.types.get_shard_iterator_input.GetShardIteratorInput = {}  # type: ignore[typeddict-item]
        input_["stream_arn"] = stream_arn
        input_["shard_id"] = shard_id
        input_["shard_iterator_type"] = shard_iterator_type
        if sequence_number is not None:
            input_["sequence_number"] = sequence_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_streams(
        self,
        *,
        config_overrides: Optional[AsyncDynamoDBStreamsClientConfig] = None,
        table_name: Optional[
            "aws_sdk_dynamodb_streams.types.table_name.TableName"
        ] = None,
        limit: Optional[
            "aws_sdk_dynamodb_streams.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        exclusive_start_stream_arn: Optional[
            "aws_sdk_dynamodb_streams.types.stream_arn.StreamArn"
        ] = None,
    ) -> "aws_sdk_dynamodb_streams.types.list_streams_output.ListStreamsOutput":
        """<p>Returns an array of stream ARNs associated with the current account and endpoint. If the <code>TableName</code> parameter is present, then <code>ListStreams</code> will return only the streams ARNs for that table.</p> <note> <p>You can call <code>ListStreams</code> at a maximum rate of 5 times per second.</p> </note>

        Args:
            table_name: <p>If this parameter is provided, then only the streams associated with this table name are returned.</p>
            limit: <p>The maximum number of streams to return. The upper limit is 100.</p>
            exclusive_start_stream_arn: <p>The ARN (Amazon Resource Name) of the first item that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedStreamArn</code> in the previous operation. </p>

        Examples:
            To list all of the stream ARNs
            The following example lists all of the stream ARNs.

            >>> await client.list_streams()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_dynamodb_streams.types.list_streams_input.ListStreamsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_dynamodb_streams.types.list_streams_output.ListStreamsOutput"
        ]:
            import aws_sdk_dynamodb_streams._operations.dynamo_db_streams_20120810.list_streams

            (
                output,
                http_response,
            ) = await aws_sdk_dynamodb_streams._operations.dynamo_db_streams_20120810.list_streams.async_list_streams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dynamodb_streams.types.list_streams_input.ListStreamsInput = {}  # type: ignore[typeddict-item]
        if table_name is not None:
            input_["table_name"] = table_name
        if limit is not None:
            input_["limit"] = limit
        if exclusive_start_stream_arn is not None:
            input_["exclusive_start_stream_arn"] = exclusive_start_stream_arn

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
