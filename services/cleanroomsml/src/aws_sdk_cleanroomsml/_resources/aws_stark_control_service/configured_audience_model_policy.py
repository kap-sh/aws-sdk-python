from typing import Optional, TYPE_CHECKING
from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import ensure_async_iterator
from aws_sdk_cleanroomsml._services.clean_rooms_ml import ensure_sync_iterator
from aws_sdk_cleanroomsml._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_cleanroomsml._auth._signers
import aws_sdk_cleanroomsml._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import CleanRoomsMLClient, CleanRoomsMLClientConfig
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import AsyncCleanRoomsMLClient, AsyncCleanRoomsMLClientConfig
    import aws_sdk_cleanroomsml.types.configured_audience_model_arn
    import aws_sdk_cleanroomsml.types.delete_configured_audience_model_policy_request
    import aws_sdk_cleanroomsml.types.get_configured_audience_model_policy_request
    import aws_sdk_cleanroomsml.types.get_configured_audience_model_policy_response
    import aws_sdk_cleanroomsml.types.hash
    import aws_sdk_cleanroomsml.types.policy_existence_condition
    import aws_sdk_cleanroomsml.types.put_configured_audience_model_policy_request
    import aws_sdk_cleanroomsml.types.put_configured_audience_model_policy_response
    import aws_sdk_cleanroomsml.types.resource_policy

class ConfiguredAudienceModelPolicy:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service
    def put(self, configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn", configured_audience_model_policy: "aws_sdk_cleanroomsml.types.resource_policy.ResourcePolicy", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, previous_policy_hash: Optional["aws_sdk_cleanroomsml.types.hash.Hash"] = None, policy_existence_condition: Optional["aws_sdk_cleanroomsml.types.policy_existence_condition.PolicyExistenceCondition"] = None) -> "aws_sdk_cleanroomsml.types.put_configured_audience_model_policy_response.PutConfiguredAudienceModelPolicyResponse":
        """<p>Create or update the resource policy for a configured audience model.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that the resource policy will govern.</p>
            configured_audience_model_policy: <p>The IAM resource policy.</p>
            previous_policy_hash: <p>A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.</p>
            policy_existence_condition: <p>Use this to prevent unexpected concurrent modification of the policy.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.put_configured_audience_model_policy_request.PutConfiguredAudienceModelPolicyRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.put_configured_audience_model_policy_response.PutConfiguredAudienceModelPolicyResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.put_configured_audience_model_policy
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.put_configured_audience_model_policy.put_configured_audience_model_policy(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.put_configured_audience_model_policy_request.PutConfiguredAudienceModelPolicyRequest = {}  # type: ignore[typeddict-item]
        input["configured_audience_model_arn"] = configured_audience_model_arn
        input["configured_audience_model_policy"] = configured_audience_model_policy
        if previous_policy_hash is not None:
            input["previous_policy_hash"] = previous_policy_hash
        if policy_existence_condition is not None:
            input["policy_existence_condition"] = policy_existence_condition

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None) -> "aws_sdk_cleanroomsml.types.get_configured_audience_model_policy_response.GetConfiguredAudienceModelPolicyResponse":
        """<p>Returns information about a configured audience model policy.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.get_configured_audience_model_policy_request.GetConfiguredAudienceModelPolicyRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.get_configured_audience_model_policy_response.GetConfiguredAudienceModelPolicyResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model_policy
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model_policy.get_configured_audience_model_policy(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_configured_audience_model_policy_request.GetConfiguredAudienceModelPolicyRequest = {}  # type: ignore[typeddict-item]
        input["configured_audience_model_arn"] = configured_audience_model_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None) -> None:
        """<p>Deletes the specified configured audience model policy.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model policy that you want to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest]') -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model_policy
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model_policy.delete_configured_audience_model_policy(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest = {}  # type: ignore[typeddict-item]
        input["configured_audience_model_arn"] = configured_audience_model_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncConfiguredAudienceModelPolicy:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service
    async def put(self, configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn", configured_audience_model_policy: "aws_sdk_cleanroomsml.types.resource_policy.ResourcePolicy", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, previous_policy_hash: Optional["aws_sdk_cleanroomsml.types.hash.Hash"] = None, policy_existence_condition: Optional["aws_sdk_cleanroomsml.types.policy_existence_condition.PolicyExistenceCondition"] = None) -> "aws_sdk_cleanroomsml.types.put_configured_audience_model_policy_response.PutConfiguredAudienceModelPolicyResponse":
        """<p>Create or update the resource policy for a configured audience model.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that the resource policy will govern.</p>
            configured_audience_model_policy: <p>The IAM resource policy.</p>
            previous_policy_hash: <p>A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.</p>
            policy_existence_condition: <p>Use this to prevent unexpected concurrent modification of the policy.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.put_configured_audience_model_policy_request.PutConfiguredAudienceModelPolicyRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.put_configured_audience_model_policy_response.PutConfiguredAudienceModelPolicyResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.put_configured_audience_model_policy
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.put_configured_audience_model_policy.async_put_configured_audience_model_policy(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.put_configured_audience_model_policy_request.PutConfiguredAudienceModelPolicyRequest = {}  # type: ignore[typeddict-item]
        input["configured_audience_model_arn"] = configured_audience_model_arn
        input["configured_audience_model_policy"] = configured_audience_model_policy
        if previous_policy_hash is not None:
            input["previous_policy_hash"] = previous_policy_hash
        if policy_existence_condition is not None:
            input["policy_existence_condition"] = policy_existence_condition

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None) -> "aws_sdk_cleanroomsml.types.get_configured_audience_model_policy_response.GetConfiguredAudienceModelPolicyResponse":
        """<p>Returns information about a configured audience model policy.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_configured_audience_model_policy_request.GetConfiguredAudienceModelPolicyRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.get_configured_audience_model_policy_response.GetConfiguredAudienceModelPolicyResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model_policy
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model_policy.async_get_configured_audience_model_policy(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_configured_audience_model_policy_request.GetConfiguredAudienceModelPolicyRequest = {}  # type: ignore[typeddict-item]
        input["configured_audience_model_arn"] = configured_audience_model_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None) -> None:
        """<p>Deletes the specified configured audience model policy.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model policy that you want to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest]') -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model_policy
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model_policy.async_delete_configured_audience_model_policy(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest = {}  # type: ignore[typeddict-item]
        input["configured_audience_model_arn"] = configured_audience_model_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output