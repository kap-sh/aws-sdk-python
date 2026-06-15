from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_pipes._auth._signers
import aws_sdk_pipes._auth._sigv4
from aws_sdk_pipes._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_pipes.types.arn
    import aws_sdk_pipes.types.arn_or_url
    import aws_sdk_pipes.types.create_pipe_request
    import aws_sdk_pipes.types.create_pipe_response
    import aws_sdk_pipes.types.delete_pipe_request
    import aws_sdk_pipes.types.delete_pipe_response
    import aws_sdk_pipes.types.describe_pipe_request
    import aws_sdk_pipes.types.describe_pipe_response
    import aws_sdk_pipes.types.kms_key_identifier
    import aws_sdk_pipes.types.limit_max100
    import aws_sdk_pipes.types.list_pipes_request
    import aws_sdk_pipes.types.list_pipes_response
    import aws_sdk_pipes.types.next_token
    import aws_sdk_pipes.types.optional_arn
    import aws_sdk_pipes.types.pipe
    import aws_sdk_pipes.types.pipe_description
    import aws_sdk_pipes.types.pipe_enrichment_parameters
    import aws_sdk_pipes.types.pipe_log_configuration_parameters
    import aws_sdk_pipes.types.pipe_name
    import aws_sdk_pipes.types.pipe_source_parameters
    import aws_sdk_pipes.types.pipe_state
    import aws_sdk_pipes.types.pipe_target_parameters
    import aws_sdk_pipes.types.requested_pipe_state
    import aws_sdk_pipes.types.resource_arn
    import aws_sdk_pipes.types.role_arn
    import aws_sdk_pipes.types.start_pipe_request
    import aws_sdk_pipes.types.start_pipe_response
    import aws_sdk_pipes.types.stop_pipe_request
    import aws_sdk_pipes.types.stop_pipe_response
    import aws_sdk_pipes.types.tag_map
    import aws_sdk_pipes.types.update_pipe_request
    import aws_sdk_pipes.types.update_pipe_response
    import aws_sdk_pipes.types.update_pipe_source_parameters
    from aws_sdk_pipes._services.async_pipes import (
        AsyncPipesClient,
        AsyncPipesClientConfig,
    )
    from aws_sdk_pipes._services.pipes import PipesClient, PipesClientConfig


class PipeResource:
    def __init__(self, service: PipesClient) -> None:
        self._service = service

    def put(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        source: "aws_sdk_pipes.types.arn_or_url.ArnOrUrl",
        target: "aws_sdk_pipes.types.arn.Arn",
        role_arn: "aws_sdk_pipes.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
        description: Optional[
            "aws_sdk_pipes.types.pipe_description.PipeDescription"
        ] = None,
        desired_state: Optional[
            "aws_sdk_pipes.types.requested_pipe_state.RequestedPipeState"
        ] = None,
        source_parameters: Optional[
            "aws_sdk_pipes.types.pipe_source_parameters.PipeSourceParameters"
        ] = None,
        enrichment: Optional["aws_sdk_pipes.types.optional_arn.OptionalArn"] = None,
        enrichment_parameters: Optional[
            "aws_sdk_pipes.types.pipe_enrichment_parameters.PipeEnrichmentParameters"
        ] = None,
        target_parameters: Optional[
            "aws_sdk_pipes.types.pipe_target_parameters.PipeTargetParameters"
        ] = None,
        tags: Optional["aws_sdk_pipes.types.tag_map.TagMap"] = None,
        log_configuration: Optional[
            "aws_sdk_pipes.types.pipe_log_configuration_parameters.PipeLogConfigurationParameters"
        ] = None,
        kms_key_identifier: Optional[
            "aws_sdk_pipes.types.kms_key_identifier.KmsKeyIdentifier"
        ] = None,
    ) -> "aws_sdk_pipes.types.create_pipe_response.CreatePipeResponse":
        r"""<p>Create a pipe. Amazon EventBridge Pipes connect event sources to targets and reduces the need for specialized knowledge and integration code.</p>

        Args:
            name: <p>The name of the pipe.</p>
            description: <p>A description of the pipe.</p>
            desired_state: <p>The state the pipe should be in.</p>
            source: <p>The ARN of the source resource.</p>
            source_parameters: <p>The parameters required to set up a source for your pipe.</p>
            enrichment: <p>The ARN of the enrichment resource.</p>
            enrichment_parameters: <p>The parameters required to set up enrichment on your pipe.</p>
            target: <p>The ARN of the target resource.</p>
            target_parameters: <p>The parameters required to set up a target for your pipe.</p> <p>For more information about pipe target parameters, including how to use dynamic path parameters, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html\">Target parameters</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            role_arn: <p>The ARN of the role that allows the pipe to send data to the target.</p>
            tags: <p>The list of key-value pairs to associate with the pipe.</p>
            log_configuration: <p>The logging configuration settings for the pipe.</p>
            kms_key_identifier: <p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>If you do not specify a customer managed key identifier, EventBridge uses an Amazon Web Services owned key to encrypt pipe data.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html\">Managing keys</a> in the <i>Key Management Service Developer Guide</i>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pipes.types.create_pipe_request.CreatePipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_pipes.types.create_pipe_response.CreatePipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.create_pipe

            output, http_response = (
                aws_sdk_pipes._operations.pipes.create_pipe.create_pipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.create_pipe_request.CreatePipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if desired_state is not None:
            input_["desired_state"] = desired_state
        input_["source"] = source
        if source_parameters is not None:
            input_["source_parameters"] = source_parameters
        if enrichment is not None:
            input_["enrichment"] = enrichment
        if enrichment_parameters is not None:
            input_["enrichment_parameters"] = enrichment_parameters
        input_["target"] = target
        if target_parameters is not None:
            input_["target_parameters"] = target_parameters
        input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.describe_pipe_response.DescribePipeResponse":
        r"""<p>Get the information about an existing pipe. For more information about pipes, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html\">Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name: <p>The name of the pipe.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pipes.types.describe_pipe_request.DescribePipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_pipes.types.describe_pipe_response.DescribePipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.describe_pipe

            output, http_response = (
                aws_sdk_pipes._operations.pipes.describe_pipe.describe_pipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.describe_pipe_request.DescribePipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        role_arn: "aws_sdk_pipes.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
        description: Optional[
            "aws_sdk_pipes.types.pipe_description.PipeDescription"
        ] = None,
        desired_state: Optional[
            "aws_sdk_pipes.types.requested_pipe_state.RequestedPipeState"
        ] = None,
        source_parameters: Optional[
            "aws_sdk_pipes.types.update_pipe_source_parameters.UpdatePipeSourceParameters"
        ] = None,
        enrichment: Optional["aws_sdk_pipes.types.optional_arn.OptionalArn"] = None,
        enrichment_parameters: Optional[
            "aws_sdk_pipes.types.pipe_enrichment_parameters.PipeEnrichmentParameters"
        ] = None,
        target: Optional["aws_sdk_pipes.types.arn.Arn"] = None,
        target_parameters: Optional[
            "aws_sdk_pipes.types.pipe_target_parameters.PipeTargetParameters"
        ] = None,
        log_configuration: Optional[
            "aws_sdk_pipes.types.pipe_log_configuration_parameters.PipeLogConfigurationParameters"
        ] = None,
        kms_key_identifier: Optional[
            "aws_sdk_pipes.types.kms_key_identifier.KmsKeyIdentifier"
        ] = None,
    ) -> "aws_sdk_pipes.types.update_pipe_response.UpdatePipeResponse":
        r"""<p>Update an existing pipe. When you call <code>UpdatePipe</code>, EventBridge only the updates fields you have specified in the request; the rest remain unchanged. The exception to this is if you modify any Amazon Web Services-service specific fields in the <code>SourceParameters</code>, <code>EnrichmentParameters</code>, or <code>TargetParameters</code> objects. For example, <code>DynamoDBStreamParameters</code> or <code>EventBridgeEventBusParameters</code>. EventBridge updates the fields in these objects atomically as one and overrides existing values. This is by design, and means that if you don't specify an optional field in one of these <code>Parameters</code> objects, EventBridge sets that field to its system-default value during the update.</p> <p>For more information about pipes, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html\"> Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name: <p>The name of the pipe.</p>
            description: <p>A description of the pipe.</p>
            desired_state: <p>The state the pipe should be in.</p>
            source_parameters: <p>The parameters required to set up a source for your pipe.</p>
            enrichment: <p>The ARN of the enrichment resource.</p>
            enrichment_parameters: <p>The parameters required to set up enrichment on your pipe.</p>
            target: <p>The ARN of the target resource.</p>
            target_parameters: <p>The parameters required to set up a target for your pipe.</p> <p>For more information about pipe target parameters, including how to use dynamic path parameters, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html\">Target parameters</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            role_arn: <p>The ARN of the role that allows the pipe to send data to the target.</p>
            log_configuration: <p>The logging configuration settings for the pipe.</p>
            kms_key_identifier: <p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>To update a pipe that is using the default Amazon Web Services owned key to use a customer managed key instead, or update a pipe that is using a customer managed key to use a different customer managed key, specify a customer managed key identifier.</p> <p>To update a pipe that is using a customer managed key to use the default Amazon Web Services owned key, specify an empty string.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html\">Managing keys</a> in the <i>Key Management Service Developer Guide</i>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pipes.types.update_pipe_request.UpdatePipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_pipes.types.update_pipe_response.UpdatePipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.update_pipe

            output, http_response = (
                aws_sdk_pipes._operations.pipes.update_pipe.update_pipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.update_pipe_request.UpdatePipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if desired_state is not None:
            input_["desired_state"] = desired_state
        if source_parameters is not None:
            input_["source_parameters"] = source_parameters
        if enrichment is not None:
            input_["enrichment"] = enrichment
        if enrichment_parameters is not None:
            input_["enrichment_parameters"] = enrichment_parameters
        if target is not None:
            input_["target"] = target
        if target_parameters is not None:
            input_["target_parameters"] = target_parameters
        input_["role_arn"] = role_arn
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.delete_pipe_response.DeletePipeResponse":
        r"""<p>Delete an existing pipe. For more information about pipes, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html\">Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name: <p>The name of the pipe.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pipes.types.delete_pipe_request.DeletePipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_pipes.types.delete_pipe_response.DeletePipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.delete_pipe

            output, http_response = (
                aws_sdk_pipes._operations.pipes.delete_pipe.delete_pipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.delete_pipe_request.DeletePipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[PipesClientConfig] = None,
        name_prefix: Optional["aws_sdk_pipes.types.pipe_name.PipeName"] = None,
        desired_state: Optional[
            "aws_sdk_pipes.types.requested_pipe_state.RequestedPipeState"
        ] = None,
        current_state: Optional["aws_sdk_pipes.types.pipe_state.PipeState"] = None,
        source_prefix: Optional["aws_sdk_pipes.types.resource_arn.ResourceArn"] = None,
        target_prefix: Optional["aws_sdk_pipes.types.resource_arn.ResourceArn"] = None,
        next_token: Optional["aws_sdk_pipes.types.next_token.NextToken"] = None,
        limit: Optional["aws_sdk_pipes.types.limit_max100.LimitMax100"] = None,
    ) -> "aws_sdk_pipes.types.list_pipes_response.ListPipesResponse":
        r"""<p>Get the pipes associated with this account. For more information about pipes, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html\">Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name_prefix: <p>A value that will return a subset of the pipes associated with this account. For example, <code>\"NamePrefix\": \"ABC\"</code> will return all endpoints with \"ABC\" in the name.</p>
            desired_state: <p>The state the pipe should be in.</p>
            current_state: <p>The state the pipe is in.</p>
            source_prefix: <p>The prefix matching the pipe source.</p>
            target_prefix: <p>The prefix matching the pipe target.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>
            limit: <p>The maximum number of pipes to include in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pipes.types.list_pipes_request.ListPipesRequest]",
        ) -> OperationResponse[
            "aws_sdk_pipes.types.list_pipes_response.ListPipesResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.list_pipes

            output, http_response = (
                aws_sdk_pipes._operations.pipes.list_pipes.list_pipes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.list_pipes_request.ListPipesRequest = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if desired_state is not None:
            input_["desired_state"] = desired_state
        if current_state is not None:
            input_["current_state"] = current_state
        if source_prefix is not None:
            input_["source_prefix"] = source_prefix
        if target_prefix is not None:
            input_["target_prefix"] = target_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_pipe(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.start_pipe_response.StartPipeResponse":
        """<p>Start an existing pipe.</p>

        Args:
            name: <p>The name of the pipe.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pipes.types.start_pipe_request.StartPipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_pipes.types.start_pipe_response.StartPipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.start_pipe

            output, http_response = (
                aws_sdk_pipes._operations.pipes.start_pipe.start_pipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.start_pipe_request.StartPipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_pipe(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.stop_pipe_response.StopPipeResponse":
        """<p>Stop an existing pipe.</p>

        Args:
            name: <p>The name of the pipe.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pipes.types.stop_pipe_request.StopPipeRequest]",
        ) -> OperationResponse[
            "aws_sdk_pipes.types.stop_pipe_response.StopPipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.stop_pipe

            output, http_response = aws_sdk_pipes._operations.pipes.stop_pipe.stop_pipe(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.stop_pipe_request.StopPipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncPipeResource:
    def __init__(self, service: AsyncPipesClient) -> None:
        self._service = service

    async def put(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        source: "aws_sdk_pipes.types.arn_or_url.ArnOrUrl",
        target: "aws_sdk_pipes.types.arn.Arn",
        role_arn: "aws_sdk_pipes.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
        description: Optional[
            "aws_sdk_pipes.types.pipe_description.PipeDescription"
        ] = None,
        desired_state: Optional[
            "aws_sdk_pipes.types.requested_pipe_state.RequestedPipeState"
        ] = None,
        source_parameters: Optional[
            "aws_sdk_pipes.types.pipe_source_parameters.PipeSourceParameters"
        ] = None,
        enrichment: Optional["aws_sdk_pipes.types.optional_arn.OptionalArn"] = None,
        enrichment_parameters: Optional[
            "aws_sdk_pipes.types.pipe_enrichment_parameters.PipeEnrichmentParameters"
        ] = None,
        target_parameters: Optional[
            "aws_sdk_pipes.types.pipe_target_parameters.PipeTargetParameters"
        ] = None,
        tags: Optional["aws_sdk_pipes.types.tag_map.TagMap"] = None,
        log_configuration: Optional[
            "aws_sdk_pipes.types.pipe_log_configuration_parameters.PipeLogConfigurationParameters"
        ] = None,
        kms_key_identifier: Optional[
            "aws_sdk_pipes.types.kms_key_identifier.KmsKeyIdentifier"
        ] = None,
    ) -> "aws_sdk_pipes.types.create_pipe_response.CreatePipeResponse":
        r"""<p>Create a pipe. Amazon EventBridge Pipes connect event sources to targets and reduces the need for specialized knowledge and integration code.</p>

        Args:
            name: <p>The name of the pipe.</p>
            description: <p>A description of the pipe.</p>
            desired_state: <p>The state the pipe should be in.</p>
            source: <p>The ARN of the source resource.</p>
            source_parameters: <p>The parameters required to set up a source for your pipe.</p>
            enrichment: <p>The ARN of the enrichment resource.</p>
            enrichment_parameters: <p>The parameters required to set up enrichment on your pipe.</p>
            target: <p>The ARN of the target resource.</p>
            target_parameters: <p>The parameters required to set up a target for your pipe.</p> <p>For more information about pipe target parameters, including how to use dynamic path parameters, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html\">Target parameters</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            role_arn: <p>The ARN of the role that allows the pipe to send data to the target.</p>
            tags: <p>The list of key-value pairs to associate with the pipe.</p>
            log_configuration: <p>The logging configuration settings for the pipe.</p>
            kms_key_identifier: <p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>If you do not specify a customer managed key identifier, EventBridge uses an Amazon Web Services owned key to encrypt pipe data.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html\">Managing keys</a> in the <i>Key Management Service Developer Guide</i>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pipes.types.create_pipe_request.CreatePipeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pipes.types.create_pipe_response.CreatePipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.create_pipe

            (
                output,
                http_response,
            ) = await aws_sdk_pipes._operations.pipes.create_pipe.async_create_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.create_pipe_request.CreatePipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if desired_state is not None:
            input_["desired_state"] = desired_state
        input_["source"] = source
        if source_parameters is not None:
            input_["source_parameters"] = source_parameters
        if enrichment is not None:
            input_["enrichment"] = enrichment
        if enrichment_parameters is not None:
            input_["enrichment_parameters"] = enrichment_parameters
        input_["target"] = target
        if target_parameters is not None:
            input_["target_parameters"] = target_parameters
        input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.describe_pipe_response.DescribePipeResponse":
        r"""<p>Get the information about an existing pipe. For more information about pipes, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html\">Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name: <p>The name of the pipe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pipes.types.describe_pipe_request.DescribePipeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pipes.types.describe_pipe_response.DescribePipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.describe_pipe

            (
                output,
                http_response,
            ) = await aws_sdk_pipes._operations.pipes.describe_pipe.async_describe_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.describe_pipe_request.DescribePipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        role_arn: "aws_sdk_pipes.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
        description: Optional[
            "aws_sdk_pipes.types.pipe_description.PipeDescription"
        ] = None,
        desired_state: Optional[
            "aws_sdk_pipes.types.requested_pipe_state.RequestedPipeState"
        ] = None,
        source_parameters: Optional[
            "aws_sdk_pipes.types.update_pipe_source_parameters.UpdatePipeSourceParameters"
        ] = None,
        enrichment: Optional["aws_sdk_pipes.types.optional_arn.OptionalArn"] = None,
        enrichment_parameters: Optional[
            "aws_sdk_pipes.types.pipe_enrichment_parameters.PipeEnrichmentParameters"
        ] = None,
        target: Optional["aws_sdk_pipes.types.arn.Arn"] = None,
        target_parameters: Optional[
            "aws_sdk_pipes.types.pipe_target_parameters.PipeTargetParameters"
        ] = None,
        log_configuration: Optional[
            "aws_sdk_pipes.types.pipe_log_configuration_parameters.PipeLogConfigurationParameters"
        ] = None,
        kms_key_identifier: Optional[
            "aws_sdk_pipes.types.kms_key_identifier.KmsKeyIdentifier"
        ] = None,
    ) -> "aws_sdk_pipes.types.update_pipe_response.UpdatePipeResponse":
        r"""<p>Update an existing pipe. When you call <code>UpdatePipe</code>, EventBridge only the updates fields you have specified in the request; the rest remain unchanged. The exception to this is if you modify any Amazon Web Services-service specific fields in the <code>SourceParameters</code>, <code>EnrichmentParameters</code>, or <code>TargetParameters</code> objects. For example, <code>DynamoDBStreamParameters</code> or <code>EventBridgeEventBusParameters</code>. EventBridge updates the fields in these objects atomically as one and overrides existing values. This is by design, and means that if you don't specify an optional field in one of these <code>Parameters</code> objects, EventBridge sets that field to its system-default value during the update.</p> <p>For more information about pipes, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html\"> Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name: <p>The name of the pipe.</p>
            description: <p>A description of the pipe.</p>
            desired_state: <p>The state the pipe should be in.</p>
            source_parameters: <p>The parameters required to set up a source for your pipe.</p>
            enrichment: <p>The ARN of the enrichment resource.</p>
            enrichment_parameters: <p>The parameters required to set up enrichment on your pipe.</p>
            target: <p>The ARN of the target resource.</p>
            target_parameters: <p>The parameters required to set up a target for your pipe.</p> <p>For more information about pipe target parameters, including how to use dynamic path parameters, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html\">Target parameters</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            role_arn: <p>The ARN of the role that allows the pipe to send data to the target.</p>
            log_configuration: <p>The logging configuration settings for the pipe.</p>
            kms_key_identifier: <p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>To update a pipe that is using the default Amazon Web Services owned key to use a customer managed key instead, or update a pipe that is using a customer managed key to use a different customer managed key, specify a customer managed key identifier.</p> <p>To update a pipe that is using a customer managed key to use the default Amazon Web Services owned key, specify an empty string.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html\">Managing keys</a> in the <i>Key Management Service Developer Guide</i>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pipes.types.update_pipe_request.UpdatePipeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pipes.types.update_pipe_response.UpdatePipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.update_pipe

            (
                output,
                http_response,
            ) = await aws_sdk_pipes._operations.pipes.update_pipe.async_update_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.update_pipe_request.UpdatePipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if desired_state is not None:
            input_["desired_state"] = desired_state
        if source_parameters is not None:
            input_["source_parameters"] = source_parameters
        if enrichment is not None:
            input_["enrichment"] = enrichment
        if enrichment_parameters is not None:
            input_["enrichment_parameters"] = enrichment_parameters
        if target is not None:
            input_["target"] = target
        if target_parameters is not None:
            input_["target_parameters"] = target_parameters
        input_["role_arn"] = role_arn
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.delete_pipe_response.DeletePipeResponse":
        r"""<p>Delete an existing pipe. For more information about pipes, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html\">Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name: <p>The name of the pipe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pipes.types.delete_pipe_request.DeletePipeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pipes.types.delete_pipe_response.DeletePipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.delete_pipe

            (
                output,
                http_response,
            ) = await aws_sdk_pipes._operations.pipes.delete_pipe.async_delete_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.delete_pipe_request.DeletePipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
        name_prefix: Optional["aws_sdk_pipes.types.pipe_name.PipeName"] = None,
        desired_state: Optional[
            "aws_sdk_pipes.types.requested_pipe_state.RequestedPipeState"
        ] = None,
        current_state: Optional["aws_sdk_pipes.types.pipe_state.PipeState"] = None,
        source_prefix: Optional["aws_sdk_pipes.types.resource_arn.ResourceArn"] = None,
        target_prefix: Optional["aws_sdk_pipes.types.resource_arn.ResourceArn"] = None,
        next_token: Optional["aws_sdk_pipes.types.next_token.NextToken"] = None,
        limit: Optional["aws_sdk_pipes.types.limit_max100.LimitMax100"] = None,
    ) -> "aws_sdk_pipes.types.list_pipes_response.ListPipesResponse":
        r"""<p>Get the pipes associated with this account. For more information about pipes, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html\">Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name_prefix: <p>A value that will return a subset of the pipes associated with this account. For example, <code>\"NamePrefix\": \"ABC\"</code> will return all endpoints with \"ABC\" in the name.</p>
            desired_state: <p>The state the pipe should be in.</p>
            current_state: <p>The state the pipe is in.</p>
            source_prefix: <p>The prefix matching the pipe source.</p>
            target_prefix: <p>The prefix matching the pipe target.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>
            limit: <p>The maximum number of pipes to include in the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pipes.types.list_pipes_request.ListPipesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pipes.types.list_pipes_response.ListPipesResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.list_pipes

            (
                output,
                http_response,
            ) = await aws_sdk_pipes._operations.pipes.list_pipes.async_list_pipes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.list_pipes_request.ListPipesRequest = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if desired_state is not None:
            input_["desired_state"] = desired_state
        if current_state is not None:
            input_["current_state"] = current_state
        if source_prefix is not None:
            input_["source_prefix"] = source_prefix
        if target_prefix is not None:
            input_["target_prefix"] = target_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_pipe(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.start_pipe_response.StartPipeResponse":
        """<p>Start an existing pipe.</p>

        Args:
            name: <p>The name of the pipe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pipes.types.start_pipe_request.StartPipeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pipes.types.start_pipe_response.StartPipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.start_pipe

            (
                output,
                http_response,
            ) = await aws_sdk_pipes._operations.pipes.start_pipe.async_start_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.start_pipe_request.StartPipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_pipe(
        self,
        name: "aws_sdk_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
    ) -> "aws_sdk_pipes.types.stop_pipe_response.StopPipeResponse":
        """<p>Stop an existing pipe.</p>

        Args:
            name: <p>The name of the pipe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pipes.types.stop_pipe_request.StopPipeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pipes.types.stop_pipe_response.StopPipeResponse"
        ]:
            import aws_sdk_pipes._operations.pipes.stop_pipe

            (
                output,
                http_response,
            ) = await aws_sdk_pipes._operations.pipes.stop_pipe.async_stop_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pipes.types.stop_pipe_request.StopPipeRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
