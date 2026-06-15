from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_aiops._auth._signers
import aws_sdk_aiops._auth._sigv4
from aws_sdk_aiops._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_aiops.types.delete_investigation_group_policy_output
    import aws_sdk_aiops.types.delete_investigation_group_policy_request
    import aws_sdk_aiops.types.get_investigation_group_policy_request
    import aws_sdk_aiops.types.get_investigation_group_policy_response
    import aws_sdk_aiops.types.investigation_group_identifier
    import aws_sdk_aiops.types.investigation_group_policy_document
    import aws_sdk_aiops.types.put_investigation_group_policy_request
    import aws_sdk_aiops.types.put_investigation_group_policy_response
    from aws_sdk_aiops._services.ai_ops import AIOpsClient, AIOpsClientConfig
    from aws_sdk_aiops._services.async_ai_ops import (
        AsyncAIOpsClient,
        AsyncAIOpsClientConfig,
    )


class InvestigationGroupPolicy:
    def __init__(self, service: AIOpsClient) -> None:
        self._service = service

    def put(
        self,
        identifier: "aws_sdk_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        policy: "aws_sdk_aiops.types.investigation_group_policy_document.InvestigationGroupPolicyDocument",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "aws_sdk_aiops.types.put_investigation_group_policy_response.PutInvestigationGroupPolicyResponse":
        r"""<p>Creates an IAM resource policy and assigns it to the specified investigation group.</p> <p>If you create your investigation group with <code>CreateInvestigationGroup</code> and you want to enable CloudWatch alarms to create investigations and add events to investigations, you must use this operation to create a policy similar to this example.</p> <p> <code> { \"Version\": \"2008-10-17\", \"Statement\": [ { \"Effect\": \"Allow\", \"Principal\": { \"Service\": \"aiops.alarms.cloudwatch.amazonaws.com\" }, \"Action\": [ \"aiops:CreateInvestigation\", \"aiops:CreateInvestigationEvent\" ], \"Resource\": \"*\", \"Condition\": { \"StringEquals\": { \"aws:SourceAccount\": \"account-id\" }, \"ArnLike\": { \"aws:SourceArn\": \"arn:aws:cloudwatch:region:account-id:alarm:*\" } } } ] } </code> </p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to assign the policy to.</p>
            policy: <p>The policy, in JSON format.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_aiops.types.put_investigation_group_policy_request.PutInvestigationGroupPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_aiops.types.put_investigation_group_policy_response.PutInvestigationGroupPolicyResponse"
        ]:
            import aws_sdk_aiops._operations.ai_ops.put_investigation_group_policy

            output, http_response = (
                aws_sdk_aiops._operations.ai_ops.put_investigation_group_policy.put_investigation_group_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_aiops.types.put_investigation_group_policy_request.PutInvestigationGroupPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        identifier: "aws_sdk_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "aws_sdk_aiops.types.get_investigation_group_policy_response.GetInvestigationGroupPolicyResponse":
        r"""<p>Returns the JSON of the IAM resource policy associated with the specified investigation group in a string. For example, <code>{\\"Version\\":\\"2012-10-17\\",\\"Statement\\":[{\\"Effect\\":\\"Allow\\",\\"Principal\\":{\\"Service\\":\\"aiops.alarms.cloudwatch.amazonaws.com\\"},\\"Action\\":[\\"aiops:CreateInvestigation\\",\\"aiops:CreateInvestigationEvent\\"],\\"Resource\\":\\"*\\",\\"Condition\\":{\\"StringEquals\\":{\\"aws:SourceAccount\\":\\"111122223333\\"},\\"ArnLike\\":{\\"aws:SourceArn\\":\\"arn:aws:cloudwatch:us-east-1:111122223333:alarm:*\\"}}}]}</code>.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to view the policy of.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_aiops.types.get_investigation_group_policy_request.GetInvestigationGroupPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_aiops.types.get_investigation_group_policy_response.GetInvestigationGroupPolicyResponse"
        ]:
            import aws_sdk_aiops._operations.ai_ops.get_investigation_group_policy

            output, http_response = (
                aws_sdk_aiops._operations.ai_ops.get_investigation_group_policy.get_investigation_group_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_aiops.types.get_investigation_group_policy_request.GetInvestigationGroupPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identifier: "aws_sdk_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "aws_sdk_aiops.types.delete_investigation_group_policy_output.DeleteInvestigationGroupPolicyOutput":
        """<p>Removes the IAM resource policy from being associated with the investigation group that you specify.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to remove the policy from.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_aiops.types.delete_investigation_group_policy_request.DeleteInvestigationGroupPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_aiops.types.delete_investigation_group_policy_output.DeleteInvestigationGroupPolicyOutput"
        ]:
            import aws_sdk_aiops._operations.ai_ops.delete_investigation_group_policy

            output, http_response = (
                aws_sdk_aiops._operations.ai_ops.delete_investigation_group_policy.delete_investigation_group_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_aiops.types.delete_investigation_group_policy_request.DeleteInvestigationGroupPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncInvestigationGroupPolicy:
    def __init__(self, service: AsyncAIOpsClient) -> None:
        self._service = service

    async def put(
        self,
        identifier: "aws_sdk_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        policy: "aws_sdk_aiops.types.investigation_group_policy_document.InvestigationGroupPolicyDocument",
        *,
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
    ) -> "aws_sdk_aiops.types.put_investigation_group_policy_response.PutInvestigationGroupPolicyResponse":
        r"""<p>Creates an IAM resource policy and assigns it to the specified investigation group.</p> <p>If you create your investigation group with <code>CreateInvestigationGroup</code> and you want to enable CloudWatch alarms to create investigations and add events to investigations, you must use this operation to create a policy similar to this example.</p> <p> <code> { \"Version\": \"2008-10-17\", \"Statement\": [ { \"Effect\": \"Allow\", \"Principal\": { \"Service\": \"aiops.alarms.cloudwatch.amazonaws.com\" }, \"Action\": [ \"aiops:CreateInvestigation\", \"aiops:CreateInvestigationEvent\" ], \"Resource\": \"*\", \"Condition\": { \"StringEquals\": { \"aws:SourceAccount\": \"account-id\" }, \"ArnLike\": { \"aws:SourceArn\": \"arn:aws:cloudwatch:region:account-id:alarm:*\" } } } ] } </code> </p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to assign the policy to.</p>
            policy: <p>The policy, in JSON format.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_aiops.types.put_investigation_group_policy_request.PutInvestigationGroupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_aiops.types.put_investigation_group_policy_response.PutInvestigationGroupPolicyResponse"
        ]:
            import aws_sdk_aiops._operations.ai_ops.put_investigation_group_policy

            (
                output,
                http_response,
            ) = await aws_sdk_aiops._operations.ai_ops.put_investigation_group_policy.async_put_investigation_group_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_aiops.types.put_investigation_group_policy_request.PutInvestigationGroupPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identifier: "aws_sdk_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
    ) -> "aws_sdk_aiops.types.get_investigation_group_policy_response.GetInvestigationGroupPolicyResponse":
        r"""<p>Returns the JSON of the IAM resource policy associated with the specified investigation group in a string. For example, <code>{\\"Version\\":\\"2012-10-17\\",\\"Statement\\":[{\\"Effect\\":\\"Allow\\",\\"Principal\\":{\\"Service\\":\\"aiops.alarms.cloudwatch.amazonaws.com\\"},\\"Action\\":[\\"aiops:CreateInvestigation\\",\\"aiops:CreateInvestigationEvent\\"],\\"Resource\\":\\"*\\",\\"Condition\\":{\\"StringEquals\\":{\\"aws:SourceAccount\\":\\"111122223333\\"},\\"ArnLike\\":{\\"aws:SourceArn\\":\\"arn:aws:cloudwatch:us-east-1:111122223333:alarm:*\\"}}}]}</code>.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to view the policy of.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_aiops.types.get_investigation_group_policy_request.GetInvestigationGroupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_aiops.types.get_investigation_group_policy_response.GetInvestigationGroupPolicyResponse"
        ]:
            import aws_sdk_aiops._operations.ai_ops.get_investigation_group_policy

            (
                output,
                http_response,
            ) = await aws_sdk_aiops._operations.ai_ops.get_investigation_group_policy.async_get_investigation_group_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_aiops.types.get_investigation_group_policy_request.GetInvestigationGroupPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identifier: "aws_sdk_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier",
        *,
        config_overrides: Optional[AsyncAIOpsClientConfig] = None,
    ) -> "aws_sdk_aiops.types.delete_investigation_group_policy_output.DeleteInvestigationGroupPolicyOutput":
        """<p>Removes the IAM resource policy from being associated with the investigation group that you specify.</p>

        Args:
            identifier: <p>Specify either the name or the ARN of the investigation group that you want to remove the policy from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_aiops.types.delete_investigation_group_policy_request.DeleteInvestigationGroupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_aiops.types.delete_investigation_group_policy_output.DeleteInvestigationGroupPolicyOutput"
        ]:
            import aws_sdk_aiops._operations.ai_ops.delete_investigation_group_policy

            (
                output,
                http_response,
            ) = await aws_sdk_aiops._operations.ai_ops.delete_investigation_group_policy.async_delete_investigation_group_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_aiops.types.delete_investigation_group_policy_request.DeleteInvestigationGroupPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
