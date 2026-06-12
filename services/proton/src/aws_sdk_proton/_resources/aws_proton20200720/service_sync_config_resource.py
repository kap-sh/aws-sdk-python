from typing import Optional, TYPE_CHECKING
from aws_sdk_proton._services.async_proton import ensure_async_iterator
from aws_sdk_proton._services.proton import ensure_sync_iterator
from aws_sdk_proton._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
if TYPE_CHECKING:
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig
    from aws_sdk_proton._services.async_proton import AsyncProtonClient, AsyncProtonClientConfig
    import aws_sdk_proton.types.create_service_sync_config_input
    import aws_sdk_proton.types.create_service_sync_config_output
    import aws_sdk_proton.types.delete_service_sync_config_input
    import aws_sdk_proton.types.delete_service_sync_config_output
    import aws_sdk_proton.types.get_service_sync_config_input
    import aws_sdk_proton.types.get_service_sync_config_output
    import aws_sdk_proton.types.git_branch_name
    import aws_sdk_proton.types.ops_file_path
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.update_service_sync_config_input
    import aws_sdk_proton.types.update_service_sync_config_output

class ServiceSyncConfigResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service
    def put(self, service_name: "aws_sdk_proton.types.resource_name.ResourceName", repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider", repository_name: "aws_sdk_proton.types.repository_name.RepositoryName", branch: "aws_sdk_proton.types.git_branch_name.GitBranchName", file_path: "aws_sdk_proton.types.ops_file_path.OpsFilePath", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.create_service_sync_config_output.CreateServiceSyncConfigOutput":
        """<p>Create the Proton Ops configuration file.</p>

        Args:
            service_name: <p>The name of the service the Proton Ops file is for.</p>
            repository_provider: <p>The provider type for your repository.</p>
            repository_name: <p>The repository name.</p>
            branch: <p>The repository branch for your Proton Ops file.</p>
            file_path: <p>The path to the Proton Ops file.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.create_service_sync_config_input.CreateServiceSyncConfigInput]') -> OperationResponse["aws_sdk_proton.types.create_service_sync_config_output.CreateServiceSyncConfigOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.create_service_sync_config
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.create_service_sync_config.create_service_sync_config(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_service_sync_config_input.CreateServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
        input["service_name"] = service_name
        input["repository_provider"] = repository_provider
        input["repository_name"] = repository_name
        input["branch"] = branch
        input["file_path"] = file_path

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, service_name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.get_service_sync_config_output.GetServiceSyncConfigOutput":
        """<p>Get detailed information for the service sync configuration.</p>

        Args:
            service_name: <p>The name of the service that you want to get the service sync configuration for.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.get_service_sync_config_input.GetServiceSyncConfigInput]') -> OperationResponse["aws_sdk_proton.types.get_service_sync_config_output.GetServiceSyncConfigOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service_sync_config
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.get_service_sync_config.get_service_sync_config(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_service_sync_config_input.GetServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
        input["service_name"] = service_name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, service_name: "aws_sdk_proton.types.resource_name.ResourceName", repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider", repository_name: "aws_sdk_proton.types.repository_name.RepositoryName", branch: "aws_sdk_proton.types.git_branch_name.GitBranchName", file_path: "aws_sdk_proton.types.ops_file_path.OpsFilePath", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.update_service_sync_config_output.UpdateServiceSyncConfigOutput":
        """<p>Update the Proton Ops config file.</p>

        Args:
            service_name: <p>The name of the service the Proton Ops file is for.</p>
            repository_provider: <p>The name of the repository provider where the Proton Ops file is found.</p>
            repository_name: <p>The name of the repository where the Proton Ops file is found.</p>
            branch: <p>The name of the code repository branch where the Proton Ops file is found.</p>
            file_path: <p>The path to the Proton Ops file.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.update_service_sync_config_input.UpdateServiceSyncConfigInput]') -> OperationResponse["aws_sdk_proton.types.update_service_sync_config_output.UpdateServiceSyncConfigOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service_sync_config
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.update_service_sync_config.update_service_sync_config(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_service_sync_config_input.UpdateServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
        input["service_name"] = service_name
        input["repository_provider"] = repository_provider
        input["repository_name"] = repository_name
        input["branch"] = branch
        input["file_path"] = file_path

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, service_name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.delete_service_sync_config_output.DeleteServiceSyncConfigOutput":
        """<p>Delete the Proton Ops file.</p>

        Args:
            service_name: <p>The name of the service that you want to delete the service sync configuration for.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.delete_service_sync_config_input.DeleteServiceSyncConfigInput]') -> OperationResponse["aws_sdk_proton.types.delete_service_sync_config_output.DeleteServiceSyncConfigOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_service_sync_config
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.delete_service_sync_config.delete_service_sync_config(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.delete_service_sync_config_input.DeleteServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
        input["service_name"] = service_name

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncServiceSyncConfigResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service
    async def put(self, service_name: "aws_sdk_proton.types.resource_name.ResourceName", repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider", repository_name: "aws_sdk_proton.types.repository_name.RepositoryName", branch: "aws_sdk_proton.types.git_branch_name.GitBranchName", file_path: "aws_sdk_proton.types.ops_file_path.OpsFilePath", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.create_service_sync_config_output.CreateServiceSyncConfigOutput":
        """<p>Create the Proton Ops configuration file.</p>

        Args:
            service_name: <p>The name of the service the Proton Ops file is for.</p>
            repository_provider: <p>The provider type for your repository.</p>
            repository_name: <p>The repository name.</p>
            branch: <p>The repository branch for your Proton Ops file.</p>
            file_path: <p>The path to the Proton Ops file.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.create_service_sync_config_input.CreateServiceSyncConfigInput]') -> AsyncOperationResponse["aws_sdk_proton.types.create_service_sync_config_output.CreateServiceSyncConfigOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.create_service_sync_config
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.create_service_sync_config.async_create_service_sync_config(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_service_sync_config_input.CreateServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
        input["service_name"] = service_name
        input["repository_provider"] = repository_provider
        input["repository_name"] = repository_name
        input["branch"] = branch
        input["file_path"] = file_path

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, service_name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.get_service_sync_config_output.GetServiceSyncConfigOutput":
        """<p>Get detailed information for the service sync configuration.</p>

        Args:
            service_name: <p>The name of the service that you want to get the service sync configuration for.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.get_service_sync_config_input.GetServiceSyncConfigInput]') -> AsyncOperationResponse["aws_sdk_proton.types.get_service_sync_config_output.GetServiceSyncConfigOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service_sync_config
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.get_service_sync_config.async_get_service_sync_config(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_service_sync_config_input.GetServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
        input["service_name"] = service_name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, service_name: "aws_sdk_proton.types.resource_name.ResourceName", repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider", repository_name: "aws_sdk_proton.types.repository_name.RepositoryName", branch: "aws_sdk_proton.types.git_branch_name.GitBranchName", file_path: "aws_sdk_proton.types.ops_file_path.OpsFilePath", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.update_service_sync_config_output.UpdateServiceSyncConfigOutput":
        """<p>Update the Proton Ops config file.</p>

        Args:
            service_name: <p>The name of the service the Proton Ops file is for.</p>
            repository_provider: <p>The name of the repository provider where the Proton Ops file is found.</p>
            repository_name: <p>The name of the repository where the Proton Ops file is found.</p>
            branch: <p>The name of the code repository branch where the Proton Ops file is found.</p>
            file_path: <p>The path to the Proton Ops file.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.update_service_sync_config_input.UpdateServiceSyncConfigInput]') -> AsyncOperationResponse["aws_sdk_proton.types.update_service_sync_config_output.UpdateServiceSyncConfigOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service_sync_config
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.update_service_sync_config.async_update_service_sync_config(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_service_sync_config_input.UpdateServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
        input["service_name"] = service_name
        input["repository_provider"] = repository_provider
        input["repository_name"] = repository_name
        input["branch"] = branch
        input["file_path"] = file_path

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, service_name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.delete_service_sync_config_output.DeleteServiceSyncConfigOutput":
        """<p>Delete the Proton Ops file.</p>

        Args:
            service_name: <p>The name of the service that you want to delete the service sync configuration for.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.delete_service_sync_config_input.DeleteServiceSyncConfigInput]') -> AsyncOperationResponse["aws_sdk_proton.types.delete_service_sync_config_output.DeleteServiceSyncConfigOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_service_sync_config
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.delete_service_sync_config.async_delete_service_sync_config(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.delete_service_sync_config_input.DeleteServiceSyncConfigInput = {}  # type: ignore[typeddict-item]
        input["service_name"] = service_name

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output