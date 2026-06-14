"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#CloudApiService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_cloudcontrol._auth._signers
import aws_sdk_cloudcontrol._auth._sigv4
from aws_sdk_cloudcontrol._auth._identity import Credentials
from aws_sdk_cloudcontrol._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_cloudcontrol._auth._zapros_handler import AuthMiddleware
from aws_sdk_cloudcontrol._pagination import resolve_path as _resolve_path
from aws_sdk_cloudcontrol._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.cancel_resource_request_input
    import aws_sdk_cloudcontrol.types.cancel_resource_request_output
    import aws_sdk_cloudcontrol.types.client_token
    import aws_sdk_cloudcontrol.types.create_resource_input
    import aws_sdk_cloudcontrol.types.create_resource_output
    import aws_sdk_cloudcontrol.types.delete_resource_input
    import aws_sdk_cloudcontrol.types.delete_resource_output
    import aws_sdk_cloudcontrol.types.get_resource_input
    import aws_sdk_cloudcontrol.types.get_resource_output
    import aws_sdk_cloudcontrol.types.get_resource_request_status_input
    import aws_sdk_cloudcontrol.types.get_resource_request_status_output
    import aws_sdk_cloudcontrol.types.handler_next_token
    import aws_sdk_cloudcontrol.types.identifier
    import aws_sdk_cloudcontrol.types.list_resource_requests_input
    import aws_sdk_cloudcontrol.types.list_resource_requests_output
    import aws_sdk_cloudcontrol.types.list_resources_input
    import aws_sdk_cloudcontrol.types.list_resources_output
    import aws_sdk_cloudcontrol.types.max_results
    import aws_sdk_cloudcontrol.types.next_token
    import aws_sdk_cloudcontrol.types.patch_document
    import aws_sdk_cloudcontrol.types.progress_event
    import aws_sdk_cloudcontrol.types.properties
    import aws_sdk_cloudcontrol.types.request_token
    import aws_sdk_cloudcontrol.types.resource_description
    import aws_sdk_cloudcontrol.types.resource_request_status_filter
    import aws_sdk_cloudcontrol.types.role_arn
    import aws_sdk_cloudcontrol.types.type_name
    import aws_sdk_cloudcontrol.types.type_version_id
    import aws_sdk_cloudcontrol.types.update_resource_input
    import aws_sdk_cloudcontrol.types.update_resource_output


class AsyncCloudControlClientConfig(TypedDict, total=False):
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


class AsyncCloudControlClient:
    """A client for the ``CloudControl`` service.

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
        self.config = AsyncCloudControlClientConfig(
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
        self, config_overrides: Optional[AsyncCloudControlClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCloudControlClientConfig = config_overrides or {}
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

    async def cancel_resource_request(
        self,
        request_token: "aws_sdk_cloudcontrol.types.request_token.RequestToken",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
    ) -> "aws_sdk_cloudcontrol.types.cancel_resource_request_output.CancelResourceRequestOutput":
        """<p>Cancels the specified resource operation request. For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-cancel\">Canceling resource operation requests</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>Only resource operations requests with a status of <code>PENDING</code> or <code>IN_PROGRESS</code> can be canceled.</p>

        Args:
            request_token: <p>The <code>RequestToken</code> of the <code>ProgressEvent</code> object returned by the resource operation request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudcontrol.types.cancel_resource_request_input.CancelResourceRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudcontrol.types.cancel_resource_request_output.CancelResourceRequestOutput"
        ]:
            import aws_sdk_cloudcontrol._operations.cloud_api_service.cancel_resource_request

            (
                output,
                http_response,
            ) = await aws_sdk_cloudcontrol._operations.cloud_api_service.cancel_resource_request.async_cancel_resource_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudcontrol.types.cancel_resource_request_input.CancelResourceRequestInput = {}  # type: ignore[typeddict-item]
        input_["request_token"] = request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_resource(
        self,
        type_name: "aws_sdk_cloudcontrol.types.type_name.TypeName",
        desired_state: "aws_sdk_cloudcontrol.types.properties.Properties",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "aws_sdk_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["aws_sdk_cloudcontrol.types.role_arn.RoleArn"] = None,
        client_token: Optional[
            "aws_sdk_cloudcontrol.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_cloudcontrol.types.create_resource_output.CreateResourceOutput":
        """<p>Creates the specified resource. For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-create.html\">Creating a resource</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>After you have initiated a resource creation request, you can monitor the progress of your request by calling <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html\">GetResourceRequestStatus</a> using the <code>RequestToken</code> of the <code>ProgressEvent</code> type returned by <code>CreateResource</code>.</p>

        Args:
            type_name: <p>The name of the resource type.</p>
            type_version_id: <p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers\">handlers</a> </code> section of the <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html\">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions\">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            client_token: <p>A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately distinguish between request retries and new resource requests. You might retry a resource request to ensure that it was successfully received.</p> <p>A client token is valid for 36 hours once used. After that, a resource request with the same client token is treated as a new request.</p> <p>If you do not specify a client token, one is generated for inclusion in the request.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-idempotency\">Ensuring resource operation requests are unique</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            desired_state: <p>Structured data format representing the desired state of the resource, consisting of that resource's properties and their desired values.</p> <note> <p>Cloud Control API currently supports JSON as a structured data format.</p> </note> <p>Specify the desired state as one of the following:</p> <ul> <li> <p>A JSON blob</p> </li> <li> <p>A local path containing the desired state in JSON data format</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-create.html#resource-operations-create-desiredstate\">Composing the desired state of the resource</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>For more information about the properties of a specific resource, refer to the related topic for the resource in the <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html\">Resource and property types reference</a> in the <i>CloudFormation Users Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudcontrol.types.create_resource_input.CreateResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudcontrol.types.create_resource_output.CreateResourceOutput"
        ]:
            import aws_sdk_cloudcontrol._operations.cloud_api_service.create_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cloudcontrol._operations.cloud_api_service.create_resource.async_create_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudcontrol.types.create_resource_input.CreateResourceInput = {}  # type: ignore[typeddict-item]
        input_["type_name"] = type_name
        if type_version_id is not None:
            input_["type_version_id"] = type_version_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["desired_state"] = desired_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource(
        self,
        type_name: "aws_sdk_cloudcontrol.types.type_name.TypeName",
        identifier: "aws_sdk_cloudcontrol.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "aws_sdk_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["aws_sdk_cloudcontrol.types.role_arn.RoleArn"] = None,
        client_token: Optional[
            "aws_sdk_cloudcontrol.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_cloudcontrol.types.delete_resource_output.DeleteResourceOutput":
        """<p>Deletes the specified resource. For details, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-delete.html\">Deleting a resource</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>After you have initiated a resource deletion request, you can monitor the progress of your request by calling <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html\">GetResourceRequestStatus</a> using the <code>RequestToken</code> of the <code>ProgressEvent</code> returned by <code>DeleteResource</code>.</p>

        Args:
            type_name: <p>The name of the resource type.</p>
            type_version_id: <p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers\">handlers</a> </code> section of the <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html\">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions\">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            client_token: <p>A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately distinguish between request retries and new resource requests. You might retry a resource request to ensure that it was successfully received.</p> <p>A client token is valid for 36 hours once used. After that, a resource request with the same client token is treated as a new request.</p> <p>If you do not specify a client token, one is generated for inclusion in the request.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-idempotency\">Ensuring resource operation requests are unique</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            identifier: <p>The identifier for the resource.</p> <p>You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Primary identifiers can be specified as a string or JSON; secondary identifiers must be specified as JSON.</p> <p>For compound primary identifiers (that is, one that consists of multiple resource properties strung together), to specify the primary identifier as a string, list the property values <i>in the order they are specified</i> in the primary identifier definition, separated by <code>|</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html\">Identifying resources</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudcontrol.types.delete_resource_input.DeleteResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudcontrol.types.delete_resource_output.DeleteResourceOutput"
        ]:
            import aws_sdk_cloudcontrol._operations.cloud_api_service.delete_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cloudcontrol._operations.cloud_api_service.delete_resource.async_delete_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudcontrol.types.delete_resource_input.DeleteResourceInput = {}  # type: ignore[typeddict-item]
        input_["type_name"] = type_name
        if type_version_id is not None:
            input_["type_version_id"] = type_version_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource(
        self,
        type_name: "aws_sdk_cloudcontrol.types.type_name.TypeName",
        identifier: "aws_sdk_cloudcontrol.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "aws_sdk_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["aws_sdk_cloudcontrol.types.role_arn.RoleArn"] = None,
    ) -> "aws_sdk_cloudcontrol.types.get_resource_output.GetResourceOutput":
        """<p>Returns information about the current state of the specified resource. For details, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-read.html\">Reading a resource's current state</a>.</p> <p>You can use this action to return information about an existing resource in your account and Amazon Web Services Region, whether those resources were provisioned using Cloud Control API.</p>

        Args:
            type_name: <p>The name of the resource type.</p>
            type_version_id: <p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers\">handlers</a> </code> section of the <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html\">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions\">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            identifier: <p>The identifier for the resource.</p> <p>You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Primary identifiers can be specified as a string or JSON; secondary identifiers must be specified as JSON.</p> <p>For compound primary identifiers (that is, one that consists of multiple resource properties strung together), to specify the primary identifier as a string, list the property values <i>in the order they are specified</i> in the primary identifier definition, separated by <code>|</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html\">Identifying resources</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudcontrol.types.get_resource_input.GetResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudcontrol.types.get_resource_output.GetResourceOutput"
        ]:
            import aws_sdk_cloudcontrol._operations.cloud_api_service.get_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cloudcontrol._operations.cloud_api_service.get_resource.async_get_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudcontrol.types.get_resource_input.GetResourceInput = {}  # type: ignore[typeddict-item]
        input_["type_name"] = type_name
        if type_version_id is not None:
            input_["type_version_id"] = type_version_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_request_status(
        self,
        request_token: "aws_sdk_cloudcontrol.types.request_token.RequestToken",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
    ) -> "aws_sdk_cloudcontrol.types.get_resource_request_status_output.GetResourceRequestStatusOutput":
        """<p>Returns the current status of a resource operation request. For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-track\">Tracking the progress of resource operation requests</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>

        Args:
            request_token: <p>A unique token used to track the progress of the resource operation request.</p> <p>Request tokens are included in the <code>ProgressEvent</code> type returned by a resource operation request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudcontrol.types.get_resource_request_status_input.GetResourceRequestStatusInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudcontrol.types.get_resource_request_status_output.GetResourceRequestStatusOutput"
        ]:
            import aws_sdk_cloudcontrol._operations.cloud_api_service.get_resource_request_status

            (
                output,
                http_response,
            ) = await aws_sdk_cloudcontrol._operations.cloud_api_service.get_resource_request_status.async_get_resource_request_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudcontrol.types.get_resource_request_status_input.GetResourceRequestStatusInput = {}  # type: ignore[typeddict-item]
        input_["request_token"] = request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_resource_requests(
        self,
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        max_results: Optional[
            "aws_sdk_cloudcontrol.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_cloudcontrol.types.next_token.NextToken"] = None,
        resource_request_status_filter: Optional[
            "aws_sdk_cloudcontrol.types.resource_request_status_filter.ResourceRequestStatusFilter"
        ] = None,
    ) -> "aws_sdk_cloudcontrol.types.list_resource_requests_output.ListResourceRequestsOutput":
        """<p>Returns existing resource operation requests. This includes requests of all status types. For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-list\">Listing active resource operation requests</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <note> <p>Resource operation requests expire after 7 days.</p> </note>

        Args:
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p> <p>The default is <code>20</code>.</p>
            next_token: <p>If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.</p>
            resource_request_status_filter: <p>The filter criteria to apply to the requests returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudcontrol.types.list_resource_requests_input.ListResourceRequestsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudcontrol.types.list_resource_requests_output.ListResourceRequestsOutput"
        ]:
            import aws_sdk_cloudcontrol._operations.cloud_api_service.list_resource_requests

            (
                output,
                http_response,
            ) = await aws_sdk_cloudcontrol._operations.cloud_api_service.list_resource_requests.async_list_resource_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudcontrol.types.list_resource_requests_input.ListResourceRequestsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_request_status_filter is not None:
            input_["resource_request_status_filter"] = resource_request_status_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_resource_requests(
        self,
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        max_results: Optional[
            "aws_sdk_cloudcontrol.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_cloudcontrol.types.next_token.NextToken"] = None,
        resource_request_status_filter: Optional[
            "aws_sdk_cloudcontrol.types.resource_request_status_filter.ResourceRequestStatusFilter"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_cloudcontrol.types.progress_event.ProgressEvent]":
        _token = next_token
        while True:
            _response = await self.list_resource_requests(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                resource_request_status_filter=resource_request_status_filter,
            )
            _page = _resolve_path(_response, ("resource_request_status_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resources(
        self,
        type_name: "aws_sdk_cloudcontrol.types.type_name.TypeName",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "aws_sdk_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["aws_sdk_cloudcontrol.types.role_arn.RoleArn"] = None,
        next_token: Optional[
            "aws_sdk_cloudcontrol.types.handler_next_token.HandlerNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_cloudcontrol.types.max_results.MaxResults"
        ] = None,
        resource_model: Optional[
            "aws_sdk_cloudcontrol.types.properties.Properties"
        ] = None,
    ) -> "aws_sdk_cloudcontrol.types.list_resources_output.ListResourcesOutput":
        """<p>Returns information about the specified resources. For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-list.html\">Discovering resources</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>You can use this action to return information about existing resources in your account and Amazon Web Services Region, whether those resources were provisioned using Cloud Control API.</p>

        Args:
            type_name: <p>The name of the resource type.</p>
            type_version_id: <p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers\">handlers</a> </code> section of the <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html\">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions\">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            next_token: <p>If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.</p>
            max_results: <p>Reserved.</p>
            resource_model: <p>The resource model to use to select the resources to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudcontrol.types.list_resources_input.ListResourcesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudcontrol.types.list_resources_output.ListResourcesOutput"
        ]:
            import aws_sdk_cloudcontrol._operations.cloud_api_service.list_resources

            (
                output,
                http_response,
            ) = await aws_sdk_cloudcontrol._operations.cloud_api_service.list_resources.async_list_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudcontrol.types.list_resources_input.ListResourcesInput = {}  # type: ignore[typeddict-item]
        input_["type_name"] = type_name
        if type_version_id is not None:
            input_["type_version_id"] = type_version_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_model is not None:
            input_["resource_model"] = resource_model

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_resources(
        self,
        type_name: "aws_sdk_cloudcontrol.types.type_name.TypeName",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "aws_sdk_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["aws_sdk_cloudcontrol.types.role_arn.RoleArn"] = None,
        next_token: Optional[
            "aws_sdk_cloudcontrol.types.handler_next_token.HandlerNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_cloudcontrol.types.max_results.MaxResults"
        ] = None,
        resource_model: Optional[
            "aws_sdk_cloudcontrol.types.properties.Properties"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_cloudcontrol.types.resource_description.ResourceDescription]":
        _token = next_token
        while True:
            _response = await self.list_resources(
                type_name,
                config_overrides=config_overrides,
                type_version_id=type_version_id,
                role_arn=role_arn,
                next_token=_token,
                max_results=max_results,
                resource_model=resource_model,
            )
            _page = _resolve_path(_response, ("resource_descriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_resource(
        self,
        type_name: "aws_sdk_cloudcontrol.types.type_name.TypeName",
        identifier: "aws_sdk_cloudcontrol.types.identifier.Identifier",
        patch_document: "aws_sdk_cloudcontrol.types.patch_document.PatchDocument",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "aws_sdk_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["aws_sdk_cloudcontrol.types.role_arn.RoleArn"] = None,
        client_token: Optional[
            "aws_sdk_cloudcontrol.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_cloudcontrol.types.update_resource_output.UpdateResourceOutput":
        """<p>Updates the specified property values in the resource.</p> <p>You specify your resource property updates as a list of patch operations contained in a JSON patch document that adheres to the <a href=\"https://datatracker.ietf.org/doc/html/rfc6902\"> <i>RFC 6902 - JavaScript Object Notation (JSON) Patch</i> </a> standard.</p> <p>For details on how Cloud Control API performs resource update operations, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-update.html\">Updating a resource</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>After you have initiated a resource update request, you can monitor the progress of your request by calling <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html\">GetResourceRequestStatus</a> using the <code>RequestToken</code> of the <code>ProgressEvent</code> returned by <code>UpdateResource</code>.</p> <p>For more information about the properties of a specific resource, refer to the related topic for the resource in the <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html\">Resource and property types reference</a> in the <i>CloudFormation Users Guide</i>.</p>

        Args:
            type_name: <p>The name of the resource type.</p>
            type_version_id: <p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers\">handlers</a> </code> section of the <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html\">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions\">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            client_token: <p>A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately distinguish between request retries and new resource requests. You might retry a resource request to ensure that it was successfully received.</p> <p>A client token is valid for 36 hours once used. After that, a resource request with the same client token is treated as a new request.</p> <p>If you do not specify a client token, one is generated for inclusion in the request.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-idempotency\">Ensuring resource operation requests are unique</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            identifier: <p>The identifier for the resource.</p> <p>You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Primary identifiers can be specified as a string or JSON; secondary identifiers must be specified as JSON.</p> <p>For compound primary identifiers (that is, one that consists of multiple resource properties strung together), to specify the primary identifier as a string, list the property values <i>in the order they are specified</i> in the primary identifier definition, separated by <code>|</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html\">Identifying resources</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            patch_document: <p>A JavaScript Object Notation (JSON) document listing the patch operations that represent the updates to apply to the current resource properties. For details, see <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-update.html#resource-operations-update-patch\">Composing the patch document</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudcontrol.types.update_resource_input.UpdateResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudcontrol.types.update_resource_output.UpdateResourceOutput"
        ]:
            import aws_sdk_cloudcontrol._operations.cloud_api_service.update_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cloudcontrol._operations.cloud_api_service.update_resource.async_update_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudcontrol.types.update_resource_input.UpdateResourceInput = {}  # type: ignore[typeddict-item]
        input_["type_name"] = type_name
        if type_version_id is not None:
            input_["type_version_id"] = type_version_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["identifier"] = identifier
        input_["patch_document"] = patch_document

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
