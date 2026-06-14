"""Generated from Smithy shape ``com.amazonaws.mediastoredata#MediaStoreObject_20170901``."""

import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_mediastore_data._auth._signers
import aws_sdk_mediastore_data._auth._sigv4
from aws_sdk_mediastore_data._auth._identity import Credentials
from aws_sdk_mediastore_data._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_mediastore_data._auth._zapros_handler import AuthMiddleware
from aws_sdk_mediastore_data._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_mediastore_data.types.content_type
    import aws_sdk_mediastore_data.types.delete_object_request
    import aws_sdk_mediastore_data.types.delete_object_response
    import aws_sdk_mediastore_data.types.describe_object_request
    import aws_sdk_mediastore_data.types.describe_object_response
    import aws_sdk_mediastore_data.types.get_object_request
    import aws_sdk_mediastore_data.types.get_object_response
    import aws_sdk_mediastore_data.types.list_items_request
    import aws_sdk_mediastore_data.types.list_items_response
    import aws_sdk_mediastore_data.types.list_limit
    import aws_sdk_mediastore_data.types.list_path_naming
    import aws_sdk_mediastore_data.types.pagination_token
    import aws_sdk_mediastore_data.types.path_naming
    import aws_sdk_mediastore_data.types.payload_blob
    import aws_sdk_mediastore_data.types.put_object_request
    import aws_sdk_mediastore_data.types.put_object_response
    import aws_sdk_mediastore_data.types.range_pattern
    import aws_sdk_mediastore_data.types.storage_class
    import aws_sdk_mediastore_data.types.string_primitive
    import aws_sdk_mediastore_data.types.upload_availability


class AsyncMediaStoreDataClientConfig(TypedDict, total=False):
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


class AsyncMediaStoreDataClient:
    """A client for the ``MediaStoreData`` service.

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
        self.config = AsyncMediaStoreDataClientConfig(
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
        self, config_overrides: Optional[AsyncMediaStoreDataClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMediaStoreDataClientConfig = config_overrides or {}
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

    async def delete_object(
        self,
        path: "aws_sdk_mediastore_data.types.path_naming.PathNaming",
        *,
        config_overrides: Optional[AsyncMediaStoreDataClientConfig] = None,
    ) -> "aws_sdk_mediastore_data.types.delete_object_response.DeleteObjectResponse":
        """<p>Deletes an object at the specified path.</p>

        Args:
            path: <p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore_data.types.delete_object_request.DeleteObjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore_data.types.delete_object_response.DeleteObjectResponse"
        ]:
            import aws_sdk_mediastore_data._operations.media_store_object_20170901.delete_object

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore_data._operations.media_store_object_20170901.delete_object.async_delete_object(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediastore_data.types.delete_object_request.DeleteObjectRequest = {}  # type: ignore[typeddict-item]
        input_["path"] = path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_object(
        self,
        path: "aws_sdk_mediastore_data.types.path_naming.PathNaming",
        *,
        config_overrides: Optional[AsyncMediaStoreDataClientConfig] = None,
    ) -> (
        "aws_sdk_mediastore_data.types.describe_object_response.DescribeObjectResponse"
    ):
        """<p>Gets the headers for an object at the specified path.</p>

        Args:
            path: <p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore_data.types.describe_object_request.DescribeObjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore_data.types.describe_object_response.DescribeObjectResponse"
        ]:
            import aws_sdk_mediastore_data._operations.media_store_object_20170901.describe_object

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore_data._operations.media_store_object_20170901.describe_object.async_describe_object(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediastore_data.types.describe_object_request.DescribeObjectRequest = {}  # type: ignore[typeddict-item]
        input_["path"] = path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    @asynccontextmanager
    async def get_object(
        self,
        path: "aws_sdk_mediastore_data.types.path_naming.PathNaming",
        *,
        config_overrides: Optional[AsyncMediaStoreDataClientConfig] = None,
        range: Optional[
            "aws_sdk_mediastore_data.types.range_pattern.RangePattern"
        ] = None,
    ) -> "AsyncGenerator[aws_sdk_mediastore_data.types.get_object_response.GetObjectResponse]":
        """<p>Downloads the object at the specified path. If the object’s upload availability is set to <code>streaming</code>, AWS Elemental MediaStore downloads the object even if it’s still uploading the object.</p>

        Args:
            path: <p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p> <p>For example, to upload the file <code>mlaw.avi</code> to the folder path <code>premium\canada</code> in the container <code>movies</code>, enter the path <code>premium/canada/mlaw.avi</code>.</p> <p>Do not include the container name in this path.</p> <p>If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing <code>premium/usa</code> subfolder. If you specify <code>premium/canada</code>, the service creates a <code>canada</code> subfolder in the <code>premium</code> folder. You then have two subfolders, <code>usa</code> and <code>canada</code>, in the <code>premium</code> folder. </p> <p>There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.</p> <p>For more information about folders and how they exist in a container, see the <a href=\"http://docs.aws.amazon.com/mediastore/latest/ug/\">AWS Elemental MediaStore User Guide</a>.</p> <p>The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. </p>
            range: <p>The range bytes of an object to retrieve. For more information about the <code>Range</code> header, see <a href=\"http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35\">http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35</a>. AWS Elemental MediaStore ignores this header for partially uploaded objects that have streaming upload availability.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore_data.types.get_object_request.GetObjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore_data.types.get_object_response.GetObjectResponse"
        ]:
            import aws_sdk_mediastore_data._operations.media_store_object_20170901.get_object

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore_data._operations.media_store_object_20170901.get_object.async_get_object(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediastore_data.types.get_object_request.GetObjectRequest = {}  # type: ignore[typeddict-item]
        input_["path"] = path
        if range is not None:
            input_["range"] = range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    async def list_items(
        self,
        *,
        config_overrides: Optional[AsyncMediaStoreDataClientConfig] = None,
        path: Optional[
            "aws_sdk_mediastore_data.types.list_path_naming.ListPathNaming"
        ] = None,
        max_results: Optional[
            "aws_sdk_mediastore_data.types.list_limit.ListLimit"
        ] = None,
        next_token: Optional[
            "aws_sdk_mediastore_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mediastore_data.types.list_items_response.ListItemsResponse":
        """<p>Provides a list of metadata entries about folders and objects in the specified folder.</p>

        Args:
            path: <p>The path in the container from which to retrieve items. Format: <folder name>/<folder name>/<file name></p>
            max_results: <p>The maximum number of results to return per API request. For example, you submit a <code>ListItems</code> request with <code>MaxResults</code> set at 500. Although 2,000 items match your request, the service returns no more than the first 500 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) The service might return fewer results than the <code>MaxResults</code> value.</p> <p>If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 1,000 results per page.</p>
            next_token: <p>The token that identifies which batch of results that you want to see. For example, you submit a <code>ListItems</code> request with <code>MaxResults</code> set at 500. The service returns the first batch of results (up to 500) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListItems</code> request a second time and specify the <code>NextToken</code> value.</p> <p>Tokens expire after 15 minutes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore_data.types.list_items_request.ListItemsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore_data.types.list_items_response.ListItemsResponse"
        ]:
            import aws_sdk_mediastore_data._operations.media_store_object_20170901.list_items

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore_data._operations.media_store_object_20170901.list_items.async_list_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediastore_data.types.list_items_request.ListItemsRequest = {}  # type: ignore[typeddict-item]
        if path is not None:
            input_["path"] = path
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

    async def put_object(
        self,
        body: AsyncIterator[bytes] | bytes,
        path: "aws_sdk_mediastore_data.types.path_naming.PathNaming",
        *,
        config_overrides: Optional[AsyncMediaStoreDataClientConfig] = None,
        content_type: Optional[
            "aws_sdk_mediastore_data.types.content_type.ContentType"
        ] = None,
        cache_control: Optional[
            "aws_sdk_mediastore_data.types.string_primitive.StringPrimitive"
        ] = None,
        storage_class: Optional[
            "aws_sdk_mediastore_data.types.storage_class.StorageClass"
        ] = None,
        upload_availability: Optional[
            "aws_sdk_mediastore_data.types.upload_availability.UploadAvailability"
        ] = None,
    ) -> "aws_sdk_mediastore_data.types.put_object_response.PutObjectResponse":
        """<p>Uploads an object to the specified path. Object sizes are limited to 25 MB for standard upload availability and 10 MB for streaming upload availability.</p>

        Args:
            body: <p>The bytes to be stored. </p>
            path: <p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p> <p>For example, to upload the file <code>mlaw.avi</code> to the folder path <code>premium\canada</code> in the container <code>movies</code>, enter the path <code>premium/canada/mlaw.avi</code>.</p> <p>Do not include the container name in this path.</p> <p>If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing <code>premium/usa</code> subfolder. If you specify <code>premium/canada</code>, the service creates a <code>canada</code> subfolder in the <code>premium</code> folder. You then have two subfolders, <code>usa</code> and <code>canada</code>, in the <code>premium</code> folder. </p> <p>There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.</p> <p>For more information about folders and how they exist in a container, see the <a href=\"http://docs.aws.amazon.com/mediastore/latest/ug/\">AWS Elemental MediaStore User Guide</a>.</p> <p>The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. </p>
            content_type: <p>The content type of the object.</p>
            cache_control: <p>An optional <code>CacheControl</code> header that allows the caller to control the object's cache behavior. Headers can be passed in as specified in the HTTP at <a href=\"https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9\">https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9</a>.</p> <p>Headers with a custom user-defined value are also accepted.</p>
            storage_class: <p>Indicates the storage class of a <code>Put</code> request. Defaults to high-performance temporal storage class, and objects are persisted into durable storage shortly after being received.</p>
            upload_availability: <p>Indicates the availability of an object while it is still uploading. If the value is set to <code>streaming</code>, the object is available for downloading after some initial buffering but before the object is uploaded completely. If the value is set to <code>standard</code>, the object is available for downloading only when it is uploaded completely. The default value for this header is <code>standard</code>.</p> <p>To use this header, you must also set the HTTP <code>Transfer-Encoding</code> header to <code>chunked</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore_data.types.put_object_request.PutObjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore_data.types.put_object_response.PutObjectResponse"
        ]:
            import aws_sdk_mediastore_data._operations.media_store_object_20170901.put_object

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore_data._operations.media_store_object_20170901.put_object.async_put_object(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediastore_data.types.put_object_request.PutObjectRequest = {}  # type: ignore[typeddict-item]
        input_["body"] = ensure_async_iterator(body)  # type: ignore
        input_["path"] = path
        if content_type is not None:
            input_["content_type"] = content_type
        if cache_control is not None:
            input_["cache_control"] = cache_control
        if storage_class is not None:
            input_["storage_class"] = storage_class
        if upload_availability is not None:
            input_["upload_availability"] = upload_availability

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
