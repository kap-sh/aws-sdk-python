from typing import TYPE_CHECKING, Optional

from aws_sdk_proton._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.create_environment_template_input
    import aws_sdk_proton.types.create_environment_template_output
    import aws_sdk_proton.types.delete_environment_template_input
    import aws_sdk_proton.types.delete_environment_template_output
    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.display_name
    import aws_sdk_proton.types.environment_template_summary
    import aws_sdk_proton.types.get_environment_template_input
    import aws_sdk_proton.types.get_environment_template_output
    import aws_sdk_proton.types.list_environment_templates_input
    import aws_sdk_proton.types.list_environment_templates_output
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.provisioning
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.tag_list
    import aws_sdk_proton.types.update_environment_template_input
    import aws_sdk_proton.types.update_environment_template_output
    from aws_sdk_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig


class EnvironmentTemplateResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def put(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        display_name: Optional["aws_sdk_proton.types.display_name.DisplayName"] = None,
        description: Optional["aws_sdk_proton.types.description.Description"] = None,
        encryption_key: Optional["aws_sdk_proton.types.arn.Arn"] = None,
        provisioning: Optional["aws_sdk_proton.types.provisioning.Provisioning"] = None,
        tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_proton.types.create_environment_template_output.CreateEnvironmentTemplateOutput":
        """<p>Create an environment template for Proton. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html\">Environment Templates</a> in the <i>Proton User Guide</i>.</p> <p>You can create an environment template in one of the two following ways:</p> <ul> <li> <p>Register and publish a <i>standard</i> environment template that instructs Proton to deploy and manage environment infrastructure.</p> </li> <li> <p>Register and publish a <i>customer managed</i> environment template that connects Proton to your existing provisioned infrastructure that you manage. Proton <i>doesn't</i> manage your existing provisioned infrastructure. To create an environment template for customer provisioned and managed infrastructure, include the <code>provisioning</code> parameter and set the value to <code>CUSTOMER_MANAGED</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/template-create.html\">Register and publish an environment template</a> in the <i>Proton User Guide</i>.</p> </li> </ul>

        Args:
            name: <p>The name of the environment template.</p>
            display_name: <p>The environment template name as displayed in the developer interface.</p>
            description: <p>A description of the environment template.</p>
            encryption_key: <p>A customer provided encryption key that Proton uses to encrypt data.</p>
            provisioning: <p>When included, indicates that the environment template is for customer provisioned and managed infrastructure.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.create_environment_template_input.CreateEnvironmentTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.create_environment_template_output.CreateEnvironmentTemplateOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.create_environment_template

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.create_environment_template.create_environment_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_environment_template_input.CreateEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if display_name is not None:
            input["display_name"] = display_name
        if description is not None:
            input["description"] = description
        if encryption_key is not None:
            input["encryption_key"] = encryption_key
        if provisioning is not None:
            input["provisioning"] = provisioning
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.get_environment_template_output.GetEnvironmentTemplateOutput":
        """<p>Get detailed data for an environment template.</p>

        Args:
            name: <p>The name of the environment template that you want to get the detailed data for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.get_environment_template_input.GetEnvironmentTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.get_environment_template_output.GetEnvironmentTemplateOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_environment_template

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.get_environment_template.get_environment_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_environment_template_input.GetEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        display_name: Optional["aws_sdk_proton.types.display_name.DisplayName"] = None,
        description: Optional["aws_sdk_proton.types.description.Description"] = None,
    ) -> "aws_sdk_proton.types.update_environment_template_output.UpdateEnvironmentTemplateOutput":
        """<p>Update an environment template.</p>

        Args:
            name: <p>The name of the environment template to update.</p>
            display_name: <p>The name of the environment template to update as displayed in the developer interface.</p>
            description: <p>A description of the environment template update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.update_environment_template_input.UpdateEnvironmentTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.update_environment_template_output.UpdateEnvironmentTemplateOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.update_environment_template

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.update_environment_template.update_environment_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_environment_template_input.UpdateEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if display_name is not None:
            input["display_name"] = display_name
        if description is not None:
            input["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.delete_environment_template_output.DeleteEnvironmentTemplateOutput":
        """<p>If no other major or minor versions of an environment template exist, delete the environment template.</p>

        Args:
            name: <p>The name of the environment template to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.delete_environment_template_input.DeleteEnvironmentTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.delete_environment_template_output.DeleteEnvironmentTemplateOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_environment_template

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.delete_environment_template.delete_environment_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.delete_environment_template_input.DeleteEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "aws_sdk_proton.types.list_environment_templates_output.ListEnvironmentTemplatesOutput":
        """<p>List environment templates.</p>

        Args:
            next_token: <p>A token that indicates the location of the next environment template in the array of environment templates, after the list of environment templates that was previously requested.</p>
            max_results: <p>The maximum number of environment templates to list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.list_environment_templates_input.ListEnvironmentTemplatesInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.list_environment_templates_output.ListEnvironmentTemplatesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_environment_templates

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.list_environment_templates.list_environment_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.list_environment_templates_input.ListEnvironmentTemplatesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEnvironmentTemplateResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def put(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        display_name: Optional["aws_sdk_proton.types.display_name.DisplayName"] = None,
        description: Optional["aws_sdk_proton.types.description.Description"] = None,
        encryption_key: Optional["aws_sdk_proton.types.arn.Arn"] = None,
        provisioning: Optional["aws_sdk_proton.types.provisioning.Provisioning"] = None,
        tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_proton.types.create_environment_template_output.CreateEnvironmentTemplateOutput":
        """<p>Create an environment template for Proton. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html\">Environment Templates</a> in the <i>Proton User Guide</i>.</p> <p>You can create an environment template in one of the two following ways:</p> <ul> <li> <p>Register and publish a <i>standard</i> environment template that instructs Proton to deploy and manage environment infrastructure.</p> </li> <li> <p>Register and publish a <i>customer managed</i> environment template that connects Proton to your existing provisioned infrastructure that you manage. Proton <i>doesn't</i> manage your existing provisioned infrastructure. To create an environment template for customer provisioned and managed infrastructure, include the <code>provisioning</code> parameter and set the value to <code>CUSTOMER_MANAGED</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/template-create.html\">Register and publish an environment template</a> in the <i>Proton User Guide</i>.</p> </li> </ul>

        Args:
            name: <p>The name of the environment template.</p>
            display_name: <p>The environment template name as displayed in the developer interface.</p>
            description: <p>A description of the environment template.</p>
            encryption_key: <p>A customer provided encryption key that Proton uses to encrypt data.</p>
            provisioning: <p>When included, indicates that the environment template is for customer provisioned and managed infrastructure.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.create_environment_template_input.CreateEnvironmentTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.create_environment_template_output.CreateEnvironmentTemplateOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.create_environment_template

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.create_environment_template.async_create_environment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_environment_template_input.CreateEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if display_name is not None:
            input["display_name"] = display_name
        if description is not None:
            input["description"] = description
        if encryption_key is not None:
            input["encryption_key"] = encryption_key
        if provisioning is not None:
            input["provisioning"] = provisioning
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.get_environment_template_output.GetEnvironmentTemplateOutput":
        """<p>Get detailed data for an environment template.</p>

        Args:
            name: <p>The name of the environment template that you want to get the detailed data for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.get_environment_template_input.GetEnvironmentTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.get_environment_template_output.GetEnvironmentTemplateOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_environment_template

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.get_environment_template.async_get_environment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_environment_template_input.GetEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        display_name: Optional["aws_sdk_proton.types.display_name.DisplayName"] = None,
        description: Optional["aws_sdk_proton.types.description.Description"] = None,
    ) -> "aws_sdk_proton.types.update_environment_template_output.UpdateEnvironmentTemplateOutput":
        """<p>Update an environment template.</p>

        Args:
            name: <p>The name of the environment template to update.</p>
            display_name: <p>The name of the environment template to update as displayed in the developer interface.</p>
            description: <p>A description of the environment template update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.update_environment_template_input.UpdateEnvironmentTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.update_environment_template_output.UpdateEnvironmentTemplateOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.update_environment_template

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.update_environment_template.async_update_environment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_environment_template_input.UpdateEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if display_name is not None:
            input["display_name"] = display_name
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.delete_environment_template_output.DeleteEnvironmentTemplateOutput":
        """<p>If no other major or minor versions of an environment template exist, delete the environment template.</p>

        Args:
            name: <p>The name of the environment template to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.delete_environment_template_input.DeleteEnvironmentTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.delete_environment_template_output.DeleteEnvironmentTemplateOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_environment_template

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.delete_environment_template.async_delete_environment_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.delete_environment_template_input.DeleteEnvironmentTemplateInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "aws_sdk_proton.types.list_environment_templates_output.ListEnvironmentTemplatesOutput":
        """<p>List environment templates.</p>

        Args:
            next_token: <p>A token that indicates the location of the next environment template in the array of environment templates, after the list of environment templates that was previously requested.</p>
            max_results: <p>The maximum number of environment templates to list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.list_environment_templates_input.ListEnvironmentTemplatesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.list_environment_templates_output.ListEnvironmentTemplatesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_environment_templates

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.list_environment_templates.async_list_environment_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.list_environment_templates_input.ListEnvironmentTemplatesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
