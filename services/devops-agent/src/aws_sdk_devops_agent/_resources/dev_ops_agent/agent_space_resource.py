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
    import aws_sdk_devops_agent.types.agent_space
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.agent_space_name
    import aws_sdk_devops_agent.types.auth_flow
    import aws_sdk_devops_agent.types.create_agent_space_input
    import aws_sdk_devops_agent.types.create_agent_space_output
    import aws_sdk_devops_agent.types.delete_agent_space_input
    import aws_sdk_devops_agent.types.delete_agent_space_output
    import aws_sdk_devops_agent.types.description
    import aws_sdk_devops_agent.types.disable_operator_app_input
    import aws_sdk_devops_agent.types.enable_operator_app_input
    import aws_sdk_devops_agent.types.enable_operator_app_output
    import aws_sdk_devops_agent.types.get_agent_space_input
    import aws_sdk_devops_agent.types.get_agent_space_output
    import aws_sdk_devops_agent.types.get_operator_app_input
    import aws_sdk_devops_agent.types.get_operator_app_output
    import aws_sdk_devops_agent.types.idp_client_id
    import aws_sdk_devops_agent.types.idp_client_secret
    import aws_sdk_devops_agent.types.kms_key_arn
    import aws_sdk_devops_agent.types.list_agent_spaces_input
    import aws_sdk_devops_agent.types.list_agent_spaces_output
    import aws_sdk_devops_agent.types.locale
    import aws_sdk_devops_agent.types.next_token
    import aws_sdk_devops_agent.types.role_arn
    import aws_sdk_devops_agent.types.tags
    import aws_sdk_devops_agent.types.update_agent_space_input
    import aws_sdk_devops_agent.types.update_agent_space_output
    import aws_sdk_devops_agent.types.update_operator_app_idp_config_input
    import aws_sdk_devops_agent.types.update_operator_app_idp_config_output
    from aws_sdk_devops_agent._services.async_dev_ops_agent import (
        AsyncDevOpsAgentClient,
        AsyncDevOpsAgentClientConfig,
    )
    from aws_sdk_devops_agent._services.dev_ops_agent import (
        DevOpsAgentClient,
        DevOpsAgentClientConfig,
    )


class AgentSpaceResource:
    def __init__(self, service: DevOpsAgentClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_devops_agent.types.agent_space_name.AgentSpaceName",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        description: Optional[
            "aws_sdk_devops_agent.types.description.Description"
        ] = None,
        locale: Optional["aws_sdk_devops_agent.types.locale.Locale"] = None,
        kms_key_arn: Optional[
            "aws_sdk_devops_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["aws_sdk_devops_agent.types.tags.Tags"] = None,
    ) -> "aws_sdk_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput":
        """<p>Creates a new AgentSpace with the specified name and description. Duplicate space names are allowed.</p>

        Args:
            name: <p>The name of the AgentSpace.</p>
            description: <p>The description of the AgentSpace.</p>
            locale: <p>The locale for the AgentSpace, which determines the language used in agent responses.</p>
            kms_key_arn: <p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>
            client_token: <p>Client-provided token to ensure request idempotency. When the same token is provided in subsequent calls, the same response is returned within a 8-hour window.</p>
            tags: <p>Tags to add to the AgentSpace at creation time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.create_agent_space

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.create_agent_space.create_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if locale is not None:
            input_["locale"] = locale
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput":
        """<p>Retrieves detailed information about a specific AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.get_agent_space_input.GetAgentSpaceInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_agent_space

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.get_agent_space.get_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_agent_space_input.GetAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        name: Optional[
            "aws_sdk_devops_agent.types.agent_space_name.AgentSpaceName"
        ] = None,
        description: Optional[
            "aws_sdk_devops_agent.types.description.Description"
        ] = None,
        locale: Optional["aws_sdk_devops_agent.types.locale.Locale"] = None,
    ) -> "aws_sdk_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput":
        """<p>Updates the information of an existing AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            name: <p>The updated name of the AgentSpace.</p>
            description: <p>The updated description of the AgentSpace.</p>
            locale: <p>The updated locale for the AgentSpace, which determines the language used in agent responses.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_agent_space

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.update_agent_space.update_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if locale is not None:
            input_["locale"] = locale

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput":
        """<p>Deletes an AgentSpace. This operation is idempotent and returns a 204 No Content response on success.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.delete_agent_space

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.delete_agent_space.delete_agent_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_operator_app(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        auth_flow: Optional["aws_sdk_devops_agent.types.auth_flow.AuthFlow"] = None,
    ) -> None:
        """<p>Disable the Operator App for the specified AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            auth_flow: <p>The authentication flow configured for the operator App. e.g. idc</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.disable_operator_app_input.DisableOperatorAppInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.disable_operator_app

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.disable_operator_app.disable_operator_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.disable_operator_app_input.DisableOperatorAppInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if auth_flow is not None:
            input_["auth_flow"] = auth_flow

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_operator_app(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        auth_flow: "aws_sdk_devops_agent.types.auth_flow.AuthFlow",
        operator_app_role_arn: "aws_sdk_devops_agent.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        idc_instance_arn: Optional[str] = None,
        issuer_url: Optional[str] = None,
        idp_client_id: Optional[
            "aws_sdk_devops_agent.types.idp_client_id.IdpClientId"
        ] = None,
        idp_client_secret: Optional[
            "aws_sdk_devops_agent.types.idp_client_secret.IdpClientSecret"
        ] = None,
        provider: Optional[str] = None,
    ) -> (
        "aws_sdk_devops_agent.types.enable_operator_app_output.EnableOperatorAppOutput"
    ):
        """<p>Enable the Operator App to access the given AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            auth_flow: <p>The authentication flow configured for the operator App. e.g. iam or idc</p>
            operator_app_role_arn: <p>The IAM role end users assume to access AIDevOps APIs</p>
            idc_instance_arn: <p>The IdC instance Arn used to create an IdC auth application</p>
            issuer_url: <p>The OIDC issuer URL of the external Identity Provider</p>
            idp_client_id: <p>The OIDC client ID for the IdP application</p>
            idp_client_secret: <p>The OIDC client secret for the IdP application</p>
            provider: <p>The Identity Provider name (e.g., Entra, Okta, Google)</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.enable_operator_app_output.EnableOperatorAppOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.enable_operator_app

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.enable_operator_app.enable_operator_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["auth_flow"] = auth_flow
        input_["operator_app_role_arn"] = operator_app_role_arn
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if issuer_url is not None:
            input_["issuer_url"] = issuer_url
        if idp_client_id is not None:
            input_["idp_client_id"] = idp_client_id
        if idp_client_secret is not None:
            input_["idp_client_secret"] = idp_client_secret
        if provider is not None:
            input_["provider"] = provider

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_operator_app(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.get_operator_app_output.GetOperatorAppOutput":
        """<p>Get the full auth configuration of operator including any enabled auth flow</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.get_operator_app_input.GetOperatorAppInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.get_operator_app_output.GetOperatorAppOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_operator_app

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.get_operator_app.get_operator_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_operator_app_input.GetOperatorAppInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_operator_app_idp_config(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        idp_client_secret: Optional[
            "aws_sdk_devops_agent.types.idp_client_secret.IdpClientSecret"
        ] = None,
    ) -> "aws_sdk_devops_agent.types.update_operator_app_idp_config_output.UpdateOperatorAppIdpConfigOutput":
        """<p>Update the external Identity Provider configuration for the Operator App</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            idp_client_secret: <p>The OIDC client secret for the IdP application</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.update_operator_app_idp_config_output.UpdateOperatorAppIdpConfigOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_operator_app_idp_config

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.update_operator_app_idp_config.update_operator_app_idp_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if idp_client_secret is not None:
            input_["idp_client_secret"] = idp_client_secret

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_agent_spaces(
        self,
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput":
        """<p>Lists all AgentSpaces with optional pagination.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.list_agent_spaces_input.ListAgentSpacesInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_agent_spaces

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.list_agent_spaces.list_agent_spaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_agent_spaces_input.ListAgentSpacesInput = {}  # type: ignore[typeddict-item]
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


class AsyncAgentSpaceResource:
    def __init__(self, service: AsyncDevOpsAgentClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_devops_agent.types.agent_space_name.AgentSpaceName",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        description: Optional[
            "aws_sdk_devops_agent.types.description.Description"
        ] = None,
        locale: Optional["aws_sdk_devops_agent.types.locale.Locale"] = None,
        kms_key_arn: Optional[
            "aws_sdk_devops_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["aws_sdk_devops_agent.types.tags.Tags"] = None,
    ) -> "aws_sdk_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput":
        """<p>Creates a new AgentSpace with the specified name and description. Duplicate space names are allowed.</p>

        Args:
            name: <p>The name of the AgentSpace.</p>
            description: <p>The description of the AgentSpace.</p>
            locale: <p>The locale for the AgentSpace, which determines the language used in agent responses.</p>
            kms_key_arn: <p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>
            client_token: <p>Client-provided token to ensure request idempotency. When the same token is provided in subsequent calls, the same response is returned within a 8-hour window.</p>
            tags: <p>Tags to add to the AgentSpace at creation time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.create_agent_space

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.create_agent_space.async_create_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if locale is not None:
            input_["locale"] = locale
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput":
        """<p>Retrieves detailed information about a specific AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.get_agent_space_input.GetAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_agent_space

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.get_agent_space.async_get_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_agent_space_input.GetAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        name: Optional[
            "aws_sdk_devops_agent.types.agent_space_name.AgentSpaceName"
        ] = None,
        description: Optional[
            "aws_sdk_devops_agent.types.description.Description"
        ] = None,
        locale: Optional["aws_sdk_devops_agent.types.locale.Locale"] = None,
    ) -> "aws_sdk_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput":
        """<p>Updates the information of an existing AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            name: <p>The updated name of the AgentSpace.</p>
            description: <p>The updated description of the AgentSpace.</p>
            locale: <p>The updated locale for the AgentSpace, which determines the language used in agent responses.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_agent_space

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.update_agent_space.async_update_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput":
        """<p>Deletes an AgentSpace. This operation is idempotent and returns a 204 No Content response on success.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.delete_agent_space

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.delete_agent_space.async_delete_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_operator_app(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        auth_flow: Optional["aws_sdk_devops_agent.types.auth_flow.AuthFlow"] = None,
    ) -> None:
        """<p>Disable the Operator App for the specified AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            auth_flow: <p>The authentication flow configured for the operator App. e.g. idc</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.disable_operator_app_input.DisableOperatorAppInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.disable_operator_app

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.disable_operator_app.async_disable_operator_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.disable_operator_app_input.DisableOperatorAppInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if auth_flow is not None:
            input_["auth_flow"] = auth_flow

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_operator_app(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        auth_flow: "aws_sdk_devops_agent.types.auth_flow.AuthFlow",
        operator_app_role_arn: "aws_sdk_devops_agent.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        idc_instance_arn: Optional[str] = None,
        issuer_url: Optional[str] = None,
        idp_client_id: Optional[
            "aws_sdk_devops_agent.types.idp_client_id.IdpClientId"
        ] = None,
        idp_client_secret: Optional[
            "aws_sdk_devops_agent.types.idp_client_secret.IdpClientSecret"
        ] = None,
        provider: Optional[str] = None,
    ) -> (
        "aws_sdk_devops_agent.types.enable_operator_app_output.EnableOperatorAppOutput"
    ):
        """<p>Enable the Operator App to access the given AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            auth_flow: <p>The authentication flow configured for the operator App. e.g. iam or idc</p>
            operator_app_role_arn: <p>The IAM role end users assume to access AIDevOps APIs</p>
            idc_instance_arn: <p>The IdC instance Arn used to create an IdC auth application</p>
            issuer_url: <p>The OIDC issuer URL of the external Identity Provider</p>
            idp_client_id: <p>The OIDC client ID for the IdP application</p>
            idp_client_secret: <p>The OIDC client secret for the IdP application</p>
            provider: <p>The Identity Provider name (e.g., Entra, Okta, Google)</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.enable_operator_app_output.EnableOperatorAppOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.enable_operator_app

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.enable_operator_app.async_enable_operator_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["auth_flow"] = auth_flow
        input_["operator_app_role_arn"] = operator_app_role_arn
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if issuer_url is not None:
            input_["issuer_url"] = issuer_url
        if idp_client_id is not None:
            input_["idp_client_id"] = idp_client_id
        if idp_client_secret is not None:
            input_["idp_client_secret"] = idp_client_secret
        if provider is not None:
            input_["provider"] = provider

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_operator_app(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.get_operator_app_output.GetOperatorAppOutput":
        """<p>Get the full auth configuration of operator including any enabled auth flow</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.get_operator_app_input.GetOperatorAppInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.get_operator_app_output.GetOperatorAppOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_operator_app

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.get_operator_app.async_get_operator_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_operator_app_input.GetOperatorAppInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_operator_app_idp_config(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        idp_client_secret: Optional[
            "aws_sdk_devops_agent.types.idp_client_secret.IdpClientSecret"
        ] = None,
    ) -> "aws_sdk_devops_agent.types.update_operator_app_idp_config_output.UpdateOperatorAppIdpConfigOutput":
        """<p>Update the external Identity Provider configuration for the Operator App</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            idp_client_secret: <p>The OIDC client secret for the IdP application</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.update_operator_app_idp_config_output.UpdateOperatorAppIdpConfigOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_operator_app_idp_config

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.update_operator_app_idp_config.async_update_operator_app_idp_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if idp_client_secret is not None:
            input_["idp_client_secret"] = idp_client_secret

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_agent_spaces(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput":
        """<p>Lists all AgentSpaces with optional pagination.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_agent_spaces_input.ListAgentSpacesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_agent_spaces

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_agent_spaces.async_list_agent_spaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_agent_spaces_input.ListAgentSpacesInput = {}  # type: ignore[typeddict-item]
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
