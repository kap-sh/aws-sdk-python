"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesStreams``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

from aws_sdk_keyspacesstreams._auth._identity import Credentials
from aws_sdk_keyspacesstreams._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_keyspacesstreams._auth._zapros_handler import AuthMiddleware
from aws_sdk_keyspacesstreams._pagination import resolve_path as _resolve_path
from aws_sdk_keyspacesstreams._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.get_records_input
    import aws_sdk_keyspacesstreams.types.get_records_output
    import aws_sdk_keyspacesstreams.types.get_shard_iterator_input
    import aws_sdk_keyspacesstreams.types.get_shard_iterator_output
    import aws_sdk_keyspacesstreams.types.get_stream_input
    import aws_sdk_keyspacesstreams.types.get_stream_output
    import aws_sdk_keyspacesstreams.types.keyspace_name
    import aws_sdk_keyspacesstreams.types.list_streams_input
    import aws_sdk_keyspacesstreams.types.list_streams_output
    import aws_sdk_keyspacesstreams.types.sequence_number
    import aws_sdk_keyspacesstreams.types.shard
    import aws_sdk_keyspacesstreams.types.shard_filter
    import aws_sdk_keyspacesstreams.types.shard_id
    import aws_sdk_keyspacesstreams.types.shard_id_token
    import aws_sdk_keyspacesstreams.types.shard_iterator
    import aws_sdk_keyspacesstreams.types.shard_iterator_type
    import aws_sdk_keyspacesstreams.types.stream
    import aws_sdk_keyspacesstreams.types.stream_arn
    import aws_sdk_keyspacesstreams.types.stream_arn_token
    import aws_sdk_keyspacesstreams.types.table_name


class KeyspacesStreamsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class KeyspacesStreamsClient:
    """A client for the ``KeyspacesStreams`` service.

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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = KeyspacesStreamsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[KeyspacesStreamsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: KeyspacesStreamsClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def get_records(
        self,
        shard_iterator: "aws_sdk_keyspacesstreams.types.shard_iterator.ShardIterator",
        *,
        config_overrides: Optional[KeyspacesStreamsClientConfig] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_keyspacesstreams.types.get_records_output.GetRecordsOutput":
        """<p>Retrieves data records from a specified shard in an Amazon Keyspaces data stream. This operation returns a collection of data records from the shard, including the primary key columns and information about modifications made to the captured table data. Each record represents a single data modification in the Amazon Keyspaces table and includes metadata about when the change occurred.</p>

        Args:
            shard_iterator: <p> The unique identifier of the shard iterator. A shard iterator specifies the position in the shard from which you want to start reading data records sequentially. You obtain this value by calling the <code>GetShardIterator </code> operation. Each shard iterator is valid for 15 minutes after creation. </p>
            max_results: <p> The maximum number of records to return in a single <code>GetRecords</code> request. The default value is 100. You can specify a limit between 1 and 1000, but the actual number returned might be less than the specified maximum if the size of the data for the returned records exceeds the internal size limit. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_keyspacesstreams.types.get_records_input.GetRecordsInput]",
        ) -> OperationResponse[
            "aws_sdk_keyspacesstreams.types.get_records_output.GetRecordsOutput"
        ]:
            import aws_sdk_keyspacesstreams._operations.keyspaces_streams.get_records

            output, http_response = (
                aws_sdk_keyspacesstreams._operations.keyspaces_streams.get_records.get_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_keyspacesstreams.types.get_records_input.GetRecordsInput = {}  # type: ignore[typeddict-item]
        input["shard_iterator"] = shard_iterator
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_shard_iterator(
        self,
        stream_arn: "aws_sdk_keyspacesstreams.types.stream_arn.StreamArn",
        shard_id: "aws_sdk_keyspacesstreams.types.shard_id.ShardId",
        shard_iterator_type: "aws_sdk_keyspacesstreams.types.shard_iterator_type.ShardIteratorType",
        *,
        config_overrides: Optional[KeyspacesStreamsClientConfig] = None,
        sequence_number: Optional[
            "aws_sdk_keyspacesstreams.types.sequence_number.SequenceNumber"
        ] = None,
    ) -> "aws_sdk_keyspacesstreams.types.get_shard_iterator_output.GetShardIteratorOutput":
        """<p>Returns a shard iterator that serves as a bookmark for reading data from a specific position in an Amazon Keyspaces data stream's shard. The shard iterator specifies the shard position from which to start reading data records sequentially. You can specify whether to begin reading at the latest record, the oldest record, or at a particular sequence number within the shard.</p>

        Args:
            stream_arn: <p> The Amazon Resource Name (ARN) of the stream for which to get the shard iterator. The ARN uniquely identifies the stream within Amazon Keyspaces. </p>
            shard_id: <p> The identifier of the shard within the stream. The shard ID uniquely identifies a subset of the stream's data records that you want to access. </p>
            shard_iterator_type: <p> Determines how the shard iterator is positioned. Must be one of the following: </p> <ul> <li> <p> <code>TRIM_HORIZON</code> - Start reading at the last untrimmed record in the shard, which is the oldest data record in the shard.</p> </li> <li> <p> <code>AT_SEQUENCE_NUMBER</code> - Start reading exactly from the specified sequence number.</p> </li> <li> <p> <code>AFTER_SEQUENCE_NUMBER</code> - Start reading right after the specified sequence number. </p> </li> <li> <p> <code>LATEST</code> - Start reading just after the most recent record in the shard, so that you always read the most recent data. </p> </li> </ul>
            sequence_number: <p> The sequence number of the data record in the shard from which to start reading. Required if <code>ShardIteratorType</code> is <code>AT_SEQUENCE_NUMBER</code> or <code>AFTER_SEQUENCE_NUMBER</code>. This parameter is ignored for other iterator types. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_keyspacesstreams.types.get_shard_iterator_input.GetShardIteratorInput]",
        ) -> OperationResponse[
            "aws_sdk_keyspacesstreams.types.get_shard_iterator_output.GetShardIteratorOutput"
        ]:
            import aws_sdk_keyspacesstreams._operations.keyspaces_streams.get_shard_iterator

            output, http_response = (
                aws_sdk_keyspacesstreams._operations.keyspaces_streams.get_shard_iterator.get_shard_iterator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_keyspacesstreams.types.get_shard_iterator_input.GetShardIteratorInput = {}  # type: ignore[typeddict-item]
        input["stream_arn"] = stream_arn
        input["shard_id"] = shard_id
        input["shard_iterator_type"] = shard_iterator_type
        if sequence_number is not None:
            input["sequence_number"] = sequence_number

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_stream(
        self,
        stream_arn: "aws_sdk_keyspacesstreams.types.stream_arn.StreamArn",
        *,
        config_overrides: Optional[KeyspacesStreamsClientConfig] = None,
        max_results: Optional[int] = None,
        shard_filter: Optional[
            "aws_sdk_keyspacesstreams.types.shard_filter.ShardFilter"
        ] = None,
        next_token: Optional[
            "aws_sdk_keyspacesstreams.types.shard_id_token.ShardIdToken"
        ] = None,
    ) -> "aws_sdk_keyspacesstreams.types.get_stream_output.GetStreamOutput":
        """<p>Returns detailed information about a specific data capture stream for an Amazon Keyspaces table. The information includes the stream's Amazon Resource Name (ARN), creation time, current status, retention period, shard composition, and associated table details. This operation helps you monitor and manage the configuration of your Amazon Keyspaces data streams.</p>

        Args:
            stream_arn: <p> The Amazon Resource Name (ARN) of the stream for which detailed information is requested. This uniquely identifies the specific stream you want to get information about. </p>
            max_results: <p> The maximum number of shard objects to return in a single <code>GetStream</code> request. The default value is 100. The minimum value is 1 and the maximum value is 100. </p>
            shard_filter: <p> Optional filter criteria to apply when retrieving shards. You can filter shards based on their parent <code>shardID</code> to get a list of children shards to narrow down the results returned by the <code>GetStream</code> operation. </p>
            next_token: <p> An optional pagination token provided by a previous <code>GetStream</code> operation. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_keyspacesstreams.types.get_stream_input.GetStreamInput]",
        ) -> OperationResponse[
            "aws_sdk_keyspacesstreams.types.get_stream_output.GetStreamOutput"
        ]:
            import aws_sdk_keyspacesstreams._operations.keyspaces_streams.get_stream

            output, http_response = (
                aws_sdk_keyspacesstreams._operations.keyspaces_streams.get_stream.get_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_keyspacesstreams.types.get_stream_input.GetStreamInput = {}  # type: ignore[typeddict-item]
        input["stream_arn"] = stream_arn
        if max_results is not None:
            input["max_results"] = max_results
        if shard_filter is not None:
            input["shard_filter"] = shard_filter
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_stream(
        self,
        stream_arn: "aws_sdk_keyspacesstreams.types.stream_arn.StreamArn",
        *,
        config_overrides: Optional[KeyspacesStreamsClientConfig] = None,
        max_results: Optional[int] = None,
        shard_filter: Optional[
            "aws_sdk_keyspacesstreams.types.shard_filter.ShardFilter"
        ] = None,
        next_token: Optional[
            "aws_sdk_keyspacesstreams.types.shard_id_token.ShardIdToken"
        ] = None,
    ) -> "Iterator[aws_sdk_keyspacesstreams.types.shard.Shard]":
        _token = next_token
        while True:
            _response = self.get_stream(
                stream_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                shard_filter=shard_filter,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("shards",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_streams(
        self,
        *,
        config_overrides: Optional[KeyspacesStreamsClientConfig] = None,
        keyspace_name: Optional[
            "aws_sdk_keyspacesstreams.types.keyspace_name.KeyspaceName"
        ] = None,
        table_name: Optional[
            "aws_sdk_keyspacesstreams.types.table_name.TableName"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_keyspacesstreams.types.stream_arn_token.StreamArnToken"
        ] = None,
    ) -> "aws_sdk_keyspacesstreams.types.list_streams_output.ListStreamsOutput":
        """<p>Returns a list of all data capture streams associated with your Amazon Keyspaces account or for a specific keyspace or table. The response includes information such as stream ARNs, table associations, creation timestamps, and current status. This operation helps you discover and manage all active data streams in your Amazon Keyspaces environment.</p>

        Args:
            keyspace_name: <p> The name of the keyspace for which to list streams. If specified, only streams associated with tables in this keyspace are returned. If omitted, streams from all keyspaces are included in the results. </p>
            table_name: <p> The name of the table for which to list streams. Must be used together with <code>keyspaceName</code>. If specified, only streams associated with this specific table are returned. </p>
            max_results: <p> The maximum number of streams to return in a single <code>ListStreams</code> request. The default value is 100. The minimum value is 1 and the maximum value is 100. </p>
            next_token: <p> An optional pagination token provided by a previous <code>ListStreams</code> operation. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>maxResults</code>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_keyspacesstreams.types.list_streams_input.ListStreamsInput]",
        ) -> OperationResponse[
            "aws_sdk_keyspacesstreams.types.list_streams_output.ListStreamsOutput"
        ]:
            import aws_sdk_keyspacesstreams._operations.keyspaces_streams.list_streams

            output, http_response = (
                aws_sdk_keyspacesstreams._operations.keyspaces_streams.list_streams.list_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_keyspacesstreams.types.list_streams_input.ListStreamsInput = {}  # type: ignore[typeddict-item]
        if keyspace_name is not None:
            input["keyspace_name"] = keyspace_name
        if table_name is not None:
            input["table_name"] = table_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_streams(
        self,
        *,
        config_overrides: Optional[KeyspacesStreamsClientConfig] = None,
        keyspace_name: Optional[
            "aws_sdk_keyspacesstreams.types.keyspace_name.KeyspaceName"
        ] = None,
        table_name: Optional[
            "aws_sdk_keyspacesstreams.types.table_name.TableName"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_keyspacesstreams.types.stream_arn_token.StreamArnToken"
        ] = None,
    ) -> "Iterator[aws_sdk_keyspacesstreams.types.stream.Stream]":
        _token = next_token
        while True:
            _response = self.list_streams(
                config_overrides=config_overrides,
                keyspace_name=keyspace_name,
                table_name=table_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("streams",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
