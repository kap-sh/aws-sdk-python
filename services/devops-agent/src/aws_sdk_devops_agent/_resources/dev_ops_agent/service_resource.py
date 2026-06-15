from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_devops_agent._auth._signers
import aws_sdk_devops_agent._auth._sigv4
from aws_sdk_devops_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.deregister_service_input
    import aws_sdk_devops_agent.types.deregister_service_output
    import aws_sdk_devops_agent.types.get_service_input
    import aws_sdk_devops_agent.types.get_service_output
    import aws_sdk_devops_agent.types.kms_key_arn
    import aws_sdk_devops_agent.types.list_services_input
    import aws_sdk_devops_agent.types.list_services_output
    import aws_sdk_devops_agent.types.next_token
    import aws_sdk_devops_agent.types.post_register_service_supported_service
    import aws_sdk_devops_agent.types.private_connection_name
    import aws_sdk_devops_agent.types.register_service_input
    import aws_sdk_devops_agent.types.register_service_output
    import aws_sdk_devops_agent.types.registered_service
    import aws_sdk_devops_agent.types.service
    import aws_sdk_devops_agent.types.service_details
    import aws_sdk_devops_agent.types.service_id
    import aws_sdk_devops_agent.types.service_name
    import aws_sdk_devops_agent.types.tags
    from aws_sdk_devops_agent._services.async_dev_ops_agent import (
        AsyncDevOpsAgentClient,
        AsyncDevOpsAgentClientConfig,
    )
    from aws_sdk_devops_agent._services.dev_ops_agent import (
        DevOpsAgentClient,
        DevOpsAgentClientConfig,
    )


class ServiceResource:
    def __init__(self, service: DevOpsAgentClient) -> None:
        self._service = service

    def create(
        self,
        service: "aws_sdk_devops_agent.types.post_register_service_supported_service.PostRegisterServiceSupportedService",
        service_details: "aws_sdk_devops_agent.types.service_details.ServiceDetails",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        kms_key_arn: Optional[
            "aws_sdk_devops_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        private_connection_name: Optional[
            "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        target_url_private_connection_name: Optional[
            "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        exchange_url_private_connection_name: Optional[
            "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        name: Optional["aws_sdk_devops_agent.types.service_name.ServiceName"] = None,
        tags: Optional["aws_sdk_devops_agent.types.tags.Tags"] = None,
    ) -> "aws_sdk_devops_agent.types.register_service_output.RegisterServiceOutput":
        """<p>This operation registers the specified service</p>

        Args:
            service_details: <p>Service-specific authorization configuration parameters</p>
            kms_key_arn: <p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>
            private_connection_name: <p>The name of the private connection to use for VPC connectivity.</p>
            target_url_private_connection_name: <p>The name of the private connection to use for API calls (target URL) only. Cannot be specified when privateConnectionName is provided.</p>
            exchange_url_private_connection_name: <p>The name of the private connection to use for OAuth token exchange requests only. Cannot be specified when privateConnectionName is provided.</p>
            name: <p>The display name for the service registration.</p>
            tags: <p>Tags to add to the Service at registration time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.register_service_input.RegisterServiceInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.register_service_output.RegisterServiceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.register_service

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.register_service.register_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.register_service_input.RegisterServiceInput = {}  # type: ignore[typeddict-item]
        input_["service"] = service
        input_["service_details"] = service_details
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if private_connection_name is not None:
            input_["private_connection_name"] = private_connection_name
        if target_url_private_connection_name is not None:
            input_["target_url_private_connection_name"] = (
                target_url_private_connection_name
            )
        if exchange_url_private_connection_name is not None:
            input_["exchange_url_private_connection_name"] = (
                exchange_url_private_connection_name
            )
        if name is not None:
            input_["name"] = name
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
        service_id: "aws_sdk_devops_agent.types.service_id.ServiceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.get_service_output.GetServiceOutput":
        """<p>Retrieves given service by it's unique identifier</p>

        Args:
            service_id: <p>The unique identifier of the given service.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.get_service_input.GetServiceInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.get_service_output.GetServiceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_service

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_service_input.GetServiceInput = {}  # type: ignore[typeddict-item]
        input_["service_id"] = service_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        service_id: "aws_sdk_devops_agent.types.service_id.ServiceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.deregister_service_output.DeregisterServiceOutput":
        """<p>Deregister a service</p>

        Args:
            service_id: <p>The service id to deregister. A service can only be deregistered if it is not associated with any AgentSpace.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.deregister_service_input.DeregisterServiceInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.deregister_service_output.DeregisterServiceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.deregister_service

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.deregister_service.deregister_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.deregister_service_input.DeregisterServiceInput = {}  # type: ignore[typeddict-item]
        input_["service_id"] = service_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_services(
        self,
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        filter_service_type: Optional[
            "aws_sdk_devops_agent.types.service.Service"
        ] = None,
    ) -> "aws_sdk_devops_agent.types.list_services_output.ListServicesOutput":
        """<p>List a list of registered service on the account level.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>
            filter_service_type: <p>Optional filter to list only services of a specific type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.list_services_input.ListServicesInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.list_services_output.ListServicesOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_services

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_services_input.ListServicesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_service_type is not None:
            input_["filter_service_type"] = filter_service_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncServiceResource:
    def __init__(self, service: AsyncDevOpsAgentClient) -> None:
        self._service = service

    async def create(
        self,
        service: "aws_sdk_devops_agent.types.post_register_service_supported_service.PostRegisterServiceSupportedService",
        service_details: "aws_sdk_devops_agent.types.service_details.ServiceDetails",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        kms_key_arn: Optional[
            "aws_sdk_devops_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        private_connection_name: Optional[
            "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        target_url_private_connection_name: Optional[
            "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        exchange_url_private_connection_name: Optional[
            "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        name: Optional["aws_sdk_devops_agent.types.service_name.ServiceName"] = None,
        tags: Optional["aws_sdk_devops_agent.types.tags.Tags"] = None,
    ) -> "aws_sdk_devops_agent.types.register_service_output.RegisterServiceOutput":
        """<p>This operation registers the specified service</p>

        Args:
            service_details: <p>Service-specific authorization configuration parameters</p>
            kms_key_arn: <p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>
            private_connection_name: <p>The name of the private connection to use for VPC connectivity.</p>
            target_url_private_connection_name: <p>The name of the private connection to use for API calls (target URL) only. Cannot be specified when privateConnectionName is provided.</p>
            exchange_url_private_connection_name: <p>The name of the private connection to use for OAuth token exchange requests only. Cannot be specified when privateConnectionName is provided.</p>
            name: <p>The display name for the service registration.</p>
            tags: <p>Tags to add to the Service at registration time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.register_service_input.RegisterServiceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.register_service_output.RegisterServiceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.register_service

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.register_service.async_register_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.register_service_input.RegisterServiceInput = {}  # type: ignore[typeddict-item]
        input_["service"] = service
        input_["service_details"] = service_details
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if private_connection_name is not None:
            input_["private_connection_name"] = private_connection_name
        if target_url_private_connection_name is not None:
            input_["target_url_private_connection_name"] = (
                target_url_private_connection_name
            )
        if exchange_url_private_connection_name is not None:
            input_["exchange_url_private_connection_name"] = (
                exchange_url_private_connection_name
            )
        if name is not None:
            input_["name"] = name
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
        service_id: "aws_sdk_devops_agent.types.service_id.ServiceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.get_service_output.GetServiceOutput":
        """<p>Retrieves given service by it's unique identifier</p>

        Args:
            service_id: <p>The unique identifier of the given service.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.get_service_input.GetServiceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.get_service_output.GetServiceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_service

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.get_service.async_get_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_service_input.GetServiceInput = {}  # type: ignore[typeddict-item]
        input_["service_id"] = service_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        service_id: "aws_sdk_devops_agent.types.service_id.ServiceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.deregister_service_output.DeregisterServiceOutput":
        """<p>Deregister a service</p>

        Args:
            service_id: <p>The service id to deregister. A service can only be deregistered if it is not associated with any AgentSpace.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.deregister_service_input.DeregisterServiceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.deregister_service_output.DeregisterServiceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.deregister_service

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.deregister_service.async_deregister_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.deregister_service_input.DeregisterServiceInput = {}  # type: ignore[typeddict-item]
        input_["service_id"] = service_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_services(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        filter_service_type: Optional[
            "aws_sdk_devops_agent.types.service.Service"
        ] = None,
    ) -> "aws_sdk_devops_agent.types.list_services_output.ListServicesOutput":
        """<p>List a list of registered service on the account level.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>
            filter_service_type: <p>Optional filter to list only services of a specific type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_services_input.ListServicesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_services_output.ListServicesOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_services

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_services_input.ListServicesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_service_type is not None:
            input_["filter_service_type"] = filter_service_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
