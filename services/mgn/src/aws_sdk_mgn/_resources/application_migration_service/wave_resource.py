from typing import Optional, TYPE_CHECKING
from aws_sdk_mgn._services.async_mgn import ensure_async_iterator
from aws_sdk_mgn._services.mgn import ensure_sync_iterator
from aws_sdk_mgn._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_mgn._auth._signers
import aws_sdk_mgn._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_mgn._services.mgn import mgnClient, mgnClientConfig
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.application_i_ds
    import aws_sdk_mgn.types.archive_wave_request
    import aws_sdk_mgn.types.associate_applications_request
    import aws_sdk_mgn.types.associate_applications_response
    import aws_sdk_mgn.types.create_wave_request
    import aws_sdk_mgn.types.delete_wave_request
    import aws_sdk_mgn.types.delete_wave_response
    import aws_sdk_mgn.types.disassociate_applications_request
    import aws_sdk_mgn.types.disassociate_applications_response
    import aws_sdk_mgn.types.list_waves_request
    import aws_sdk_mgn.types.list_waves_request_filters
    import aws_sdk_mgn.types.list_waves_response
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.unarchive_wave_request
    import aws_sdk_mgn.types.update_wave_request
    import aws_sdk_mgn.types.wave
    import aws_sdk_mgn.types.wave_description
    import aws_sdk_mgn.types.wave_id
    import aws_sdk_mgn.types.wave_name

class WaveResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service
    def create(self, name: "aws_sdk_mgn.types.wave_name.WaveName", *, config_overrides: Optional[mgnClientConfig] = None, description: Optional["aws_sdk_mgn.types.wave_description.WaveDescription"] = None, tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.wave.Wave":
        """<p>Create wave.</p>

        Args:
            name: <p>Wave name.</p>
            description: <p>Wave description.</p>
            tags: <p>Wave tags.</p>
            account_id: <p>Account ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.create_wave_request.CreateWaveRequest]') -> OperationResponse["aws_sdk_mgn.types.wave.Wave"]:
            import aws_sdk_mgn._operations.application_migration_service.create_wave
            output, http_response = aws_sdk_mgn._operations.application_migration_service.create_wave.create_wave(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.create_wave_request.CreateWaveRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", *, config_overrides: Optional[mgnClientConfig] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.delete_wave_response.DeleteWaveResponse":
        """<p>Delete wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.delete_wave_request.DeleteWaveRequest]') -> OperationResponse["aws_sdk_mgn.types.delete_wave_response.DeleteWaveResponse"]:
            import aws_sdk_mgn._operations.application_migration_service.delete_wave
            output, http_response = aws_sdk_mgn._operations.application_migration_service.delete_wave.delete_wave(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.delete_wave_request.DeleteWaveRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[mgnClientConfig] = None, filters: Optional["aws_sdk_mgn.types.list_waves_request_filters.ListWavesRequestFilters"] = None, max_results: Optional["aws_sdk_mgn.types.max_results_type.MaxResultsType"] = None, next_token: Optional["aws_sdk_mgn.types.pagination_token.PaginationToken"] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.list_waves_response.ListWavesResponse":
        """<p>Retrieves all waves or multiple waves by ID.</p>

        Args:
            filters: <p>Waves list filters.</p>
            max_results: <p>Maximum results to return when listing waves.</p>
            next_token: <p>Request next token.</p>
            account_id: <p>Request account ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.list_waves_request.ListWavesRequest]') -> OperationResponse["aws_sdk_mgn.types.list_waves_response.ListWavesResponse"]:
            import aws_sdk_mgn._operations.application_migration_service.list_waves
            output, http_response = aws_sdk_mgn._operations.application_migration_service.list_waves.list_waves(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.list_waves_request.ListWavesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def archive_wave(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", *, config_overrides: Optional[mgnClientConfig] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.wave.Wave":
        """<p>Archive wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.archive_wave_request.ArchiveWaveRequest]') -> OperationResponse["aws_sdk_mgn.types.wave.Wave"]:
            import aws_sdk_mgn._operations.application_migration_service.archive_wave
            output, http_response = aws_sdk_mgn._operations.application_migration_service.archive_wave.archive_wave(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.archive_wave_request.ArchiveWaveRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def associate_applications(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", application_i_ds: "aws_sdk_mgn.types.application_i_ds.ApplicationIDs", *, config_overrides: Optional[mgnClientConfig] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.associate_applications_response.AssociateApplicationsResponse":
        """<p>Associate applications to wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            application_i_ds: <p>Application IDs list.</p>
            account_id: <p>Account ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.associate_applications_request.AssociateApplicationsRequest]') -> OperationResponse["aws_sdk_mgn.types.associate_applications_response.AssociateApplicationsResponse"]:
            import aws_sdk_mgn._operations.application_migration_service.associate_applications
            output, http_response = aws_sdk_mgn._operations.application_migration_service.associate_applications.associate_applications(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.associate_applications_request.AssociateApplicationsRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        input["application_i_ds"] = application_i_ds
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def disassociate_applications(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", application_i_ds: "aws_sdk_mgn.types.application_i_ds.ApplicationIDs", *, config_overrides: Optional[mgnClientConfig] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.disassociate_applications_response.DisassociateApplicationsResponse":
        """<p>Disassociate applications from wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            application_i_ds: <p>Application IDs list.</p>
            account_id: <p>Account ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.disassociate_applications_request.DisassociateApplicationsRequest]') -> OperationResponse["aws_sdk_mgn.types.disassociate_applications_response.DisassociateApplicationsResponse"]:
            import aws_sdk_mgn._operations.application_migration_service.disassociate_applications
            output, http_response = aws_sdk_mgn._operations.application_migration_service.disassociate_applications.disassociate_applications(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.disassociate_applications_request.DisassociateApplicationsRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        input["application_i_ds"] = application_i_ds
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def unarchive_wave(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", *, config_overrides: Optional[mgnClientConfig] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.wave.Wave":
        """<p>Unarchive wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.unarchive_wave_request.UnarchiveWaveRequest]') -> OperationResponse["aws_sdk_mgn.types.wave.Wave"]:
            import aws_sdk_mgn._operations.application_migration_service.unarchive_wave
            output, http_response = aws_sdk_mgn._operations.application_migration_service.unarchive_wave.unarchive_wave(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.unarchive_wave_request.UnarchiveWaveRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update_wave(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", *, config_overrides: Optional[mgnClientConfig] = None, name: Optional["aws_sdk_mgn.types.wave_name.WaveName"] = None, description: Optional["aws_sdk_mgn.types.wave_description.WaveDescription"] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.wave.Wave":
        """<p>Update wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            name: <p>Wave name.</p>
            description: <p>Wave description.</p>
            account_id: <p>Account ID.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_mgn.types.update_wave_request.UpdateWaveRequest]') -> OperationResponse["aws_sdk_mgn.types.wave.Wave"]:
            import aws_sdk_mgn._operations.application_migration_service.update_wave
            output, http_response = aws_sdk_mgn._operations.application_migration_service.update_wave.update_wave(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_wave_request.UpdateWaveRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncWaveResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service
    async def create(self, name: "aws_sdk_mgn.types.wave_name.WaveName", *, config_overrides: Optional[AsyncmgnClientConfig] = None, description: Optional["aws_sdk_mgn.types.wave_description.WaveDescription"] = None, tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.wave.Wave":
        """<p>Create wave.</p>

        Args:
            name: <p>Wave name.</p>
            description: <p>Wave description.</p>
            tags: <p>Wave tags.</p>
            account_id: <p>Account ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.create_wave_request.CreateWaveRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.wave.Wave"]:
            import aws_sdk_mgn._operations.application_migration_service.create_wave
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.create_wave.async_create_wave(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.create_wave_request.CreateWaveRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", *, config_overrides: Optional[AsyncmgnClientConfig] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.delete_wave_response.DeleteWaveResponse":
        """<p>Delete wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.delete_wave_request.DeleteWaveRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.delete_wave_response.DeleteWaveResponse"]:
            import aws_sdk_mgn._operations.application_migration_service.delete_wave
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.delete_wave.async_delete_wave(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.delete_wave_request.DeleteWaveRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncmgnClientConfig] = None, filters: Optional["aws_sdk_mgn.types.list_waves_request_filters.ListWavesRequestFilters"] = None, max_results: Optional["aws_sdk_mgn.types.max_results_type.MaxResultsType"] = None, next_token: Optional["aws_sdk_mgn.types.pagination_token.PaginationToken"] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.list_waves_response.ListWavesResponse":
        """<p>Retrieves all waves or multiple waves by ID.</p>

        Args:
            filters: <p>Waves list filters.</p>
            max_results: <p>Maximum results to return when listing waves.</p>
            next_token: <p>Request next token.</p>
            account_id: <p>Request account ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.list_waves_request.ListWavesRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.list_waves_response.ListWavesResponse"]:
            import aws_sdk_mgn._operations.application_migration_service.list_waves
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.list_waves.async_list_waves(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.list_waves_request.ListWavesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def archive_wave(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", *, config_overrides: Optional[AsyncmgnClientConfig] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.wave.Wave":
        """<p>Archive wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.archive_wave_request.ArchiveWaveRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.wave.Wave"]:
            import aws_sdk_mgn._operations.application_migration_service.archive_wave
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.archive_wave.async_archive_wave(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.archive_wave_request.ArchiveWaveRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def associate_applications(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", application_i_ds: "aws_sdk_mgn.types.application_i_ds.ApplicationIDs", *, config_overrides: Optional[AsyncmgnClientConfig] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.associate_applications_response.AssociateApplicationsResponse":
        """<p>Associate applications to wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            application_i_ds: <p>Application IDs list.</p>
            account_id: <p>Account ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.associate_applications_request.AssociateApplicationsRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.associate_applications_response.AssociateApplicationsResponse"]:
            import aws_sdk_mgn._operations.application_migration_service.associate_applications
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.associate_applications.async_associate_applications(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.associate_applications_request.AssociateApplicationsRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        input["application_i_ds"] = application_i_ds
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def disassociate_applications(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", application_i_ds: "aws_sdk_mgn.types.application_i_ds.ApplicationIDs", *, config_overrides: Optional[AsyncmgnClientConfig] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.disassociate_applications_response.DisassociateApplicationsResponse":
        """<p>Disassociate applications from wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            application_i_ds: <p>Application IDs list.</p>
            account_id: <p>Account ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.disassociate_applications_request.DisassociateApplicationsRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.disassociate_applications_response.DisassociateApplicationsResponse"]:
            import aws_sdk_mgn._operations.application_migration_service.disassociate_applications
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.disassociate_applications.async_disassociate_applications(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.disassociate_applications_request.DisassociateApplicationsRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        input["application_i_ds"] = application_i_ds
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def unarchive_wave(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", *, config_overrides: Optional[AsyncmgnClientConfig] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.wave.Wave":
        """<p>Unarchive wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.unarchive_wave_request.UnarchiveWaveRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.wave.Wave"]:
            import aws_sdk_mgn._operations.application_migration_service.unarchive_wave
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.unarchive_wave.async_unarchive_wave(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.unarchive_wave_request.UnarchiveWaveRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update_wave(self, wave_id: "aws_sdk_mgn.types.wave_id.WaveID", *, config_overrides: Optional[AsyncmgnClientConfig] = None, name: Optional["aws_sdk_mgn.types.wave_name.WaveName"] = None, description: Optional["aws_sdk_mgn.types.wave_description.WaveDescription"] = None, account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None) -> "aws_sdk_mgn.types.wave.Wave":
        """<p>Update wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            name: <p>Wave name.</p>
            description: <p>Wave description.</p>
            account_id: <p>Account ID.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_mgn.types.update_wave_request.UpdateWaveRequest]') -> AsyncOperationResponse["aws_sdk_mgn.types.wave.Wave"]:
            import aws_sdk_mgn._operations.application_migration_service.update_wave
            output, http_response = await aws_sdk_mgn._operations.application_migration_service.update_wave.async_update_wave(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_wave_request.UpdateWaveRequest = {}  # type: ignore[typeddict-item]
        input["wave_id"] = wave_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output