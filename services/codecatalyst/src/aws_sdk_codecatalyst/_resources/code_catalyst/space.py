from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_codecatalyst._auth._signers
import aws_sdk_codecatalyst._auth._sigv4
from aws_sdk_codecatalyst._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.delete_space_request
    import aws_sdk_codecatalyst.types.delete_space_response
    import aws_sdk_codecatalyst.types.dev_environment_summary
    import aws_sdk_codecatalyst.types.filters
    import aws_sdk_codecatalyst.types.get_space_request
    import aws_sdk_codecatalyst.types.get_space_response
    import aws_sdk_codecatalyst.types.list_dev_environments_request
    import aws_sdk_codecatalyst.types.list_dev_environments_response
    import aws_sdk_codecatalyst.types.list_spaces_request
    import aws_sdk_codecatalyst.types.list_spaces_response
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.space_description
    import aws_sdk_codecatalyst.types.space_summary
    import aws_sdk_codecatalyst.types.update_space_request
    import aws_sdk_codecatalyst.types.update_space_response
    from aws_sdk_codecatalyst._services.async_code_catalyst import (
        AsyncCodeCatalystClient,
        AsyncCodeCatalystClientConfig,
    )
    from aws_sdk_codecatalyst._services.code_catalyst import (
        CodeCatalystClient,
        CodeCatalystClientConfig,
    )


class Space:
    def __init__(self, service: CodeCatalystClient) -> None:
        self._service = service

    def read(
        self,
        name: "aws_sdk_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "aws_sdk_codecatalyst.types.get_space_response.GetSpaceResponse":
        """<p>Returns information about an space.</p>

        Args:
            name: <p>The name of the space.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codecatalyst.types.get_space_request.GetSpaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_codecatalyst.types.get_space_response.GetSpaceResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.get_space

            output, http_response = (
                aws_sdk_codecatalyst._operations.code_catalyst.get_space.get_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.get_space_request.GetSpaceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        name: "aws_sdk_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        description: Optional[
            "aws_sdk_codecatalyst.types.space_description.SpaceDescription"
        ] = None,
    ) -> "aws_sdk_codecatalyst.types.update_space_response.UpdateSpaceResponse":
        """<p>Changes one or more values for a space.</p>

        Args:
            name: <p>The name of the space.</p>
            description: <p>The description of the space.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codecatalyst.types.update_space_request.UpdateSpaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_codecatalyst.types.update_space_response.UpdateSpaceResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.update_space

            output, http_response = (
                aws_sdk_codecatalyst._operations.code_catalyst.update_space.update_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.update_space_request.UpdateSpaceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        name: "aws_sdk_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "aws_sdk_codecatalyst.types.delete_space_response.DeleteSpaceResponse":
        """<p>Deletes a space.</p> <important> <p>Deleting a space cannot be undone. Additionally, since space names must be unique across Amazon CodeCatalyst, you cannot reuse names of deleted spaces.</p> </important>

        Args:
            name: <p>The name of the space. To retrieve a list of space names, use <a>ListSpaces</a>.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codecatalyst.types.delete_space_request.DeleteSpaceRequest]",
        ) -> OperationResponse[
            "aws_sdk_codecatalyst.types.delete_space_response.DeleteSpaceResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.delete_space

            output, http_response = (
                aws_sdk_codecatalyst._operations.code_catalyst.delete_space.delete_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.delete_space_request.DeleteSpaceRequest = {}  # type: ignore[typeddict-item]
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
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_codecatalyst.types.list_spaces_response.ListSpacesResponse":
        """<p>Retrieves a list of spaces.</p>

        Args:
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codecatalyst.types.list_spaces_request.ListSpacesRequest]",
        ) -> OperationResponse[
            "aws_sdk_codecatalyst.types.list_spaces_response.ListSpacesResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.list_spaces

            output, http_response = (
                aws_sdk_codecatalyst._operations.code_catalyst.list_spaces.list_spaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.list_spaces_request.ListSpacesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_dev_environments(
        self,
        space_name: "aws_sdk_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        project_name: Optional[
            "aws_sdk_codecatalyst.types.name_string.NameString"
        ] = None,
        filters: Optional["aws_sdk_codecatalyst.types.filters.Filters"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_codecatalyst.types.list_dev_environments_response.ListDevEnvironmentsResponse":
        """<p>Retrieves a list of Dev Environments in a project.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            filters: <p>Information about filters to apply to narrow the results returned in the list.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codecatalyst.types.list_dev_environments_request.ListDevEnvironmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_codecatalyst.types.list_dev_environments_response.ListDevEnvironmentsResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.list_dev_environments

            output, http_response = (
                aws_sdk_codecatalyst._operations.code_catalyst.list_dev_environments.list_dev_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.list_dev_environments_request.ListDevEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        input_["space_name"] = space_name
        if project_name is not None:
            input_["project_name"] = project_name
        if filters is not None:
            input_["filters"] = filters
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


class AsyncSpace:
    def __init__(self, service: AsyncCodeCatalystClient) -> None:
        self._service = service

    async def read(
        self,
        name: "aws_sdk_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
    ) -> "aws_sdk_codecatalyst.types.get_space_response.GetSpaceResponse":
        """<p>Returns information about an space.</p>

        Args:
            name: <p>The name of the space.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecatalyst.types.get_space_request.GetSpaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecatalyst.types.get_space_response.GetSpaceResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.get_space

            (
                output,
                http_response,
            ) = await aws_sdk_codecatalyst._operations.code_catalyst.get_space.async_get_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.get_space_request.GetSpaceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        name: "aws_sdk_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        description: Optional[
            "aws_sdk_codecatalyst.types.space_description.SpaceDescription"
        ] = None,
    ) -> "aws_sdk_codecatalyst.types.update_space_response.UpdateSpaceResponse":
        """<p>Changes one or more values for a space.</p>

        Args:
            name: <p>The name of the space.</p>
            description: <p>The description of the space.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecatalyst.types.update_space_request.UpdateSpaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecatalyst.types.update_space_response.UpdateSpaceResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.update_space

            (
                output,
                http_response,
            ) = await aws_sdk_codecatalyst._operations.code_catalyst.update_space.async_update_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.update_space_request.UpdateSpaceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        name: "aws_sdk_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
    ) -> "aws_sdk_codecatalyst.types.delete_space_response.DeleteSpaceResponse":
        """<p>Deletes a space.</p> <important> <p>Deleting a space cannot be undone. Additionally, since space names must be unique across Amazon CodeCatalyst, you cannot reuse names of deleted spaces.</p> </important>

        Args:
            name: <p>The name of the space. To retrieve a list of space names, use <a>ListSpaces</a>.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecatalyst.types.delete_space_request.DeleteSpaceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecatalyst.types.delete_space_response.DeleteSpaceResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.delete_space

            (
                output,
                http_response,
            ) = await aws_sdk_codecatalyst._operations.code_catalyst.delete_space.async_delete_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.delete_space_request.DeleteSpaceRequest = {}  # type: ignore[typeddict-item]
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
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_codecatalyst.types.list_spaces_response.ListSpacesResponse":
        """<p>Retrieves a list of spaces.</p>

        Args:
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecatalyst.types.list_spaces_request.ListSpacesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecatalyst.types.list_spaces_response.ListSpacesResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.list_spaces

            (
                output,
                http_response,
            ) = await aws_sdk_codecatalyst._operations.code_catalyst.list_spaces.async_list_spaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.list_spaces_request.ListSpacesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_dev_environments(
        self,
        space_name: "aws_sdk_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        project_name: Optional[
            "aws_sdk_codecatalyst.types.name_string.NameString"
        ] = None,
        filters: Optional["aws_sdk_codecatalyst.types.filters.Filters"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_codecatalyst.types.list_dev_environments_response.ListDevEnvironmentsResponse":
        """<p>Retrieves a list of Dev Environments in a project.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            filters: <p>Information about filters to apply to narrow the results returned in the list.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecatalyst.types.list_dev_environments_request.ListDevEnvironmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecatalyst.types.list_dev_environments_response.ListDevEnvironmentsResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.list_dev_environments

            (
                output,
                http_response,
            ) = await aws_sdk_codecatalyst._operations.code_catalyst.list_dev_environments.async_list_dev_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.list_dev_environments_request.ListDevEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        input_["space_name"] = space_name
        if project_name is not None:
            input_["project_name"] = project_name
        if filters is not None:
            input_["filters"] = filters
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
