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
    import aws_sdk_mgn.types.action_category
    import aws_sdk_mgn.types.action_description
    import aws_sdk_mgn.types.action_id
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.boot_mode
    import aws_sdk_mgn.types.bounded_string
    import aws_sdk_mgn.types.create_launch_configuration_template_request
    import aws_sdk_mgn.types.delete_launch_configuration_template_request
    import aws_sdk_mgn.types.delete_launch_configuration_template_response
    import aws_sdk_mgn.types.describe_launch_configuration_templates_request
    import aws_sdk_mgn.types.describe_launch_configuration_templates_response
    import aws_sdk_mgn.types.document_version
    import aws_sdk_mgn.types.kms_key_arn
    import aws_sdk_mgn.types.launch_configuration_template
    import aws_sdk_mgn.types.launch_configuration_template_i_ds
    import aws_sdk_mgn.types.launch_configuration_template_id
    import aws_sdk_mgn.types.launch_disposition
    import aws_sdk_mgn.types.launch_template_disk_conf
    import aws_sdk_mgn.types.licensing
    import aws_sdk_mgn.types.list_template_actions_request
    import aws_sdk_mgn.types.list_template_actions_response
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.operating_system_string
    import aws_sdk_mgn.types.order_type
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.positive_integer
    import aws_sdk_mgn.types.post_launch_actions
    import aws_sdk_mgn.types.put_template_action_request
    import aws_sdk_mgn.types.remove_template_action_request
    import aws_sdk_mgn.types.remove_template_action_response
    import aws_sdk_mgn.types.ssm_document_external_parameters
    import aws_sdk_mgn.types.ssm_document_parameters
    import aws_sdk_mgn.types.strictly_positive_integer
    import aws_sdk_mgn.types.tag_value
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.target_instance_type_right_sizing_method
    import aws_sdk_mgn.types.template_action_document
    import aws_sdk_mgn.types.template_actions_request_filters
    import aws_sdk_mgn.types.update_launch_configuration_template_request
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from aws_sdk_mgn._services.mgn import mgnClient, mgnClientConfig


class LaunchConfigurationTemplateResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        post_launch_actions: Optional[
            "aws_sdk_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional[
            "aws_sdk_mgn.types.tag_value.TagValue"
        ] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        launch_disposition: Optional[
            "aws_sdk_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "aws_sdk_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        associate_public_ip_address: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["aws_sdk_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["aws_sdk_mgn.types.boot_mode.BootMode"] = None,
        small_volume_max_size: Optional[
            "aws_sdk_mgn.types.positive_integer.PositiveInteger"
        ] = None,
        small_volume_conf: Optional[
            "aws_sdk_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        large_volume_conf: Optional[
            "aws_sdk_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        enable_parameters_encryption: Optional[bool] = None,
        parameters_encryption_key: Optional[
            "aws_sdk_mgn.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "aws_sdk_mgn.types.launch_configuration_template.LaunchConfigurationTemplate":
        """<p>Creates a new Launch Configuration Template.</p>

        Args:
            post_launch_actions: <p>Launch configuration template post launch actions.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration template map auto tagging MPE ID.</p>
            tags: <p>Request to associate tags during creation of a Launch Configuration Template.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private Ip.</p>
            associate_public_ip_address: <p>Associate public Ip address.</p>
            copy_tags: <p>Copy tags.</p>
            boot_mode: <p>Launch configuration template boot mode.</p>
            small_volume_max_size: <p>Small volume maximum size.</p>
            small_volume_conf: <p>Small volume config.</p>
            large_volume_conf: <p>Large volume config.</p>
            enable_parameters_encryption: <p>Enable parameters encryption.</p>
            parameters_encryption_key: <p>Parameters encryption key.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.create_launch_configuration_template

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.create_launch_configuration_template.create_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if tags is not None:
            input_["tags"] = tags
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if small_volume_max_size is not None:
            input_["small_volume_max_size"] = small_volume_max_size
        if small_volume_conf is not None:
            input_["small_volume_conf"] = small_volume_conf
        if large_volume_conf is not None:
            input_["large_volume_conf"] = large_volume_conf
        if enable_parameters_encryption is not None:
            input_["enable_parameters_encryption"] = enable_parameters_encryption
        if parameters_encryption_key is not None:
            input_["parameters_encryption_key"] = parameters_encryption_key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        post_launch_actions: Optional[
            "aws_sdk_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional[
            "aws_sdk_mgn.types.tag_value.TagValue"
        ] = None,
        launch_disposition: Optional[
            "aws_sdk_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "aws_sdk_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        associate_public_ip_address: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["aws_sdk_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["aws_sdk_mgn.types.boot_mode.BootMode"] = None,
        small_volume_max_size: Optional[
            "aws_sdk_mgn.types.positive_integer.PositiveInteger"
        ] = None,
        small_volume_conf: Optional[
            "aws_sdk_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        large_volume_conf: Optional[
            "aws_sdk_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        enable_parameters_encryption: Optional[bool] = None,
        parameters_encryption_key: Optional["aws_sdk_mgn.types.arn.ARN"] = None,
    ) -> "aws_sdk_mgn.types.launch_configuration_template.LaunchConfigurationTemplate":
        """<p>Updates an existing Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>Launch Configuration Template ID.</p>
            post_launch_actions: <p>Post Launch Action to execute on the Test or Cutover instance.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration template map auto tagging MPE ID.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private Ip.</p>
            associate_public_ip_address: <p>Associate public Ip address.</p>
            copy_tags: <p>Copy tags.</p>
            boot_mode: <p>Launch configuration template boot mode.</p>
            small_volume_max_size: <p>Small volume maximum size.</p>
            small_volume_conf: <p>Small volume config.</p>
            large_volume_conf: <p>Large volume config.</p>
            enable_parameters_encryption: <p>Enable parameters encryption.</p>
            parameters_encryption_key: <p>Parameters encryption key.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.update_launch_configuration_template

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.update_launch_configuration_template.update_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["launch_configuration_template_id"] = launch_configuration_template_id
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if small_volume_max_size is not None:
            input_["small_volume_max_size"] = small_volume_max_size
        if small_volume_conf is not None:
            input_["small_volume_conf"] = small_volume_conf
        if large_volume_conf is not None:
            input_["large_volume_conf"] = large_volume_conf
        if enable_parameters_encryption is not None:
            input_["enable_parameters_encryption"] = enable_parameters_encryption
        if parameters_encryption_key is not None:
            input_["parameters_encryption_key"] = parameters_encryption_key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse":
        """<p>Deletes a single Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>ID of resource to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.delete_launch_configuration_template

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.delete_launch_configuration_template.delete_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["launch_configuration_template_id"] = launch_configuration_template_id

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
        launch_configuration_template_i_ds: Optional[
            "aws_sdk_mgn.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse":
        """<p>Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs</p>

        Args:
            launch_configuration_template_i_ds: <p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>
            max_results: <p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>
            next_token: <p>Next pagination token returned from DescribeLaunchConfigurationTemplates.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.describe_launch_configuration_templates

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.describe_launch_configuration_templates.describe_launch_configuration_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest = {}  # type: ignore[typeddict-item]
        if launch_configuration_template_i_ds is not None:
            input_["launch_configuration_template_i_ds"] = (
                launch_configuration_template_i_ds
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_template_actions(
        self,
        launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.template_actions_request_filters.TemplateActionsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_template_actions_response.ListTemplateActionsResponse":
        """<p>List template post migration custom actions.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID.</p>
            filters: <p>Filters to apply when listing template post migration custom actions.</p>
            max_results: <p>Maximum amount of items to return when listing template post migration custom actions.</p>
            next_token: <p>Next token to use when listing template post migration custom actions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_template_actions_request.ListTemplateActionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_template_actions_response.ListTemplateActionsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_template_actions

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_template_actions.list_template_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_template_actions_request.ListTemplateActionsRequest = {}  # type: ignore[typeddict-item]
        input_["launch_configuration_template_id"] = launch_configuration_template_id
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_template_action(
        self,
        launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        action_name: "aws_sdk_mgn.types.bounded_string.BoundedString",
        document_identifier: "aws_sdk_mgn.types.bounded_string.BoundedString",
        order: "aws_sdk_mgn.types.order_type.OrderType",
        action_id: "aws_sdk_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        document_version: Optional[
            "aws_sdk_mgn.types.document_version.DocumentVersion"
        ] = None,
        active: Optional[bool] = None,
        timeout_seconds: Optional[
            "aws_sdk_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        must_succeed_for_cutover: Optional[bool] = None,
        parameters: Optional[
            "aws_sdk_mgn.types.ssm_document_parameters.SsmDocumentParameters"
        ] = None,
        operating_system: Optional[
            "aws_sdk_mgn.types.operating_system_string.OperatingSystemString"
        ] = None,
        external_parameters: Optional[
            "aws_sdk_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
        ] = None,
        description: Optional[
            "aws_sdk_mgn.types.action_description.ActionDescription"
        ] = None,
        category: Optional["aws_sdk_mgn.types.action_category.ActionCategory"] = None,
    ) -> "aws_sdk_mgn.types.template_action_document.TemplateActionDocument":
        """<p>Put template post migration custom action.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID.</p>
            action_name: <p>Template post migration custom action name.</p>
            document_identifier: <p>Template post migration custom action document identifier.</p>
            order: <p>Template post migration custom action order.</p>
            action_id: <p>Template post migration custom action ID.</p>
            document_version: <p>Template post migration custom action document version.</p>
            active: <p>Template post migration custom action active status.</p>
            timeout_seconds: <p>Template post migration custom action timeout in seconds.</p>
            must_succeed_for_cutover: <p>Template post migration custom action must succeed for cutover.</p>
            parameters: <p>Template post migration custom action parameters.</p>
            operating_system: <p>Operating system eligible for this template post migration custom action.</p>
            external_parameters: <p>Template post migration custom action external parameters.</p>
            description: <p>Template post migration custom action description.</p>
            category: <p>Template post migration custom action category.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.put_template_action_request.PutTemplateActionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.template_action_document.TemplateActionDocument"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.put_template_action

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.put_template_action.put_template_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.put_template_action_request.PutTemplateActionRequest = {}  # type: ignore[typeddict-item]
        input_["launch_configuration_template_id"] = launch_configuration_template_id
        input_["action_name"] = action_name
        input_["document_identifier"] = document_identifier
        input_["order"] = order
        input_["action_id"] = action_id
        if document_version is not None:
            input_["document_version"] = document_version
        if active is not None:
            input_["active"] = active
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if must_succeed_for_cutover is not None:
            input_["must_succeed_for_cutover"] = must_succeed_for_cutover
        if parameters is not None:
            input_["parameters"] = parameters
        if operating_system is not None:
            input_["operating_system"] = operating_system
        if external_parameters is not None:
            input_["external_parameters"] = external_parameters
        if description is not None:
            input_["description"] = description
        if category is not None:
            input_["category"] = category

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_template_action(
        self,
        launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        action_id: "aws_sdk_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> (
        "aws_sdk_mgn.types.remove_template_action_response.RemoveTemplateActionResponse"
    ):
        """<p>Remove template post migration custom action.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID of the post migration custom action to remove.</p>
            action_id: <p>Template post migration custom action ID to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.remove_template_action_request.RemoveTemplateActionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.remove_template_action_response.RemoveTemplateActionResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.remove_template_action

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.remove_template_action.remove_template_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.remove_template_action_request.RemoveTemplateActionRequest = {}  # type: ignore[typeddict-item]
        input_["launch_configuration_template_id"] = launch_configuration_template_id
        input_["action_id"] = action_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncLaunchConfigurationTemplateResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        post_launch_actions: Optional[
            "aws_sdk_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional[
            "aws_sdk_mgn.types.tag_value.TagValue"
        ] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        launch_disposition: Optional[
            "aws_sdk_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "aws_sdk_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        associate_public_ip_address: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["aws_sdk_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["aws_sdk_mgn.types.boot_mode.BootMode"] = None,
        small_volume_max_size: Optional[
            "aws_sdk_mgn.types.positive_integer.PositiveInteger"
        ] = None,
        small_volume_conf: Optional[
            "aws_sdk_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        large_volume_conf: Optional[
            "aws_sdk_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        enable_parameters_encryption: Optional[bool] = None,
        parameters_encryption_key: Optional[
            "aws_sdk_mgn.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "aws_sdk_mgn.types.launch_configuration_template.LaunchConfigurationTemplate":
        """<p>Creates a new Launch Configuration Template.</p>

        Args:
            post_launch_actions: <p>Launch configuration template post launch actions.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration template map auto tagging MPE ID.</p>
            tags: <p>Request to associate tags during creation of a Launch Configuration Template.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private Ip.</p>
            associate_public_ip_address: <p>Associate public Ip address.</p>
            copy_tags: <p>Copy tags.</p>
            boot_mode: <p>Launch configuration template boot mode.</p>
            small_volume_max_size: <p>Small volume maximum size.</p>
            small_volume_conf: <p>Small volume config.</p>
            large_volume_conf: <p>Large volume config.</p>
            enable_parameters_encryption: <p>Enable parameters encryption.</p>
            parameters_encryption_key: <p>Parameters encryption key.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.create_launch_configuration_template

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.create_launch_configuration_template.async_create_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if tags is not None:
            input_["tags"] = tags
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if small_volume_max_size is not None:
            input_["small_volume_max_size"] = small_volume_max_size
        if small_volume_conf is not None:
            input_["small_volume_conf"] = small_volume_conf
        if large_volume_conf is not None:
            input_["large_volume_conf"] = large_volume_conf
        if enable_parameters_encryption is not None:
            input_["enable_parameters_encryption"] = enable_parameters_encryption
        if parameters_encryption_key is not None:
            input_["parameters_encryption_key"] = parameters_encryption_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        post_launch_actions: Optional[
            "aws_sdk_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional[
            "aws_sdk_mgn.types.tag_value.TagValue"
        ] = None,
        launch_disposition: Optional[
            "aws_sdk_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "aws_sdk_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        associate_public_ip_address: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["aws_sdk_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["aws_sdk_mgn.types.boot_mode.BootMode"] = None,
        small_volume_max_size: Optional[
            "aws_sdk_mgn.types.positive_integer.PositiveInteger"
        ] = None,
        small_volume_conf: Optional[
            "aws_sdk_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        large_volume_conf: Optional[
            "aws_sdk_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        enable_parameters_encryption: Optional[bool] = None,
        parameters_encryption_key: Optional["aws_sdk_mgn.types.arn.ARN"] = None,
    ) -> "aws_sdk_mgn.types.launch_configuration_template.LaunchConfigurationTemplate":
        """<p>Updates an existing Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>Launch Configuration Template ID.</p>
            post_launch_actions: <p>Post Launch Action to execute on the Test or Cutover instance.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration template map auto tagging MPE ID.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private Ip.</p>
            associate_public_ip_address: <p>Associate public Ip address.</p>
            copy_tags: <p>Copy tags.</p>
            boot_mode: <p>Launch configuration template boot mode.</p>
            small_volume_max_size: <p>Small volume maximum size.</p>
            small_volume_conf: <p>Small volume config.</p>
            large_volume_conf: <p>Large volume config.</p>
            enable_parameters_encryption: <p>Enable parameters encryption.</p>
            parameters_encryption_key: <p>Parameters encryption key.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.update_launch_configuration_template

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.update_launch_configuration_template.async_update_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["launch_configuration_template_id"] = launch_configuration_template_id
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if small_volume_max_size is not None:
            input_["small_volume_max_size"] = small_volume_max_size
        if small_volume_conf is not None:
            input_["small_volume_conf"] = small_volume_conf
        if large_volume_conf is not None:
            input_["large_volume_conf"] = large_volume_conf
        if enable_parameters_encryption is not None:
            input_["enable_parameters_encryption"] = enable_parameters_encryption
        if parameters_encryption_key is not None:
            input_["parameters_encryption_key"] = parameters_encryption_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> "aws_sdk_mgn.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse":
        """<p>Deletes a single Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>ID of resource to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.delete_launch_configuration_template

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.delete_launch_configuration_template.async_delete_launch_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["launch_configuration_template_id"] = launch_configuration_template_id

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
        launch_configuration_template_i_ds: Optional[
            "aws_sdk_mgn.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse":
        """<p>Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs</p>

        Args:
            launch_configuration_template_i_ds: <p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>
            max_results: <p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>
            next_token: <p>Next pagination token returned from DescribeLaunchConfigurationTemplates.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.describe_launch_configuration_templates

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.describe_launch_configuration_templates.async_describe_launch_configuration_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest = {}  # type: ignore[typeddict-item]
        if launch_configuration_template_i_ds is not None:
            input_["launch_configuration_template_i_ds"] = (
                launch_configuration_template_i_ds
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_template_actions(
        self,
        launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.template_actions_request_filters.TemplateActionsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_template_actions_response.ListTemplateActionsResponse":
        """<p>List template post migration custom actions.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID.</p>
            filters: <p>Filters to apply when listing template post migration custom actions.</p>
            max_results: <p>Maximum amount of items to return when listing template post migration custom actions.</p>
            next_token: <p>Next token to use when listing template post migration custom actions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_template_actions_request.ListTemplateActionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_template_actions_response.ListTemplateActionsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_template_actions

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_template_actions.async_list_template_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_template_actions_request.ListTemplateActionsRequest = {}  # type: ignore[typeddict-item]
        input_["launch_configuration_template_id"] = launch_configuration_template_id
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_template_action(
        self,
        launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        action_name: "aws_sdk_mgn.types.bounded_string.BoundedString",
        document_identifier: "aws_sdk_mgn.types.bounded_string.BoundedString",
        order: "aws_sdk_mgn.types.order_type.OrderType",
        action_id: "aws_sdk_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        document_version: Optional[
            "aws_sdk_mgn.types.document_version.DocumentVersion"
        ] = None,
        active: Optional[bool] = None,
        timeout_seconds: Optional[
            "aws_sdk_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        must_succeed_for_cutover: Optional[bool] = None,
        parameters: Optional[
            "aws_sdk_mgn.types.ssm_document_parameters.SsmDocumentParameters"
        ] = None,
        operating_system: Optional[
            "aws_sdk_mgn.types.operating_system_string.OperatingSystemString"
        ] = None,
        external_parameters: Optional[
            "aws_sdk_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
        ] = None,
        description: Optional[
            "aws_sdk_mgn.types.action_description.ActionDescription"
        ] = None,
        category: Optional["aws_sdk_mgn.types.action_category.ActionCategory"] = None,
    ) -> "aws_sdk_mgn.types.template_action_document.TemplateActionDocument":
        """<p>Put template post migration custom action.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID.</p>
            action_name: <p>Template post migration custom action name.</p>
            document_identifier: <p>Template post migration custom action document identifier.</p>
            order: <p>Template post migration custom action order.</p>
            action_id: <p>Template post migration custom action ID.</p>
            document_version: <p>Template post migration custom action document version.</p>
            active: <p>Template post migration custom action active status.</p>
            timeout_seconds: <p>Template post migration custom action timeout in seconds.</p>
            must_succeed_for_cutover: <p>Template post migration custom action must succeed for cutover.</p>
            parameters: <p>Template post migration custom action parameters.</p>
            operating_system: <p>Operating system eligible for this template post migration custom action.</p>
            external_parameters: <p>Template post migration custom action external parameters.</p>
            description: <p>Template post migration custom action description.</p>
            category: <p>Template post migration custom action category.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.put_template_action_request.PutTemplateActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.template_action_document.TemplateActionDocument"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.put_template_action

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.put_template_action.async_put_template_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.put_template_action_request.PutTemplateActionRequest = {}  # type: ignore[typeddict-item]
        input_["launch_configuration_template_id"] = launch_configuration_template_id
        input_["action_name"] = action_name
        input_["document_identifier"] = document_identifier
        input_["order"] = order
        input_["action_id"] = action_id
        if document_version is not None:
            input_["document_version"] = document_version
        if active is not None:
            input_["active"] = active
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if must_succeed_for_cutover is not None:
            input_["must_succeed_for_cutover"] = must_succeed_for_cutover
        if parameters is not None:
            input_["parameters"] = parameters
        if operating_system is not None:
            input_["operating_system"] = operating_system
        if external_parameters is not None:
            input_["external_parameters"] = external_parameters
        if description is not None:
            input_["description"] = description
        if category is not None:
            input_["category"] = category

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_template_action(
        self,
        launch_configuration_template_id: "aws_sdk_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        action_id: "aws_sdk_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> (
        "aws_sdk_mgn.types.remove_template_action_response.RemoveTemplateActionResponse"
    ):
        """<p>Remove template post migration custom action.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID of the post migration custom action to remove.</p>
            action_id: <p>Template post migration custom action ID to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.remove_template_action_request.RemoveTemplateActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.remove_template_action_response.RemoveTemplateActionResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.remove_template_action

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.remove_template_action.async_remove_template_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.remove_template_action_request.RemoveTemplateActionRequest = {}  # type: ignore[typeddict-item]
        input_["launch_configuration_template_id"] = launch_configuration_template_id
        input_["action_id"] = action_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
