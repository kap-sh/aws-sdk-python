from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import ensure_async_iterator
from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import ensure_sync_iterator
from aws_sdk_bedrock_agentcore._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore._auth._signers
import aws_sdk_bedrock_agentcore._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import BedrockAgentCoreClient, BedrockAgentCoreClientConfig
    from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import AsyncBedrockAgentCoreClient, AsyncBedrockAgentCoreClientConfig
    import aws_sdk_bedrock_agentcore.types.ab_test_description
    import aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config
    import aws_sdk_bedrock_agentcore.types.ab_test_execution_status
    import aws_sdk_bedrock_agentcore.types.ab_test_id
    import aws_sdk_bedrock_agentcore.types.ab_test_name
    import aws_sdk_bedrock_agentcore.types.ab_test_summary
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_description
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_id
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_name
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_summary
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.create_ab_test_request
    import aws_sdk_bedrock_agentcore.types.create_ab_test_response
    import aws_sdk_bedrock_agentcore.types.data_source_config
    import aws_sdk_bedrock_agentcore.types.delete_ab_test_request
    import aws_sdk_bedrock_agentcore.types.delete_ab_test_response
    import aws_sdk_bedrock_agentcore.types.delete_batch_evaluation_request
    import aws_sdk_bedrock_agentcore.types.delete_batch_evaluation_response
    import aws_sdk_bedrock_agentcore.types.delete_recommendation_request
    import aws_sdk_bedrock_agentcore.types.delete_recommendation_response
    import aws_sdk_bedrock_agentcore.types.evaluate_request
    import aws_sdk_bedrock_agentcore.types.evaluate_response
    import aws_sdk_bedrock_agentcore.types.evaluation_input
    import aws_sdk_bedrock_agentcore.types.evaluation_metadata
    import aws_sdk_bedrock_agentcore.types.evaluation_reference_inputs
    import aws_sdk_bedrock_agentcore.types.evaluation_target
    import aws_sdk_bedrock_agentcore.types.evaluator_id
    import aws_sdk_bedrock_agentcore.types.evaluator_list
    import aws_sdk_bedrock_agentcore.types.gateway_arn
    import aws_sdk_bedrock_agentcore.types.gateway_filter
    import aws_sdk_bedrock_agentcore.types.get_ab_test_request
    import aws_sdk_bedrock_agentcore.types.get_ab_test_response
    import aws_sdk_bedrock_agentcore.types.get_batch_evaluation_request
    import aws_sdk_bedrock_agentcore.types.get_batch_evaluation_response
    import aws_sdk_bedrock_agentcore.types.get_recommendation_request
    import aws_sdk_bedrock_agentcore.types.get_recommendation_response
    import aws_sdk_bedrock_agentcore.types.list_ab_tests_request
    import aws_sdk_bedrock_agentcore.types.list_ab_tests_response
    import aws_sdk_bedrock_agentcore.types.list_batch_evaluations_request
    import aws_sdk_bedrock_agentcore.types.list_batch_evaluations_response
    import aws_sdk_bedrock_agentcore.types.list_recommendations_request
    import aws_sdk_bedrock_agentcore.types.list_recommendations_response
    import aws_sdk_bedrock_agentcore.types.next_token
    import aws_sdk_bedrock_agentcore.types.recommendation_config
    import aws_sdk_bedrock_agentcore.types.recommendation_description
    import aws_sdk_bedrock_agentcore.types.recommendation_id
    import aws_sdk_bedrock_agentcore.types.recommendation_name
    import aws_sdk_bedrock_agentcore.types.recommendation_status
    import aws_sdk_bedrock_agentcore.types.recommendation_summary
    import aws_sdk_bedrock_agentcore.types.recommendation_type
    import aws_sdk_bedrock_agentcore.types.role_arn
    import aws_sdk_bedrock_agentcore.types.start_batch_evaluation_request
    import aws_sdk_bedrock_agentcore.types.start_batch_evaluation_response
    import aws_sdk_bedrock_agentcore.types.start_recommendation_request
    import aws_sdk_bedrock_agentcore.types.start_recommendation_response
    import aws_sdk_bedrock_agentcore.types.stop_batch_evaluation_request
    import aws_sdk_bedrock_agentcore.types.stop_batch_evaluation_response
    import aws_sdk_bedrock_agentcore.types.update_ab_test_request
    import aws_sdk_bedrock_agentcore.types.update_ab_test_response
    import aws_sdk_bedrock_agentcore.types.variant_list

class EvaluationResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service
    def create_ab_test(self, name: "aws_sdk_bedrock_agentcore.types.ab_test_name.ABTestName", gateway_arn: "aws_sdk_bedrock_agentcore.types.gateway_arn.GatewayArn", variants: "aws_sdk_bedrock_agentcore.types.variant_list.VariantList", evaluation_config: "aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig", role_arn: "aws_sdk_bedrock_agentcore.types.role_arn.RoleArn", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore.types.ab_test_description.ABTestDescription"] = None, gateway_filter: Optional["aws_sdk_bedrock_agentcore.types.gateway_filter.GatewayFilter"] = None, enable_on_create: Optional[bool] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.create_ab_test_response.CreateABTestResponse":
        """<p>Creates an A/B test for comparing agent configurations. A/B tests split traffic between a control variant and a treatment variant through a gateway, then evaluate performance using online evaluation configurations to determine which variant performs better.</p>

        Args:
            name: <p>The name of the A/B test. Must be unique within your account.</p>
            description: <p>The description of the A/B test.</p>
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to use for traffic splitting.</p>
            variants: <p>The list of variants for the A/B test. Must contain exactly two variants: a control (C) and a treatment (T1), each with a configuration bundle or target reference and a traffic weight.</p>
            gateway_filter: <p>Optional filter to restrict which gateway target paths are included in the A/B test.</p>
            evaluation_config: <p>The evaluation configuration specifying which online evaluation configurations to use for measuring variant performance.</p>
            role_arn: <p>The IAM role ARN that grants permissions for the A/B test to access gateway and evaluation resources.</p>
            enable_on_create: <p>Whether to enable the A/B test immediately upon creation. If true, traffic splitting begins automatically.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.create_ab_test_request.CreateABTestRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.create_ab_test_response.CreateABTestResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_ab_test
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_ab_test.create_ab_test(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.create_ab_test_request.CreateABTestRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["gateway_arn"] = gateway_arn
        input["variants"] = variants
        if gateway_filter is not None:
            input["gateway_filter"] = gateway_filter
        input["evaluation_config"] = evaluation_config
        input["role_arn"] = role_arn
        if enable_on_create is not None:
            input["enable_on_create"] = enable_on_create
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete_ab_test(self, ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.delete_ab_test_response.DeleteABTestResponse":
        """<p>Deletes an A/B test and its associated gateway rules.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.delete_ab_test_request.DeleteABTestRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.delete_ab_test_response.DeleteABTestResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_ab_test
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_ab_test.delete_ab_test(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.delete_ab_test_request.DeleteABTestRequest = {}  # type: ignore[typeddict-item]
        input["ab_test_id"] = ab_test_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete_batch_evaluation(self, batch_evaluation_id: "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.delete_batch_evaluation_response.DeleteBatchEvaluationResponse":
        """<p>Deletes a batch evaluation and its associated results.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.delete_batch_evaluation_request.DeleteBatchEvaluationRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.delete_batch_evaluation_response.DeleteBatchEvaluationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_batch_evaluation
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_batch_evaluation.delete_batch_evaluation(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.delete_batch_evaluation_request.DeleteBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
        input["batch_evaluation_id"] = batch_evaluation_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete_recommendation(self, recommendation_id: "aws_sdk_bedrock_agentcore.types.recommendation_id.RecommendationId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.delete_recommendation_response.DeleteRecommendationResponse":
        """<p>Deletes a recommendation and its associated results.</p>

        Args:
            recommendation_id: <p>The unique identifier of the recommendation to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.delete_recommendation_request.DeleteRecommendationRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.delete_recommendation_response.DeleteRecommendationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_recommendation
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_recommendation.delete_recommendation(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.delete_recommendation_request.DeleteRecommendationRequest = {}  # type: ignore[typeddict-item]
        input["recommendation_id"] = recommendation_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def evaluate(self, evaluator_id: "aws_sdk_bedrock_agentcore.types.evaluator_id.EvaluatorId", evaluation_input: "aws_sdk_bedrock_agentcore.types.evaluation_input.EvaluationInput", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, evaluation_target: Optional["aws_sdk_bedrock_agentcore.types.evaluation_target.EvaluationTarget"] = None, evaluation_reference_inputs: Optional["aws_sdk_bedrock_agentcore.types.evaluation_reference_inputs.EvaluationReferenceInputs"] = None) -> "aws_sdk_bedrock_agentcore.types.evaluate_response.EvaluateResponse":
        """<p> Performs on-demand evaluation of agent traces using a specified evaluator. This synchronous API accepts traces in OpenTelemetry format and returns immediate scoring results with detailed explanations.</p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to use for scoring. Can be a built-in evaluator (e.g., <code>Builtin.Helpfulness</code>, <code>Builtin.Correctness</code>) or a custom evaluator Id created through the control plane API. </p>
            evaluation_input: <p> The input data containing agent session spans to be evaluated. Includes a list of spans in OpenTelemetry format from supported frameworks like Strands (AgentCore Runtime) or LangGraph with OpenInference instrumentation. </p>
            evaluation_target: <p> The specific trace or span IDs to evaluate within the provided input. Allows targeting evaluation at different levels: individual tool calls, single request-response interactions (traces), or entire conversation sessions. </p>
            evaluation_reference_inputs: <p> Ground truth data to compare against agent responses during evaluation. Allows to provide expected responses, assertions, and expected tool trajectories at different evaluation levels. Session-level reference inputs apply to the entire conversation, while trace-level reference inputs target specific request-response interactions identified by trace ID. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.evaluate_request.EvaluateRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.evaluate_response.EvaluateResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.evaluate
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.evaluate.evaluate(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.evaluate_request.EvaluateRequest = {}  # type: ignore[typeddict-item]
        input["evaluator_id"] = evaluator_id
        input["evaluation_input"] = evaluation_input
        if evaluation_target is not None:
            input["evaluation_target"] = evaluation_target
        if evaluation_reference_inputs is not None:
            input["evaluation_reference_inputs"] = evaluation_reference_inputs

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_ab_test(self, ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_ab_test_response.GetABTestResponse":
        """<p>Retrieves detailed information about an A/B test, including its configuration, status, and statistical results.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.get_ab_test_request.GetABTestRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.get_ab_test_response.GetABTestResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_ab_test
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_ab_test.get_ab_test(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_ab_test_request.GetABTestRequest = {}  # type: ignore[typeddict-item]
        input["ab_test_id"] = ab_test_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_batch_evaluation(self, batch_evaluation_id: "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse":
        """<p>Retrieves detailed information about a batch evaluation, including its status, configuration, results, and any error details.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.get_batch_evaluation_request.GetBatchEvaluationRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_batch_evaluation
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_batch_evaluation.get_batch_evaluation(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_batch_evaluation_request.GetBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
        input["batch_evaluation_id"] = batch_evaluation_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_recommendation(self, recommendation_id: "aws_sdk_bedrock_agentcore.types.recommendation_id.RecommendationId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse":
        """<p>Retrieves detailed information about a recommendation, including its configuration, status, and results.</p>

        Args:
            recommendation_id: <p>The unique identifier of the recommendation to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.get_recommendation_request.GetRecommendationRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_recommendation
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_recommendation.get_recommendation(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_recommendation_request.GetRecommendationRequest = {}  # type: ignore[typeddict-item]
        input["recommendation_id"] = recommendation_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_ab_tests(self, *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, max_results: Optional[int] = None, next_token: Optional[str] = None) -> "aws_sdk_bedrock_agentcore.types.list_ab_tests_response.ListABTestsResponse":
        """<p>Lists all A/B tests in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_ab_tests_request.ListABTestsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_ab_tests_response.ListABTestsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_ab_tests
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_ab_tests.list_ab_tests(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_ab_tests_request.ListABTestsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_batch_evaluations(self, *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, max_results: Optional[int] = None, next_token: Optional[str] = None) -> "aws_sdk_bedrock_agentcore.types.list_batch_evaluations_response.ListBatchEvaluationsResponse":
        """<p>Lists all batch evaluations in the account, providing summary information about each evaluation's status and configuration.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_batch_evaluations_request.ListBatchEvaluationsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_batch_evaluations_response.ListBatchEvaluationsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_batch_evaluations
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_batch_evaluations.list_batch_evaluations(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_batch_evaluations_request.ListBatchEvaluationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_recommendations(self, *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, max_results: Optional[int] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.next_token.NextToken"] = None, status_filter: Optional["aws_sdk_bedrock_agentcore.types.recommendation_status.RecommendationStatus"] = None) -> "aws_sdk_bedrock_agentcore.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>Lists all recommendations in the account, with optional filtering by status.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            status_filter: <p>Optional filter to return only recommendations with the specified status.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_recommendations_request.ListRecommendationsRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_recommendations_response.ListRecommendationsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_recommendations
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_recommendations.list_recommendations(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_recommendations_request.ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if status_filter is not None:
            input["status_filter"] = status_filter

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def start_batch_evaluation(self, batch_evaluation_name: "aws_sdk_bedrock_agentcore.types.batch_evaluation_name.BatchEvaluationName", data_source_config: "aws_sdk_bedrock_agentcore.types.data_source_config.DataSourceConfig", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, evaluators: Optional["aws_sdk_bedrock_agentcore.types.evaluator_list.EvaluatorList"] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None, evaluation_metadata: Optional["aws_sdk_bedrock_agentcore.types.evaluation_metadata.EvaluationMetadata"] = None, description: Optional["aws_sdk_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"] = None) -> "aws_sdk_bedrock_agentcore.types.start_batch_evaluation_response.StartBatchEvaluationResponse":
        """<p>Starts a batch evaluation job that evaluates agent performance across multiple sessions. Batch evaluations pull agent traces from CloudWatch Logs or an existing online evaluation configuration and run specified evaluators and insights against them.</p>

        Args:
            batch_evaluation_name: <p>The name of the batch evaluation. Must be unique within your account.</p>
            evaluators: <p>The list of evaluators to apply during the batch evaluation. Can include both built-in evaluators and custom evaluators. Maximum of 10 evaluators.</p>
            data_source_config: <p>The data source configuration that specifies where to pull agent session traces from for evaluation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            evaluation_metadata: <p>Optional metadata for the evaluation, including session-specific ground truth data and test scenario identifiers.</p>
            description: <p>The description of the batch evaluation.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.start_batch_evaluation_request.StartBatchEvaluationRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.start_batch_evaluation_response.StartBatchEvaluationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_batch_evaluation
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_batch_evaluation.start_batch_evaluation(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.start_batch_evaluation_request.StartBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
        input["batch_evaluation_name"] = batch_evaluation_name
        if evaluators is not None:
            input["evaluators"] = evaluators
        input["data_source_config"] = data_source_config
        if client_token is not None:
            input["client_token"] = client_token
        if evaluation_metadata is not None:
            input["evaluation_metadata"] = evaluation_metadata
        if description is not None:
            input["description"] = description

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def start_recommendation(self, name: "aws_sdk_bedrock_agentcore.types.recommendation_name.RecommendationName", type: "aws_sdk_bedrock_agentcore.types.recommendation_type.RecommendationType", recommendation_config: "aws_sdk_bedrock_agentcore.types.recommendation_config.RecommendationConfig", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore.types.recommendation_description.RecommendationDescription"] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse":
        """<p>Starts a recommendation job that analyzes agent traces and generates optimization suggestions for system prompts or tool descriptions to improve agent performance.</p>

        Args:
            name: <p>The name of the recommendation. Must be unique within your account.</p>
            description: <p>The description of the recommendation.</p>
            type: <p>The type of recommendation to generate. Valid values are <code>SYSTEM_PROMPT_RECOMMENDATION</code> for system prompt optimization or <code>TOOL_DESCRIPTION_RECOMMENDATION</code> for tool description optimization.</p>
            recommendation_config: <p>The configuration for the recommendation, including the input to optimize, agent traces to analyze, and evaluation settings.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_recommendation
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_recommendation.start_recommendation(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["type"] = type
        input["recommendation_config"] = recommendation_config
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def stop_batch_evaluation(self, batch_evaluation_id: "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.stop_batch_evaluation_response.StopBatchEvaluationResponse":
        """<p>Stops a running batch evaluation. Sessions that have already been evaluated retain their results.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to stop.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.stop_batch_evaluation_request.StopBatchEvaluationRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.stop_batch_evaluation_response.StopBatchEvaluationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_batch_evaluation
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_batch_evaluation.stop_batch_evaluation(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.stop_batch_evaluation_request.StopBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
        input["batch_evaluation_id"] = batch_evaluation_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update_ab_test(self, ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None, name: Optional["aws_sdk_bedrock_agentcore.types.ab_test_name.ABTestName"] = None, description: Optional["aws_sdk_bedrock_agentcore.types.ab_test_description.ABTestDescription"] = None, variants: Optional["aws_sdk_bedrock_agentcore.types.variant_list.VariantList"] = None, gateway_filter: Optional["aws_sdk_bedrock_agentcore.types.gateway_filter.GatewayFilter"] = None, evaluation_config: Optional["aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig"] = None, role_arn: Optional["aws_sdk_bedrock_agentcore.types.role_arn.RoleArn"] = None, execution_status: Optional["aws_sdk_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"] = None) -> "aws_sdk_bedrock_agentcore.types.update_ab_test_response.UpdateABTestResponse":
        """<p>Updates an A/B test's configuration, including variants, traffic allocation, evaluation settings, or execution status.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            name: <p>The updated name of the A/B test.</p>
            description: <p>The updated description of the A/B test.</p>
            variants: <p>The updated list of variants.</p>
            gateway_filter: <p>The updated gateway filter.</p>
            evaluation_config: <p>The updated evaluation configuration.</p>
            role_arn: <p>The updated IAM role ARN.</p>
            execution_status: <p>The updated execution status to enable or disable the A/B test.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.update_ab_test_request.UpdateABTestRequest]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.update_ab_test_response.UpdateABTestResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_ab_test
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_ab_test.update_ab_test(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.update_ab_test_request.UpdateABTestRequest = {}  # type: ignore[typeddict-item]
        input["ab_test_id"] = ab_test_id
        if client_token is not None:
            input["client_token"] = client_token
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if variants is not None:
            input["variants"] = variants
        if gateway_filter is not None:
            input["gateway_filter"] = gateway_filter
        if evaluation_config is not None:
            input["evaluation_config"] = evaluation_config
        if role_arn is not None:
            input["role_arn"] = role_arn
        if execution_status is not None:
            input["execution_status"] = execution_status

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncEvaluationResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service
    async def create_ab_test(self, name: "aws_sdk_bedrock_agentcore.types.ab_test_name.ABTestName", gateway_arn: "aws_sdk_bedrock_agentcore.types.gateway_arn.GatewayArn", variants: "aws_sdk_bedrock_agentcore.types.variant_list.VariantList", evaluation_config: "aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig", role_arn: "aws_sdk_bedrock_agentcore.types.role_arn.RoleArn", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore.types.ab_test_description.ABTestDescription"] = None, gateway_filter: Optional["aws_sdk_bedrock_agentcore.types.gateway_filter.GatewayFilter"] = None, enable_on_create: Optional[bool] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.create_ab_test_response.CreateABTestResponse":
        """<p>Creates an A/B test for comparing agent configurations. A/B tests split traffic between a control variant and a treatment variant through a gateway, then evaluate performance using online evaluation configurations to determine which variant performs better.</p>

        Args:
            name: <p>The name of the A/B test. Must be unique within your account.</p>
            description: <p>The description of the A/B test.</p>
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to use for traffic splitting.</p>
            variants: <p>The list of variants for the A/B test. Must contain exactly two variants: a control (C) and a treatment (T1), each with a configuration bundle or target reference and a traffic weight.</p>
            gateway_filter: <p>Optional filter to restrict which gateway target paths are included in the A/B test.</p>
            evaluation_config: <p>The evaluation configuration specifying which online evaluation configurations to use for measuring variant performance.</p>
            role_arn: <p>The IAM role ARN that grants permissions for the A/B test to access gateway and evaluation resources.</p>
            enable_on_create: <p>Whether to enable the A/B test immediately upon creation. If true, traffic splitting begins automatically.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.create_ab_test_request.CreateABTestRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.create_ab_test_response.CreateABTestResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_ab_test
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_ab_test.async_create_ab_test(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.create_ab_test_request.CreateABTestRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["gateway_arn"] = gateway_arn
        input["variants"] = variants
        if gateway_filter is not None:
            input["gateway_filter"] = gateway_filter
        input["evaluation_config"] = evaluation_config
        input["role_arn"] = role_arn
        if enable_on_create is not None:
            input["enable_on_create"] = enable_on_create
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete_ab_test(self, ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.delete_ab_test_response.DeleteABTestResponse":
        """<p>Deletes an A/B test and its associated gateway rules.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.delete_ab_test_request.DeleteABTestRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.delete_ab_test_response.DeleteABTestResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_ab_test
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_ab_test.async_delete_ab_test(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.delete_ab_test_request.DeleteABTestRequest = {}  # type: ignore[typeddict-item]
        input["ab_test_id"] = ab_test_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete_batch_evaluation(self, batch_evaluation_id: "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.delete_batch_evaluation_response.DeleteBatchEvaluationResponse":
        """<p>Deletes a batch evaluation and its associated results.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.delete_batch_evaluation_request.DeleteBatchEvaluationRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.delete_batch_evaluation_response.DeleteBatchEvaluationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_batch_evaluation
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_batch_evaluation.async_delete_batch_evaluation(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.delete_batch_evaluation_request.DeleteBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
        input["batch_evaluation_id"] = batch_evaluation_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete_recommendation(self, recommendation_id: "aws_sdk_bedrock_agentcore.types.recommendation_id.RecommendationId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.delete_recommendation_response.DeleteRecommendationResponse":
        """<p>Deletes a recommendation and its associated results.</p>

        Args:
            recommendation_id: <p>The unique identifier of the recommendation to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.delete_recommendation_request.DeleteRecommendationRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.delete_recommendation_response.DeleteRecommendationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_recommendation
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_recommendation.async_delete_recommendation(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.delete_recommendation_request.DeleteRecommendationRequest = {}  # type: ignore[typeddict-item]
        input["recommendation_id"] = recommendation_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def evaluate(self, evaluator_id: "aws_sdk_bedrock_agentcore.types.evaluator_id.EvaluatorId", evaluation_input: "aws_sdk_bedrock_agentcore.types.evaluation_input.EvaluationInput", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, evaluation_target: Optional["aws_sdk_bedrock_agentcore.types.evaluation_target.EvaluationTarget"] = None, evaluation_reference_inputs: Optional["aws_sdk_bedrock_agentcore.types.evaluation_reference_inputs.EvaluationReferenceInputs"] = None) -> "aws_sdk_bedrock_agentcore.types.evaluate_response.EvaluateResponse":
        """<p> Performs on-demand evaluation of agent traces using a specified evaluator. This synchronous API accepts traces in OpenTelemetry format and returns immediate scoring results with detailed explanations.</p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to use for scoring. Can be a built-in evaluator (e.g., <code>Builtin.Helpfulness</code>, <code>Builtin.Correctness</code>) or a custom evaluator Id created through the control plane API. </p>
            evaluation_input: <p> The input data containing agent session spans to be evaluated. Includes a list of spans in OpenTelemetry format from supported frameworks like Strands (AgentCore Runtime) or LangGraph with OpenInference instrumentation. </p>
            evaluation_target: <p> The specific trace or span IDs to evaluate within the provided input. Allows targeting evaluation at different levels: individual tool calls, single request-response interactions (traces), or entire conversation sessions. </p>
            evaluation_reference_inputs: <p> Ground truth data to compare against agent responses during evaluation. Allows to provide expected responses, assertions, and expected tool trajectories at different evaluation levels. Session-level reference inputs apply to the entire conversation, while trace-level reference inputs target specific request-response interactions identified by trace ID. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.evaluate_request.EvaluateRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.evaluate_response.EvaluateResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.evaluate
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.evaluate.async_evaluate(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.evaluate_request.EvaluateRequest = {}  # type: ignore[typeddict-item]
        input["evaluator_id"] = evaluator_id
        input["evaluation_input"] = evaluation_input
        if evaluation_target is not None:
            input["evaluation_target"] = evaluation_target
        if evaluation_reference_inputs is not None:
            input["evaluation_reference_inputs"] = evaluation_reference_inputs

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_ab_test(self, ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_ab_test_response.GetABTestResponse":
        """<p>Retrieves detailed information about an A/B test, including its configuration, status, and statistical results.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_ab_test_request.GetABTestRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.get_ab_test_response.GetABTestResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_ab_test
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_ab_test.async_get_ab_test(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_ab_test_request.GetABTestRequest = {}  # type: ignore[typeddict-item]
        input["ab_test_id"] = ab_test_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_batch_evaluation(self, batch_evaluation_id: "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse":
        """<p>Retrieves detailed information about a batch evaluation, including its status, configuration, results, and any error details.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_batch_evaluation_request.GetBatchEvaluationRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_batch_evaluation
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_batch_evaluation.async_get_batch_evaluation(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_batch_evaluation_request.GetBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
        input["batch_evaluation_id"] = batch_evaluation_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_recommendation(self, recommendation_id: "aws_sdk_bedrock_agentcore.types.recommendation_id.RecommendationId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse":
        """<p>Retrieves detailed information about a recommendation, including its configuration, status, and results.</p>

        Args:
            recommendation_id: <p>The unique identifier of the recommendation to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_recommendation_request.GetRecommendationRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_recommendation
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_recommendation.async_get_recommendation(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_recommendation_request.GetRecommendationRequest = {}  # type: ignore[typeddict-item]
        input["recommendation_id"] = recommendation_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_ab_tests(self, *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, max_results: Optional[int] = None, next_token: Optional[str] = None) -> "aws_sdk_bedrock_agentcore.types.list_ab_tests_response.ListABTestsResponse":
        """<p>Lists all A/B tests in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_ab_tests_request.ListABTestsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_ab_tests_response.ListABTestsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_ab_tests
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_ab_tests.async_list_ab_tests(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_ab_tests_request.ListABTestsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_batch_evaluations(self, *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, max_results: Optional[int] = None, next_token: Optional[str] = None) -> "aws_sdk_bedrock_agentcore.types.list_batch_evaluations_response.ListBatchEvaluationsResponse":
        """<p>Lists all batch evaluations in the account, providing summary information about each evaluation's status and configuration.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_batch_evaluations_request.ListBatchEvaluationsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_batch_evaluations_response.ListBatchEvaluationsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_batch_evaluations
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_batch_evaluations.async_list_batch_evaluations(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_batch_evaluations_request.ListBatchEvaluationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_recommendations(self, *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, max_results: Optional[int] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.next_token.NextToken"] = None, status_filter: Optional["aws_sdk_bedrock_agentcore.types.recommendation_status.RecommendationStatus"] = None) -> "aws_sdk_bedrock_agentcore.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>Lists all recommendations in the account, with optional filtering by status.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            status_filter: <p>Optional filter to return only recommendations with the specified status.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_recommendations_request.ListRecommendationsRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_recommendations_response.ListRecommendationsResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_recommendations
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_recommendations.async_list_recommendations(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_recommendations_request.ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if status_filter is not None:
            input["status_filter"] = status_filter

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def start_batch_evaluation(self, batch_evaluation_name: "aws_sdk_bedrock_agentcore.types.batch_evaluation_name.BatchEvaluationName", data_source_config: "aws_sdk_bedrock_agentcore.types.data_source_config.DataSourceConfig", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, evaluators: Optional["aws_sdk_bedrock_agentcore.types.evaluator_list.EvaluatorList"] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None, evaluation_metadata: Optional["aws_sdk_bedrock_agentcore.types.evaluation_metadata.EvaluationMetadata"] = None, description: Optional["aws_sdk_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"] = None) -> "aws_sdk_bedrock_agentcore.types.start_batch_evaluation_response.StartBatchEvaluationResponse":
        """<p>Starts a batch evaluation job that evaluates agent performance across multiple sessions. Batch evaluations pull agent traces from CloudWatch Logs or an existing online evaluation configuration and run specified evaluators and insights against them.</p>

        Args:
            batch_evaluation_name: <p>The name of the batch evaluation. Must be unique within your account.</p>
            evaluators: <p>The list of evaluators to apply during the batch evaluation. Can include both built-in evaluators and custom evaluators. Maximum of 10 evaluators.</p>
            data_source_config: <p>The data source configuration that specifies where to pull agent session traces from for evaluation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            evaluation_metadata: <p>Optional metadata for the evaluation, including session-specific ground truth data and test scenario identifiers.</p>
            description: <p>The description of the batch evaluation.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.start_batch_evaluation_request.StartBatchEvaluationRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.start_batch_evaluation_response.StartBatchEvaluationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_batch_evaluation
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_batch_evaluation.async_start_batch_evaluation(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.start_batch_evaluation_request.StartBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
        input["batch_evaluation_name"] = batch_evaluation_name
        if evaluators is not None:
            input["evaluators"] = evaluators
        input["data_source_config"] = data_source_config
        if client_token is not None:
            input["client_token"] = client_token
        if evaluation_metadata is not None:
            input["evaluation_metadata"] = evaluation_metadata
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def start_recommendation(self, name: "aws_sdk_bedrock_agentcore.types.recommendation_name.RecommendationName", type: "aws_sdk_bedrock_agentcore.types.recommendation_type.RecommendationType", recommendation_config: "aws_sdk_bedrock_agentcore.types.recommendation_config.RecommendationConfig", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, description: Optional["aws_sdk_bedrock_agentcore.types.recommendation_description.RecommendationDescription"] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None) -> "aws_sdk_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse":
        """<p>Starts a recommendation job that analyzes agent traces and generates optimization suggestions for system prompts or tool descriptions to improve agent performance.</p>

        Args:
            name: <p>The name of the recommendation. Must be unique within your account.</p>
            description: <p>The description of the recommendation.</p>
            type: <p>The type of recommendation to generate. Valid values are <code>SYSTEM_PROMPT_RECOMMENDATION</code> for system prompt optimization or <code>TOOL_DESCRIPTION_RECOMMENDATION</code> for tool description optimization.</p>
            recommendation_config: <p>The configuration for the recommendation, including the input to optimize, agent traces to analyze, and evaluation settings.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_recommendation
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_recommendation.async_start_recommendation(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["type"] = type
        input["recommendation_config"] = recommendation_config
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def stop_batch_evaluation(self, batch_evaluation_id: "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.stop_batch_evaluation_response.StopBatchEvaluationResponse":
        """<p>Stops a running batch evaluation. Sessions that have already been evaluated retain their results.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to stop.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.stop_batch_evaluation_request.StopBatchEvaluationRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.stop_batch_evaluation_response.StopBatchEvaluationResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_batch_evaluation
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_batch_evaluation.async_stop_batch_evaluation(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.stop_batch_evaluation_request.StopBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
        input["batch_evaluation_id"] = batch_evaluation_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update_ab_test(self, ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, client_token: Optional["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"] = None, name: Optional["aws_sdk_bedrock_agentcore.types.ab_test_name.ABTestName"] = None, description: Optional["aws_sdk_bedrock_agentcore.types.ab_test_description.ABTestDescription"] = None, variants: Optional["aws_sdk_bedrock_agentcore.types.variant_list.VariantList"] = None, gateway_filter: Optional["aws_sdk_bedrock_agentcore.types.gateway_filter.GatewayFilter"] = None, evaluation_config: Optional["aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig"] = None, role_arn: Optional["aws_sdk_bedrock_agentcore.types.role_arn.RoleArn"] = None, execution_status: Optional["aws_sdk_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"] = None) -> "aws_sdk_bedrock_agentcore.types.update_ab_test_response.UpdateABTestResponse":
        """<p>Updates an A/B test's configuration, including variants, traffic allocation, evaluation settings, or execution status.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            name: <p>The updated name of the A/B test.</p>
            description: <p>The updated description of the A/B test.</p>
            variants: <p>The updated list of variants.</p>
            gateway_filter: <p>The updated gateway filter.</p>
            evaluation_config: <p>The updated evaluation configuration.</p>
            role_arn: <p>The updated IAM role ARN.</p>
            execution_status: <p>The updated execution status to enable or disable the A/B test.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.update_ab_test_request.UpdateABTestRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.update_ab_test_response.UpdateABTestResponse"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_ab_test
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_ab_test.async_update_ab_test(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.update_ab_test_request.UpdateABTestRequest = {}  # type: ignore[typeddict-item]
        input["ab_test_id"] = ab_test_id
        if client_token is not None:
            input["client_token"] = client_token
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if variants is not None:
            input["variants"] = variants
        if gateway_filter is not None:
            input["gateway_filter"] = gateway_filter
        if evaluation_config is not None:
            input["evaluation_config"] = evaluation_config
        if role_arn is not None:
            input["role_arn"] = role_arn
        if execution_status is not None:
            input["execution_status"] = execution_status

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output