from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_mgn._auth._signers
import aws_sdk_mgn._auth._sigv4
from aws_sdk_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.application
    import aws_sdk_mgn.types.application_description
    import aws_sdk_mgn.types.application_id
    import aws_sdk_mgn.types.application_name
    import aws_sdk_mgn.types.archive_application_request
    import aws_sdk_mgn.types.associate_source_servers_request
    import aws_sdk_mgn.types.associate_source_servers_request_source_server_i_ds
    import aws_sdk_mgn.types.associate_source_servers_response
    import aws_sdk_mgn.types.create_application_request
    import aws_sdk_mgn.types.delete_application_request
    import aws_sdk_mgn.types.delete_application_response
    import aws_sdk_mgn.types.disassociate_source_servers_request
    import aws_sdk_mgn.types.disassociate_source_servers_request_source_server_i_ds
    import aws_sdk_mgn.types.disassociate_source_servers_response
    import aws_sdk_mgn.types.list_applications_request
    import aws_sdk_mgn.types.list_applications_request_filters
    import aws_sdk_mgn.types.list_applications_response
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.unarchive_application_request
    import aws_sdk_mgn.types.update_application_request
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from aws_sdk_mgn._services.mgn import mgnClient, mgnClientConfig


class ApplicationResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_mgn.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        description: Optional[
            "aws_sdk_mgn.types.application_description.ApplicationDescription"
        ] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.application.Application":
        """<p>Create application.</p>

        Args:
            name: <p>Application name.</p>
            description: <p>Application description.</p>
            tags: <p>Application tags.</p>
            account_id: <p>Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.application.Application"]:
            import aws_sdk_mgn._operations.application_migration_service.create_application

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.create_application_request.CreateApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.delete_application_response.DeleteApplicationResponse":
        """<p>Delete application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.delete_application

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.delete_application_request.DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_applications_request_filters.ListApplicationsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.list_applications_response.ListApplicationsResponse":
        """<p>Retrieves all applications or multiple applications by ID.</p>

        Args:
            filters: <p>Applications list filters.</p>
            max_results: <p>Maximum results to return when listing applications.</p>
            next_token: <p>Request next token.</p>
            account_id: <p>Applications list Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_applications_response.ListApplicationsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_applications

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_applications_request.ListApplicationsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def archive_application(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.application.Application":
        """<p>Archive application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.archive_application_request.ArchiveApplicationRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.application.Application"]:
            import aws_sdk_mgn._operations.application_migration_service.archive_application

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.archive_application.archive_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.archive_application_request.ArchiveApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_source_servers(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        source_server_i_ds: "aws_sdk_mgn.types.associate_source_servers_request_source_server_i_ds.AssociateSourceServersRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.associate_source_servers_response.AssociateSourceServersResponse":
        """<p>Associate source servers to application.</p>

        Args:
            application_id: <p>Application ID.</p>
            source_server_i_ds: <p>Source server IDs list.</p>
            account_id: <p>Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.associate_source_servers_request.AssociateSourceServersRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.associate_source_servers_response.AssociateSourceServersResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.associate_source_servers

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.associate_source_servers.associate_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.associate_source_servers_request.AssociateSourceServersRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["source_server_i_ds"] = source_server_i_ds
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_source_servers(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        source_server_i_ds: "aws_sdk_mgn.types.disassociate_source_servers_request_source_server_i_ds.DisassociateSourceServersRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.disassociate_source_servers_response.DisassociateSourceServersResponse":
        """<p>Disassociate source servers from application.</p>

        Args:
            application_id: <p>Application ID.</p>
            source_server_i_ds: <p>Source server IDs list.</p>
            account_id: <p>Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.disassociate_source_servers_request.DisassociateSourceServersRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.disassociate_source_servers_response.DisassociateSourceServersResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.disassociate_source_servers

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.disassociate_source_servers.disassociate_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.disassociate_source_servers_request.DisassociateSourceServersRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["source_server_i_ds"] = source_server_i_ds
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def unarchive_application(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.application.Application":
        """<p>Unarchive application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.unarchive_application_request.UnarchiveApplicationRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.application.Application"]:
            import aws_sdk_mgn._operations.application_migration_service.unarchive_application

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.unarchive_application.unarchive_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.unarchive_application_request.UnarchiveApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_application(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["aws_sdk_mgn.types.application_name.ApplicationName"] = None,
        description: Optional[
            "aws_sdk_mgn.types.application_description.ApplicationDescription"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.application.Application":
        """<p>Update application.</p>

        Args:
            application_id: <p>Application ID.</p>
            name: <p>Application name.</p>
            description: <p>Application description.</p>
            account_id: <p>Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.application.Application"]:
            import aws_sdk_mgn._operations.application_migration_service.update_application

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.update_application_request.UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncApplicationResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_mgn.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        description: Optional[
            "aws_sdk_mgn.types.application_description.ApplicationDescription"
        ] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.application.Application":
        """<p>Create application.</p>

        Args:
            name: <p>Application name.</p>
            description: <p>Application description.</p>
            tags: <p>Application tags.</p>
            account_id: <p>Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.application.Application"]:
            import aws_sdk_mgn._operations.application_migration_service.create_application

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.create_application_request.CreateApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.delete_application_response.DeleteApplicationResponse":
        """<p>Delete application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.delete_application

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.delete_application_request.DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_applications_request_filters.ListApplicationsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.list_applications_response.ListApplicationsResponse":
        """<p>Retrieves all applications or multiple applications by ID.</p>

        Args:
            filters: <p>Applications list filters.</p>
            max_results: <p>Maximum results to return when listing applications.</p>
            next_token: <p>Request next token.</p>
            account_id: <p>Applications list Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_applications_response.ListApplicationsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_applications

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_applications_request.ListApplicationsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def archive_application(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.application.Application":
        """<p>Archive application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.archive_application_request.ArchiveApplicationRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.application.Application"]:
            import aws_sdk_mgn._operations.application_migration_service.archive_application

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.archive_application.async_archive_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.archive_application_request.ArchiveApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_source_servers(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        source_server_i_ds: "aws_sdk_mgn.types.associate_source_servers_request_source_server_i_ds.AssociateSourceServersRequestSourceServerIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.associate_source_servers_response.AssociateSourceServersResponse":
        """<p>Associate source servers to application.</p>

        Args:
            application_id: <p>Application ID.</p>
            source_server_i_ds: <p>Source server IDs list.</p>
            account_id: <p>Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.associate_source_servers_request.AssociateSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.associate_source_servers_response.AssociateSourceServersResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.associate_source_servers

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.associate_source_servers.async_associate_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.associate_source_servers_request.AssociateSourceServersRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["source_server_i_ds"] = source_server_i_ds
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_source_servers(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        source_server_i_ds: "aws_sdk_mgn.types.disassociate_source_servers_request_source_server_i_ds.DisassociateSourceServersRequestSourceServerIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.disassociate_source_servers_response.DisassociateSourceServersResponse":
        """<p>Disassociate source servers from application.</p>

        Args:
            application_id: <p>Application ID.</p>
            source_server_i_ds: <p>Source server IDs list.</p>
            account_id: <p>Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.disassociate_source_servers_request.DisassociateSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.disassociate_source_servers_response.DisassociateSourceServersResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.disassociate_source_servers

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.disassociate_source_servers.async_disassociate_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.disassociate_source_servers_request.DisassociateSourceServersRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["source_server_i_ds"] = source_server_i_ds
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def unarchive_application(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.application.Application":
        """<p>Unarchive application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.unarchive_application_request.UnarchiveApplicationRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.application.Application"]:
            import aws_sdk_mgn._operations.application_migration_service.unarchive_application

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.unarchive_application.async_unarchive_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.unarchive_application_request.UnarchiveApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_application(
        self,
        application_id: "aws_sdk_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        name: Optional["aws_sdk_mgn.types.application_name.ApplicationName"] = None,
        description: Optional[
            "aws_sdk_mgn.types.application_description.ApplicationDescription"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.application.Application":
        """<p>Update application.</p>

        Args:
            application_id: <p>Application ID.</p>
            name: <p>Application name.</p>
            description: <p>Application description.</p>
            account_id: <p>Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.application.Application"]:
            import aws_sdk_mgn._operations.application_migration_service.update_application

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.update_application_request.UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
