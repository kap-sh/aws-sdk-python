from typing import Optional, TYPE_CHECKING
from aws_sdk_proton._services.async_proton import ensure_async_iterator
from aws_sdk_proton._services.proton import ensure_sync_iterator
from aws_sdk_proton._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
if TYPE_CHECKING:
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig
    from aws_sdk_proton._services.async_proton import AsyncProtonClient, AsyncProtonClientConfig
    import aws_sdk_proton.types.client_token
    import aws_sdk_proton.types.create_service_instance_input
    import aws_sdk_proton.types.create_service_instance_output
    import aws_sdk_proton.types.deployment_update_type
    import aws_sdk_proton.types.get_service_instance_input
    import aws_sdk_proton.types.get_service_instance_output
    import aws_sdk_proton.types.list_service_instances_filter_list
    import aws_sdk_proton.types.list_service_instances_input
    import aws_sdk_proton.types.list_service_instances_output
    import aws_sdk_proton.types.list_service_instances_sort_by
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.service_instance_summary
    import aws_sdk_proton.types.sort_order
    import aws_sdk_proton.types.spec_contents
    import aws_sdk_proton.types.tag_list
    import aws_sdk_proton.types.template_version_part
    import aws_sdk_proton.types.update_service_instance_input
    import aws_sdk_proton.types.update_service_instance_output

class ServiceInstanceResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service
    def put(self, name: "aws_sdk_proton.types.resource_name.ResourceName", service_name: "aws_sdk_proton.types.resource_name.ResourceName", spec: "aws_sdk_proton.types.spec_contents.SpecContents", *, config_overrides: Optional[ProtonClientConfig] = None, template_major_version: Optional["aws_sdk_proton.types.template_version_part.TemplateVersionPart"] = None, template_minor_version: Optional["aws_sdk_proton.types.template_version_part.TemplateVersionPart"] = None, tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None, client_token: Optional["aws_sdk_proton.types.client_token.ClientToken"] = None) -> "aws_sdk_proton.types.create_service_instance_output.CreateServiceInstanceOutput":
        """<p>Create a service instance.</p>

        Args:
            name: <p>The name of the service instance to create.</p>
            service_name: <p>The name of the service the service instance is added to.</p>
            spec: <p>The spec for the service instance you want to create.</p>
            template_major_version: <p>To create a new major and minor version of the service template, <i>exclude</i> <code>major Version</code>.</p>
            template_minor_version: <p>To create a new minor version of the service template, include a <code>major Version</code>.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service instance. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            client_token: <p>The client token of the service instance to create.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.create_service_instance_input.CreateServiceInstanceInput]') -> OperationResponse["aws_sdk_proton.types.create_service_instance_output.CreateServiceInstanceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.create_service_instance
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.create_service_instance.create_service_instance(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_service_instance_input.CreateServiceInstanceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["service_name"] = service_name
        input["spec"] = spec
        if template_major_version is not None:
            input["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input["template_minor_version"] = template_minor_version
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, name: "aws_sdk_proton.types.resource_name.ResourceName", service_name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.get_service_instance_output.GetServiceInstanceOutput":
        """<p>Get detailed data for a service instance. A service instance is an instantiation of service template and it runs in a specific environment.</p>

        Args:
            name: <p>The name of a service instance that you want to get the detailed data for.</p>
            service_name: <p>The name of the service that you want the service instance input for.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.get_service_instance_input.GetServiceInstanceInput]') -> OperationResponse["aws_sdk_proton.types.get_service_instance_output.GetServiceInstanceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service_instance
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.get_service_instance.get_service_instance(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_service_instance_input.GetServiceInstanceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["service_name"] = service_name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, name: "aws_sdk_proton.types.resource_name.ResourceName", service_name: "aws_sdk_proton.types.resource_name.ResourceName", deployment_type: "aws_sdk_proton.types.deployment_update_type.DeploymentUpdateType", *, config_overrides: Optional[ProtonClientConfig] = None, spec: Optional["aws_sdk_proton.types.spec_contents.SpecContents"] = None, template_major_version: Optional["aws_sdk_proton.types.template_version_part.TemplateVersionPart"] = None, template_minor_version: Optional["aws_sdk_proton.types.template_version_part.TemplateVersionPart"] = None, client_token: Optional["aws_sdk_proton.types.client_token.ClientToken"] = None) -> "aws_sdk_proton.types.update_service_instance_output.UpdateServiceInstanceOutput":
        """<p>Update a service instance.</p> <p>There are a few modes for updating a service instance. The <code>deploymentType</code> field defines the mode.</p> <note> <p>You can't update a service instance while its deployment status, or the deployment status of a component attached to it, is <code>IN_PROGRESS</code>.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service instance to update.</p>
            service_name: <p>The name of the service that the service instance belongs to.</p>
            deployment_type: <p>The deployment type. It defines the mode for updating a service instance, as follows:</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this deployment type.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>
            spec: <p>The formatted specification that defines the service instance update.</p>
            template_major_version: <p>The major version of the service template to update.</p>
            template_minor_version: <p>The minor version of the service template to update.</p>
            client_token: <p>The client token of the service instance to update.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.update_service_instance_input.UpdateServiceInstanceInput]') -> OperationResponse["aws_sdk_proton.types.update_service_instance_output.UpdateServiceInstanceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service_instance
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.update_service_instance.update_service_instance(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_service_instance_input.UpdateServiceInstanceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["service_name"] = service_name
        input["deployment_type"] = deployment_type
        if spec is not None:
            input["spec"] = spec
        if template_major_version is not None:
            input["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input["template_minor_version"] = template_minor_version
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[ProtonClientConfig] = None, service_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_proton.types.max_page_results.MaxPageResults"] = None, filters: Optional["aws_sdk_proton.types.list_service_instances_filter_list.ListServiceInstancesFilterList"] = None, sort_by: Optional["aws_sdk_proton.types.list_service_instances_sort_by.ListServiceInstancesSortBy"] = None, sort_order: Optional["aws_sdk_proton.types.sort_order.SortOrder"] = None) -> "aws_sdk_proton.types.list_service_instances_output.ListServiceInstancesOutput":
        """<p>List service instances with summary data. This action lists service instances of all services in the Amazon Web Services account.</p>

        Args:
            service_name: <p>The name of the service that the service instance belongs to.</p>
            next_token: <p>A token that indicates the location of the next service in the array of service instances, after the list of service instances that was previously requested.</p>
            max_results: <p>The maximum number of service instances to list.</p>
            filters: <p>An array of filtering criteria that scope down the result list. By default, all service instances in the Amazon Web Services account are returned.</p>
            sort_by: <p>The field that the result list is sorted by.</p> <p>When you choose to sort by <code>serviceName</code>, service instances within each service are sorted by service instance name.</p> <p>Default: <code>serviceName</code> </p>
            sort_order: <p>Result list sort order.</p> <p>Default: <code>ASCENDING</code> </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.list_service_instances_input.ListServiceInstancesInput]') -> OperationResponse["aws_sdk_proton.types.list_service_instances_output.ListServiceInstancesOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.list_service_instances
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.list_service_instances.list_service_instances(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.list_service_instances_input.ListServiceInstancesInput = {}  # type: ignore[typeddict-item]
        if service_name is not None:
            input["service_name"] = service_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if filters is not None:
            input["filters"] = filters
        if sort_by is not None:
            input["sort_by"] = sort_by
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncServiceInstanceResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service
    async def put(self, name: "aws_sdk_proton.types.resource_name.ResourceName", service_name: "aws_sdk_proton.types.resource_name.ResourceName", spec: "aws_sdk_proton.types.spec_contents.SpecContents", *, config_overrides: Optional[AsyncProtonClientConfig] = None, template_major_version: Optional["aws_sdk_proton.types.template_version_part.TemplateVersionPart"] = None, template_minor_version: Optional["aws_sdk_proton.types.template_version_part.TemplateVersionPart"] = None, tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None, client_token: Optional["aws_sdk_proton.types.client_token.ClientToken"] = None) -> "aws_sdk_proton.types.create_service_instance_output.CreateServiceInstanceOutput":
        """<p>Create a service instance.</p>

        Args:
            name: <p>The name of the service instance to create.</p>
            service_name: <p>The name of the service the service instance is added to.</p>
            spec: <p>The spec for the service instance you want to create.</p>
            template_major_version: <p>To create a new major and minor version of the service template, <i>exclude</i> <code>major Version</code>.</p>
            template_minor_version: <p>To create a new minor version of the service template, include a <code>major Version</code>.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service instance. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            client_token: <p>The client token of the service instance to create.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.create_service_instance_input.CreateServiceInstanceInput]') -> AsyncOperationResponse["aws_sdk_proton.types.create_service_instance_output.CreateServiceInstanceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.create_service_instance
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.create_service_instance.async_create_service_instance(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_service_instance_input.CreateServiceInstanceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["service_name"] = service_name
        input["spec"] = spec
        if template_major_version is not None:
            input["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input["template_minor_version"] = template_minor_version
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, name: "aws_sdk_proton.types.resource_name.ResourceName", service_name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.get_service_instance_output.GetServiceInstanceOutput":
        """<p>Get detailed data for a service instance. A service instance is an instantiation of service template and it runs in a specific environment.</p>

        Args:
            name: <p>The name of a service instance that you want to get the detailed data for.</p>
            service_name: <p>The name of the service that you want the service instance input for.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.get_service_instance_input.GetServiceInstanceInput]') -> AsyncOperationResponse["aws_sdk_proton.types.get_service_instance_output.GetServiceInstanceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service_instance
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.get_service_instance.async_get_service_instance(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_service_instance_input.GetServiceInstanceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["service_name"] = service_name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, name: "aws_sdk_proton.types.resource_name.ResourceName", service_name: "aws_sdk_proton.types.resource_name.ResourceName", deployment_type: "aws_sdk_proton.types.deployment_update_type.DeploymentUpdateType", *, config_overrides: Optional[AsyncProtonClientConfig] = None, spec: Optional["aws_sdk_proton.types.spec_contents.SpecContents"] = None, template_major_version: Optional["aws_sdk_proton.types.template_version_part.TemplateVersionPart"] = None, template_minor_version: Optional["aws_sdk_proton.types.template_version_part.TemplateVersionPart"] = None, client_token: Optional["aws_sdk_proton.types.client_token.ClientToken"] = None) -> "aws_sdk_proton.types.update_service_instance_output.UpdateServiceInstanceOutput":
        """<p>Update a service instance.</p> <p>There are a few modes for updating a service instance. The <code>deploymentType</code> field defines the mode.</p> <note> <p>You can't update a service instance while its deployment status, or the deployment status of a component attached to it, is <code>IN_PROGRESS</code>.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service instance to update.</p>
            service_name: <p>The name of the service that the service instance belongs to.</p>
            deployment_type: <p>The deployment type. It defines the mode for updating a service instance, as follows:</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this deployment type.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service instance is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>
            spec: <p>The formatted specification that defines the service instance update.</p>
            template_major_version: <p>The major version of the service template to update.</p>
            template_minor_version: <p>The minor version of the service template to update.</p>
            client_token: <p>The client token of the service instance to update.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.update_service_instance_input.UpdateServiceInstanceInput]') -> AsyncOperationResponse["aws_sdk_proton.types.update_service_instance_output.UpdateServiceInstanceOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service_instance
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.update_service_instance.async_update_service_instance(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_service_instance_input.UpdateServiceInstanceInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["service_name"] = service_name
        input["deployment_type"] = deployment_type
        if spec is not None:
            input["spec"] = spec
        if template_major_version is not None:
            input["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input["template_minor_version"] = template_minor_version
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncProtonClientConfig] = None, service_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_proton.types.max_page_results.MaxPageResults"] = None, filters: Optional["aws_sdk_proton.types.list_service_instances_filter_list.ListServiceInstancesFilterList"] = None, sort_by: Optional["aws_sdk_proton.types.list_service_instances_sort_by.ListServiceInstancesSortBy"] = None, sort_order: Optional["aws_sdk_proton.types.sort_order.SortOrder"] = None) -> "aws_sdk_proton.types.list_service_instances_output.ListServiceInstancesOutput":
        """<p>List service instances with summary data. This action lists service instances of all services in the Amazon Web Services account.</p>

        Args:
            service_name: <p>The name of the service that the service instance belongs to.</p>
            next_token: <p>A token that indicates the location of the next service in the array of service instances, after the list of service instances that was previously requested.</p>
            max_results: <p>The maximum number of service instances to list.</p>
            filters: <p>An array of filtering criteria that scope down the result list. By default, all service instances in the Amazon Web Services account are returned.</p>
            sort_by: <p>The field that the result list is sorted by.</p> <p>When you choose to sort by <code>serviceName</code>, service instances within each service are sorted by service instance name.</p> <p>Default: <code>serviceName</code> </p>
            sort_order: <p>Result list sort order.</p> <p>Default: <code>ASCENDING</code> </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.list_service_instances_input.ListServiceInstancesInput]') -> AsyncOperationResponse["aws_sdk_proton.types.list_service_instances_output.ListServiceInstancesOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.list_service_instances
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.list_service_instances.async_list_service_instances(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.list_service_instances_input.ListServiceInstancesInput = {}  # type: ignore[typeddict-item]
        if service_name is not None:
            input["service_name"] = service_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if filters is not None:
            input["filters"] = filters
        if sort_by is not None:
            input["sort_by"] = sort_by
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output