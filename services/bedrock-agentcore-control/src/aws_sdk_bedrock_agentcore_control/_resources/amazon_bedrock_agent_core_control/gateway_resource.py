from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
from aws_sdk_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.authorizer_type
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.create_gateway_request
    import aws_sdk_bedrock_agentcore_control.types.create_gateway_response
    import aws_sdk_bedrock_agentcore_control.types.delete_gateway_request
    import aws_sdk_bedrock_agentcore_control.types.delete_gateway_response
    import aws_sdk_bedrock_agentcore_control.types.exception_level
    import aws_sdk_bedrock_agentcore_control.types.gateway_description
    import aws_sdk_bedrock_agentcore_control.types.gateway_identifier
    import aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations
    import aws_sdk_bedrock_agentcore_control.types.gateway_max_results
    import aws_sdk_bedrock_agentcore_control.types.gateway_name
    import aws_sdk_bedrock_agentcore_control.types.gateway_next_token
    import aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration
    import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration
    import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type
    import aws_sdk_bedrock_agentcore_control.types.gateway_summary
    import aws_sdk_bedrock_agentcore_control.types.get_gateway_request
    import aws_sdk_bedrock_agentcore_control.types.get_gateway_response
    import aws_sdk_bedrock_agentcore_control.types.kms_key_arn
    import aws_sdk_bedrock_agentcore_control.types.list_gateways_request
    import aws_sdk_bedrock_agentcore_control.types.list_gateways_response
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_gateway_request
    import aws_sdk_bedrock_agentcore_control.types.update_gateway_response
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class GatewayResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create_gateway(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.gateway_name.GatewayName",
        role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn",
        authorizer_type: "aws_sdk_bedrock_agentcore_control.types.authorizer_type.AuthorizerType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        protocol_type: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
        ] = None,
        protocol_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration.GatewayProtocolConfiguration"
        ] = None,
        authorizer_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        kms_key_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        interceptor_configurations: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations.GatewayInterceptorConfigurations"
        ] = None,
        policy_engine_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration.GatewayPolicyEngineConfiguration"
        ] = None,
        exception_level: Optional[
            "aws_sdk_bedrock_agentcore_control.types.exception_level.ExceptionLevel"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_gateway_response.CreateGatewayResponse":
        r"""<p>Creates a gateway for Amazon Bedrock Agent. A gateway serves as an integration point between your agent and external services.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the gateway. The name must be unique within your account.</p>
            description: <p>The description of the gateway.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the gateway to access Amazon Web Services services.</p>
            protocol_type: <p>The protocol type for the gateway.</p>
            protocol_configuration: <p>The configuration settings for the protocol specified in the <code>protocolType</code> parameter.</p>
            authorizer_type: <p>The type of authorizer to use for the gateway.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> <li> <p> <code>NONE</code> - No authorization</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the gateway. Required if <code>authorizerType</code> is <code>CUSTOM_JWT</code>.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt data associated with the gateway.</p>
            interceptor_configurations: <p>A list of configuration settings for a gateway interceptor. Gateway interceptors allow custom code to be invoked during gateway invocations.</p>
            policy_engine_configuration: <p>The policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.</p>
            exception_level: <p>The level of detail in error messages returned when invoking the gateway.</p> <ul> <li> <p>If the value is <code>DEBUG</code>, granular exception messages are returned to help a user debug the gateway.</p> </li> <li> <p>If the value is omitted, a generic error message is returned to the end user.</p> </li> </ul>
            tags: <p>A map of key-value pairs to associate with the gateway as metadata tags.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_gateway_request.CreateGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway.create_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_gateway_request.CreateGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_token is not None:
            input_["client_token"] = client_token
        input_["role_arn"] = role_arn
        if protocol_type is not None:
            input_["protocol_type"] = protocol_type
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if interceptor_configurations is not None:
            input_["interceptor_configurations"] = interceptor_configurations
        if policy_engine_configuration is not None:
            input_["policy_engine_configuration"] = policy_engine_configuration
        if exception_level is not None:
            input_["exception_level"] = exception_level
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_gateway(
        self,
        gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_gateway_response.DeleteGatewayResponse":
        """<p>Deletes a gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to delete.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_gateway_response.DeleteGatewayResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway.delete_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_gateway_request.DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_identifier"] = gateway_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_gateway(
        self,
        gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_gateway_response.GetGatewayResponse":
        """<p>Retrieves information about a specific Gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to retrieve.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_gateway_request.GetGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_gateway_response.GetGatewayResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway.get_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_gateway_request.GetGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_identifier"] = gateway_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_gateways(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_max_results.GatewayMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_next_token.GatewayNextToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_gateways_response.ListGatewaysResponse":
        """<p>Lists all gateways in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_gateways_request.ListGatewaysRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateways

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateways.list_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_gateways_request.ListGatewaysRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_gateway(
        self,
        gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        name: "aws_sdk_bedrock_agentcore_control.types.gateway_name.GatewayName",
        role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn",
        authorizer_type: "aws_sdk_bedrock_agentcore_control.types.authorizer_type.AuthorizerType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
        ] = None,
        protocol_type: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
        ] = None,
        protocol_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration.GatewayProtocolConfiguration"
        ] = None,
        authorizer_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        kms_key_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        interceptor_configurations: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations.GatewayInterceptorConfigurations"
        ] = None,
        policy_engine_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration.GatewayPolicyEngineConfiguration"
        ] = None,
        exception_level: Optional[
            "aws_sdk_bedrock_agentcore_control.types.exception_level.ExceptionLevel"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_gateway_response.UpdateGatewayResponse":
        """<p>Updates an existing gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to update.</p>
            name: <p>The name of the gateway. This name must be the same as the one when the gateway was created.</p>
            description: <p>The updated description for the gateway.</p>
            role_arn: <p>The updated IAM role ARN that provides permissions for the gateway.</p>
            protocol_type: <p>The updated protocol type for the gateway.</p>
            authorizer_type: <p>The updated authorizer type for the gateway.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the gateway.</p>
            kms_key_arn: <p>The updated ARN of the KMS key used to encrypt the gateway.</p>
            interceptor_configurations: <p>The updated interceptor configurations for the gateway.</p>
            policy_engine_configuration: <p>The updated policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.</p>
            exception_level: <p>The level of detail in error messages returned when invoking the gateway.</p> <ul> <li> <p>If the value is <code>DEBUG</code>, granular exception messages are returned to help a user debug the gateway.</p> </li> <li> <p>If the value is omitted, a generic error message is returned to the end user.</p> </li> </ul>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_gateway_request.UpdateGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_gateway_response.UpdateGatewayResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway.update_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_gateway_request.UpdateGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_identifier"] = gateway_identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["role_arn"] = role_arn
        if protocol_type is not None:
            input_["protocol_type"] = protocol_type
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if interceptor_configurations is not None:
            input_["interceptor_configurations"] = interceptor_configurations
        if policy_engine_configuration is not None:
            input_["policy_engine_configuration"] = policy_engine_configuration
        if exception_level is not None:
            input_["exception_level"] = exception_level

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncGatewayResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create_gateway(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.gateway_name.GatewayName",
        role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn",
        authorizer_type: "aws_sdk_bedrock_agentcore_control.types.authorizer_type.AuthorizerType",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        protocol_type: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
        ] = None,
        protocol_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration.GatewayProtocolConfiguration"
        ] = None,
        authorizer_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        kms_key_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        interceptor_configurations: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations.GatewayInterceptorConfigurations"
        ] = None,
        policy_engine_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration.GatewayPolicyEngineConfiguration"
        ] = None,
        exception_level: Optional[
            "aws_sdk_bedrock_agentcore_control.types.exception_level.ExceptionLevel"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_gateway_response.CreateGatewayResponse":
        r"""<p>Creates a gateway for Amazon Bedrock Agent. A gateway serves as an integration point between your agent and external services.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the gateway. The name must be unique within your account.</p>
            description: <p>The description of the gateway.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the gateway to access Amazon Web Services services.</p>
            protocol_type: <p>The protocol type for the gateway.</p>
            protocol_configuration: <p>The configuration settings for the protocol specified in the <code>protocolType</code> parameter.</p>
            authorizer_type: <p>The type of authorizer to use for the gateway.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> <li> <p> <code>NONE</code> - No authorization</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the gateway. Required if <code>authorizerType</code> is <code>CUSTOM_JWT</code>.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt data associated with the gateway.</p>
            interceptor_configurations: <p>A list of configuration settings for a gateway interceptor. Gateway interceptors allow custom code to be invoked during gateway invocations.</p>
            policy_engine_configuration: <p>The policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.</p>
            exception_level: <p>The level of detail in error messages returned when invoking the gateway.</p> <ul> <li> <p>If the value is <code>DEBUG</code>, granular exception messages are returned to help a user debug the gateway.</p> </li> <li> <p>If the value is omitted, a generic error message is returned to the end user.</p> </li> </ul>
            tags: <p>A map of key-value pairs to associate with the gateway as metadata tags.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_gateway_request.CreateGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway.async_create_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_gateway_request.CreateGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_token is not None:
            input_["client_token"] = client_token
        input_["role_arn"] = role_arn
        if protocol_type is not None:
            input_["protocol_type"] = protocol_type
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if interceptor_configurations is not None:
            input_["interceptor_configurations"] = interceptor_configurations
        if policy_engine_configuration is not None:
            input_["policy_engine_configuration"] = policy_engine_configuration
        if exception_level is not None:
            input_["exception_level"] = exception_level
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_gateway(
        self,
        gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_gateway_response.DeleteGatewayResponse":
        """<p>Deletes a gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to delete.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_gateway_response.DeleteGatewayResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway.async_delete_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_gateway_request.DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_identifier"] = gateway_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_gateway(
        self,
        gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_gateway_response.GetGatewayResponse":
        """<p>Retrieves information about a specific Gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to retrieve.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_gateway_request.GetGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_gateway_response.GetGatewayResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway.async_get_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_gateway_request.GetGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_identifier"] = gateway_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_gateways(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_max_results.GatewayMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_next_token.GatewayNextToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_gateways_response.ListGatewaysResponse":
        """<p>Lists all gateways in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_gateways_request.ListGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateways

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateways.async_list_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_gateways_request.ListGatewaysRequest = {}  # type: ignore[typeddict-item]
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

    async def update_gateway(
        self,
        gateway_identifier: "aws_sdk_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        name: "aws_sdk_bedrock_agentcore_control.types.gateway_name.GatewayName",
        role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn",
        authorizer_type: "aws_sdk_bedrock_agentcore_control.types.authorizer_type.AuthorizerType",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
        ] = None,
        protocol_type: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
        ] = None,
        protocol_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration.GatewayProtocolConfiguration"
        ] = None,
        authorizer_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        kms_key_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        interceptor_configurations: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations.GatewayInterceptorConfigurations"
        ] = None,
        policy_engine_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration.GatewayPolicyEngineConfiguration"
        ] = None,
        exception_level: Optional[
            "aws_sdk_bedrock_agentcore_control.types.exception_level.ExceptionLevel"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_gateway_response.UpdateGatewayResponse":
        """<p>Updates an existing gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to update.</p>
            name: <p>The name of the gateway. This name must be the same as the one when the gateway was created.</p>
            description: <p>The updated description for the gateway.</p>
            role_arn: <p>The updated IAM role ARN that provides permissions for the gateway.</p>
            protocol_type: <p>The updated protocol type for the gateway.</p>
            authorizer_type: <p>The updated authorizer type for the gateway.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the gateway.</p>
            kms_key_arn: <p>The updated ARN of the KMS key used to encrypt the gateway.</p>
            interceptor_configurations: <p>The updated interceptor configurations for the gateway.</p>
            policy_engine_configuration: <p>The updated policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.</p>
            exception_level: <p>The level of detail in error messages returned when invoking the gateway.</p> <ul> <li> <p>If the value is <code>DEBUG</code>, granular exception messages are returned to help a user debug the gateway.</p> </li> <li> <p>If the value is omitted, a generic error message is returned to the end user.</p> </li> </ul>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_gateway_request.UpdateGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_gateway_response.UpdateGatewayResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway.async_update_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_gateway_request.UpdateGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_identifier"] = gateway_identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["role_arn"] = role_arn
        if protocol_type is not None:
            input_["protocol_type"] = protocol_type
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if interceptor_configurations is not None:
            input_["interceptor_configurations"] = interceptor_configurations
        if policy_engine_configuration is not None:
            input_["policy_engine_configuration"] = policy_engine_configuration
        if exception_level is not None:
            input_["exception_level"] = exception_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
