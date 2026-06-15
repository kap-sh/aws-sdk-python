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
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.create_online_evaluation_config_request
    import aws_sdk_bedrock_agentcore_control.types.create_online_evaluation_config_response
    import aws_sdk_bedrock_agentcore_control.types.data_source_config
    import aws_sdk_bedrock_agentcore_control.types.delete_online_evaluation_config_request
    import aws_sdk_bedrock_agentcore_control.types.delete_online_evaluation_config_response
    import aws_sdk_bedrock_agentcore_control.types.evaluation_config_description
    import aws_sdk_bedrock_agentcore_control.types.evaluation_config_name
    import aws_sdk_bedrock_agentcore_control.types.evaluator_list
    import aws_sdk_bedrock_agentcore_control.types.get_online_evaluation_config_request
    import aws_sdk_bedrock_agentcore_control.types.get_online_evaluation_config_response
    import aws_sdk_bedrock_agentcore_control.types.list_online_evaluation_configs_request
    import aws_sdk_bedrock_agentcore_control.types.list_online_evaluation_configs_response
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.rule
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_online_evaluation_config_request
    import aws_sdk_bedrock_agentcore_control.types.update_online_evaluation_config_response
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class OnlineEvaluationConfig:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        online_evaluation_config_name: "aws_sdk_bedrock_agentcore_control.types.evaluation_config_name.EvaluationConfigName",
        rule: "aws_sdk_bedrock_agentcore_control.types.rule.Rule",
        data_source_config: "aws_sdk_bedrock_agentcore_control.types.data_source_config.DataSourceConfig",
        evaluators: "aws_sdk_bedrock_agentcore_control.types.evaluator_list.EvaluatorList",
        evaluation_execution_role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn",
        enable_on_create: bool,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_online_evaluation_config_response.CreateOnlineEvaluationConfigResponse":
        r"""<p> Creates an online evaluation configuration for continuous monitoring of agent performance. Online evaluation automatically samples live traffic from CloudWatch logs at specified rates and applies evaluators to assess agent quality in production. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            online_evaluation_config_name: <p> The name of the online evaluation configuration. Must be unique within your account. </p>
            description: <p> The description of the online evaluation configuration that explains its monitoring purpose and scope. </p>
            rule: <p> The evaluation rule that defines sampling configuration, filters, and session detection settings for the online evaluation. </p>
            data_source_config: <p> The data source configuration that specifies CloudWatch log groups and service names to monitor for agent traces. </p>
            evaluators: <p> The list of evaluators to apply during online evaluation. Can include both built-in evaluators and custom evaluators created with <code>CreateEvaluator</code>. </p>
            evaluation_execution_role_arn: <p> The Amazon Resource Name (ARN) of the IAM role that grants permissions to read from CloudWatch logs, write evaluation results, and invoke Amazon Bedrock models for evaluation. If the configuration references evaluators encrypted with a customer managed KMS key, this role must also have <code>kms:Decrypt</code> permission on the KMS key. The service validates this permission at configuration creation time. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html\">Encryption at rest for AgentCore Evaluations</a>. </p>
            enable_on_create: <p> Whether to enable the online evaluation configuration immediately upon creation. If true, evaluation begins automatically. </p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Online Evaluation Config. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_online_evaluation_config_request.CreateOnlineEvaluationConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_online_evaluation_config_response.CreateOnlineEvaluationConfigResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_online_evaluation_config

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_online_evaluation_config.create_online_evaluation_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_online_evaluation_config_request.CreateOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["online_evaluation_config_name"] = online_evaluation_config_name
        if description is not None:
            input_["description"] = description
        input_["rule"] = rule
        input_["data_source_config"] = data_source_config
        input_["evaluators"] = evaluators
        input_["evaluation_execution_role_arn"] = evaluation_execution_role_arn
        input_["enable_on_create"] = enable_on_create
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
        online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_online_evaluation_config_response.GetOnlineEvaluationConfigResponse":
        """<p> Retrieves detailed information about an online evaluation configuration, including its rules, data sources, evaluators, and execution status. </p>

        Args:
            online_evaluation_config_id: <p> The unique identifier of the online evaluation configuration to retrieve. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_online_evaluation_config_request.GetOnlineEvaluationConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_online_evaluation_config_response.GetOnlineEvaluationConfigResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_online_evaluation_config

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_online_evaluation_config.get_online_evaluation_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_online_evaluation_config_request.GetOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
        input_["online_evaluation_config_id"] = online_evaluation_config_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
        ] = None,
        rule: Optional["aws_sdk_bedrock_agentcore_control.types.rule.Rule"] = None,
        data_source_config: Optional[
            "aws_sdk_bedrock_agentcore_control.types.data_source_config.DataSourceConfig"
        ] = None,
        evaluators: Optional[
            "aws_sdk_bedrock_agentcore_control.types.evaluator_list.EvaluatorList"
        ] = None,
        evaluation_execution_role_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        execution_status: Optional[
            "aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_online_evaluation_config_response.UpdateOnlineEvaluationConfigResponse":
        r"""<p> Updates an online evaluation configuration's settings, including rules, data sources, evaluators, and execution status. Changes take effect immediately for ongoing evaluations. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            online_evaluation_config_id: <p> The unique identifier of the online evaluation configuration to update. </p>
            description: <p> The updated description of the online evaluation configuration. </p>
            rule: <p> The updated evaluation rule containing sampling configuration, filters, and session settings. </p>
            data_source_config: <p> The updated data source configuration specifying CloudWatch log groups and service names to monitor. </p>
            evaluators: <p> The updated list of evaluators to apply during online evaluation. </p>
            evaluation_execution_role_arn: <p> The updated Amazon Resource Name (ARN) of the IAM role used for evaluation execution. </p>
            execution_status: <p> The updated execution status to enable or disable the online evaluation. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_online_evaluation_config_request.UpdateOnlineEvaluationConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_online_evaluation_config_response.UpdateOnlineEvaluationConfigResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_online_evaluation_config

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_online_evaluation_config.update_online_evaluation_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_online_evaluation_config_request.UpdateOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["online_evaluation_config_id"] = online_evaluation_config_id
        if description is not None:
            input_["description"] = description
        if rule is not None:
            input_["rule"] = rule
        if data_source_config is not None:
            input_["data_source_config"] = data_source_config
        if evaluators is not None:
            input_["evaluators"] = evaluators
        if evaluation_execution_role_arn is not None:
            input_["evaluation_execution_role_arn"] = evaluation_execution_role_arn
        if execution_status is not None:
            input_["execution_status"] = execution_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_online_evaluation_config_response.DeleteOnlineEvaluationConfigResponse":
        """<p> Deletes an online evaluation configuration and stops any ongoing evaluation processes associated with it. </p>

        Args:
            online_evaluation_config_id: <p> The unique identifier of the online evaluation configuration to delete. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_online_evaluation_config_request.DeleteOnlineEvaluationConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_online_evaluation_config_response.DeleteOnlineEvaluationConfigResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_online_evaluation_config

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_online_evaluation_config.delete_online_evaluation_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_online_evaluation_config_request.DeleteOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
        input_["online_evaluation_config_id"] = online_evaluation_config_id

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
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_online_evaluation_configs_response.ListOnlineEvaluationConfigsResponse":
        """<p> Lists all online evaluation configurations in the account, providing summary information about each configuration's status and settings. </p>

        Args:
            next_token: <p> The pagination token from a previous request to retrieve the next page of results. </p>
            max_results: <p> The maximum number of online evaluation configurations to return in a single response. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_online_evaluation_configs_request.ListOnlineEvaluationConfigsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_online_evaluation_configs_response.ListOnlineEvaluationConfigsResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_online_evaluation_configs

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_online_evaluation_configs.list_online_evaluation_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_online_evaluation_configs_request.ListOnlineEvaluationConfigsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncOnlineEvaluationConfig:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        online_evaluation_config_name: "aws_sdk_bedrock_agentcore_control.types.evaluation_config_name.EvaluationConfigName",
        rule: "aws_sdk_bedrock_agentcore_control.types.rule.Rule",
        data_source_config: "aws_sdk_bedrock_agentcore_control.types.data_source_config.DataSourceConfig",
        evaluators: "aws_sdk_bedrock_agentcore_control.types.evaluator_list.EvaluatorList",
        evaluation_execution_role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn",
        enable_on_create: bool,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_online_evaluation_config_response.CreateOnlineEvaluationConfigResponse":
        r"""<p> Creates an online evaluation configuration for continuous monitoring of agent performance. Online evaluation automatically samples live traffic from CloudWatch logs at specified rates and applies evaluators to assess agent quality in production. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            online_evaluation_config_name: <p> The name of the online evaluation configuration. Must be unique within your account. </p>
            description: <p> The description of the online evaluation configuration that explains its monitoring purpose and scope. </p>
            rule: <p> The evaluation rule that defines sampling configuration, filters, and session detection settings for the online evaluation. </p>
            data_source_config: <p> The data source configuration that specifies CloudWatch log groups and service names to monitor for agent traces. </p>
            evaluators: <p> The list of evaluators to apply during online evaluation. Can include both built-in evaluators and custom evaluators created with <code>CreateEvaluator</code>. </p>
            evaluation_execution_role_arn: <p> The Amazon Resource Name (ARN) of the IAM role that grants permissions to read from CloudWatch logs, write evaluation results, and invoke Amazon Bedrock models for evaluation. If the configuration references evaluators encrypted with a customer managed KMS key, this role must also have <code>kms:Decrypt</code> permission on the KMS key. The service validates this permission at configuration creation time. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html\">Encryption at rest for AgentCore Evaluations</a>. </p>
            enable_on_create: <p> Whether to enable the online evaluation configuration immediately upon creation. If true, evaluation begins automatically. </p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Online Evaluation Config. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_online_evaluation_config_request.CreateOnlineEvaluationConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_online_evaluation_config_response.CreateOnlineEvaluationConfigResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_online_evaluation_config

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_online_evaluation_config.async_create_online_evaluation_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_online_evaluation_config_request.CreateOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["online_evaluation_config_name"] = online_evaluation_config_name
        if description is not None:
            input_["description"] = description
        input_["rule"] = rule
        input_["data_source_config"] = data_source_config
        input_["evaluators"] = evaluators
        input_["evaluation_execution_role_arn"] = evaluation_execution_role_arn
        input_["enable_on_create"] = enable_on_create
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
        online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_online_evaluation_config_response.GetOnlineEvaluationConfigResponse":
        """<p> Retrieves detailed information about an online evaluation configuration, including its rules, data sources, evaluators, and execution status. </p>

        Args:
            online_evaluation_config_id: <p> The unique identifier of the online evaluation configuration to retrieve. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_online_evaluation_config_request.GetOnlineEvaluationConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_online_evaluation_config_response.GetOnlineEvaluationConfigResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_online_evaluation_config

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_online_evaluation_config.async_get_online_evaluation_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_online_evaluation_config_request.GetOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
        input_["online_evaluation_config_id"] = online_evaluation_config_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
        ] = None,
        rule: Optional["aws_sdk_bedrock_agentcore_control.types.rule.Rule"] = None,
        data_source_config: Optional[
            "aws_sdk_bedrock_agentcore_control.types.data_source_config.DataSourceConfig"
        ] = None,
        evaluators: Optional[
            "aws_sdk_bedrock_agentcore_control.types.evaluator_list.EvaluatorList"
        ] = None,
        evaluation_execution_role_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        execution_status: Optional[
            "aws_sdk_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_online_evaluation_config_response.UpdateOnlineEvaluationConfigResponse":
        r"""<p> Updates an online evaluation configuration's settings, including rules, data sources, evaluators, and execution status. Changes take effect immediately for ongoing evaluations. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            online_evaluation_config_id: <p> The unique identifier of the online evaluation configuration to update. </p>
            description: <p> The updated description of the online evaluation configuration. </p>
            rule: <p> The updated evaluation rule containing sampling configuration, filters, and session settings. </p>
            data_source_config: <p> The updated data source configuration specifying CloudWatch log groups and service names to monitor. </p>
            evaluators: <p> The updated list of evaluators to apply during online evaluation. </p>
            evaluation_execution_role_arn: <p> The updated Amazon Resource Name (ARN) of the IAM role used for evaluation execution. </p>
            execution_status: <p> The updated execution status to enable or disable the online evaluation. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_online_evaluation_config_request.UpdateOnlineEvaluationConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_online_evaluation_config_response.UpdateOnlineEvaluationConfigResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_online_evaluation_config

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_online_evaluation_config.async_update_online_evaluation_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_online_evaluation_config_request.UpdateOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["online_evaluation_config_id"] = online_evaluation_config_id
        if description is not None:
            input_["description"] = description
        if rule is not None:
            input_["rule"] = rule
        if data_source_config is not None:
            input_["data_source_config"] = data_source_config
        if evaluators is not None:
            input_["evaluators"] = evaluators
        if evaluation_execution_role_arn is not None:
            input_["evaluation_execution_role_arn"] = evaluation_execution_role_arn
        if execution_status is not None:
            input_["execution_status"] = execution_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        online_evaluation_config_id: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_online_evaluation_config_response.DeleteOnlineEvaluationConfigResponse":
        """<p> Deletes an online evaluation configuration and stops any ongoing evaluation processes associated with it. </p>

        Args:
            online_evaluation_config_id: <p> The unique identifier of the online evaluation configuration to delete. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_online_evaluation_config_request.DeleteOnlineEvaluationConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_online_evaluation_config_response.DeleteOnlineEvaluationConfigResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_online_evaluation_config

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_online_evaluation_config.async_delete_online_evaluation_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_online_evaluation_config_request.DeleteOnlineEvaluationConfigRequest = {}  # type: ignore[typeddict-item]
        input_["online_evaluation_config_id"] = online_evaluation_config_id

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
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_online_evaluation_configs_response.ListOnlineEvaluationConfigsResponse":
        """<p> Lists all online evaluation configurations in the account, providing summary information about each configuration's status and settings. </p>

        Args:
            next_token: <p> The pagination token from a previous request to retrieve the next page of results. </p>
            max_results: <p> The maximum number of online evaluation configurations to return in a single response. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_online_evaluation_configs_request.ListOnlineEvaluationConfigsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_online_evaluation_configs_response.ListOnlineEvaluationConfigsResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_online_evaluation_configs

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_online_evaluation_configs.async_list_online_evaluation_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_online_evaluation_configs_request.ListOnlineEvaluationConfigsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
