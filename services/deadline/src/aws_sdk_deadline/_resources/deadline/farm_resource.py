from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_deadline._auth._signers
import aws_sdk_deadline._auth._sigv4
from aws_sdk_deadline._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_deadline.types.amount_requirement_name
    import aws_sdk_deadline.types.associate_member_to_farm_request
    import aws_sdk_deadline.types.associate_member_to_farm_response
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.cost_scale_factor
    import aws_sdk_deadline.types.create_farm_request
    import aws_sdk_deadline.types.create_farm_response
    import aws_sdk_deadline.types.create_limit_request
    import aws_sdk_deadline.types.create_limit_response
    import aws_sdk_deadline.types.create_storage_profile_request
    import aws_sdk_deadline.types.create_storage_profile_response
    import aws_sdk_deadline.types.deadline_principal_type
    import aws_sdk_deadline.types.delete_farm_request
    import aws_sdk_deadline.types.delete_farm_response
    import aws_sdk_deadline.types.delete_limit_request
    import aws_sdk_deadline.types.delete_limit_response
    import aws_sdk_deadline.types.delete_storage_profile_request
    import aws_sdk_deadline.types.delete_storage_profile_response
    import aws_sdk_deadline.types.description
    import aws_sdk_deadline.types.disassociate_member_from_farm_request
    import aws_sdk_deadline.types.disassociate_member_from_farm_response
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.farm_member
    import aws_sdk_deadline.types.farm_summary
    import aws_sdk_deadline.types.file_system_locations_list
    import aws_sdk_deadline.types.get_farm_request
    import aws_sdk_deadline.types.get_farm_response
    import aws_sdk_deadline.types.get_limit_request
    import aws_sdk_deadline.types.get_limit_response
    import aws_sdk_deadline.types.get_storage_profile_request
    import aws_sdk_deadline.types.get_storage_profile_response
    import aws_sdk_deadline.types.identity_center_principal_id
    import aws_sdk_deadline.types.identity_store_id
    import aws_sdk_deadline.types.kms_key_arn
    import aws_sdk_deadline.types.limit_id
    import aws_sdk_deadline.types.limit_summary
    import aws_sdk_deadline.types.list_farm_members_request
    import aws_sdk_deadline.types.list_farm_members_response
    import aws_sdk_deadline.types.list_farms_request
    import aws_sdk_deadline.types.list_farms_response
    import aws_sdk_deadline.types.list_limits_request
    import aws_sdk_deadline.types.list_limits_response
    import aws_sdk_deadline.types.list_storage_profiles_request
    import aws_sdk_deadline.types.list_storage_profiles_response
    import aws_sdk_deadline.types.max_count
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.membership_level
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.region
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.storage_profile_id
    import aws_sdk_deadline.types.storage_profile_operating_system_family
    import aws_sdk_deadline.types.storage_profile_summary
    import aws_sdk_deadline.types.tags
    import aws_sdk_deadline.types.update_farm_request
    import aws_sdk_deadline.types.update_farm_response
    import aws_sdk_deadline.types.update_limit_request
    import aws_sdk_deadline.types.update_limit_response
    import aws_sdk_deadline.types.update_storage_profile_request
    import aws_sdk_deadline.types.update_storage_profile_response
    from aws_sdk_deadline._services.async_deadline import (
        AsyncdeadlineClient,
        AsyncdeadlineClientConfig,
    )
    from aws_sdk_deadline._services.deadline import deadlineClient, deadlineClientConfig


class FarmResource:
    def __init__(self, service: deadlineClient) -> None:
        self._service = service

    def create(
        self,
        display_name: "aws_sdk_deadline.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        description: Optional["aws_sdk_deadline.types.description.Description"] = None,
        kms_key_arn: Optional["aws_sdk_deadline.types.kms_key_arn.KmsKeyArn"] = None,
        cost_scale_factor: Optional[
            "aws_sdk_deadline.types.cost_scale_factor.CostScaleFactor"
        ] = None,
        tags: Optional["aws_sdk_deadline.types.tags.Tags"] = None,
    ) -> "aws_sdk_deadline.types.create_farm_response.CreateFarmResponse":
        """<p>Creates a farm to allow space for queues and fleets. Farms are the space where the components of your renders gather and are pieced together in the cloud. Farms contain budgets and allow you to enforce permissions. Deadline Cloud farms are a useful container for large projects.</p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            kms_key_arn: <p>The ARN of the KMS key to use on the farm.</p>
            cost_scale_factor: <p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment. The default value is 1.</p>
            tags: <p>The tags to add to your farm. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.create_farm_request.CreateFarmRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.create_farm_response.CreateFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_farm

            output, http_response = (
                aws_sdk_deadline._operations.deadline.create_farm.create_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_farm_request.CreateFarmRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if cost_scale_factor is not None:
            input_["cost_scale_factor"] = cost_scale_factor
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
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_farm_response.GetFarmResponse":
        """<p>Get a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.get_farm_request.GetFarmRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.get_farm_response.GetFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_farm

            output, http_response = (
                aws_sdk_deadline._operations.deadline.get_farm.get_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_farm_request.GetFarmRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        display_name: Optional[
            "aws_sdk_deadline.types.resource_name.ResourceName"
        ] = None,
        description: Optional["aws_sdk_deadline.types.description.Description"] = None,
        cost_scale_factor: Optional[
            "aws_sdk_deadline.types.cost_scale_factor.CostScaleFactor"
        ] = None,
    ) -> "aws_sdk_deadline.types.update_farm_response.UpdateFarmResponse":
        """<p>Updates a farm.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            display_name: <p>The display name of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            cost_scale_factor: <p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.update_farm_request.UpdateFarmRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.update_farm_response.UpdateFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_farm

            output, http_response = (
                aws_sdk_deadline._operations.deadline.update_farm.update_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_farm_request.UpdateFarmRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if cost_scale_factor is not None:
            input_["cost_scale_factor"] = cost_scale_factor

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_farm_response.DeleteFarmResponse":
        """<p>Deletes a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.delete_farm_request.DeleteFarmRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.delete_farm_response.DeleteFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_farm

            output, http_response = (
                aws_sdk_deadline._operations.deadline.delete_farm.delete_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_farm_request.DeleteFarmRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
    ) -> "aws_sdk_deadline.types.list_farms_response.ListFarmsResponse":
        """<p>Lists farms.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            principal_id: <p>The principal ID of the member to list on the farm.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_farms_request.ListFarmsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_farms_response.ListFarmsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_farms

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_farms.list_farms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_farms_request.ListFarmsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if principal_id is not None:
            input_["principal_id"] = principal_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_member_to_farm(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        principal_type: "aws_sdk_deadline.types.deadline_principal_type.DeadlinePrincipalType",
        identity_store_id: "aws_sdk_deadline.types.identity_store_id.IdentityStoreId",
        membership_level: "aws_sdk_deadline.types.membership_level.MembershipLevel",
        principal_id: "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        identity_center_region: Optional["aws_sdk_deadline.types.region.Region"] = None,
    ) -> "aws_sdk_deadline.types.associate_member_to_farm_response.AssociateMemberToFarmResponse":
        """<p>Assigns a farm membership level to a member.</p>

        Args:
            farm_id: <p>The ID of the farm to associate with the member.</p>
            principal_type: <p>The principal type of the member to associate with the farm.</p>
            identity_store_id: <p>The identity store ID of the member to associate with the farm.</p>
            membership_level: <p>The principal's membership level for the associated farm.</p>
            principal_id: <p>The member's principal ID to associate with the farm.</p>
            identity_center_region: <p>The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.associate_member_to_farm_request.AssociateMemberToFarmRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.associate_member_to_farm_response.AssociateMemberToFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.associate_member_to_farm

            output, http_response = (
                aws_sdk_deadline._operations.deadline.associate_member_to_farm.associate_member_to_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.associate_member_to_farm_request.AssociateMemberToFarmRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["principal_type"] = principal_type
        input_["identity_store_id"] = identity_store_id
        input_["membership_level"] = membership_level
        input_["principal_id"] = principal_id
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_limit(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        display_name: "aws_sdk_deadline.types.resource_name.ResourceName",
        amount_requirement_name: "aws_sdk_deadline.types.amount_requirement_name.AmountRequirementName",
        max_count: "aws_sdk_deadline.types.max_count.MaxCount",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        description: Optional["aws_sdk_deadline.types.description.Description"] = None,
    ) -> "aws_sdk_deadline.types.create_limit_response.CreateLimitResponse":
        """<p>Creates a limit that manages the distribution of shared resources, such as floating licenses. A limit can throttle work assignments, help manage workloads, and track current usage. Before you use a limit, you must associate the limit with one or more queues. </p> <p>You must add the <code>amountRequirementName</code> to a step in a job template to declare the limit requirement.</p>

        Args:
            farm_id: <p>The farm ID of the farm that contains the limit.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            amount_requirement_name: <p>The value that you specify as the <code>name</code> in the <code>amounts</code> field of the <code>hostRequirements</code> in a step of a job template to declare the limit requirement.</p>
            max_count: <p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>
            description: <p>A description of the limit. A description helps you identify the purpose of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.create_limit_request.CreateLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.create_limit_response.CreateLimitResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_limit

            output, http_response = (
                aws_sdk_deadline._operations.deadline.create_limit.create_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_limit_request.CreateLimitRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["display_name"] = display_name
        input_["amount_requirement_name"] = amount_requirement_name
        input_["max_count"] = max_count
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_storage_profile(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        display_name: "aws_sdk_deadline.types.resource_name.ResourceName",
        os_family: "aws_sdk_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        file_system_locations: Optional[
            "aws_sdk_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
    ) -> "aws_sdk_deadline.types.create_storage_profile_response.CreateStorageProfileResponse":
        """<p>Creates a storage profile that specifies the operating system, file type, and file location of resources used on a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to connect to the storage profile.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the storage profile.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            os_family: <p>The type of operating system (OS) for the storage profile.</p>
            file_system_locations: <p>File system paths to include in the storage profile.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.create_storage_profile_request.CreateStorageProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.create_storage_profile_response.CreateStorageProfileResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_storage_profile

            output, http_response = (
                aws_sdk_deadline._operations.deadline.create_storage_profile.create_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_storage_profile_request.CreateStorageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["display_name"] = display_name
        input_["os_family"] = os_family
        if file_system_locations is not None:
            input_["file_system_locations"] = file_system_locations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_limit(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        limit_id: "aws_sdk_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_limit_response.DeleteLimitResponse":
        """<p>Removes a limit from the specified farm. Before you delete a limit you must use the <code>DeleteQueueLimitAssociation</code> operation to remove the association with any queues. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit to delete.</p>
            limit_id: <p>The unique identifier of the limit to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.delete_limit_request.DeleteLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.delete_limit_response.DeleteLimitResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_limit

            output, http_response = (
                aws_sdk_deadline._operations.deadline.delete_limit.delete_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_limit_request.DeleteLimitRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["limit_id"] = limit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_storage_profile(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_storage_profile_response.DeleteStorageProfileResponse":
        """<p>Deletes a storage profile.</p>

        Args:
            farm_id: <p>The farm ID of the farm from which to remove the storage profile.</p>
            storage_profile_id: <p>The storage profile ID of the storage profile to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.delete_storage_profile_request.DeleteStorageProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.delete_storage_profile_response.DeleteStorageProfileResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_storage_profile

            output, http_response = (
                aws_sdk_deadline._operations.deadline.delete_storage_profile.delete_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_storage_profile_request.DeleteStorageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["storage_profile_id"] = storage_profile_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_member_from_farm(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        principal_id: "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.disassociate_member_from_farm_response.DisassociateMemberFromFarmResponse":
        """<p>Disassociates a member from a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to disassociate from the member.</p>
            principal_id: <p>A member's principal ID to disassociate from a farm.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.disassociate_member_from_farm_request.DisassociateMemberFromFarmRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.disassociate_member_from_farm_response.DisassociateMemberFromFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.disassociate_member_from_farm

            output, http_response = (
                aws_sdk_deadline._operations.deadline.disassociate_member_from_farm.disassociate_member_from_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.disassociate_member_from_farm_request.DisassociateMemberFromFarmRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["principal_id"] = principal_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_limit(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        limit_id: "aws_sdk_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_limit_response.GetLimitResponse":
        """<p>Gets information about a specific limit.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit.</p>
            limit_id: <p>The unique identifier of the limit to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.get_limit_request.GetLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.get_limit_response.GetLimitResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_limit

            output, http_response = (
                aws_sdk_deadline._operations.deadline.get_limit.get_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_limit_request.GetLimitRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["limit_id"] = limit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_storage_profile(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> (
        "aws_sdk_deadline.types.get_storage_profile_response.GetStorageProfileResponse"
    ):
        """<p>Gets a storage profile.</p>

        Args:
            farm_id: <p>The farm ID for the storage profile.</p>
            storage_profile_id: <p>The storage profile ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.get_storage_profile_request.GetStorageProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.get_storage_profile_response.GetStorageProfileResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_storage_profile

            output, http_response = (
                aws_sdk_deadline._operations.deadline.get_storage_profile.get_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_storage_profile_request.GetStorageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["storage_profile_id"] = storage_profile_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_farm_members(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_farm_members_response.ListFarmMembersResponse":
        """<p>Lists the members of a farm.</p>

        Args:
            farm_id: <p>The farm ID.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_farm_members_request.ListFarmMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_farm_members_response.ListFarmMembersResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_farm_members

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_farm_members.list_farm_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_farm_members_request.ListFarmMembersRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
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

    def list_limits(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_limits_response.ListLimitsResponse":
        """<p>Gets a list of limits defined in the specified farm.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limits.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of limits to return in each page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_limits_request.ListLimitsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_limits_response.ListLimitsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_limits

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_limits.list_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_limits_request.ListLimitsRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
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

    def list_storage_profiles(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_storage_profiles_response.ListStorageProfilesResponse":
        """<p>Lists storage profiles.</p>

        Args:
            farm_id: <p>The farm ID of the storage profile.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_storage_profiles_request.ListStorageProfilesRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_storage_profiles_response.ListStorageProfilesResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_storage_profiles

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_storage_profiles.list_storage_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_storage_profiles_request.ListStorageProfilesRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
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

    def update_limit(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        limit_id: "aws_sdk_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        display_name: Optional[
            "aws_sdk_deadline.types.resource_name.ResourceName"
        ] = None,
        description: Optional["aws_sdk_deadline.types.description.Description"] = None,
        max_count: Optional["aws_sdk_deadline.types.max_count.MaxCount"] = None,
    ) -> "aws_sdk_deadline.types.update_limit_response.UpdateLimitResponse":
        """<p>Updates the properties of the specified limit. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit.</p>
            limit_id: <p>The unique identifier of the limit to update.</p>
            display_name: <p>The new display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The new description of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            max_count: <p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>If more than the new maximum number is currently in use, running jobs finish but no new jobs are started until the number of resources in use is below the new maximum number.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.update_limit_request.UpdateLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.update_limit_response.UpdateLimitResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_limit

            output, http_response = (
                aws_sdk_deadline._operations.deadline.update_limit.update_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_limit_request.UpdateLimitRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["limit_id"] = limit_id
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if max_count is not None:
            input_["max_count"] = max_count

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_storage_profile(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        display_name: Optional[
            "aws_sdk_deadline.types.resource_name.ResourceName"
        ] = None,
        os_family: Optional[
            "aws_sdk_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
        ] = None,
        file_system_locations_to_add: Optional[
            "aws_sdk_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
        file_system_locations_to_remove: Optional[
            "aws_sdk_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
    ) -> "aws_sdk_deadline.types.update_storage_profile_response.UpdateStorageProfileResponse":
        """<p>Updates a storage profile.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            storage_profile_id: <p>The storage profile ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the storage profile to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            os_family: <p>The OS system to update.</p>
            file_system_locations_to_add: <p>The file system location names to add.</p>
            file_system_locations_to_remove: <p>The file system location names to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.update_storage_profile_response.UpdateStorageProfileResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_storage_profile

            output, http_response = (
                aws_sdk_deadline._operations.deadline.update_storage_profile.update_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["storage_profile_id"] = storage_profile_id
        if client_token is not None:
            input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if os_family is not None:
            input_["os_family"] = os_family
        if file_system_locations_to_add is not None:
            input_["file_system_locations_to_add"] = file_system_locations_to_add
        if file_system_locations_to_remove is not None:
            input_["file_system_locations_to_remove"] = file_system_locations_to_remove

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncFarmResource:
    def __init__(self, service: AsyncdeadlineClient) -> None:
        self._service = service

    async def create(
        self,
        display_name: "aws_sdk_deadline.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        description: Optional["aws_sdk_deadline.types.description.Description"] = None,
        kms_key_arn: Optional["aws_sdk_deadline.types.kms_key_arn.KmsKeyArn"] = None,
        cost_scale_factor: Optional[
            "aws_sdk_deadline.types.cost_scale_factor.CostScaleFactor"
        ] = None,
        tags: Optional["aws_sdk_deadline.types.tags.Tags"] = None,
    ) -> "aws_sdk_deadline.types.create_farm_response.CreateFarmResponse":
        """<p>Creates a farm to allow space for queues and fleets. Farms are the space where the components of your renders gather and are pieced together in the cloud. Farms contain budgets and allow you to enforce permissions. Deadline Cloud farms are a useful container for large projects.</p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            kms_key_arn: <p>The ARN of the KMS key to use on the farm.</p>
            cost_scale_factor: <p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment. The default value is 1.</p>
            tags: <p>The tags to add to your farm. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.create_farm_request.CreateFarmRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.create_farm_response.CreateFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_farm

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.create_farm.async_create_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_farm_request.CreateFarmRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if cost_scale_factor is not None:
            input_["cost_scale_factor"] = cost_scale_factor
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
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_farm_response.GetFarmResponse":
        """<p>Get a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.get_farm_request.GetFarmRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.get_farm_response.GetFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_farm

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.get_farm.async_get_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_farm_request.GetFarmRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        display_name: Optional[
            "aws_sdk_deadline.types.resource_name.ResourceName"
        ] = None,
        description: Optional["aws_sdk_deadline.types.description.Description"] = None,
        cost_scale_factor: Optional[
            "aws_sdk_deadline.types.cost_scale_factor.CostScaleFactor"
        ] = None,
    ) -> "aws_sdk_deadline.types.update_farm_response.UpdateFarmResponse":
        """<p>Updates a farm.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            display_name: <p>The display name of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            cost_scale_factor: <p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.update_farm_request.UpdateFarmRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.update_farm_response.UpdateFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_farm

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.update_farm.async_update_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_farm_request.UpdateFarmRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if cost_scale_factor is not None:
            input_["cost_scale_factor"] = cost_scale_factor

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_farm_response.DeleteFarmResponse":
        """<p>Deletes a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.delete_farm_request.DeleteFarmRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.delete_farm_response.DeleteFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_farm

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.delete_farm.async_delete_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_farm_request.DeleteFarmRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
    ) -> "aws_sdk_deadline.types.list_farms_response.ListFarmsResponse":
        """<p>Lists farms.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            principal_id: <p>The principal ID of the member to list on the farm.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.list_farms_request.ListFarmsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.list_farms_response.ListFarmsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_farms

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.list_farms.async_list_farms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_farms_request.ListFarmsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if principal_id is not None:
            input_["principal_id"] = principal_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_member_to_farm(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        principal_type: "aws_sdk_deadline.types.deadline_principal_type.DeadlinePrincipalType",
        identity_store_id: "aws_sdk_deadline.types.identity_store_id.IdentityStoreId",
        membership_level: "aws_sdk_deadline.types.membership_level.MembershipLevel",
        principal_id: "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        identity_center_region: Optional["aws_sdk_deadline.types.region.Region"] = None,
    ) -> "aws_sdk_deadline.types.associate_member_to_farm_response.AssociateMemberToFarmResponse":
        """<p>Assigns a farm membership level to a member.</p>

        Args:
            farm_id: <p>The ID of the farm to associate with the member.</p>
            principal_type: <p>The principal type of the member to associate with the farm.</p>
            identity_store_id: <p>The identity store ID of the member to associate with the farm.</p>
            membership_level: <p>The principal's membership level for the associated farm.</p>
            principal_id: <p>The member's principal ID to associate with the farm.</p>
            identity_center_region: <p>The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.associate_member_to_farm_request.AssociateMemberToFarmRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.associate_member_to_farm_response.AssociateMemberToFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.associate_member_to_farm

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.associate_member_to_farm.async_associate_member_to_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.associate_member_to_farm_request.AssociateMemberToFarmRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["principal_type"] = principal_type
        input_["identity_store_id"] = identity_store_id
        input_["membership_level"] = membership_level
        input_["principal_id"] = principal_id
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_limit(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        display_name: "aws_sdk_deadline.types.resource_name.ResourceName",
        amount_requirement_name: "aws_sdk_deadline.types.amount_requirement_name.AmountRequirementName",
        max_count: "aws_sdk_deadline.types.max_count.MaxCount",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        description: Optional["aws_sdk_deadline.types.description.Description"] = None,
    ) -> "aws_sdk_deadline.types.create_limit_response.CreateLimitResponse":
        """<p>Creates a limit that manages the distribution of shared resources, such as floating licenses. A limit can throttle work assignments, help manage workloads, and track current usage. Before you use a limit, you must associate the limit with one or more queues. </p> <p>You must add the <code>amountRequirementName</code> to a step in a job template to declare the limit requirement.</p>

        Args:
            farm_id: <p>The farm ID of the farm that contains the limit.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            amount_requirement_name: <p>The value that you specify as the <code>name</code> in the <code>amounts</code> field of the <code>hostRequirements</code> in a step of a job template to declare the limit requirement.</p>
            max_count: <p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>
            description: <p>A description of the limit. A description helps you identify the purpose of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.create_limit_request.CreateLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.create_limit_response.CreateLimitResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_limit

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.create_limit.async_create_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_limit_request.CreateLimitRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["display_name"] = display_name
        input_["amount_requirement_name"] = amount_requirement_name
        input_["max_count"] = max_count
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_storage_profile(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        display_name: "aws_sdk_deadline.types.resource_name.ResourceName",
        os_family: "aws_sdk_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        file_system_locations: Optional[
            "aws_sdk_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
    ) -> "aws_sdk_deadline.types.create_storage_profile_response.CreateStorageProfileResponse":
        """<p>Creates a storage profile that specifies the operating system, file type, and file location of resources used on a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to connect to the storage profile.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the storage profile.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            os_family: <p>The type of operating system (OS) for the storage profile.</p>
            file_system_locations: <p>File system paths to include in the storage profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.create_storage_profile_request.CreateStorageProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.create_storage_profile_response.CreateStorageProfileResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_storage_profile

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.create_storage_profile.async_create_storage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_storage_profile_request.CreateStorageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["display_name"] = display_name
        input_["os_family"] = os_family
        if file_system_locations is not None:
            input_["file_system_locations"] = file_system_locations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_limit(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        limit_id: "aws_sdk_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_limit_response.DeleteLimitResponse":
        """<p>Removes a limit from the specified farm. Before you delete a limit you must use the <code>DeleteQueueLimitAssociation</code> operation to remove the association with any queues. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit to delete.</p>
            limit_id: <p>The unique identifier of the limit to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.delete_limit_request.DeleteLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.delete_limit_response.DeleteLimitResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_limit

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.delete_limit.async_delete_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_limit_request.DeleteLimitRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["limit_id"] = limit_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_storage_profile(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_storage_profile_response.DeleteStorageProfileResponse":
        """<p>Deletes a storage profile.</p>

        Args:
            farm_id: <p>The farm ID of the farm from which to remove the storage profile.</p>
            storage_profile_id: <p>The storage profile ID of the storage profile to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.delete_storage_profile_request.DeleteStorageProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.delete_storage_profile_response.DeleteStorageProfileResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_storage_profile

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.delete_storage_profile.async_delete_storage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_storage_profile_request.DeleteStorageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["storage_profile_id"] = storage_profile_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_member_from_farm(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        principal_id: "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.disassociate_member_from_farm_response.DisassociateMemberFromFarmResponse":
        """<p>Disassociates a member from a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to disassociate from the member.</p>
            principal_id: <p>A member's principal ID to disassociate from a farm.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.disassociate_member_from_farm_request.DisassociateMemberFromFarmRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.disassociate_member_from_farm_response.DisassociateMemberFromFarmResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.disassociate_member_from_farm

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.disassociate_member_from_farm.async_disassociate_member_from_farm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.disassociate_member_from_farm_request.DisassociateMemberFromFarmRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["principal_id"] = principal_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_limit(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        limit_id: "aws_sdk_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_limit_response.GetLimitResponse":
        """<p>Gets information about a specific limit.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit.</p>
            limit_id: <p>The unique identifier of the limit to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.get_limit_request.GetLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.get_limit_response.GetLimitResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_limit

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.get_limit.async_get_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_limit_request.GetLimitRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["limit_id"] = limit_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_storage_profile(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> (
        "aws_sdk_deadline.types.get_storage_profile_response.GetStorageProfileResponse"
    ):
        """<p>Gets a storage profile.</p>

        Args:
            farm_id: <p>The farm ID for the storage profile.</p>
            storage_profile_id: <p>The storage profile ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.get_storage_profile_request.GetStorageProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.get_storage_profile_response.GetStorageProfileResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_storage_profile

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.get_storage_profile.async_get_storage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_storage_profile_request.GetStorageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["storage_profile_id"] = storage_profile_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_farm_members(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_farm_members_response.ListFarmMembersResponse":
        """<p>Lists the members of a farm.</p>

        Args:
            farm_id: <p>The farm ID.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.list_farm_members_request.ListFarmMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.list_farm_members_response.ListFarmMembersResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_farm_members

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.list_farm_members.async_list_farm_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_farm_members_request.ListFarmMembersRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
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

    async def list_limits(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_limits_response.ListLimitsResponse":
        """<p>Gets a list of limits defined in the specified farm.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limits.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of limits to return in each page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.list_limits_request.ListLimitsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.list_limits_response.ListLimitsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_limits

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.list_limits.async_list_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_limits_request.ListLimitsRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
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

    async def list_storage_profiles(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_storage_profiles_response.ListStorageProfilesResponse":
        """<p>Lists storage profiles.</p>

        Args:
            farm_id: <p>The farm ID of the storage profile.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.list_storage_profiles_request.ListStorageProfilesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.list_storage_profiles_response.ListStorageProfilesResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_storage_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.list_storage_profiles.async_list_storage_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_storage_profiles_request.ListStorageProfilesRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
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

    async def update_limit(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        limit_id: "aws_sdk_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        display_name: Optional[
            "aws_sdk_deadline.types.resource_name.ResourceName"
        ] = None,
        description: Optional["aws_sdk_deadline.types.description.Description"] = None,
        max_count: Optional["aws_sdk_deadline.types.max_count.MaxCount"] = None,
    ) -> "aws_sdk_deadline.types.update_limit_response.UpdateLimitResponse":
        """<p>Updates the properties of the specified limit. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit.</p>
            limit_id: <p>The unique identifier of the limit to update.</p>
            display_name: <p>The new display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The new description of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            max_count: <p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>If more than the new maximum number is currently in use, running jobs finish but no new jobs are started until the number of resources in use is below the new maximum number.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.update_limit_request.UpdateLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.update_limit_response.UpdateLimitResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_limit

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.update_limit.async_update_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_limit_request.UpdateLimitRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["limit_id"] = limit_id
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if max_count is not None:
            input_["max_count"] = max_count

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_storage_profile(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        storage_profile_id: "aws_sdk_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        display_name: Optional[
            "aws_sdk_deadline.types.resource_name.ResourceName"
        ] = None,
        os_family: Optional[
            "aws_sdk_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
        ] = None,
        file_system_locations_to_add: Optional[
            "aws_sdk_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
        file_system_locations_to_remove: Optional[
            "aws_sdk_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
    ) -> "aws_sdk_deadline.types.update_storage_profile_response.UpdateStorageProfileResponse":
        """<p>Updates a storage profile.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            storage_profile_id: <p>The storage profile ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the storage profile to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            os_family: <p>The OS system to update.</p>
            file_system_locations_to_add: <p>The file system location names to add.</p>
            file_system_locations_to_remove: <p>The file system location names to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.update_storage_profile_response.UpdateStorageProfileResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_storage_profile

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.update_storage_profile.async_update_storage_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["storage_profile_id"] = storage_profile_id
        if client_token is not None:
            input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if os_family is not None:
            input_["os_family"] = os_family
        if file_system_locations_to_add is not None:
            input_["file_system_locations_to_add"] = file_system_locations_to_add
        if file_system_locations_to_remove is not None:
            input_["file_system_locations_to_remove"] = file_system_locations_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
