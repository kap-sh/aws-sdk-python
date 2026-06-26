from __future__ import annotations

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
    from aws_sdk_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig


class ServiceResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def put(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        template_name: "aws_sdk_proton.types.resource_name.ResourceName",
        template_major_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart",
        spec: "aws_sdk_proton.types.spec_contents.SpecContents",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        description: Optional["aws_sdk_proton.types.description.Description"] = None,
        template_minor_version: Optional[
            "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        repository_connection_arn: Optional["aws_sdk_proton.types.arn.Arn"] = None,
        repository_id: Optional[
            "aws_sdk_proton.types.repository_id.RepositoryId"
        ] = None,
        branch_name: Optional[
            "aws_sdk_proton.types.git_branch_name.GitBranchName"
        ] = None,
        tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_proton.types.create_service_output.CreateServiceOutput":
        r"""<p>Create an Proton service. An Proton service is an instantiation of a service template and often includes several service instances and pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-services.html\">Services</a> in the <i>Proton User Guide</i>.</p>

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

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            aws_sdk_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html\">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.create_service_input.CreateServiceInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.create_service_output.CreateServiceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.create_service

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.create_service.create_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.create_service_input.CreateServiceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["template_name"] = template_name
        input_["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
        input_["spec"] = spec
        if repository_connection_arn is not None:
            input_["repository_connection_arn"] = repository_connection_arn
        if repository_id is not None:
            input_["repository_id"] = repository_id
        if branch_name is not None:
            input_["branch_name"] = branch_name
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
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.get_service_output.GetServiceOutput":
        """<p>Get detailed data for a service.</p>

        Args:
            name: <p>The name of the service that you want to get the detailed data for.</p>

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.get_service_input.GetServiceInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.get_service_output.GetServiceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.get_service_input.GetServiceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        description: Optional["aws_sdk_proton.types.description.Description"] = None,
        spec: Optional["aws_sdk_proton.types.spec_contents.SpecContents"] = None,
    ) -> "aws_sdk_proton.types.update_service_output.UpdateServiceOutput":
        r"""<p>Edit a service description or use a spec to add and delete service instances.</p> <note> <p>Existing service instances and the service pipeline <i>can't</i> be edited using this API. They can only be deleted.</p> </note> <p>Use the <code>description</code> parameter to modify the description.</p> <p>Edit the <code>spec</code> parameter to add or delete instances.</p> <note> <p>You can't delete a service instance (remove it from the spec) if it has an attached component.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service to edit.</p>
            description: <p>The edited service description.</p>
            spec: <p>Lists the service instances to add and the existing service instances to remain. Omit the existing service instances to delete from the list. <i>Don't</i> include edits to the existing service instances or pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-update.html\">Edit a service</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            aws_sdk_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html\">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.update_service_input.UpdateServiceInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.update_service_output.UpdateServiceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.update_service.update_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.update_service_input.UpdateServiceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if spec is not None:
            input_["spec"] = spec

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.delete_service_output.DeleteServiceOutput":
        r"""<p>Delete a service, with its instances and pipeline.</p> <note> <p>You can't delete a service if it has any service instances that have components attached to them.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service to delete.</p>

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.delete_service_input.DeleteServiceInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.delete_service_output.DeleteServiceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_service

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.delete_service.delete_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.delete_service_input.DeleteServiceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
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
    ) -> "aws_sdk_proton.types.list_services_output.ListServicesOutput":
        """<p>List services with summaries of detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next service in the array of services, after the list of services that was previously requested.</p>
            max_results: <p>The maximum number of services to list.</p>

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.list_services_input.ListServicesInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.list_services_output.ListServicesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_services

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_services_input.ListServicesInput = {}  # type: ignore[typeddict-item]
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


class AsyncServiceResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def put(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        template_name: "aws_sdk_proton.types.resource_name.ResourceName",
        template_major_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart",
        spec: "aws_sdk_proton.types.spec_contents.SpecContents",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["aws_sdk_proton.types.description.Description"] = None,
        template_minor_version: Optional[
            "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        repository_connection_arn: Optional["aws_sdk_proton.types.arn.Arn"] = None,
        repository_id: Optional[
            "aws_sdk_proton.types.repository_id.RepositoryId"
        ] = None,
        branch_name: Optional[
            "aws_sdk_proton.types.git_branch_name.GitBranchName"
        ] = None,
        tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_proton.types.create_service_output.CreateServiceOutput":
        r"""<p>Create an Proton service. An Proton service is an instantiation of a service template and often includes several service instances and pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-services.html\">Services</a> in the <i>Proton User Guide</i>.</p>

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

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            aws_sdk_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html\">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.create_service_input.CreateServiceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.create_service_output.CreateServiceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.create_service

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.create_service.async_create_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.create_service_input.CreateServiceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["template_name"] = template_name
        input_["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
        input_["spec"] = spec
        if repository_connection_arn is not None:
            input_["repository_connection_arn"] = repository_connection_arn
        if repository_id is not None:
            input_["repository_id"] = repository_id
        if branch_name is not None:
            input_["branch_name"] = branch_name
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
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.get_service_output.GetServiceOutput":
        """<p>Get detailed data for a service.</p>

        Args:
            name: <p>The name of the service that you want to get the detailed data for.</p>

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.get_service_input.GetServiceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.get_service_output.GetServiceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.get_service.async_get_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.get_service_input.GetServiceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["aws_sdk_proton.types.description.Description"] = None,
        spec: Optional["aws_sdk_proton.types.spec_contents.SpecContents"] = None,
    ) -> "aws_sdk_proton.types.update_service_output.UpdateServiceOutput":
        r"""<p>Edit a service description or use a spec to add and delete service instances.</p> <note> <p>Existing service instances and the service pipeline <i>can't</i> be edited using this API. They can only be deleted.</p> </note> <p>Use the <code>description</code> parameter to modify the description.</p> <p>Edit the <code>spec</code> parameter to add or delete instances.</p> <note> <p>You can't delete a service instance (remove it from the spec) if it has an attached component.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service to edit.</p>
            description: <p>The edited service description.</p>
            spec: <p>Lists the service instances to add and the existing service instances to remain. Omit the existing service instances to delete from the list. <i>Don't</i> include edits to the existing service instances or pipeline. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-update.html\">Edit a service</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            aws_sdk_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html\">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.update_service_input.UpdateServiceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.update_service_output.UpdateServiceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.update_service.async_update_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.update_service_input.UpdateServiceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if spec is not None:
            input_["spec"] = spec

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.delete_service_output.DeleteServiceOutput":
        r"""<p>Delete a service, with its instances and pipeline.</p> <note> <p>You can't delete a service if it has any service instances that have components attached to them.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            name: <p>The name of the service to delete.</p>

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.delete_service_input.DeleteServiceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.delete_service_output.DeleteServiceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_service

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.delete_service.async_delete_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.delete_service_input.DeleteServiceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
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
    ) -> "aws_sdk_proton.types.list_services_output.ListServicesOutput":
        """<p>List services with summaries of detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next service in the array of services, after the list of services that was previously requested.</p>
            max_results: <p>The maximum number of services to list.</p>

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.list_services_input.ListServicesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.list_services_output.ListServicesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_services

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_services_input.ListServicesInput = {}  # type: ignore[typeddict-item]
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
