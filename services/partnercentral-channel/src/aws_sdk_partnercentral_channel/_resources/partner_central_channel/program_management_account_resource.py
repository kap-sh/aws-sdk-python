from typing import TYPE_CHECKING, Optional

from aws_sdk_partnercentral_channel._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.account_id
    import aws_sdk_partnercentral_channel.types.account_id_list
    import aws_sdk_partnercentral_channel.types.catalog
    import aws_sdk_partnercentral_channel.types.client_token
    import aws_sdk_partnercentral_channel.types.create_program_management_account_request
    import aws_sdk_partnercentral_channel.types.create_program_management_account_response
    import aws_sdk_partnercentral_channel.types.delete_program_management_account_request
    import aws_sdk_partnercentral_channel.types.delete_program_management_account_response
    import aws_sdk_partnercentral_channel.types.list_program_management_accounts_request
    import aws_sdk_partnercentral_channel.types.list_program_management_accounts_response
    import aws_sdk_partnercentral_channel.types.list_program_management_accounts_sort_base
    import aws_sdk_partnercentral_channel.types.next_token
    import aws_sdk_partnercentral_channel.types.program
    import aws_sdk_partnercentral_channel.types.program_list
    import aws_sdk_partnercentral_channel.types.program_management_account_display_name
    import aws_sdk_partnercentral_channel.types.program_management_account_display_name_list
    import aws_sdk_partnercentral_channel.types.program_management_account_identifier
    import aws_sdk_partnercentral_channel.types.program_management_account_status_list
    import aws_sdk_partnercentral_channel.types.program_management_account_summary
    import aws_sdk_partnercentral_channel.types.revision
    import aws_sdk_partnercentral_channel.types.tag_list
    import aws_sdk_partnercentral_channel.types.update_program_management_account_request
    import aws_sdk_partnercentral_channel.types.update_program_management_account_response
    from aws_sdk_partnercentral_channel._services.async_partner_central_channel import (
        AsyncPartnerCentralChannelClient,
        AsyncPartnerCentralChannelClientConfig,
    )
    from aws_sdk_partnercentral_channel._services.partner_central_channel import (
        PartnerCentralChannelClient,
        PartnerCentralChannelClientConfig,
    )


class ProgramManagementAccountResource:
    def __init__(self, service: PartnerCentralChannelClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        program: "aws_sdk_partnercentral_channel.types.program.Program",
        display_name: "aws_sdk_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName",
        account_id: "aws_sdk_partnercentral_channel.types.account_id.AccountId",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_partnercentral_channel.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_channel.types.create_program_management_account_response.CreateProgramManagementAccountResponse":
        """<p>Creates a new program management account for managing partner relationships.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            program: <p>The program type for the management account.</p>
            display_name: <p>A human-readable name for the program management account.</p>
            account_id: <p>The AWS account ID to associate with the program management account.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the program management account.</p>

        Examples:
            Example for CreateProgramManagementAccount

            >>> client.create(catalog='AWS', program='SOLUTION_PROVIDER', display_name='TestDisplayName', account_id='111122223333', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.create_program_management_account_request.CreateProgramManagementAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.create_program_management_account_response.CreateProgramManagementAccountResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.create_program_management_account

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.create_program_management_account.create_program_management_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.create_program_management_account_request.CreateProgramManagementAccountRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["program"] = program
        input_["display_name"] = display_name
        input_["account_id"] = account_id
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        revision: Optional[
            "aws_sdk_partnercentral_channel.types.revision.Revision"
        ] = None,
        display_name: Optional[
            "aws_sdk_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
        ] = None,
    ) -> "aws_sdk_partnercentral_channel.types.update_program_management_account_response.UpdateProgramManagementAccountResponse":
        """<p>Updates the properties of a program management account.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            identifier: <p>The unique identifier of the program management account to update.</p>
            revision: <p>The current revision number of the program management account.</p>
            display_name: <p>The new display name for the program management account.</p>

        Examples:
            Example for UpdateProgramManagementAccount

            >>> client.update(catalog='AWS', identifier='pma-u8ic702rtzng8', revision='3', display_name='TestDisplayName')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.update_program_management_account_request.UpdateProgramManagementAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.update_program_management_account_response.UpdateProgramManagementAccountResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.update_program_management_account

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.update_program_management_account.update_program_management_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.update_program_management_account_request.UpdateProgramManagementAccountRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
        if revision is not None:
            input_["revision"] = revision
        if display_name is not None:
            input_["display_name"] = display_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_channel.types.delete_program_management_account_response.DeleteProgramManagementAccountResponse":
        """<p>Deletes a program management account.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            identifier: <p>The unique identifier of the program management account to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Examples:
            Example for DeleteProgramManagementAccount

            >>> client.delete(catalog='AWS', identifier='pma-u8ic702rtzng8', client_token='clientToken')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.delete_program_management_account_request.DeleteProgramManagementAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.delete_program_management_account_response.DeleteProgramManagementAccountResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.delete_program_management_account

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.delete_program_management_account.delete_program_management_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.delete_program_management_account_request.DeleteProgramManagementAccountRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        display_names: Optional[
            "aws_sdk_partnercentral_channel.types.program_management_account_display_name_list.ProgramManagementAccountDisplayNameList"
        ] = None,
        programs: Optional[
            "aws_sdk_partnercentral_channel.types.program_list.ProgramList"
        ] = None,
        account_ids: Optional[
            "aws_sdk_partnercentral_channel.types.account_id_list.AccountIdList"
        ] = None,
        statuses: Optional[
            "aws_sdk_partnercentral_channel.types.program_management_account_status_list.ProgramManagementAccountStatusList"
        ] = None,
        sort: Optional[
            "aws_sdk_partnercentral_channel.types.list_program_management_accounts_sort_base.ListProgramManagementAccountsSortBase"
        ] = None,
        next_token: Optional[
            "aws_sdk_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_channel.types.list_program_management_accounts_response.ListProgramManagementAccountsResponse":
        """<p>Lists program management accounts based on specified criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter accounts.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            display_names: <p>Filter by display names.</p>
            programs: <p>Filter by program types.</p>
            account_ids: <p>Filter by AWS account IDs.</p>
            statuses: <p>Filter by program management account statuses.</p>
            sort: <p>Sorting options for the results.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Examples:
            Example for ListProgramManagementAccounts

            >>> client.list(catalog='AWS', max_results=20, programs=['SOLUTION_PROVIDER'], display_names=['TestDisplayName'], account_ids=['111122223333'], statuses=['PENDING'], sort={'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_channel.types.list_program_management_accounts_request.ListProgramManagementAccountsRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_channel.types.list_program_management_accounts_response.ListProgramManagementAccountsResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.list_program_management_accounts

            output, http_response = (
                aws_sdk_partnercentral_channel._operations.partner_central_channel.list_program_management_accounts.list_program_management_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.list_program_management_accounts_request.ListProgramManagementAccountsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if max_results is not None:
            input_["max_results"] = max_results
        if display_names is not None:
            input_["display_names"] = display_names
        if programs is not None:
            input_["programs"] = programs
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if statuses is not None:
            input_["statuses"] = statuses
        if sort is not None:
            input_["sort"] = sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncProgramManagementAccountResource:
    def __init__(self, service: AsyncPartnerCentralChannelClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        program: "aws_sdk_partnercentral_channel.types.program.Program",
        display_name: "aws_sdk_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName",
        account_id: "aws_sdk_partnercentral_channel.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_partnercentral_channel.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_channel.types.create_program_management_account_response.CreateProgramManagementAccountResponse":
        """<p>Creates a new program management account for managing partner relationships.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            program: <p>The program type for the management account.</p>
            display_name: <p>A human-readable name for the program management account.</p>
            account_id: <p>The AWS account ID to associate with the program management account.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Key-value pairs to associate with the program management account.</p>

        Examples:
            Example for CreateProgramManagementAccount

            >>> await client.create(catalog='AWS', program='SOLUTION_PROVIDER', display_name='TestDisplayName', account_id='111122223333', client_token='clientToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.create_program_management_account_request.CreateProgramManagementAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.create_program_management_account_response.CreateProgramManagementAccountResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.create_program_management_account

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.create_program_management_account.async_create_program_management_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.create_program_management_account_request.CreateProgramManagementAccountRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["program"] = program
        input_["display_name"] = display_name
        input_["account_id"] = account_id
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        revision: Optional[
            "aws_sdk_partnercentral_channel.types.revision.Revision"
        ] = None,
        display_name: Optional[
            "aws_sdk_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
        ] = None,
    ) -> "aws_sdk_partnercentral_channel.types.update_program_management_account_response.UpdateProgramManagementAccountResponse":
        """<p>Updates the properties of a program management account.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            identifier: <p>The unique identifier of the program management account to update.</p>
            revision: <p>The current revision number of the program management account.</p>
            display_name: <p>The new display name for the program management account.</p>

        Examples:
            Example for UpdateProgramManagementAccount

            >>> await client.update(catalog='AWS', identifier='pma-u8ic702rtzng8', revision='3', display_name='TestDisplayName')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.update_program_management_account_request.UpdateProgramManagementAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.update_program_management_account_response.UpdateProgramManagementAccountResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.update_program_management_account

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.update_program_management_account.async_update_program_management_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.update_program_management_account_request.UpdateProgramManagementAccountRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
        if revision is not None:
            input_["revision"] = revision
        if display_name is not None:
            input_["display_name"] = display_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_channel.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_channel.types.delete_program_management_account_response.DeleteProgramManagementAccountResponse":
        """<p>Deletes a program management account.</p>

        Args:
            catalog: <p>The catalog identifier for the program management account.</p>
            identifier: <p>The unique identifier of the program management account to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Examples:
            Example for DeleteProgramManagementAccount

            >>> await client.delete(catalog='AWS', identifier='pma-u8ic702rtzng8', client_token='clientToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.delete_program_management_account_request.DeleteProgramManagementAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.delete_program_management_account_response.DeleteProgramManagementAccountResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.delete_program_management_account

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.delete_program_management_account.async_delete_program_management_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.delete_program_management_account_request.DeleteProgramManagementAccountRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralChannelClientConfig] = None,
        max_results: Optional[int] = None,
        display_names: Optional[
            "aws_sdk_partnercentral_channel.types.program_management_account_display_name_list.ProgramManagementAccountDisplayNameList"
        ] = None,
        programs: Optional[
            "aws_sdk_partnercentral_channel.types.program_list.ProgramList"
        ] = None,
        account_ids: Optional[
            "aws_sdk_partnercentral_channel.types.account_id_list.AccountIdList"
        ] = None,
        statuses: Optional[
            "aws_sdk_partnercentral_channel.types.program_management_account_status_list.ProgramManagementAccountStatusList"
        ] = None,
        sort: Optional[
            "aws_sdk_partnercentral_channel.types.list_program_management_accounts_sort_base.ListProgramManagementAccountsSortBase"
        ] = None,
        next_token: Optional[
            "aws_sdk_partnercentral_channel.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_channel.types.list_program_management_accounts_response.ListProgramManagementAccountsResponse":
        """<p>Lists program management accounts based on specified criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter accounts.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            display_names: <p>Filter by display names.</p>
            programs: <p>Filter by program types.</p>
            account_ids: <p>Filter by AWS account IDs.</p>
            statuses: <p>Filter by program management account statuses.</p>
            sort: <p>Sorting options for the results.</p>
            next_token: <p>Token for retrieving the next page of results.</p>

        Examples:
            Example for ListProgramManagementAccounts

            >>> await client.list(catalog='AWS', max_results=20, programs=['SOLUTION_PROVIDER'], display_names=['TestDisplayName'], account_ids=['111122223333'], statuses=['PENDING'], sort={'sortBy': 'UpdatedAt', 'sortOrder': 'Descending'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_channel.types.list_program_management_accounts_request.ListProgramManagementAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_channel.types.list_program_management_accounts_response.ListProgramManagementAccountsResponse"
        ]:
            import aws_sdk_partnercentral_channel._operations.partner_central_channel.list_program_management_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_channel._operations.partner_central_channel.list_program_management_accounts.async_list_program_management_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_channel.types.list_program_management_accounts_request.ListProgramManagementAccountsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if max_results is not None:
            input_["max_results"] = max_results
        if display_names is not None:
            input_["display_names"] = display_names
        if programs is not None:
            input_["programs"] = programs
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if statuses is not None:
            input_["statuses"] = statuses
        if sort is not None:
            input_["sort"] = sort
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
