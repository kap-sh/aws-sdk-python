from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agent._auth._signers
import aws_sdk_bedrock_agent._auth._sigv4
from aws_sdk_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.create_prompt_request
    import aws_sdk_bedrock_agent.types.create_prompt_response
    import aws_sdk_bedrock_agent.types.create_prompt_version_request
    import aws_sdk_bedrock_agent.types.create_prompt_version_response
    import aws_sdk_bedrock_agent.types.delete_prompt_request
    import aws_sdk_bedrock_agent.types.delete_prompt_response
    import aws_sdk_bedrock_agent.types.get_prompt_request
    import aws_sdk_bedrock_agent.types.get_prompt_response
    import aws_sdk_bedrock_agent.types.kms_key_arn
    import aws_sdk_bedrock_agent.types.list_prompts_request
    import aws_sdk_bedrock_agent.types.list_prompts_response
    import aws_sdk_bedrock_agent.types.max_results
    import aws_sdk_bedrock_agent.types.next_token
    import aws_sdk_bedrock_agent.types.numerical_version
    import aws_sdk_bedrock_agent.types.prompt_description
    import aws_sdk_bedrock_agent.types.prompt_identifier
    import aws_sdk_bedrock_agent.types.prompt_name
    import aws_sdk_bedrock_agent.types.prompt_summary
    import aws_sdk_bedrock_agent.types.prompt_variant_list
    import aws_sdk_bedrock_agent.types.prompt_variant_name
    import aws_sdk_bedrock_agent.types.tags_map
    import aws_sdk_bedrock_agent.types.update_prompt_request
    import aws_sdk_bedrock_agent.types.update_prompt_response
    import aws_sdk_bedrock_agent.types.version
    from aws_sdk_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from aws_sdk_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class PromptResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_bedrock_agent.types.prompt_name.PromptName",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        default_variant: Optional[
            "aws_sdk_bedrock_agent.types.prompt_variant_name.PromptVariantName"
        ] = None,
        variants: Optional[
            "aws_sdk_bedrock_agent.types.prompt_variant_list.PromptVariantList"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_bedrock_agent.types.create_prompt_response.CreatePromptResponse":
        """<p>Creates a prompt in your prompt library that you can add to a flow. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html\">Prompt management in Amazon Bedrock</a>, <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html\">Create a prompt using Prompt management</a> and <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html\">Prompt flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the prompt.</p>
            description: <p>A description for the prompt.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>
            default_variant: <p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html\">PromptVariant</a> object.</p>
            variants: <p>A list of objects, each containing details about a variant of the prompt.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the prompt. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html\">Tagging resources in Amazon Bedrock</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.create_prompt_request.CreatePromptRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.create_prompt_response.CreatePromptResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt.create_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.create_prompt_request.CreatePromptRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if default_variant is not None:
            input_["default_variant"] = default_variant
        if variants is not None:
            input_["variants"] = variants
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
        prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        prompt_version: Optional["aws_sdk_bedrock_agent.types.version.Version"] = None,
    ) -> "aws_sdk_bedrock_agent.types.get_prompt_response.GetPromptResponse":
        """<p>Retrieves information about the working draft (<code>DRAFT</code> version) of a prompt or a version of it, depending on whether you include the <code>promptVersion</code> field or not. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html\">View information about prompts using Prompt management</a> and <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-view.html\">View information about a version of your prompt</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt.</p>
            prompt_version: <p>The version of the prompt about which you want to retrieve information. Omit this field to return information about the working draft of the prompt.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.get_prompt_request.GetPromptRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.get_prompt_response.GetPromptResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_prompt

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_prompt.get_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.get_prompt_request.GetPromptRequest = {}  # type: ignore[typeddict-item]
        input_["prompt_identifier"] = prompt_identifier
        if prompt_version is not None:
            input_["prompt_version"] = prompt_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        name: "aws_sdk_bedrock_agent.types.prompt_name.PromptName",
        prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        default_variant: Optional[
            "aws_sdk_bedrock_agent.types.prompt_variant_name.PromptVariantName"
        ] = None,
        variants: Optional[
            "aws_sdk_bedrock_agent.types.prompt_variant_list.PromptVariantList"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.update_prompt_response.UpdatePromptResponse":
        """<p>Modifies a prompt in your prompt library. Include both fields that you want to keep and fields that you want to replace. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html\">Prompt management in Amazon Bedrock</a> and <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-edit\">Edit prompts in your prompt library</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the prompt.</p>
            description: <p>A description for the prompt.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>
            default_variant: <p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html\">PromptVariant</a> object.</p>
            variants: <p>A list of objects, each containing details about a variant of the prompt.</p>
            prompt_identifier: <p>The unique identifier of the prompt.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.update_prompt_request.UpdatePromptRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.update_prompt_response.UpdatePromptResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_prompt

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_prompt.update_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.update_prompt_request.UpdatePromptRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if default_variant is not None:
            input_["default_variant"] = default_variant
        if variants is not None:
            input_["variants"] = variants
        input_["prompt_identifier"] = prompt_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        prompt_version: Optional[
            "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.delete_prompt_response.DeletePromptResponse":
        """<p>Deletes a prompt or a version of it, depending on whether you include the <code>promptVersion</code> field or not. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-delete.html\">Delete prompts from the Prompt management tool</a> and <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-delete.html\">Delete a version of a prompt from the Prompt management tool</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt.</p>
            prompt_version: <p>The version of the prompt to delete. To delete the prompt, omit this field.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.delete_prompt_request.DeletePromptRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.delete_prompt_response.DeletePromptResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_prompt

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_prompt.delete_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.delete_prompt_request.DeletePromptRequest = {}  # type: ignore[typeddict-item]
        input_["prompt_identifier"] = prompt_identifier
        if prompt_version is not None:
            input_["prompt_version"] = prompt_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        prompt_identifier: Optional[
            "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier"
        ] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_prompts_response.ListPromptsResponse":
        """<p>Returns either information about the working draft (<code>DRAFT</code> version) of each prompt in an account, or information about of all versions of a prompt, depending on whether you include the <code>promptIdentifier</code> field or not. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html\">View information about prompts using Prompt management</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt for whose versions you want to return information. Omit this field to list information about all prompts in an account.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.list_prompts_request.ListPromptsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.list_prompts_response.ListPromptsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_prompts

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_prompts.list_prompts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.list_prompts_request.ListPromptsRequest = {}  # type: ignore[typeddict-item]
        if prompt_identifier is not None:
            input_["prompt_identifier"] = prompt_identifier
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

    def create_prompt_version(
        self,
        prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_bedrock_agent.types.create_prompt_version_response.CreatePromptVersionResponse":
        """<p>Creates a static snapshot of your prompt that can be deployed to production. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html\">Deploy prompts using Prompt management by creating versions</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt that you want to create a version of.</p>
            description: <p>A description for the version of the prompt.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the version of the prompt. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html\">Tagging resources in Amazon Bedrock</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.create_prompt_version_request.CreatePromptVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.create_prompt_version_response.CreatePromptVersionResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt_version

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt_version.create_prompt_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.create_prompt_version_request.CreatePromptVersionRequest = {}  # type: ignore[typeddict-item]
        input_["prompt_identifier"] = prompt_identifier
        if description is not None:
            input_["description"] = description
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


class AsyncPromptResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_bedrock_agent.types.prompt_name.PromptName",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        default_variant: Optional[
            "aws_sdk_bedrock_agent.types.prompt_variant_name.PromptVariantName"
        ] = None,
        variants: Optional[
            "aws_sdk_bedrock_agent.types.prompt_variant_list.PromptVariantList"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_bedrock_agent.types.create_prompt_response.CreatePromptResponse":
        """<p>Creates a prompt in your prompt library that you can add to a flow. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html\">Prompt management in Amazon Bedrock</a>, <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html\">Create a prompt using Prompt management</a> and <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html\">Prompt flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the prompt.</p>
            description: <p>A description for the prompt.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>
            default_variant: <p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html\">PromptVariant</a> object.</p>
            variants: <p>A list of objects, each containing details about a variant of the prompt.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the prompt. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html\">Tagging resources in Amazon Bedrock</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.create_prompt_request.CreatePromptRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.create_prompt_response.CreatePromptResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt.async_create_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.create_prompt_request.CreatePromptRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if default_variant is not None:
            input_["default_variant"] = default_variant
        if variants is not None:
            input_["variants"] = variants
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
        prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        prompt_version: Optional["aws_sdk_bedrock_agent.types.version.Version"] = None,
    ) -> "aws_sdk_bedrock_agent.types.get_prompt_response.GetPromptResponse":
        """<p>Retrieves information about the working draft (<code>DRAFT</code> version) of a prompt or a version of it, depending on whether you include the <code>promptVersion</code> field or not. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html\">View information about prompts using Prompt management</a> and <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-view.html\">View information about a version of your prompt</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt.</p>
            prompt_version: <p>The version of the prompt about which you want to retrieve information. Omit this field to return information about the working draft of the prompt.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.get_prompt_request.GetPromptRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.get_prompt_response.GetPromptResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_prompt

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_prompt.async_get_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.get_prompt_request.GetPromptRequest = {}  # type: ignore[typeddict-item]
        input_["prompt_identifier"] = prompt_identifier
        if prompt_version is not None:
            input_["prompt_version"] = prompt_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        name: "aws_sdk_bedrock_agent.types.prompt_name.PromptName",
        prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        default_variant: Optional[
            "aws_sdk_bedrock_agent.types.prompt_variant_name.PromptVariantName"
        ] = None,
        variants: Optional[
            "aws_sdk_bedrock_agent.types.prompt_variant_list.PromptVariantList"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.update_prompt_response.UpdatePromptResponse":
        """<p>Modifies a prompt in your prompt library. Include both fields that you want to keep and fields that you want to replace. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html\">Prompt management in Amazon Bedrock</a> and <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-edit\">Edit prompts in your prompt library</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the prompt.</p>
            description: <p>A description for the prompt.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>
            default_variant: <p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html\">PromptVariant</a> object.</p>
            variants: <p>A list of objects, each containing details about a variant of the prompt.</p>
            prompt_identifier: <p>The unique identifier of the prompt.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.update_prompt_request.UpdatePromptRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.update_prompt_response.UpdatePromptResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_prompt

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_prompt.async_update_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.update_prompt_request.UpdatePromptRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if default_variant is not None:
            input_["default_variant"] = default_variant
        if variants is not None:
            input_["variants"] = variants
        input_["prompt_identifier"] = prompt_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        prompt_version: Optional[
            "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.delete_prompt_response.DeletePromptResponse":
        """<p>Deletes a prompt or a version of it, depending on whether you include the <code>promptVersion</code> field or not. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-delete.html\">Delete prompts from the Prompt management tool</a> and <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-delete.html\">Delete a version of a prompt from the Prompt management tool</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt.</p>
            prompt_version: <p>The version of the prompt to delete. To delete the prompt, omit this field.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.delete_prompt_request.DeletePromptRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.delete_prompt_response.DeletePromptResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_prompt

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_prompt.async_delete_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.delete_prompt_request.DeletePromptRequest = {}  # type: ignore[typeddict-item]
        input_["prompt_identifier"] = prompt_identifier
        if prompt_version is not None:
            input_["prompt_version"] = prompt_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        prompt_identifier: Optional[
            "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier"
        ] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_prompts_response.ListPromptsResponse":
        """<p>Returns either information about the working draft (<code>DRAFT</code> version) of each prompt in an account, or information about of all versions of a prompt, depending on whether you include the <code>promptIdentifier</code> field or not. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html\">View information about prompts using Prompt management</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt for whose versions you want to return information. Omit this field to list information about all prompts in an account.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.list_prompts_request.ListPromptsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.list_prompts_response.ListPromptsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_prompts

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_prompts.async_list_prompts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.list_prompts_request.ListPromptsRequest = {}  # type: ignore[typeddict-item]
        if prompt_identifier is not None:
            input_["prompt_identifier"] = prompt_identifier
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

    async def create_prompt_version(
        self,
        prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_bedrock_agent.types.create_prompt_version_response.CreatePromptVersionResponse":
        """<p>Creates a static snapshot of your prompt that can be deployed to production. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html\">Deploy prompts using Prompt management by creating versions</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt that you want to create a version of.</p>
            description: <p>A description for the version of the prompt.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the version of the prompt. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html\">Tagging resources in Amazon Bedrock</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.create_prompt_version_request.CreatePromptVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.create_prompt_version_response.CreatePromptVersionResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt_version

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt_version.async_create_prompt_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.create_prompt_version_request.CreatePromptVersionRequest = {}  # type: ignore[typeddict-item]
        input_["prompt_identifier"] = prompt_identifier
        if description is not None:
            input_["description"] = description
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
