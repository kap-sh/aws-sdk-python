from typing import TYPE_CHECKING, Optional

from aws_sdk_mailmanager._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive
    import aws_sdk_mailmanager.types.archive_id_string
    import aws_sdk_mailmanager.types.archive_name_string
    import aws_sdk_mailmanager.types.archive_retention
    import aws_sdk_mailmanager.types.create_archive_request
    import aws_sdk_mailmanager.types.create_archive_response
    import aws_sdk_mailmanager.types.delete_archive_request
    import aws_sdk_mailmanager.types.delete_archive_response
    import aws_sdk_mailmanager.types.get_archive_request
    import aws_sdk_mailmanager.types.get_archive_response
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.kms_key_arn
    import aws_sdk_mailmanager.types.list_archives_request
    import aws_sdk_mailmanager.types.list_archives_response
    import aws_sdk_mailmanager.types.page_size
    import aws_sdk_mailmanager.types.pagination_token
    import aws_sdk_mailmanager.types.tag_list
    import aws_sdk_mailmanager.types.update_archive_request
    import aws_sdk_mailmanager.types.update_archive_response
    from aws_sdk_mailmanager._services.async_mail_manager import (
        AsyncMailManagerClient,
        AsyncMailManagerClientConfig,
    )
    from aws_sdk_mailmanager._services.mail_manager import (
        MailManagerClient,
        MailManagerClientConfig,
    )


class ArchiveResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        archive_name: "aws_sdk_mailmanager.types.archive_name_string.ArchiveNameString",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        retention: Optional[
            "aws_sdk_mailmanager.types.archive_retention.ArchiveRetention"
        ] = None,
        kms_key_arn: Optional["aws_sdk_mailmanager.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_archive_response.CreateArchiveResponse":
        """<p>Creates a new email archive resource for storing and retaining emails.</p>

        Args:
            client_token: <p>A unique token Amazon SES uses to recognize retries of this request.</p>
            archive_name: <p>A unique name for the new archive.</p>
            retention: <p>The period for retaining emails in the archive before automatic deletion.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key for encrypting emails in the archive.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.create_archive_request.CreateArchiveRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.create_archive_response.CreateArchiveResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_archive

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.create_archive.create_archive(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_archive_request.CreateArchiveRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["archive_name"] = archive_name
        if retention is not None:
            input_["retention"] = retention
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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
        archive_id: "aws_sdk_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_archive_response.GetArchiveResponse":
        """<p>Retrieves the full details and current state of a specified email archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_archive_request.GetArchiveRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_archive_response.GetArchiveResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_archive

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_archive.get_archive(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_archive_request.GetArchiveRequest = {}  # type: ignore[typeddict-item]
        input_["archive_id"] = archive_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        archive_id: "aws_sdk_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        archive_name: Optional[
            "aws_sdk_mailmanager.types.archive_name_string.ArchiveNameString"
        ] = None,
        retention: Optional[
            "aws_sdk_mailmanager.types.archive_retention.ArchiveRetention"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.update_archive_response.UpdateArchiveResponse":
        """<p>Updates the attributes of an existing email archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to update.</p>
            archive_name: <p>A new, unique name for the archive.</p>
            retention: <p>A new retention period for emails in the archive.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.update_archive_request.UpdateArchiveRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.update_archive_response.UpdateArchiveResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.update_archive

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.update_archive.update_archive(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.update_archive_request.UpdateArchiveRequest = {}  # type: ignore[typeddict-item]
        input_["archive_id"] = archive_id
        if archive_name is not None:
            input_["archive_name"] = archive_name
        if retention is not None:
            input_["retention"] = retention

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        archive_id: "aws_sdk_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_archive_response.DeleteArchiveResponse":
        """<p>Initiates deletion of an email archive. This changes the archive state to pending deletion. In this state, no new emails can be added, and existing archived emails become inaccessible (search, export, download). The archive and all of its contents will be permanently deleted 30 days after entering the pending deletion state, regardless of the configured retention period. </p>

        Args:
            archive_id: <p>The identifier of the archive to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.delete_archive_request.DeleteArchiveRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.delete_archive_response.DeleteArchiveResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_archive

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.delete_archive.delete_archive(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.delete_archive_request.DeleteArchiveRequest = {}  # type: ignore[typeddict-item]
        input_["archive_id"] = archive_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_mailmanager.types.list_archives_response.ListArchivesResponse":
        """<p>Returns a list of all email archives in your account.</p>

        Args:
            next_token: <p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. </p>
            page_size: <p>The maximum number of archives that are returned per call. You can use NextToken to obtain further pages of archives. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_archives_request.ListArchivesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_archives_response.ListArchivesResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_archives

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_archives.list_archives(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_archives_request.ListArchivesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncArchiveResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        archive_name: "aws_sdk_mailmanager.types.archive_name_string.ArchiveNameString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        retention: Optional[
            "aws_sdk_mailmanager.types.archive_retention.ArchiveRetention"
        ] = None,
        kms_key_arn: Optional["aws_sdk_mailmanager.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_archive_response.CreateArchiveResponse":
        """<p>Creates a new email archive resource for storing and retaining emails.</p>

        Args:
            client_token: <p>A unique token Amazon SES uses to recognize retries of this request.</p>
            archive_name: <p>A unique name for the new archive.</p>
            retention: <p>The period for retaining emails in the archive before automatic deletion.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key for encrypting emails in the archive.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.create_archive_request.CreateArchiveRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.create_archive_response.CreateArchiveResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_archive

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.create_archive.async_create_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_archive_request.CreateArchiveRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["archive_name"] = archive_name
        if retention is not None:
            input_["retention"] = retention
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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
        archive_id: "aws_sdk_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_archive_response.GetArchiveResponse":
        """<p>Retrieves the full details and current state of a specified email archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.get_archive_request.GetArchiveRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.get_archive_response.GetArchiveResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_archive

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.get_archive.async_get_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_archive_request.GetArchiveRequest = {}  # type: ignore[typeddict-item]
        input_["archive_id"] = archive_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        archive_id: "aws_sdk_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        archive_name: Optional[
            "aws_sdk_mailmanager.types.archive_name_string.ArchiveNameString"
        ] = None,
        retention: Optional[
            "aws_sdk_mailmanager.types.archive_retention.ArchiveRetention"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.update_archive_response.UpdateArchiveResponse":
        """<p>Updates the attributes of an existing email archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to update.</p>
            archive_name: <p>A new, unique name for the archive.</p>
            retention: <p>A new retention period for emails in the archive.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.update_archive_request.UpdateArchiveRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.update_archive_response.UpdateArchiveResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.update_archive

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.update_archive.async_update_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.update_archive_request.UpdateArchiveRequest = {}  # type: ignore[typeddict-item]
        input_["archive_id"] = archive_id
        if archive_name is not None:
            input_["archive_name"] = archive_name
        if retention is not None:
            input_["retention"] = retention

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        archive_id: "aws_sdk_mailmanager.types.archive_id_string.ArchiveIdString",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_archive_response.DeleteArchiveResponse":
        """<p>Initiates deletion of an email archive. This changes the archive state to pending deletion. In this state, no new emails can be added, and existing archived emails become inaccessible (search, export, download). The archive and all of its contents will be permanently deleted 30 days after entering the pending deletion state, regardless of the configured retention period. </p>

        Args:
            archive_id: <p>The identifier of the archive to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.delete_archive_request.DeleteArchiveRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.delete_archive_response.DeleteArchiveResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_archive

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.delete_archive.async_delete_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.delete_archive_request.DeleteArchiveRequest = {}  # type: ignore[typeddict-item]
        input_["archive_id"] = archive_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_mailmanager.types.list_archives_response.ListArchivesResponse":
        """<p>Returns a list of all email archives in your account.</p>

        Args:
            next_token: <p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. </p>
            page_size: <p>The maximum number of archives that are returned per call. You can use NextToken to obtain further pages of archives. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.list_archives_request.ListArchivesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.list_archives_response.ListArchivesResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_archives

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.list_archives.async_list_archives(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_archives_request.ListArchivesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
