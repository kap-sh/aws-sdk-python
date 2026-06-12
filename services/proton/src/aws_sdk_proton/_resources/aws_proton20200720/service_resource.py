from typing import Optional, TYPE_CHECKING
from aws_sdk_proton._services.async_proton import ensure_async_iterator
from aws_sdk_proton._services.proton import ensure_sync_iterator
from aws_sdk_proton._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
if TYPE_CHECKING:
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig
    from aws_sdk_proton._services.async_proton import AsyncProtonClient, AsyncProtonClientConfig
    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.create_service_input
    import aws_sdk_proton.types.create_service_output
    import aws_sdk_proton.types.delete_service_input
    import aws_sdk_proton.types.delete_service_output
    import aws_sdk_proton.types.description
    import aws_sdk_proton.types.get_service_input
    import aws_sdk_proton.types.get_service_output
    import aws_sdk_proton.types.git_branch_name
    import aws_sdk_proton.types.list_services_input
    import aws_sdk_proton.types.list_services_output
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.repository_id
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.service_summary
    import aws_sdk_proton.types.spec_contents
    import aws_sdk_proton.types.tag_list
    import aws_sdk_proton.types.template_version_part
    import aws_sdk_proton.types.update_service_input
    import aws_sdk_proton.types.update_service_output

class ServiceResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service
    def put(self, name: "aws_sdk_proton.types.resource_name.ResourceName", template_name: "aws_sdk_proton.types.resource_name.ResourceName", template_major_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart", spec: "aws_sdk_proton.types.spec_contents.SpecContents", *, config_overrides: Optional[ProtonClientConfig] = None, description: Optional["aws_sdk_proton.types.description.Description"] = None, template_minor_version: Optional["aws_sdk_proton.types.template_version_part.TemplateVersionPart"] = None, repository_connection_arn: Optional["aws_sdk_proton.types.arn.Arn"] = None, repository_id: Optional["aws_sdk_proton.types.repository_id.RepositoryId"] = None, branch_name: Optional["aws_sdk_proton.types.git_branch_name.GitBranchName"] = None, tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None) -> "aws_sdk_proton.types.create_service_output.CreateServiceOutput":
        """<p>Create an Proton service. An Proton service is an instantiation of a service template and often includes several service instances and pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-services.html\">Services</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The service name.</p>
            description: <p>A description of the Proton service.</p>
            template_name: <p>The name of the service template that's used to create the service.</p>
            template_major_version: <p>The major version of the service template that was used to create the service.</p>
            template_minor_version: <p>The minor version of the service template that was used to create the service.</p>
            spec: <p>A link to a spec file that provides inputs as defined in the service template bundle schema file. The spec file is in YAML format. <i>Don’t</i> include pipeline inputs in the spec if your service template <i>doesn’t</i> include a service pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-create-svc.html\">Create a service</a> in the <i>Proton User Guide</i>.</p>
            repository_connection_arn: <p>The Amazon Resource Name (ARN) of the repository connection. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html#setting-up-vcontrol\">Setting up an AWS CodeStar connection</a> in the <i>Proton User Guide</i>. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>
            repository_id: <p>The ID of the code repository. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>
            branch_name: <p>The name of the code repository branch that holds the code that's deployed in Proton. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.create_service_input.CreateServiceInput]') -> OperationResponse["aws_sdk_proton.types.create_service_output.CreateServiceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.create_service
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.create_service.create_service(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_service_input.CreateServiceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["template_name"] = template_name
        input["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input["template_minor_version"] = template_minor_version
        input["spec"] = spec
        if repository_connection_arn is not None:
            input["repository_connection_arn"] = repository_connection_arn
        if repository_id is not None:
            input["repository_id"] = repository_id
        if branch_name is not None:
            input["branch_name"] = branch_name
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.get_service_output.GetServiceOutput":
        """<p>Get detailed data for a service.</p>

        Args:
            name: <p>The name of the service that you want to get the detailed data for.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.get_service_input.GetServiceInput]') -> OperationResponse["aws_sdk_proton.types.get_service_output.GetServiceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.get_service.get_service(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_service_input.GetServiceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[ProtonClientConfig] = None, description: Optional["aws_sdk_proton.types.description.Description"] = None, spec: Optional["aws_sdk_proton.types.spec_contents.SpecContents"] = None) -> "aws_sdk_proton.types.update_service_output.UpdateServiceOutput":
        """<p>Edit a service description or use a spec to add and delete service instances.</p> <note> <p>Existing service instances and the service pipeline <i>can't</i> be edited using this API. They can only be deleted.</p> </note> <p>Use the <code>description</code> parameter to modify the description.</p> <p>Edit the <code>spec</code> parameter to add or delete instances.</p> <note> <p>You can't delete a service instance (remove it from the spec) if it has an attached component.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service to edit.</p>
            description: <p>The edited service description.</p>
            spec: <p>Lists the service instances to add and the existing service instances to remain. Omit the existing service instances to delete from the list. <i>Don't</i> include edits to the existing service instances or pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-update.html\">Edit a service</a> in the <i>Proton User Guide</i>.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.update_service_input.UpdateServiceInput]') -> OperationResponse["aws_sdk_proton.types.update_service_output.UpdateServiceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.update_service.update_service(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_service_input.UpdateServiceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if spec is not None:
            input["spec"] = spec

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.delete_service_output.DeleteServiceOutput":
        """<p>Delete a service, with its instances and pipeline.</p> <note> <p>You can't delete a service if it has any service instances that have components attached to them.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.delete_service_input.DeleteServiceInput]') -> OperationResponse["aws_sdk_proton.types.delete_service_output.DeleteServiceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_service
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.delete_service.delete_service(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.delete_service_input.DeleteServiceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[ProtonClientConfig] = None, next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_proton.types.max_page_results.MaxPageResults"] = None) -> "aws_sdk_proton.types.list_services_output.ListServicesOutput":
        """<p>List services with summaries of detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next service in the array of services, after the list of services that was previously requested.</p>
            max_results: <p>The maximum number of services to list.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.list_services_input.ListServicesInput]') -> OperationResponse["aws_sdk_proton.types.list_services_output.ListServicesOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.list_services
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.list_services.list_services(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.list_services_input.ListServicesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncServiceResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service
    async def put(self, name: "aws_sdk_proton.types.resource_name.ResourceName", template_name: "aws_sdk_proton.types.resource_name.ResourceName", template_major_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart", spec: "aws_sdk_proton.types.spec_contents.SpecContents", *, config_overrides: Optional[AsyncProtonClientConfig] = None, description: Optional["aws_sdk_proton.types.description.Description"] = None, template_minor_version: Optional["aws_sdk_proton.types.template_version_part.TemplateVersionPart"] = None, repository_connection_arn: Optional["aws_sdk_proton.types.arn.Arn"] = None, repository_id: Optional["aws_sdk_proton.types.repository_id.RepositoryId"] = None, branch_name: Optional["aws_sdk_proton.types.git_branch_name.GitBranchName"] = None, tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None) -> "aws_sdk_proton.types.create_service_output.CreateServiceOutput":
        """<p>Create an Proton service. An Proton service is an instantiation of a service template and often includes several service instances and pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-services.html\">Services</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The service name.</p>
            description: <p>A description of the Proton service.</p>
            template_name: <p>The name of the service template that's used to create the service.</p>
            template_major_version: <p>The major version of the service template that was used to create the service.</p>
            template_minor_version: <p>The minor version of the service template that was used to create the service.</p>
            spec: <p>A link to a spec file that provides inputs as defined in the service template bundle schema file. The spec file is in YAML format. <i>Don’t</i> include pipeline inputs in the spec if your service template <i>doesn’t</i> include a service pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-create-svc.html\">Create a service</a> in the <i>Proton User Guide</i>.</p>
            repository_connection_arn: <p>The Amazon Resource Name (ARN) of the repository connection. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html#setting-up-vcontrol\">Setting up an AWS CodeStar connection</a> in the <i>Proton User Guide</i>. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>
            repository_id: <p>The ID of the code repository. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>
            branch_name: <p>The name of the code repository branch that holds the code that's deployed in Proton. <i>Don't</i> include this parameter if your service template <i>doesn't</i> include a service pipeline.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.create_service_input.CreateServiceInput]') -> AsyncOperationResponse["aws_sdk_proton.types.create_service_output.CreateServiceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.create_service
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.create_service.async_create_service(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_service_input.CreateServiceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["template_name"] = template_name
        input["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input["template_minor_version"] = template_minor_version
        input["spec"] = spec
        if repository_connection_arn is not None:
            input["repository_connection_arn"] = repository_connection_arn
        if repository_id is not None:
            input["repository_id"] = repository_id
        if branch_name is not None:
            input["branch_name"] = branch_name
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.get_service_output.GetServiceOutput":
        """<p>Get detailed data for a service.</p>

        Args:
            name: <p>The name of the service that you want to get the detailed data for.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.get_service_input.GetServiceInput]') -> AsyncOperationResponse["aws_sdk_proton.types.get_service_output.GetServiceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.get_service.async_get_service(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_service_input.GetServiceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[AsyncProtonClientConfig] = None, description: Optional["aws_sdk_proton.types.description.Description"] = None, spec: Optional["aws_sdk_proton.types.spec_contents.SpecContents"] = None) -> "aws_sdk_proton.types.update_service_output.UpdateServiceOutput":
        """<p>Edit a service description or use a spec to add and delete service instances.</p> <note> <p>Existing service instances and the service pipeline <i>can't</i> be edited using this API. They can only be deleted.</p> </note> <p>Use the <code>description</code> parameter to modify the description.</p> <p>Edit the <code>spec</code> parameter to add or delete instances.</p> <note> <p>You can't delete a service instance (remove it from the spec) if it has an attached component.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service to edit.</p>
            description: <p>The edited service description.</p>
            spec: <p>Lists the service instances to add and the existing service instances to remain. Omit the existing service instances to delete from the list. <i>Don't</i> include edits to the existing service instances or pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-update.html\">Edit a service</a> in the <i>Proton User Guide</i>.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.update_service_input.UpdateServiceInput]') -> AsyncOperationResponse["aws_sdk_proton.types.update_service_output.UpdateServiceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.update_service.async_update_service(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_service_input.UpdateServiceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if spec is not None:
            input["spec"] = spec

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.delete_service_output.DeleteServiceOutput":
        """<p>Delete a service, with its instances and pipeline.</p> <note> <p>You can't delete a service if it has any service instances that have components attached to them.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.delete_service_input.DeleteServiceInput]') -> AsyncOperationResponse["aws_sdk_proton.types.delete_service_output.DeleteServiceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_service
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.delete_service.async_delete_service(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.delete_service_input.DeleteServiceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncProtonClientConfig] = None, next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_proton.types.max_page_results.MaxPageResults"] = None) -> "aws_sdk_proton.types.list_services_output.ListServicesOutput":
        """<p>List services with summaries of detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next service in the array of services, after the list of services that was previously requested.</p>
            max_results: <p>The maximum number of services to list.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.list_services_input.ListServicesInput]') -> AsyncOperationResponse["aws_sdk_proton.types.list_services_output.ListServicesOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.list_services
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.list_services.async_list_services(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.list_services_input.ListServicesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output