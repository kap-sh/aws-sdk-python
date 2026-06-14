from typing import TYPE_CHECKING, Optional

from aws_sdk_verifiedpermissions._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.alias
    import aws_sdk_verifiedpermissions.types.create_policy_store_alias_input
    import aws_sdk_verifiedpermissions.types.create_policy_store_alias_output
    import aws_sdk_verifiedpermissions.types.delete_policy_store_alias_input
    import aws_sdk_verifiedpermissions.types.delete_policy_store_alias_output
    import aws_sdk_verifiedpermissions.types.deletion_mode
    import aws_sdk_verifiedpermissions.types.get_policy_store_alias_input
    import aws_sdk_verifiedpermissions.types.get_policy_store_alias_output
    import aws_sdk_verifiedpermissions.types.list_policy_store_aliases_input
    import aws_sdk_verifiedpermissions.types.list_policy_store_aliases_output
    import aws_sdk_verifiedpermissions.types.max_results
    import aws_sdk_verifiedpermissions.types.next_token
    import aws_sdk_verifiedpermissions.types.policy_store_alias_filter
    import aws_sdk_verifiedpermissions.types.policy_store_alias_item
    import aws_sdk_verifiedpermissions.types.policy_store_id
    from aws_sdk_verifiedpermissions._services.async_verified_permissions import (
        AsyncVerifiedPermissionsClient,
        AsyncVerifiedPermissionsClientConfig,
    )
    from aws_sdk_verifiedpermissions._services.verified_permissions import (
        VerifiedPermissionsClient,
        VerifiedPermissionsClientConfig,
    )


class PolicyStoreAlias:
    def __init__(self, service: VerifiedPermissionsClient) -> None:
        self._service = service

    def put(
        self,
        alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias",
        policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "aws_sdk_verifiedpermissions.types.create_policy_store_alias_output.CreatePolicyStoreAliasOutput":
        r"""<p>Creates a policy store alias for the specified policy store. A policy store alias is an alternative identifier that you can use to reference a policy store in API operations.</p> <p>This operation is idempotent. If multiple CreatePolicyStoreAlias requests are made where the <code>aliasName</code> and <code>policyStoreId</code> fields are the same between the requests, subsequent requests will be ignored. For each duplicate CreatePolicyStoreAlias request, a Success response will be returned and a new policy store alias will not be created.</p> <note> <p>Verified Permissions is <i> <a href=\"https://wikipedia.org/wiki/Eventual_consistency\">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            alias_name: <p>Specifies the name of the policy store alias to create. The name must be unique within your Amazon Web Services account and Amazon Web Services Region.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>
            policy_store_id: <p>Specifies the ID of the policy store to associate with the alias.</p> <note> <p>The associated policy store must be specified using its ID. The alias name cannot be used.</p> </note>

        Examples:
            CreatePolicyStoreAlias
            The following example creates a new policy store alias.

            >>> client.put(alias_name='policy-store-alias/example-policy-store', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_verifiedpermissions.types.create_policy_store_alias_input.CreatePolicyStoreAliasInput]",
        ) -> OperationResponse[
            "aws_sdk_verifiedpermissions.types.create_policy_store_alias_output.CreatePolicyStoreAliasOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.create_policy_store_alias

            output, http_response = (
                aws_sdk_verifiedpermissions._operations.verified_permissions.create_policy_store_alias.create_policy_store_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.create_policy_store_alias_input.CreatePolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
        input_["alias_name"] = alias_name
        input_["policy_store_id"] = policy_store_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
    ) -> "aws_sdk_verifiedpermissions.types.get_policy_store_alias_output.GetPolicyStoreAliasOutput":
        """<p>Retrieves details about the specified policy store alias.</p>

        Args:
            alias_name: <p>Specifies the name of the policy store alias that you want information about.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>

        Examples:
            GetPolicyStoreAlias
            The following example retrieves details about the policy store alias with name example-policy-store.

            >>> client.read(alias_name='policy-store-alias/example-policy-store')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_verifiedpermissions.types.get_policy_store_alias_input.GetPolicyStoreAliasInput]",
        ) -> OperationResponse[
            "aws_sdk_verifiedpermissions.types.get_policy_store_alias_output.GetPolicyStoreAliasOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.get_policy_store_alias

            output, http_response = (
                aws_sdk_verifiedpermissions._operations.verified_permissions.get_policy_store_alias.get_policy_store_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.get_policy_store_alias_input.GetPolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
        input_["alias_name"] = alias_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias",
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        deletion_mode: Optional[
            "aws_sdk_verifiedpermissions.types.deletion_mode.DeletionMode"
        ] = None,
    ) -> "aws_sdk_verifiedpermissions.types.delete_policy_store_alias_output.DeletePolicyStoreAliasOutput":
        """<p>Deletes the specified policy store alias.</p> <p>This operation is idempotent. If you specify a policy store alias that does not exist, the request response will still return a successful HTTP 200 status code.</p> <p>By default, when a policy store alias is deleted, it enters the <code>PendingDeletion</code> state. When a policy store alias is in the <code>PendingDeletion</code> state, new policy store aliases cannot be created with the same name. If the policy store alias is used in an API that has a <code>policyStoreId</code> field, the operation will fail with a <code>ResourceNotFound</code> exception.</p> <p>To immediately delete a policy store alias and bypass the <code>PendingDeletion</code> state, set the <code>deletionMode</code> parameter to <code>HardDelete</code>.</p> <important> <p>Verified Permissions is eventually consistent. If you hard delete a policy store alias and then immediately recreate it to be associated with a different policy store, requests that reference this alias may continue to be evaluated against the previously associated policy store for a short period of time.</p> </important>

        Args:
            alias_name: <p>Specifies the name of the policy store alias that you want to delete.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>
            deletion_mode: <p>Specifies the deletion mode for the policy store alias. The valid values are:</p> <ul> <li> <p> <b>SoftDelete</b> – The policy store alias enters the <code>PendingDeletion</code> state. This is the default behavior when no <code>deletionMode</code> is specified.</p> </li> <li> <p> <b>HardDelete</b> – The policy store alias is immediately deleted, bypassing the <code>PendingDeletion</code> state.</p> </li> </ul>

        Examples:
            Soft delete a policy store alias
            The following example soft deletes the policy store alias with name example-policy-store. The alias enters the PendingDeletion state.

            >>> client.delete(alias_name='policy-store-alias/example-policy-store')
            Hard delete a policy store alias
            The following example hard deletes the policy store alias with name example-policy-store. The alias is immediately deleted, bypassing the PendingDeletion state.

            >>> client.delete(alias_name='policy-store-alias/example-policy-store', deletion_mode='HardDelete')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_verifiedpermissions.types.delete_policy_store_alias_input.DeletePolicyStoreAliasInput]",
        ) -> OperationResponse[
            "aws_sdk_verifiedpermissions.types.delete_policy_store_alias_output.DeletePolicyStoreAliasOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.delete_policy_store_alias

            output, http_response = (
                aws_sdk_verifiedpermissions._operations.verified_permissions.delete_policy_store_alias.delete_policy_store_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.delete_policy_store_alias_input.DeletePolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
        input_["alias_name"] = alias_name
        if deletion_mode is not None:
            input_["deletion_mode"] = deletion_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[VerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "aws_sdk_verifiedpermissions.types.policy_store_alias_filter.PolicyStoreAliasFilter"
        ] = None,
    ) -> "aws_sdk_verifiedpermissions.types.list_policy_store_aliases_output.ListPolicyStoreAliasesOutput":
        """<p>Returns a paginated list of all policy store aliases in the calling Amazon Web Services account.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 5 policy store aliases per response. You can specify a maximum of 50 policy store aliases per response.</p>
            filter: <p>Specifies a filter to narrow the results. You can filter by <code>policyStoreId</code> to list only the policy store aliases associated with a specific policy store.</p>

        Examples:
            ListPolicyStoreAliases - Example 1
            The following example lists all policy store aliases in the AWS account in the AWS Region in which you call the operation.

            >>> client.list()
            ListPolicyStoreAliases - Example 2
            The following example lists all policy store aliases associated with the policy store with ID C7v5xMplfFH3i3e4Jrzb1a

            >>> client.list(filter={'policyStoreId': 'C7v5xMplfFH3i3e4Jrzb1a'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_verifiedpermissions.types.list_policy_store_aliases_input.ListPolicyStoreAliasesInput]",
        ) -> OperationResponse[
            "aws_sdk_verifiedpermissions.types.list_policy_store_aliases_output.ListPolicyStoreAliasesOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.list_policy_store_aliases

            output, http_response = (
                aws_sdk_verifiedpermissions._operations.verified_permissions.list_policy_store_aliases.list_policy_store_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.list_policy_store_aliases_input.ListPolicyStoreAliasesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncPolicyStoreAlias:
    def __init__(self, service: AsyncVerifiedPermissionsClient) -> None:
        self._service = service

    async def put(
        self,
        alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias",
        policy_store_id: "aws_sdk_verifiedpermissions.types.policy_store_id.PolicyStoreId",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "aws_sdk_verifiedpermissions.types.create_policy_store_alias_output.CreatePolicyStoreAliasOutput":
        r"""<p>Creates a policy store alias for the specified policy store. A policy store alias is an alternative identifier that you can use to reference a policy store in API operations.</p> <p>This operation is idempotent. If multiple CreatePolicyStoreAlias requests are made where the <code>aliasName</code> and <code>policyStoreId</code> fields are the same between the requests, subsequent requests will be ignored. For each duplicate CreatePolicyStoreAlias request, a Success response will be returned and a new policy store alias will not be created.</p> <note> <p>Verified Permissions is <i> <a href=\"https://wikipedia.org/wiki/Eventual_consistency\">eventually consistent</a> </i>. It can take a few seconds for a new or changed element to propagate through the service and be visible in the results of other Verified Permissions operations.</p> </note>

        Args:
            alias_name: <p>Specifies the name of the policy store alias to create. The name must be unique within your Amazon Web Services account and Amazon Web Services Region.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>
            policy_store_id: <p>Specifies the ID of the policy store to associate with the alias.</p> <note> <p>The associated policy store must be specified using its ID. The alias name cannot be used.</p> </note>

        Examples:
            CreatePolicyStoreAlias
            The following example creates a new policy store alias.

            >>> await client.put(alias_name='policy-store-alias/example-policy-store', policy_store_id='C7v5xMplfFH3i3e4Jrzb1a')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_verifiedpermissions.types.create_policy_store_alias_input.CreatePolicyStoreAliasInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_verifiedpermissions.types.create_policy_store_alias_output.CreatePolicyStoreAliasOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.create_policy_store_alias

            (
                output,
                http_response,
            ) = await aws_sdk_verifiedpermissions._operations.verified_permissions.create_policy_store_alias.async_create_policy_store_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.create_policy_store_alias_input.CreatePolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
        input_["alias_name"] = alias_name
        input_["policy_store_id"] = policy_store_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "aws_sdk_verifiedpermissions.types.get_policy_store_alias_output.GetPolicyStoreAliasOutput":
        """<p>Retrieves details about the specified policy store alias.</p>

        Args:
            alias_name: <p>Specifies the name of the policy store alias that you want information about.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>

        Examples:
            GetPolicyStoreAlias
            The following example retrieves details about the policy store alias with name example-policy-store.

            >>> await client.read(alias_name='policy-store-alias/example-policy-store')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_verifiedpermissions.types.get_policy_store_alias_input.GetPolicyStoreAliasInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_verifiedpermissions.types.get_policy_store_alias_output.GetPolicyStoreAliasOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.get_policy_store_alias

            (
                output,
                http_response,
            ) = await aws_sdk_verifiedpermissions._operations.verified_permissions.get_policy_store_alias.async_get_policy_store_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.get_policy_store_alias_input.GetPolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
        input_["alias_name"] = alias_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        alias_name: "aws_sdk_verifiedpermissions.types.alias.Alias",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        deletion_mode: Optional[
            "aws_sdk_verifiedpermissions.types.deletion_mode.DeletionMode"
        ] = None,
    ) -> "aws_sdk_verifiedpermissions.types.delete_policy_store_alias_output.DeletePolicyStoreAliasOutput":
        """<p>Deletes the specified policy store alias.</p> <p>This operation is idempotent. If you specify a policy store alias that does not exist, the request response will still return a successful HTTP 200 status code.</p> <p>By default, when a policy store alias is deleted, it enters the <code>PendingDeletion</code> state. When a policy store alias is in the <code>PendingDeletion</code> state, new policy store aliases cannot be created with the same name. If the policy store alias is used in an API that has a <code>policyStoreId</code> field, the operation will fail with a <code>ResourceNotFound</code> exception.</p> <p>To immediately delete a policy store alias and bypass the <code>PendingDeletion</code> state, set the <code>deletionMode</code> parameter to <code>HardDelete</code>.</p> <important> <p>Verified Permissions is eventually consistent. If you hard delete a policy store alias and then immediately recreate it to be associated with a different policy store, requests that reference this alias may continue to be evaluated against the previously associated policy store for a short period of time.</p> </important>

        Args:
            alias_name: <p>Specifies the name of the policy store alias that you want to delete.</p> <note> <p>The alias name must always be prefixed with <code>policy-store-alias/</code>.</p> </note>
            deletion_mode: <p>Specifies the deletion mode for the policy store alias. The valid values are:</p> <ul> <li> <p> <b>SoftDelete</b> – The policy store alias enters the <code>PendingDeletion</code> state. This is the default behavior when no <code>deletionMode</code> is specified.</p> </li> <li> <p> <b>HardDelete</b> – The policy store alias is immediately deleted, bypassing the <code>PendingDeletion</code> state.</p> </li> </ul>

        Examples:
            Soft delete a policy store alias
            The following example soft deletes the policy store alias with name example-policy-store. The alias enters the PendingDeletion state.

            >>> await client.delete(alias_name='policy-store-alias/example-policy-store')
            Hard delete a policy store alias
            The following example hard deletes the policy store alias with name example-policy-store. The alias is immediately deleted, bypassing the PendingDeletion state.

            >>> await client.delete(alias_name='policy-store-alias/example-policy-store', deletion_mode='HardDelete')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_verifiedpermissions.types.delete_policy_store_alias_input.DeletePolicyStoreAliasInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_verifiedpermissions.types.delete_policy_store_alias_output.DeletePolicyStoreAliasOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.delete_policy_store_alias

            (
                output,
                http_response,
            ) = await aws_sdk_verifiedpermissions._operations.verified_permissions.delete_policy_store_alias.async_delete_policy_store_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.delete_policy_store_alias_input.DeletePolicyStoreAliasInput = {}  # type: ignore[typeddict-item]
        input_["alias_name"] = alias_name
        if deletion_mode is not None:
            input_["deletion_mode"] = deletion_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_verifiedpermissions.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_verifiedpermissions.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "aws_sdk_verifiedpermissions.types.policy_store_alias_filter.PolicyStoreAliasFilter"
        ] = None,
    ) -> "aws_sdk_verifiedpermissions.types.list_policy_store_aliases_output.ListPolicyStoreAliasesOutput":
        """<p>Returns a paginated list of all policy store aliases in the calling Amazon Web Services account.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 5 policy store aliases per response. You can specify a maximum of 50 policy store aliases per response.</p>
            filter: <p>Specifies a filter to narrow the results. You can filter by <code>policyStoreId</code> to list only the policy store aliases associated with a specific policy store.</p>

        Examples:
            ListPolicyStoreAliases - Example 1
            The following example lists all policy store aliases in the AWS account in the AWS Region in which you call the operation.

            >>> await client.list()
            ListPolicyStoreAliases - Example 2
            The following example lists all policy store aliases associated with the policy store with ID C7v5xMplfFH3i3e4Jrzb1a

            >>> await client.list(filter={'policyStoreId': 'C7v5xMplfFH3i3e4Jrzb1a'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_verifiedpermissions.types.list_policy_store_aliases_input.ListPolicyStoreAliasesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_verifiedpermissions.types.list_policy_store_aliases_output.ListPolicyStoreAliasesOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.list_policy_store_aliases

            (
                output,
                http_response,
            ) = await aws_sdk_verifiedpermissions._operations.verified_permissions.list_policy_store_aliases.async_list_policy_store_aliases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.list_policy_store_aliases_input.ListPolicyStoreAliasesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
