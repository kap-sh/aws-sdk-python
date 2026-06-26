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
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.create_payment_manager_request
    import aws_sdk_bedrock_agentcore_control.types.create_payment_manager_response
    import aws_sdk_bedrock_agentcore_control.types.delete_payment_manager_request
    import aws_sdk_bedrock_agentcore_control.types.delete_payment_manager_response
    import aws_sdk_bedrock_agentcore_control.types.get_payment_manager_request
    import aws_sdk_bedrock_agentcore_control.types.get_payment_manager_response
    import aws_sdk_bedrock_agentcore_control.types.list_payment_managers_request
    import aws_sdk_bedrock_agentcore_control.types.list_payment_managers_response
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_id
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_name
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_summary
    import aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type
    import aws_sdk_bedrock_agentcore_control.types.payments_description
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_payment_manager_request
    import aws_sdk_bedrock_agentcore_control.types.update_payment_manager_response
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class PaymentManagerResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.payment_manager_name.PaymentManagerName",
        authorizer_type: "aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType",
        role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        authorizer_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_payment_manager_response.CreatePaymentManagerResponse":
        r"""<p>Creates a new payment manager in your Amazon Web Services account. A payment manager serves as the top-level resource for managing payment processing capabilities, including payment connectors that integrate with supported payment providers.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the payment manager.</p>
            description: <p>A description of the payment manager.</p>
            authorizer_type: <p>The type of authorizer to use for the payment manager.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the payment manager.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the payment manager assumes to access resources on your behalf.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            tags: <p>A map of tag keys and values to assign to the payment manager.</p>

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
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_payment_manager_request.CreatePaymentManagerRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_payment_manager_response.CreatePaymentManagerResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_manager

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_manager.create_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_payment_manager_request.CreatePaymentManagerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        input_["role_arn"] = role_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        payment_manager_id: "aws_sdk_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_payment_manager_response.GetPaymentManagerResponse":
        """<p>Retrieves information about a specific payment manager.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to retrieve.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_payment_manager_request.GetPaymentManagerRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_payment_manager_response.GetPaymentManagerResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_manager

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_manager.get_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_payment_manager_request.GetPaymentManagerRequest = {}  # type: ignore[typeddict-item]
        input_["payment_manager_id"] = payment_manager_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        payment_manager_id: "aws_sdk_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        authorizer_type: Optional[
            "aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType"
        ] = None,
        authorizer_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        role_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_payment_manager_response.UpdatePaymentManagerResponse":
        r"""<p>Updates an existing payment manager. This operation uses PATCH semantics, so you only need to specify the fields you want to change.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to update.</p>
            description: <p>The updated description of the payment manager.</p>
            authorizer_type: <p>The updated authorizer type for the payment manager.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the payment manager.</p>
            role_arn: <p>The updated Amazon Resource Name (ARN) of the IAM role for the payment manager.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>

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
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_payment_manager_request.UpdatePaymentManagerRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_payment_manager_response.UpdatePaymentManagerResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_manager

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_manager.update_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_payment_manager_request.UpdatePaymentManagerRequest = {}  # type: ignore[typeddict-item]
        input_["payment_manager_id"] = payment_manager_id
        if description is not None:
            input_["description"] = description
        if authorizer_type is not None:
            input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        payment_manager_id: "aws_sdk_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_payment_manager_response.DeletePaymentManagerResponse":
        r"""<p>Deletes a payment manager. All payment connectors associated with the payment manager must be deleted before the payment manager can be deleted. This operation initiates the deletion process asynchronously.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_payment_manager_request.DeletePaymentManagerRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_payment_manager_response.DeletePaymentManagerResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_manager

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_manager.delete_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_payment_manager_request.DeletePaymentManagerRequest = {}  # type: ignore[typeddict-item]
        input_["payment_manager_id"] = payment_manager_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_payment_managers_response.ListPaymentManagersResponse":
        """<p>Lists all payment managers in the account.</p>

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
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_payment_managers_request.ListPaymentManagersRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_payment_managers_response.ListPaymentManagersResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_managers

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_managers.list_payment_managers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_payment_managers_request.ListPaymentManagersRequest = {}  # type: ignore[typeddict-item]
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


class AsyncPaymentManagerResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.payment_manager_name.PaymentManagerName",
        authorizer_type: "aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType",
        role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        authorizer_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_payment_manager_response.CreatePaymentManagerResponse":
        r"""<p>Creates a new payment manager in your Amazon Web Services account. A payment manager serves as the top-level resource for managing payment processing capabilities, including payment connectors that integrate with supported payment providers.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the payment manager.</p>
            description: <p>A description of the payment manager.</p>
            authorizer_type: <p>The type of authorizer to use for the payment manager.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the payment manager.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the payment manager assumes to access resources on your behalf.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            tags: <p>A map of tag keys and values to assign to the payment manager.</p>

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
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_payment_manager_request.CreatePaymentManagerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_payment_manager_response.CreatePaymentManagerResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_manager

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_manager.async_create_payment_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_payment_manager_request.CreatePaymentManagerRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        input_["role_arn"] = role_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        payment_manager_id: "aws_sdk_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_payment_manager_response.GetPaymentManagerResponse":
        """<p>Retrieves information about a specific payment manager.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to retrieve.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_payment_manager_request.GetPaymentManagerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_payment_manager_response.GetPaymentManagerResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_manager

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_manager.async_get_payment_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_payment_manager_request.GetPaymentManagerRequest = {}  # type: ignore[typeddict-item]
        input_["payment_manager_id"] = payment_manager_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        payment_manager_id: "aws_sdk_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        authorizer_type: Optional[
            "aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType"
        ] = None,
        authorizer_configuration: Optional[
            "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        role_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_payment_manager_response.UpdatePaymentManagerResponse":
        r"""<p>Updates an existing payment manager. This operation uses PATCH semantics, so you only need to specify the fields you want to change.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to update.</p>
            description: <p>The updated description of the payment manager.</p>
            authorizer_type: <p>The updated authorizer type for the payment manager.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the payment manager.</p>
            role_arn: <p>The updated Amazon Resource Name (ARN) of the IAM role for the payment manager.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>

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
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_payment_manager_request.UpdatePaymentManagerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_payment_manager_response.UpdatePaymentManagerResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_manager

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_manager.async_update_payment_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_payment_manager_request.UpdatePaymentManagerRequest = {}  # type: ignore[typeddict-item]
        input_["payment_manager_id"] = payment_manager_id
        if description is not None:
            input_["description"] = description
        if authorizer_type is not None:
            input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        payment_manager_id: "aws_sdk_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_payment_manager_response.DeletePaymentManagerResponse":
        r"""<p>Deletes a payment manager. All payment connectors associated with the payment manager must be deleted before the payment manager can be deleted. This operation initiates the deletion process asynchronously.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_payment_manager_request.DeletePaymentManagerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_payment_manager_response.DeletePaymentManagerResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_manager

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_manager.async_delete_payment_manager(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_payment_manager_request.DeletePaymentManagerRequest = {}  # type: ignore[typeddict-item]
        input_["payment_manager_id"] = payment_manager_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_payment_managers_response.ListPaymentManagersResponse":
        """<p>Lists all payment managers in the account.</p>

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
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_payment_managers_request.ListPaymentManagersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_payment_managers_response.ListPaymentManagersResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_managers

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_managers.async_list_payment_managers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_payment_managers_request.ListPaymentManagersRequest = {}  # type: ignore[typeddict-item]
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
