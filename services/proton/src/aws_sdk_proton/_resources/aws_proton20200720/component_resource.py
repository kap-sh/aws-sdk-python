from typing import Optional, TYPE_CHECKING
from aws_sdk_proton._services.async_proton import ensure_async_iterator
from aws_sdk_proton._services.proton import ensure_sync_iterator
from aws_sdk_proton._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
if TYPE_CHECKING:
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig
    from aws_sdk_proton._services.async_proton import AsyncProtonClient, AsyncProtonClientConfig
    import aws_sdk_proton.types.client_token
    import aws_sdk_proton.types.component_deployment_update_type
    import aws_sdk_proton.types.component_summary
    import aws_sdk_proton.types.create_component_input
    import aws_sdk_proton.types.create_component_output
    import aws_sdk_proton.types.delete_component_input
    import aws_sdk_proton.types.delete_component_output
    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.get_component_input
    import aws_sdk_proton.types.get_component_output
    import aws_sdk_proton.types.list_components_input
    import aws_sdk_proton.types.list_components_output
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.resource_name_or_empty
    import aws_sdk_proton.types.spec_contents
    import aws_sdk_proton.types.tag_list
    import aws_sdk_proton.types.template_file_contents
    import aws_sdk_proton.types.template_manifest_contents
    import aws_sdk_proton.types.update_component_input
    import aws_sdk_proton.types.update_component_output

class ComponentResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service
    def put(self, name: "aws_sdk_proton.types.resource_name.ResourceName", template_file: "aws_sdk_proton.types.template_file_contents.TemplateFileContents", manifest: "aws_sdk_proton.types.template_manifest_contents.TemplateManifestContents", *, config_overrides: Optional[ProtonClientConfig] = None, description: Optional["aws_sdk_proton.types.description.Description"] = None, service_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, service_instance_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, environment_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, service_spec: Optional["aws_sdk_proton.types.spec_contents.SpecContents"] = None, tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None, client_token: Optional["aws_sdk_proton.types.client_token.ClientToken"] = None) -> "aws_sdk_proton.types.create_component_output.CreateComponentOutput":
        """<p>Create an Proton component. A component is an infrastructure extension for a service instance.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The customer-provided name of the component.</p>
            description: <p>An optional customer-provided description of the component.</p>
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated with. If you don't specify this, the component isn't attached to any service instance. Specify both <code>serviceInstanceName</code> and <code>serviceName</code> or neither of them.</p>
            service_instance_name: <p>The name of the service instance that you want to attach this component to. If you don't specify this, the component isn't attached to any service instance. Specify both <code>serviceInstanceName</code> and <code>serviceName</code> or neither of them.</p>
            environment_name: <p>The name of the Proton environment that you want to associate this component with. You must specify this when you don't specify <code>serviceInstanceName</code> and <code>serviceName</code>.</p>
            template_file: <p>A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.</p> <note> <p>Components support a single IaC file, even if you use Terraform as your template language.</p> </note>
            manifest: <p>A path to a manifest file that lists the Infrastructure as Code (IaC) file, template language, and rendering engine for infrastructure that a custom component provisions.</p>
            service_spec: <p>The service spec that you want the component to use to access service inputs. Set this only when you attach the component to a service instance.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton component. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            client_token: <p>The client token for the created component.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.create_component_input.CreateComponentInput]') -> OperationResponse["aws_sdk_proton.types.create_component_output.CreateComponentOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.create_component
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.create_component.create_component(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_component_input.CreateComponentInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if service_name is not None:
            input["service_name"] = service_name
        if service_instance_name is not None:
            input["service_instance_name"] = service_instance_name
        if environment_name is not None:
            input["environment_name"] = environment_name
        input["template_file"] = template_file
        input["manifest"] = manifest
        if service_spec is not None:
            input["service_spec"] = service_spec
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.get_component_output.GetComponentOutput":
        """<p>Get detailed data for a component.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the component that you want to get the detailed data for.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.get_component_input.GetComponentInput]') -> OperationResponse["aws_sdk_proton.types.get_component_output.GetComponentOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.get_component
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.get_component.get_component(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_component_input.GetComponentInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, name: "aws_sdk_proton.types.resource_name.ResourceName", deployment_type: "aws_sdk_proton.types.component_deployment_update_type.ComponentDeploymentUpdateType", *, config_overrides: Optional[ProtonClientConfig] = None, description: Optional["aws_sdk_proton.types.description.Description"] = None, service_name: Optional["aws_sdk_proton.types.resource_name_or_empty.ResourceNameOrEmpty"] = None, service_instance_name: Optional["aws_sdk_proton.types.resource_name_or_empty.ResourceNameOrEmpty"] = None, service_spec: Optional["aws_sdk_proton.types.spec_contents.SpecContents"] = None, template_file: Optional["aws_sdk_proton.types.template_file_contents.TemplateFileContents"] = None, client_token: Optional["aws_sdk_proton.types.client_token.ClientToken"] = None) -> "aws_sdk_proton.types.update_component_output.UpdateComponentOutput":
        """<p>Update a component.</p> <p>There are a few modes for updating a component. The <code>deploymentType</code> field defines the mode.</p> <note> <p>You can't update a component while its deployment status, or the deployment status of a service instance attached to it, is <code>IN_PROGRESS</code>.</p> </note> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the component to update.</p>
            deployment_type: <p>The deployment type. It defines the mode for updating a component, as follows:</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated. You can only specify <code>description</code> in this mode.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the component is deployed and updated with the new <code>serviceSpec</code>, <code>templateSource</code>, and/or <code>type</code> that you provide. Only requested parameters are updated.</p> </dd> </dl>
            description: <p>An optional customer-provided description of the component.</p>
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated with. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both <code>serviceInstanceName</code> and <code>serviceName</code> or for neither of them.</p>
            service_instance_name: <p>The name of the service instance that you want to attach this component to. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both <code>serviceInstanceName</code> and <code>serviceName</code> or for neither of them.</p>
            service_spec: <p>The service spec that you want the component to use to access service inputs. Set this only when the component is attached to a service instance.</p>
            template_file: <p>A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.</p> <note> <p>Components support a single IaC file, even if you use Terraform as your template language.</p> </note>
            client_token: <p>The client token for the updated component.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.update_component_input.UpdateComponentInput]') -> OperationResponse["aws_sdk_proton.types.update_component_output.UpdateComponentOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.update_component
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.update_component.update_component(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_component_input.UpdateComponentInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["deployment_type"] = deployment_type
        if description is not None:
            input["description"] = description
        if service_name is not None:
            input["service_name"] = service_name
        if service_instance_name is not None:
            input["service_instance_name"] = service_instance_name
        if service_spec is not None:
            input["service_spec"] = service_spec
        if template_file is not None:
            input["template_file"] = template_file
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.delete_component_output.DeleteComponentOutput":
        """<p>Delete an Proton component resource.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the component to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.delete_component_input.DeleteComponentInput]') -> OperationResponse["aws_sdk_proton.types.delete_component_output.DeleteComponentOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_component
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.delete_component.delete_component(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.delete_component_input.DeleteComponentInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[ProtonClientConfig] = None, next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None, environment_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, service_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, service_instance_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, max_results: Optional["aws_sdk_proton.types.max_page_results.MaxPageResults"] = None) -> "aws_sdk_proton.types.list_components_output.ListComponentsOutput":
        """<p>List components with summary data. You can filter the result list by environment, service, or a single service instance.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            next_token: <p>A token that indicates the location of the next component in the array of components, after the list of components that was previously requested.</p>
            environment_name: <p>The name of an environment for result list filtering. Proton returns components associated with the environment or attached to service instances running in it.</p>
            service_name: <p>The name of a service for result list filtering. Proton returns components attached to service instances of the service.</p>
            service_instance_name: <p>The name of a service instance for result list filtering. Proton returns the component attached to the service instance, if any.</p>
            max_results: <p>The maximum number of components to list.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.list_components_input.ListComponentsInput]') -> OperationResponse["aws_sdk_proton.types.list_components_output.ListComponentsOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.list_components
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.list_components.list_components(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.list_components_input.ListComponentsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if environment_name is not None:
            input["environment_name"] = environment_name
        if service_name is not None:
            input["service_name"] = service_name
        if service_instance_name is not None:
            input["service_instance_name"] = service_instance_name
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncComponentResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service
    async def put(self, name: "aws_sdk_proton.types.resource_name.ResourceName", template_file: "aws_sdk_proton.types.template_file_contents.TemplateFileContents", manifest: "aws_sdk_proton.types.template_manifest_contents.TemplateManifestContents", *, config_overrides: Optional[AsyncProtonClientConfig] = None, description: Optional["aws_sdk_proton.types.description.Description"] = None, service_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, service_instance_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, environment_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, service_spec: Optional["aws_sdk_proton.types.spec_contents.SpecContents"] = None, tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None, client_token: Optional["aws_sdk_proton.types.client_token.ClientToken"] = None) -> "aws_sdk_proton.types.create_component_output.CreateComponentOutput":
        """<p>Create an Proton component. A component is an infrastructure extension for a service instance.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The customer-provided name of the component.</p>
            description: <p>An optional customer-provided description of the component.</p>
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated with. If you don't specify this, the component isn't attached to any service instance. Specify both <code>serviceInstanceName</code> and <code>serviceName</code> or neither of them.</p>
            service_instance_name: <p>The name of the service instance that you want to attach this component to. If you don't specify this, the component isn't attached to any service instance. Specify both <code>serviceInstanceName</code> and <code>serviceName</code> or neither of them.</p>
            environment_name: <p>The name of the Proton environment that you want to associate this component with. You must specify this when you don't specify <code>serviceInstanceName</code> and <code>serviceName</code>.</p>
            template_file: <p>A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.</p> <note> <p>Components support a single IaC file, even if you use Terraform as your template language.</p> </note>
            manifest: <p>A path to a manifest file that lists the Infrastructure as Code (IaC) file, template language, and rendering engine for infrastructure that a custom component provisions.</p>
            service_spec: <p>The service spec that you want the component to use to access service inputs. Set this only when you attach the component to a service instance.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton component. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            client_token: <p>The client token for the created component.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.create_component_input.CreateComponentInput]') -> AsyncOperationResponse["aws_sdk_proton.types.create_component_output.CreateComponentOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.create_component
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.create_component.async_create_component(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_component_input.CreateComponentInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if service_name is not None:
            input["service_name"] = service_name
        if service_instance_name is not None:
            input["service_instance_name"] = service_instance_name
        if environment_name is not None:
            input["environment_name"] = environment_name
        input["template_file"] = template_file
        input["manifest"] = manifest
        if service_spec is not None:
            input["service_spec"] = service_spec
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.get_component_output.GetComponentOutput":
        """<p>Get detailed data for a component.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the component that you want to get the detailed data for.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.get_component_input.GetComponentInput]') -> AsyncOperationResponse["aws_sdk_proton.types.get_component_output.GetComponentOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.get_component
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.get_component.async_get_component(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_component_input.GetComponentInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, name: "aws_sdk_proton.types.resource_name.ResourceName", deployment_type: "aws_sdk_proton.types.component_deployment_update_type.ComponentDeploymentUpdateType", *, config_overrides: Optional[AsyncProtonClientConfig] = None, description: Optional["aws_sdk_proton.types.description.Description"] = None, service_name: Optional["aws_sdk_proton.types.resource_name_or_empty.ResourceNameOrEmpty"] = None, service_instance_name: Optional["aws_sdk_proton.types.resource_name_or_empty.ResourceNameOrEmpty"] = None, service_spec: Optional["aws_sdk_proton.types.spec_contents.SpecContents"] = None, template_file: Optional["aws_sdk_proton.types.template_file_contents.TemplateFileContents"] = None, client_token: Optional["aws_sdk_proton.types.client_token.ClientToken"] = None) -> "aws_sdk_proton.types.update_component_output.UpdateComponentOutput":
        """<p>Update a component.</p> <p>There are a few modes for updating a component. The <code>deploymentType</code> field defines the mode.</p> <note> <p>You can't update a component while its deployment status, or the deployment status of a service instance attached to it, is <code>IN_PROGRESS</code>.</p> </note> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the component to update.</p>
            deployment_type: <p>The deployment type. It defines the mode for updating a component, as follows:</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated. You can only specify <code>description</code> in this mode.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the component is deployed and updated with the new <code>serviceSpec</code>, <code>templateSource</code>, and/or <code>type</code> that you provide. Only requested parameters are updated.</p> </dd> </dl>
            description: <p>An optional customer-provided description of the component.</p>
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated with. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both <code>serviceInstanceName</code> and <code>serviceName</code> or for neither of them.</p>
            service_instance_name: <p>The name of the service instance that you want to attach this component to. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both <code>serviceInstanceName</code> and <code>serviceName</code> or for neither of them.</p>
            service_spec: <p>The service spec that you want the component to use to access service inputs. Set this only when the component is attached to a service instance.</p>
            template_file: <p>A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.</p> <note> <p>Components support a single IaC file, even if you use Terraform as your template language.</p> </note>
            client_token: <p>The client token for the updated component.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.update_component_input.UpdateComponentInput]') -> AsyncOperationResponse["aws_sdk_proton.types.update_component_output.UpdateComponentOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.update_component
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.update_component.async_update_component(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_component_input.UpdateComponentInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["deployment_type"] = deployment_type
        if description is not None:
            input["description"] = description
        if service_name is not None:
            input["service_name"] = service_name
        if service_instance_name is not None:
            input["service_instance_name"] = service_instance_name
        if service_spec is not None:
            input["service_spec"] = service_spec
        if template_file is not None:
            input["template_file"] = template_file
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.delete_component_output.DeleteComponentOutput":
        """<p>Delete an Proton component resource.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the component to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.delete_component_input.DeleteComponentInput]') -> AsyncOperationResponse["aws_sdk_proton.types.delete_component_output.DeleteComponentOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_component
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.delete_component.async_delete_component(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.delete_component_input.DeleteComponentInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncProtonClientConfig] = None, next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None, environment_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, service_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, service_instance_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, max_results: Optional["aws_sdk_proton.types.max_page_results.MaxPageResults"] = None) -> "aws_sdk_proton.types.list_components_output.ListComponentsOutput":
        """<p>List components with summary data. You can filter the result list by environment, service, or a single service instance.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            next_token: <p>A token that indicates the location of the next component in the array of components, after the list of components that was previously requested.</p>
            environment_name: <p>The name of an environment for result list filtering. Proton returns components associated with the environment or attached to service instances running in it.</p>
            service_name: <p>The name of a service for result list filtering. Proton returns components attached to service instances of the service.</p>
            service_instance_name: <p>The name of a service instance for result list filtering. Proton returns the component attached to the service instance, if any.</p>
            max_results: <p>The maximum number of components to list.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.list_components_input.ListComponentsInput]') -> AsyncOperationResponse["aws_sdk_proton.types.list_components_output.ListComponentsOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.list_components
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.list_components.async_list_components(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.list_components_input.ListComponentsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if environment_name is not None:
            input["environment_name"] = environment_name
        if service_name is not None:
            input["service_name"] = service_name
        if service_instance_name is not None:
            input["service_instance_name"] = service_instance_name
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output