from typing import TYPE_CHECKING, Optional

import aws_sdk_pca_connector_ad._auth._signers
import aws_sdk_pca_connector_ad._auth._sigv4
from aws_sdk_pca_connector_ad._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.access_control_entry_summary
    import aws_sdk_pca_connector_ad.types.access_rights
    import aws_sdk_pca_connector_ad.types.client_token
    import aws_sdk_pca_connector_ad.types.create_template_group_access_control_entry_request
    import aws_sdk_pca_connector_ad.types.delete_template_group_access_control_entry_request
    import aws_sdk_pca_connector_ad.types.display_name
    import aws_sdk_pca_connector_ad.types.get_template_group_access_control_entry_request
    import aws_sdk_pca_connector_ad.types.get_template_group_access_control_entry_response
    import aws_sdk_pca_connector_ad.types.group_security_identifier
    import aws_sdk_pca_connector_ad.types.list_template_group_access_control_entries_request
    import aws_sdk_pca_connector_ad.types.list_template_group_access_control_entries_response
    import aws_sdk_pca_connector_ad.types.max_results
    import aws_sdk_pca_connector_ad.types.next_token
    import aws_sdk_pca_connector_ad.types.template_arn
    import aws_sdk_pca_connector_ad.types.update_template_group_access_control_entry_request
    from aws_sdk_pca_connector_ad._services.async_pca_connector_ad import (
        AsyncPcaConnectorAdClient,
        AsyncPcaConnectorAdClientConfig,
    )
    from aws_sdk_pca_connector_ad._services.pca_connector_ad import (
        PcaConnectorAdClient,
        PcaConnectorAdClientConfig,
    )


class TemplateGroupAccessControlEntryResource:
    def __init__(self, service: PcaConnectorAdClient) -> None:
        self._service = service

    def put(
        self,
        template_arn: "aws_sdk_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "aws_sdk_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        group_display_name: "aws_sdk_pca_connector_ad.types.display_name.DisplayName",
        access_rights: "aws_sdk_pca_connector_ad.types.access_rights.AccessRights",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Create a group access control entry. Allow or deny Active Directory groups from enrolling and/or autoenrolling with the template based on the group security identifiers (SIDs).</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with \"S-\".</p>
            group_display_name: <p>Name of the Active Directory group. This name does not need to match the group name in Active Directory.</p>
            access_rights: <p> Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.</p>
            client_token: <p>Idempotency token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.create_template_group_access_control_entry_request.CreateTemplateGroupAccessControlEntryRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_template_group_access_control_entry

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_template_group_access_control_entry.create_template_group_access_control_entry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.create_template_group_access_control_entry_request.CreateTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
        input["template_arn"] = template_arn
        input["group_security_identifier"] = group_security_identifier
        input["group_display_name"] = group_display_name
        input["access_rights"] = access_rights
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        template_arn: "aws_sdk_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "aws_sdk_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> "aws_sdk_pca_connector_ad.types.get_template_group_access_control_entry_response.GetTemplateGroupAccessControlEntryResponse":
        """<p>Retrieves the group access control entries for a template.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with \"S-\".</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.get_template_group_access_control_entry_request.GetTemplateGroupAccessControlEntryRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_ad.types.get_template_group_access_control_entry_response.GetTemplateGroupAccessControlEntryResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_template_group_access_control_entry

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_template_group_access_control_entry.get_template_group_access_control_entry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.get_template_group_access_control_entry_request.GetTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
        input["template_arn"] = template_arn
        input["group_security_identifier"] = group_security_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        template_arn: "aws_sdk_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "aws_sdk_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        group_display_name: Optional[
            "aws_sdk_pca_connector_ad.types.display_name.DisplayName"
        ] = None,
        access_rights: Optional[
            "aws_sdk_pca_connector_ad.types.access_rights.AccessRights"
        ] = None,
    ) -> None:
        """<p>Update a group access control entry you created using <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.html\">CreateTemplateGroupAccessControlEntry</a>. </p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with \"S-\".</p>
            group_display_name: <p>Name of the Active Directory group. This name does not need to match the group name in Active Directory.</p>
            access_rights: <p>Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.update_template_group_access_control_entry_request.UpdateTemplateGroupAccessControlEntryRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.update_template_group_access_control_entry

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.update_template_group_access_control_entry.update_template_group_access_control_entry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.update_template_group_access_control_entry_request.UpdateTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
        input["template_arn"] = template_arn
        input["group_security_identifier"] = group_security_identifier
        if group_display_name is not None:
            input["group_display_name"] = group_display_name
        if access_rights is not None:
            input["access_rights"] = access_rights

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        template_arn: "aws_sdk_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "aws_sdk_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a group access control entry.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with \"S-\".</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.delete_template_group_access_control_entry_request.DeleteTemplateGroupAccessControlEntryRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_template_group_access_control_entry

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_template_group_access_control_entry.delete_template_group_access_control_entry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.delete_template_group_access_control_entry_request.DeleteTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
        input["template_arn"] = template_arn
        input["group_security_identifier"] = group_security_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        template_arn: "aws_sdk_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "aws_sdk_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_pca_connector_ad.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_pca_connector_ad.types.list_template_group_access_control_entries_response.ListTemplateGroupAccessControlEntriesResponse":
        """<p>Lists group access control entries you created. </p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.list_template_group_access_control_entries_request.ListTemplateGroupAccessControlEntriesRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_ad.types.list_template_group_access_control_entries_response.ListTemplateGroupAccessControlEntriesResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_template_group_access_control_entries

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_template_group_access_control_entries.list_template_group_access_control_entries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.list_template_group_access_control_entries_request.ListTemplateGroupAccessControlEntriesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["template_arn"] = template_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTemplateGroupAccessControlEntryResource:
    def __init__(self, service: AsyncPcaConnectorAdClient) -> None:
        self._service = service

    async def put(
        self,
        template_arn: "aws_sdk_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "aws_sdk_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        group_display_name: "aws_sdk_pca_connector_ad.types.display_name.DisplayName",
        access_rights: "aws_sdk_pca_connector_ad.types.access_rights.AccessRights",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Create a group access control entry. Allow or deny Active Directory groups from enrolling and/or autoenrolling with the template based on the group security identifiers (SIDs).</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with \"S-\".</p>
            group_display_name: <p>Name of the Active Directory group. This name does not need to match the group name in Active Directory.</p>
            access_rights: <p> Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.</p>
            client_token: <p>Idempotency token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.create_template_group_access_control_entry_request.CreateTemplateGroupAccessControlEntryRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_template_group_access_control_entry

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_template_group_access_control_entry.async_create_template_group_access_control_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.create_template_group_access_control_entry_request.CreateTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
        input["template_arn"] = template_arn
        input["group_security_identifier"] = group_security_identifier
        input["group_display_name"] = group_display_name
        input["access_rights"] = access_rights
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        template_arn: "aws_sdk_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "aws_sdk_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "aws_sdk_pca_connector_ad.types.get_template_group_access_control_entry_response.GetTemplateGroupAccessControlEntryResponse":
        """<p>Retrieves the group access control entries for a template.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with \"S-\".</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.get_template_group_access_control_entry_request.GetTemplateGroupAccessControlEntryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_ad.types.get_template_group_access_control_entry_response.GetTemplateGroupAccessControlEntryResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_template_group_access_control_entry

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_template_group_access_control_entry.async_get_template_group_access_control_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.get_template_group_access_control_entry_request.GetTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
        input["template_arn"] = template_arn
        input["group_security_identifier"] = group_security_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        template_arn: "aws_sdk_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "aws_sdk_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        group_display_name: Optional[
            "aws_sdk_pca_connector_ad.types.display_name.DisplayName"
        ] = None,
        access_rights: Optional[
            "aws_sdk_pca_connector_ad.types.access_rights.AccessRights"
        ] = None,
    ) -> None:
        """<p>Update a group access control entry you created using <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.html\">CreateTemplateGroupAccessControlEntry</a>. </p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with \"S-\".</p>
            group_display_name: <p>Name of the Active Directory group. This name does not need to match the group name in Active Directory.</p>
            access_rights: <p>Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.update_template_group_access_control_entry_request.UpdateTemplateGroupAccessControlEntryRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.update_template_group_access_control_entry

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.update_template_group_access_control_entry.async_update_template_group_access_control_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.update_template_group_access_control_entry_request.UpdateTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
        input["template_arn"] = template_arn
        input["group_security_identifier"] = group_security_identifier
        if group_display_name is not None:
            input["group_display_name"] = group_display_name
        if access_rights is not None:
            input["access_rights"] = access_rights

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        template_arn: "aws_sdk_pca_connector_ad.types.template_arn.TemplateArn",
        group_security_identifier: "aws_sdk_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a group access control entry.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>
            group_security_identifier: <p>Security identifier (SID) of the group object from Active Directory. The SID starts with \"S-\".</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.delete_template_group_access_control_entry_request.DeleteTemplateGroupAccessControlEntryRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_template_group_access_control_entry

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_template_group_access_control_entry.async_delete_template_group_access_control_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.delete_template_group_access_control_entry_request.DeleteTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
        input["template_arn"] = template_arn
        input["group_security_identifier"] = group_security_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        template_arn: "aws_sdk_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "aws_sdk_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_pca_connector_ad.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_pca_connector_ad.types.list_template_group_access_control_entries_response.ListTemplateGroupAccessControlEntriesResponse":
        """<p>Lists group access control entries you created. </p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.list_template_group_access_control_entries_request.ListTemplateGroupAccessControlEntriesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_ad.types.list_template_group_access_control_entries_response.ListTemplateGroupAccessControlEntriesResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_template_group_access_control_entries

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_template_group_access_control_entries.async_list_template_group_access_control_entries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.list_template_group_access_control_entries_request.ListTemplateGroupAccessControlEntriesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["template_arn"] = template_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
