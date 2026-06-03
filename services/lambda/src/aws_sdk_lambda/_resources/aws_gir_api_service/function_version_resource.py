from typing import Optional, TYPE_CHECKING
from aws_sdk_lambda._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)
import aws_sdk_lambda._auth._signers
import aws_sdk_lambda._auth._sigv4

if TYPE_CHECKING:
    from aws_sdk_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from aws_sdk_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )
    import aws_sdk_lambda.types.description
    import aws_sdk_lambda.types.function_configuration
    import aws_sdk_lambda.types.function_name
    import aws_sdk_lambda.types.function_version_latest_published
    import aws_sdk_lambda.types.list_versions_by_function_request
    import aws_sdk_lambda.types.list_versions_by_function_response
    import aws_sdk_lambda.types.max_list_items
    import aws_sdk_lambda.types.namespaced_function_name
    import aws_sdk_lambda.types.publish_version_request
    import aws_sdk_lambda.types.string


class FunctionVersionResource:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def create(
        self,
        function_name: "aws_sdk_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        code_sha256: Optional["aws_sdk_lambda.types.string.String"] = None,
        description: Optional["aws_sdk_lambda.types.description.Description"] = None,
        revision_id: Optional["aws_sdk_lambda.types.string.String"] = None,
        publish_to: Optional[
            "aws_sdk_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
    ) -> "aws_sdk_lambda.types.function_configuration.FunctionConfiguration":
        """<p>Creates a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html\">version</a> from the current code and configuration of a function. Use versions to create a snapshot of your function code and configuration that doesn't change.</p> <p>Lambda doesn't publish a version if the function's configuration and code haven't changed since the last version. Use <a>UpdateFunctionCode</a> or <a>UpdateFunctionConfiguration</a> to update the function before publishing a version.</p> <p>Clients can invoke versions directly or with an alias. To create an alias, use <a>CreateAlias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            code_sha256: <p>Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. You can get the hash for the version that you uploaded from the output of <a>UpdateFunctionCode</a>.</p>
            description: <p>A description for the version to override the description in the function configuration.</p>
            revision_id: <p>Only update the function if the revision ID matches the ID that's specified. Use this option to avoid publishing a version if the function configuration has changed since you last updated it.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>

        Examples:
            To publish a version of a Lambda function
            This operation publishes a version of a Lambda function

            >>> client.create(function_name='myFunction', code_sha256='', description='')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.publish_version_request.PublishVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.publish_version

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.publish_version.publish_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_lambda.types.publish_version_request.PublishVersionRequest = {}  # type: ignore[typeddict-item]
        input["function_name"] = function_name
        if code_sha256 is not None:
            input["code_sha256"] = code_sha256
        if description is not None:
            input["description"] = description
        if revision_id is not None:
            input["revision_id"] = revision_id
        if publish_to is not None:
            input["publish_to"] = publish_to

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_versions_by_function(
        self,
        function_name: "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        max_items: Optional["aws_sdk_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "aws_sdk_lambda.types.list_versions_by_function_response.ListVersionsByFunctionResponse":
        """<p>Returns a list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html\">versions</a>, with the version-specific configuration of each. Lambda returns up to 50 versions per call.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of versions to return. Note that <code>ListVersionsByFunction</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Examples:
            To list versions of a function
            The following example returns a list of versions of a function named my-function

            >>> client.list_versions_by_function(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_lambda.types.list_versions_by_function_request.ListVersionsByFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_lambda.types.list_versions_by_function_response.ListVersionsByFunctionResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.list_versions_by_function

            output, http_response = (
                aws_sdk_lambda._operations.aws_gir_api_service.list_versions_by_function.list_versions_by_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_lambda.types.list_versions_by_function_request.ListVersionsByFunctionRequest = {}  # type: ignore[typeddict-item]
        input["function_name"] = function_name
        if marker is not None:
            input["marker"] = marker
        if max_items is not None:
            input["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncFunctionVersionResource:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def create(
        self,
        function_name: "aws_sdk_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        code_sha256: Optional["aws_sdk_lambda.types.string.String"] = None,
        description: Optional["aws_sdk_lambda.types.description.Description"] = None,
        revision_id: Optional["aws_sdk_lambda.types.string.String"] = None,
        publish_to: Optional[
            "aws_sdk_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
    ) -> "aws_sdk_lambda.types.function_configuration.FunctionConfiguration":
        """<p>Creates a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html\">version</a> from the current code and configuration of a function. Use versions to create a snapshot of your function code and configuration that doesn't change.</p> <p>Lambda doesn't publish a version if the function's configuration and code haven't changed since the last version. Use <a>UpdateFunctionCode</a> or <a>UpdateFunctionConfiguration</a> to update the function before publishing a version.</p> <p>Clients can invoke versions directly or with an alias. To create an alias, use <a>CreateAlias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            code_sha256: <p>Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. You can get the hash for the version that you uploaded from the output of <a>UpdateFunctionCode</a>.</p>
            description: <p>A description for the version to override the description in the function configuration.</p>
            revision_id: <p>Only update the function if the revision ID matches the ID that's specified. Use this option to avoid publishing a version if the function configuration has changed since you last updated it.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>

        Examples:
            To publish a version of a Lambda function
            This operation publishes a version of a Lambda function

            >>> await client.create(function_name='myFunction', code_sha256='', description='')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lambda.types.publish_version_request.PublishVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.publish_version

            (
                output,
                http_response,
            ) = await aws_sdk_lambda._operations.aws_gir_api_service.publish_version.async_publish_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_lambda.types.publish_version_request.PublishVersionRequest = {}  # type: ignore[typeddict-item]
        input["function_name"] = function_name
        if code_sha256 is not None:
            input["code_sha256"] = code_sha256
        if description is not None:
            input["description"] = description
        if revision_id is not None:
            input["revision_id"] = revision_id
        if publish_to is not None:
            input["publish_to"] = publish_to

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_versions_by_function(
        self,
        function_name: "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        marker: Optional["aws_sdk_lambda.types.string.String"] = None,
        max_items: Optional["aws_sdk_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "aws_sdk_lambda.types.list_versions_by_function_response.ListVersionsByFunctionResponse":
        """<p>Returns a list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html\">versions</a>, with the version-specific configuration of each. Lambda returns up to 50 versions per call.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of versions to return. Note that <code>ListVersionsByFunction</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Examples:
            To list versions of a function
            The following example returns a list of versions of a function named my-function

            >>> await client.list_versions_by_function(function_name='my-function')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lambda.types.list_versions_by_function_request.ListVersionsByFunctionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lambda.types.list_versions_by_function_response.ListVersionsByFunctionResponse"
        ]:
            import aws_sdk_lambda._operations.aws_gir_api_service.list_versions_by_function

            (
                output,
                http_response,
            ) = await aws_sdk_lambda._operations.aws_gir_api_service.list_versions_by_function.async_list_versions_by_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_lambda.types.list_versions_by_function_request.ListVersionsByFunctionRequest = {}  # type: ignore[typeddict-item]
        input["function_name"] = function_name
        if marker is not None:
            input["marker"] = marker
        if max_items is not None:
            input["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
