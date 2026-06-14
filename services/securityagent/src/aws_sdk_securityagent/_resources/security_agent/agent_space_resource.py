from typing import TYPE_CHECKING, Optional

import aws_sdk_securityagent._auth._signers
import aws_sdk_securityagent._auth._sigv4
from aws_sdk_securityagent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_name
    import aws_sdk_securityagent.types.agent_space_id
    import aws_sdk_securityagent.types.agent_space_id_list
    import aws_sdk_securityagent.types.agent_space_summary
    import aws_sdk_securityagent.types.aws_resources
    import aws_sdk_securityagent.types.batch_get_agent_spaces_input
    import aws_sdk_securityagent.types.batch_get_agent_spaces_output
    import aws_sdk_securityagent.types.code_review_settings
    import aws_sdk_securityagent.types.create_agent_space_input
    import aws_sdk_securityagent.types.create_agent_space_output
    import aws_sdk_securityagent.types.delete_agent_space_input
    import aws_sdk_securityagent.types.delete_agent_space_output
    import aws_sdk_securityagent.types.kms_key_id
    import aws_sdk_securityagent.types.list_agent_spaces_input
    import aws_sdk_securityagent.types.list_agent_spaces_output
    import aws_sdk_securityagent.types.max_results
    import aws_sdk_securityagent.types.next_token
    import aws_sdk_securityagent.types.tag_map
    import aws_sdk_securityagent.types.target_domain_id_list
    import aws_sdk_securityagent.types.update_agent_space_input
    import aws_sdk_securityagent.types.update_agent_space_output
    from aws_sdk_securityagent._services.async_security_agent import (
        AsyncSecurityAgentClient,
        AsyncSecurityAgentClientConfig,
    )
    from aws_sdk_securityagent._services.security_agent import (
        SecurityAgentClient,
        SecurityAgentClientConfig,
    )


class AgentSpaceResource:
    def __init__(self, service: SecurityAgentClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_securityagent.types.agent_name.AgentName",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        description: Optional[str] = None,
        aws_resources: Optional[
            "aws_sdk_securityagent.types.aws_resources.AWSResources"
        ] = None,
        target_domain_ids: Optional[
            "aws_sdk_securityagent.types.target_domain_id_list.TargetDomainIdList"
        ] = None,
        code_review_settings: Optional[
            "aws_sdk_securityagent.types.code_review_settings.CodeReviewSettings"
        ] = None,
        kms_key_id: Optional["aws_sdk_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["aws_sdk_securityagent.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_securityagent.types.create_agent_space_output.CreateAgentSpaceOutput":
        """<p>Creates a new agent space. An agent space is a dedicated workspace for securing a specific application.</p>

        Args:
            name: <p>The name of the agent space.</p>
            description: <p>A description of the agent space.</p>
            aws_resources: <p>The AWS resources to associate with the agent space.</p>
            target_domain_ids: <p>The list of target domain identifiers to associate with the agent space.</p>
            code_review_settings: <p>The code review settings for the agent space.</p>
            kms_key_id: <p>The identifier of the AWS KMS key to use for encrypting data in the agent space.</p>
            tags: <p>The tags to associate with the agent space.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.create_agent_space_input.CreateAgentSpaceInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.create_agent_space_output.CreateAgentSpaceOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.create_agent_space

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.create_agent_space.create_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.create_agent_space_input.CreateAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if aws_resources is not None:
            input_["aws_resources"] = aws_resources
        if target_domain_ids is not None:
            input_["target_domain_ids"] = target_domain_ids
        if code_review_settings is not None:
            input_["code_review_settings"] = code_review_settings
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        name: Optional["aws_sdk_securityagent.types.agent_name.AgentName"] = None,
        description: Optional[str] = None,
        aws_resources: Optional[
            "aws_sdk_securityagent.types.aws_resources.AWSResources"
        ] = None,
        target_domain_ids: Optional[
            "aws_sdk_securityagent.types.target_domain_id_list.TargetDomainIdList"
        ] = None,
        code_review_settings: Optional[
            "aws_sdk_securityagent.types.code_review_settings.CodeReviewSettings"
        ] = None,
    ) -> "aws_sdk_securityagent.types.update_agent_space_output.UpdateAgentSpaceOutput":
        """<p>Updates the configuration of an existing agent space, including its name, description, AWS resources, target domains, and code review settings.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to update.</p>
            name: <p>The updated name of the agent space.</p>
            description: <p>The updated description of the agent space.</p>
            aws_resources: <p>The updated AWS resources to associate with the agent space.</p>
            target_domain_ids: <p>The updated list of target domain identifiers to associate with the agent space.</p>
            code_review_settings: <p>The updated code review settings for the agent space.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.update_agent_space_input.UpdateAgentSpaceInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.update_agent_space_output.UpdateAgentSpaceOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.update_agent_space

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.update_agent_space.update_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.update_agent_space_input.UpdateAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if aws_resources is not None:
            input_["aws_resources"] = aws_resources
        if target_domain_ids is not None:
            input_["target_domain_ids"] = target_domain_ids
        if code_review_settings is not None:
            input_["code_review_settings"] = code_review_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.delete_agent_space_output.DeleteAgentSpaceOutput":
        """<p>Deletes an agent space and all of its associated resources, including pentests, findings, and artifacts.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.delete_agent_space_input.DeleteAgentSpaceInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.delete_agent_space_output.DeleteAgentSpaceOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.delete_agent_space

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.delete_agent_space.delete_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.delete_agent_space_input.DeleteAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityagent.types.list_agent_spaces_output.ListAgentSpacesOutput":
        """<p>Returns a paginated list of agent space summaries in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.list_agent_spaces_input.ListAgentSpacesInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.list_agent_spaces_output.ListAgentSpacesOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_agent_spaces

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.list_agent_spaces.list_agent_spaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_agent_spaces_input.ListAgentSpacesInput = {}  # type: ignore[typeddict-item]
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

    def batch_get_agent_spaces(
        self,
        agent_space_ids: "aws_sdk_securityagent.types.agent_space_id_list.AgentSpaceIdList",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_agent_spaces_output.BatchGetAgentSpacesOutput":
        """<p>Retrieves information about one or more agent spaces.</p>

        Args:
            agent_space_ids: <p>The list of agent space identifiers to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.batch_get_agent_spaces_input.BatchGetAgentSpacesInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.batch_get_agent_spaces_output.BatchGetAgentSpacesOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_agent_spaces

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.batch_get_agent_spaces.batch_get_agent_spaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_agent_spaces_input.BatchGetAgentSpacesInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_ids"] = agent_space_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAgentSpaceResource:
    def __init__(self, service: AsyncSecurityAgentClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_securityagent.types.agent_name.AgentName",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        description: Optional[str] = None,
        aws_resources: Optional[
            "aws_sdk_securityagent.types.aws_resources.AWSResources"
        ] = None,
        target_domain_ids: Optional[
            "aws_sdk_securityagent.types.target_domain_id_list.TargetDomainIdList"
        ] = None,
        code_review_settings: Optional[
            "aws_sdk_securityagent.types.code_review_settings.CodeReviewSettings"
        ] = None,
        kms_key_id: Optional["aws_sdk_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["aws_sdk_securityagent.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_securityagent.types.create_agent_space_output.CreateAgentSpaceOutput":
        """<p>Creates a new agent space. An agent space is a dedicated workspace for securing a specific application.</p>

        Args:
            name: <p>The name of the agent space.</p>
            description: <p>A description of the agent space.</p>
            aws_resources: <p>The AWS resources to associate with the agent space.</p>
            target_domain_ids: <p>The list of target domain identifiers to associate with the agent space.</p>
            code_review_settings: <p>The code review settings for the agent space.</p>
            kms_key_id: <p>The identifier of the AWS KMS key to use for encrypting data in the agent space.</p>
            tags: <p>The tags to associate with the agent space.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.create_agent_space_input.CreateAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.create_agent_space_output.CreateAgentSpaceOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.create_agent_space

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.create_agent_space.async_create_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.create_agent_space_input.CreateAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if aws_resources is not None:
            input_["aws_resources"] = aws_resources
        if target_domain_ids is not None:
            input_["target_domain_ids"] = target_domain_ids
        if code_review_settings is not None:
            input_["code_review_settings"] = code_review_settings
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        name: Optional["aws_sdk_securityagent.types.agent_name.AgentName"] = None,
        description: Optional[str] = None,
        aws_resources: Optional[
            "aws_sdk_securityagent.types.aws_resources.AWSResources"
        ] = None,
        target_domain_ids: Optional[
            "aws_sdk_securityagent.types.target_domain_id_list.TargetDomainIdList"
        ] = None,
        code_review_settings: Optional[
            "aws_sdk_securityagent.types.code_review_settings.CodeReviewSettings"
        ] = None,
    ) -> "aws_sdk_securityagent.types.update_agent_space_output.UpdateAgentSpaceOutput":
        """<p>Updates the configuration of an existing agent space, including its name, description, AWS resources, target domains, and code review settings.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to update.</p>
            name: <p>The updated name of the agent space.</p>
            description: <p>The updated description of the agent space.</p>
            aws_resources: <p>The updated AWS resources to associate with the agent space.</p>
            target_domain_ids: <p>The updated list of target domain identifiers to associate with the agent space.</p>
            code_review_settings: <p>The updated code review settings for the agent space.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.update_agent_space_input.UpdateAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.update_agent_space_output.UpdateAgentSpaceOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.update_agent_space

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.update_agent_space.async_update_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.update_agent_space_input.UpdateAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if aws_resources is not None:
            input_["aws_resources"] = aws_resources
        if target_domain_ids is not None:
            input_["target_domain_ids"] = target_domain_ids
        if code_review_settings is not None:
            input_["code_review_settings"] = code_review_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.delete_agent_space_output.DeleteAgentSpaceOutput":
        """<p>Deletes an agent space and all of its associated resources, including pentests, findings, and artifacts.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.delete_agent_space_input.DeleteAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.delete_agent_space_output.DeleteAgentSpaceOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.delete_agent_space

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.delete_agent_space.async_delete_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.delete_agent_space_input.DeleteAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityagent.types.list_agent_spaces_output.ListAgentSpacesOutput":
        """<p>Returns a paginated list of agent space summaries in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_agent_spaces_input.ListAgentSpacesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_agent_spaces_output.ListAgentSpacesOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_agent_spaces

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_agent_spaces.async_list_agent_spaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_agent_spaces_input.ListAgentSpacesInput = {}  # type: ignore[typeddict-item]
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

    async def batch_get_agent_spaces(
        self,
        agent_space_ids: "aws_sdk_securityagent.types.agent_space_id_list.AgentSpaceIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_agent_spaces_output.BatchGetAgentSpacesOutput":
        """<p>Retrieves information about one or more agent spaces.</p>

        Args:
            agent_space_ids: <p>The list of agent space identifiers to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_get_agent_spaces_input.BatchGetAgentSpacesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_get_agent_spaces_output.BatchGetAgentSpacesOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_agent_spaces

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_get_agent_spaces.async_batch_get_agent_spaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_agent_spaces_input.BatchGetAgentSpacesInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_ids"] = agent_space_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
