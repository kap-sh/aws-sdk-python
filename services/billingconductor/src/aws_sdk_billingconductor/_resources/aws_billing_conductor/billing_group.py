from typing import TYPE_CHECKING, Optional

import aws_sdk_billingconductor._auth._signers
import aws_sdk_billingconductor._auth._sigv4
from aws_sdk_billingconductor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_grouping
    import aws_sdk_billingconductor.types.account_id
    import aws_sdk_billingconductor.types.account_id_list
    import aws_sdk_billingconductor.types.associate_accounts_input
    import aws_sdk_billingconductor.types.associate_accounts_output
    import aws_sdk_billingconductor.types.billing_group_arn
    import aws_sdk_billingconductor.types.billing_group_description
    import aws_sdk_billingconductor.types.billing_group_list_element
    import aws_sdk_billingconductor.types.billing_group_name
    import aws_sdk_billingconductor.types.billing_group_status
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.client_token
    import aws_sdk_billingconductor.types.computation_preference
    import aws_sdk_billingconductor.types.create_billing_group_input
    import aws_sdk_billingconductor.types.create_billing_group_output
    import aws_sdk_billingconductor.types.delete_billing_group_input
    import aws_sdk_billingconductor.types.delete_billing_group_output
    import aws_sdk_billingconductor.types.disassociate_accounts_input
    import aws_sdk_billingconductor.types.disassociate_accounts_output
    import aws_sdk_billingconductor.types.list_billing_groups_filter
    import aws_sdk_billingconductor.types.list_billing_groups_input
    import aws_sdk_billingconductor.types.list_billing_groups_output
    import aws_sdk_billingconductor.types.max_billing_group_results
    import aws_sdk_billingconductor.types.tag_map
    import aws_sdk_billingconductor.types.token
    import aws_sdk_billingconductor.types.update_billing_group_account_grouping
    import aws_sdk_billingconductor.types.update_billing_group_input
    import aws_sdk_billingconductor.types.update_billing_group_output
    from aws_sdk_billingconductor._services.async_billingconductor import (
        AsyncbillingconductorClient,
        AsyncbillingconductorClientConfig,
    )
    from aws_sdk_billingconductor._services.billingconductor import (
        billingconductorClient,
        billingconductorClientConfig,
    )


class BillingGroup:
    def __init__(self, service: billingconductorClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_billingconductor.types.billing_group_name.BillingGroupName",
        account_grouping: "aws_sdk_billingconductor.types.account_grouping.AccountGrouping",
        computation_preference: "aws_sdk_billingconductor.types.computation_preference.ComputationPreference",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        client_token: Optional[
            "aws_sdk_billingconductor.types.client_token.ClientToken"
        ] = None,
        primary_account_id: Optional[
            "aws_sdk_billingconductor.types.account_id.AccountId"
        ] = None,
        description: Optional[
            "aws_sdk_billingconductor.types.billing_group_description.BillingGroupDescription"
        ] = None,
        tags: Optional["aws_sdk_billingconductor.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_billingconductor.types.create_billing_group_output.CreateBillingGroupOutput":
        """<p> Creates a billing group that resembles a consolidated billing family that Amazon Web Services charges, based off of the predefined pricing plan computation. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The billing group name. The names must be unique. </p>
            account_grouping: <p> The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family. </p>
            computation_preference: <p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>
            primary_account_id: <p> The account ID that serves as the main account in a billing group. </p>
            description: <p>The description of the billing group. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a billing group. This feature isn't available during the beta. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.create_billing_group_input.CreateBillingGroupInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.create_billing_group_output.CreateBillingGroupOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.create_billing_group

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.create_billing_group.create_billing_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.create_billing_group_input.CreateBillingGroupInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["name"] = name
        input["account_grouping"] = account_grouping
        input["computation_preference"] = computation_preference
        if primary_account_id is not None:
            input["primary_account_id"] = primary_account_id
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        name: Optional[
            "aws_sdk_billingconductor.types.billing_group_name.BillingGroupName"
        ] = None,
        status: Optional[
            "aws_sdk_billingconductor.types.billing_group_status.BillingGroupStatus"
        ] = None,
        computation_preference: Optional[
            "aws_sdk_billingconductor.types.computation_preference.ComputationPreference"
        ] = None,
        description: Optional[
            "aws_sdk_billingconductor.types.billing_group_description.BillingGroupDescription"
        ] = None,
        account_grouping: Optional[
            "aws_sdk_billingconductor.types.update_billing_group_account_grouping.UpdateBillingGroupAccountGrouping"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput":
        """<p>This updates an existing billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group being updated. </p>
            name: <p>The name of the billing group. The names must be unique to each billing group. </p>
            status: <p>The status of the billing group. Only one of the valid values can be used. </p>
            computation_preference: <p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>
            description: <p>A description of the billing group. </p>
            account_grouping: <p>Specifies if the billing group has automatic account association (<code>AutoAssociate</code>) enabled.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.update_billing_group

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.update_billing_group.update_billing_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        if name is not None:
            input["name"] = name
        if status is not None:
            input["status"] = status
        if computation_preference is not None:
            input["computation_preference"] = computation_preference
        if description is not None:
            input["description"] = description
        if account_grouping is not None:
            input["account_grouping"] = account_grouping

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.delete_billing_group_output.DeleteBillingGroupOutput":
        """<p> Deletes a billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group that you're deleting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.delete_billing_group_input.DeleteBillingGroupInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.delete_billing_group_output.DeleteBillingGroupOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.delete_billing_group

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.delete_billing_group.delete_billing_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.delete_billing_group_input.DeleteBillingGroupInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_billing_groups_filter.ListBillingGroupsFilter"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput":
        """<p>A paginated call to retrieve a list of billing groups for the given billing period. If you don't provide a billing group, the current billing period is used.</p>

        Args:
            billing_period: <p>The preferred billing period to get billing groups. </p>
            max_results: <p>The maximum number of billing groups to retrieve. </p>
            next_token: <p>The pagination token that's used on subsequent calls to get billing groups. </p>
            filters: <p>A <code>ListBillingGroupsFilter</code> that specifies the billing group and pricing plan to retrieve billing group information. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.list_billing_groups_input.ListBillingGroupsInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_billing_groups

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.list_billing_groups.list_billing_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.list_billing_groups_input.ListBillingGroupsInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input["billing_period"] = billing_period
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_accounts(
        self,
        arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        account_ids: "aws_sdk_billingconductor.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.associate_accounts_output.AssociateAccountsOutput":
        """<p>Connects an array of account IDs in a consolidated billing family to a predefined billing group. The account IDs must be a part of the consolidated billing family during the current month, and not already associated with another billing group. The maximum number of accounts that can be associated in one call is 30. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the billing group that associates the array of account IDs. </p>
            account_ids: <p> The associating array of account IDs. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.associate_accounts_input.AssociateAccountsInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.associate_accounts_output.AssociateAccountsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.associate_accounts

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.associate_accounts.associate_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.associate_accounts_input.AssociateAccountsInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        input["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_accounts(
        self,
        arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        account_ids: "aws_sdk_billingconductor.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.disassociate_accounts_output.DisassociateAccountsOutput":
        """<p>Removes the specified list of account IDs from the given billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group that the array of account IDs will disassociate from. </p>
            account_ids: <p>The array of account IDs to disassociate. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.disassociate_accounts_input.DisassociateAccountsInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.disassociate_accounts_output.DisassociateAccountsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.disassociate_accounts

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.disassociate_accounts.disassociate_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.disassociate_accounts_input.DisassociateAccountsInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        input["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncBillingGroup:
    def __init__(self, service: AsyncbillingconductorClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_billingconductor.types.billing_group_name.BillingGroupName",
        account_grouping: "aws_sdk_billingconductor.types.account_grouping.AccountGrouping",
        computation_preference: "aws_sdk_billingconductor.types.computation_preference.ComputationPreference",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "aws_sdk_billingconductor.types.client_token.ClientToken"
        ] = None,
        primary_account_id: Optional[
            "aws_sdk_billingconductor.types.account_id.AccountId"
        ] = None,
        description: Optional[
            "aws_sdk_billingconductor.types.billing_group_description.BillingGroupDescription"
        ] = None,
        tags: Optional["aws_sdk_billingconductor.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_billingconductor.types.create_billing_group_output.CreateBillingGroupOutput":
        """<p> Creates a billing group that resembles a consolidated billing family that Amazon Web Services charges, based off of the predefined pricing plan computation. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The billing group name. The names must be unique. </p>
            account_grouping: <p> The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family. </p>
            computation_preference: <p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>
            primary_account_id: <p> The account ID that serves as the main account in a billing group. </p>
            description: <p>The description of the billing group. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a billing group. This feature isn't available during the beta. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.create_billing_group_input.CreateBillingGroupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.create_billing_group_output.CreateBillingGroupOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.create_billing_group

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.create_billing_group.async_create_billing_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.create_billing_group_input.CreateBillingGroupInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["name"] = name
        input["account_grouping"] = account_grouping
        input["computation_preference"] = computation_preference
        if primary_account_id is not None:
            input["primary_account_id"] = primary_account_id
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        name: Optional[
            "aws_sdk_billingconductor.types.billing_group_name.BillingGroupName"
        ] = None,
        status: Optional[
            "aws_sdk_billingconductor.types.billing_group_status.BillingGroupStatus"
        ] = None,
        computation_preference: Optional[
            "aws_sdk_billingconductor.types.computation_preference.ComputationPreference"
        ] = None,
        description: Optional[
            "aws_sdk_billingconductor.types.billing_group_description.BillingGroupDescription"
        ] = None,
        account_grouping: Optional[
            "aws_sdk_billingconductor.types.update_billing_group_account_grouping.UpdateBillingGroupAccountGrouping"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput":
        """<p>This updates an existing billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group being updated. </p>
            name: <p>The name of the billing group. The names must be unique to each billing group. </p>
            status: <p>The status of the billing group. Only one of the valid values can be used. </p>
            computation_preference: <p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>
            description: <p>A description of the billing group. </p>
            account_grouping: <p>Specifies if the billing group has automatic account association (<code>AutoAssociate</code>) enabled.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.update_billing_group

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.update_billing_group.async_update_billing_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        if name is not None:
            input["name"] = name
        if status is not None:
            input["status"] = status
        if computation_preference is not None:
            input["computation_preference"] = computation_preference
        if description is not None:
            input["description"] = description
        if account_grouping is not None:
            input["account_grouping"] = account_grouping

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.delete_billing_group_output.DeleteBillingGroupOutput":
        """<p> Deletes a billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group that you're deleting.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.delete_billing_group_input.DeleteBillingGroupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.delete_billing_group_output.DeleteBillingGroupOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.delete_billing_group

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.delete_billing_group.async_delete_billing_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.delete_billing_group_input.DeleteBillingGroupInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_billing_groups_filter.ListBillingGroupsFilter"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput":
        """<p>A paginated call to retrieve a list of billing groups for the given billing period. If you don't provide a billing group, the current billing period is used.</p>

        Args:
            billing_period: <p>The preferred billing period to get billing groups. </p>
            max_results: <p>The maximum number of billing groups to retrieve. </p>
            next_token: <p>The pagination token that's used on subsequent calls to get billing groups. </p>
            filters: <p>A <code>ListBillingGroupsFilter</code> that specifies the billing group and pricing plan to retrieve billing group information. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.list_billing_groups_input.ListBillingGroupsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_billing_groups

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.list_billing_groups.async_list_billing_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.list_billing_groups_input.ListBillingGroupsInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input["billing_period"] = billing_period
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_accounts(
        self,
        arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        account_ids: "aws_sdk_billingconductor.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.associate_accounts_output.AssociateAccountsOutput":
        """<p>Connects an array of account IDs in a consolidated billing family to a predefined billing group. The account IDs must be a part of the consolidated billing family during the current month, and not already associated with another billing group. The maximum number of accounts that can be associated in one call is 30. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the billing group that associates the array of account IDs. </p>
            account_ids: <p> The associating array of account IDs. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.associate_accounts_input.AssociateAccountsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.associate_accounts_output.AssociateAccountsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.associate_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.associate_accounts.async_associate_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.associate_accounts_input.AssociateAccountsInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        input["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_accounts(
        self,
        arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        account_ids: "aws_sdk_billingconductor.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.disassociate_accounts_output.DisassociateAccountsOutput":
        """<p>Removes the specified list of account IDs from the given billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group that the array of account IDs will disassociate from. </p>
            account_ids: <p>The array of account IDs to disassociate. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.disassociate_accounts_input.DisassociateAccountsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.disassociate_accounts_output.DisassociateAccountsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.disassociate_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.disassociate_accounts.async_disassociate_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_billingconductor.types.disassociate_accounts_input.DisassociateAccountsInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        input["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
