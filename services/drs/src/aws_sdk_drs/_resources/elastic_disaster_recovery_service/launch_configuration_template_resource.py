from typing import Optional, TYPE_CHECKING
from aws_sdk_drs._services.async_drs import ensure_async_iterator
from aws_sdk_drs._services.drs import ensure_sync_iterator
from aws_sdk_drs._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_drs._auth._signers
import aws_sdk_drs._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_drs._services.drs import drsClient, drsClientConfig
    from aws_sdk_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    import aws_sdk_drs.types.arn
    import aws_sdk_drs.types.create_launch_configuration_template_request
    import aws_sdk_drs.types.create_launch_configuration_template_response
    import aws_sdk_drs.types.delete_launch_configuration_template_request
    import aws_sdk_drs.types.delete_launch_configuration_template_response
    import aws_sdk_drs.types.describe_launch_configuration_templates_request
    import aws_sdk_drs.types.describe_launch_configuration_templates_response
    import aws_sdk_drs.types.launch_configuration_template
    import aws_sdk_drs.types.launch_configuration_template_i_ds
    import aws_sdk_drs.types.launch_configuration_template_id
    import aws_sdk_drs.types.launch_disposition
    import aws_sdk_drs.types.licensing
    import aws_sdk_drs.types.max_results_type
    import aws_sdk_drs.types.pagination_token
    import aws_sdk_drs.types.tags_map
    import aws_sdk_drs.types.target_instance_type_right_sizing_method
    import aws_sdk_drs.types.update_launch_configuration_template_request
    import aws_sdk_drs.types.update_launch_configuration_template_response

class LaunchConfigurationTemplateResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service
    def create(self, *, config_overrides: Optional[drsClientConfig] = None, tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None, launch_disposition: Optional["aws_sdk_drs.types.launch_disposition.LaunchDisposition"] = None, target_instance_type_right_sizing_method: Optional["aws_sdk_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"] = None, copy_private_ip: Optional[bool] = None, copy_tags: Optional[bool] = None, licensing: Optional["aws_sdk_drs.types.licensing.Licensing"] = None, export_bucket_arn: Optional["aws_sdk_drs.types.arn.ARN"] = None, post_launch_enabled: Optional[bool] = None, launch_into_source_instance: Optional[bool] = None) -> "aws_sdk_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse":
        """<p>Creates a new Launch Configuration Template.</p>

        Args:
            tags: <p>Request to associate tags during creation of a Launch Configuration Template.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private IP.</p>
            copy_tags: <p>Copy tags.</p>
            licensing: <p>Licensing.</p>
            export_bucket_arn: <p>S3 bucket ARN to export Source Network templates.</p>
            post_launch_enabled: <p>Whether we want to activate post-launch actions.</p>
            launch_into_source_instance: <p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest]') -> OperationResponse["aws_sdk_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.create_launch_configuration_template
            output, http_response = aws_sdk_drs._operations.elastic_disaster_recovery_service.create_launch_configuration_template.create_launch_configuration_template(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        if tags is not None:
            input["tags"] = tags
        if launch_disposition is not None:
            input["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input["target_instance_type_right_sizing_method"] = target_instance_type_right_sizing_method
        if copy_private_ip is not None:
            input["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input["copy_tags"] = copy_tags
        if licensing is not None:
            input["licensing"] = licensing
        if export_bucket_arn is not None:
            input["export_bucket_arn"] = export_bucket_arn
        if post_launch_enabled is not None:
            input["post_launch_enabled"] = post_launch_enabled
        if launch_into_source_instance is not None:
            input["launch_into_source_instance"] = launch_into_source_instance

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, launch_configuration_template_id: "aws_sdk_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID", *, config_overrides: Optional[drsClientConfig] = None, launch_disposition: Optional["aws_sdk_drs.types.launch_disposition.LaunchDisposition"] = None, target_instance_type_right_sizing_method: Optional["aws_sdk_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"] = None, copy_private_ip: Optional[bool] = None, copy_tags: Optional[bool] = None, licensing: Optional["aws_sdk_drs.types.licensing.Licensing"] = None, export_bucket_arn: Optional["aws_sdk_drs.types.arn.ARN"] = None, post_launch_enabled: Optional[bool] = None, launch_into_source_instance: Optional[bool] = None) -> "aws_sdk_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse":
        """<p>Updates an existing Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>Launch Configuration Template ID.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private IP.</p>
            copy_tags: <p>Copy tags.</p>
            licensing: <p>Licensing.</p>
            export_bucket_arn: <p>S3 bucket ARN to export Source Network templates.</p>
            post_launch_enabled: <p>Whether we want to activate post-launch actions.</p>
            launch_into_source_instance: <p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_drs.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest]') -> OperationResponse["aws_sdk_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.update_launch_configuration_template
            output, http_response = aws_sdk_drs._operations.elastic_disaster_recovery_service.update_launch_configuration_template.update_launch_configuration_template(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_drs.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input["launch_configuration_template_id"] = launch_configuration_template_id
        if launch_disposition is not None:
            input["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input["target_instance_type_right_sizing_method"] = target_instance_type_right_sizing_method
        if copy_private_ip is not None:
            input["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input["copy_tags"] = copy_tags
        if licensing is not None:
            input["licensing"] = licensing
        if export_bucket_arn is not None:
            input["export_bucket_arn"] = export_bucket_arn
        if post_launch_enabled is not None:
            input["post_launch_enabled"] = post_launch_enabled
        if launch_into_source_instance is not None:
            input["launch_into_source_instance"] = launch_into_source_instance

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, launch_configuration_template_id: "aws_sdk_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID", *, config_overrides: Optional[drsClientConfig] = None) -> "aws_sdk_drs.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse":
        """<p>Deletes a single Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>The ID of the Launch Configuration Template to be deleted.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_drs.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest]') -> OperationResponse["aws_sdk_drs.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_launch_configuration_template
            output, http_response = aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_launch_configuration_template.delete_launch_configuration_template(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_drs.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input["launch_configuration_template_id"] = launch_configuration_template_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[drsClientConfig] = None, launch_configuration_template_i_ds: Optional["aws_sdk_drs.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"] = None, max_results: Optional["aws_sdk_drs.types.max_results_type.MaxResultsType"] = None, next_token: Optional["aws_sdk_drs.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse":
        """<p>Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs</p>

        Args:
            launch_configuration_template_i_ds: <p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>
            max_results: <p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>
            next_token: <p>The token of the next Launch Configuration Template to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_drs.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest]') -> OperationResponse["aws_sdk_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_launch_configuration_templates
            output, http_response = aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_launch_configuration_templates.describe_launch_configuration_templates(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_drs.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest = {}  # type: ignore[typeddict-item]
        if launch_configuration_template_i_ds is not None:
            input["launch_configuration_template_i_ds"] = launch_configuration_template_i_ds
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncLaunchConfigurationTemplateResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service
    async def create(self, *, config_overrides: Optional[AsyncdrsClientConfig] = None, tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None, launch_disposition: Optional["aws_sdk_drs.types.launch_disposition.LaunchDisposition"] = None, target_instance_type_right_sizing_method: Optional["aws_sdk_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"] = None, copy_private_ip: Optional[bool] = None, copy_tags: Optional[bool] = None, licensing: Optional["aws_sdk_drs.types.licensing.Licensing"] = None, export_bucket_arn: Optional["aws_sdk_drs.types.arn.ARN"] = None, post_launch_enabled: Optional[bool] = None, launch_into_source_instance: Optional[bool] = None) -> "aws_sdk_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse":
        """<p>Creates a new Launch Configuration Template.</p>

        Args:
            tags: <p>Request to associate tags during creation of a Launch Configuration Template.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private IP.</p>
            copy_tags: <p>Copy tags.</p>
            licensing: <p>Licensing.</p>
            export_bucket_arn: <p>S3 bucket ARN to export Source Network templates.</p>
            post_launch_enabled: <p>Whether we want to activate post-launch actions.</p>
            launch_into_source_instance: <p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest]') -> AsyncOperationResponse["aws_sdk_drs.types.create_launch_configuration_template_response.CreateLaunchConfigurationTemplateResponse"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.create_launch_configuration_template
            output, http_response = await aws_sdk_drs._operations.elastic_disaster_recovery_service.create_launch_configuration_template.async_create_launch_configuration_template(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_drs.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        if tags is not None:
            input["tags"] = tags
        if launch_disposition is not None:
            input["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input["target_instance_type_right_sizing_method"] = target_instance_type_right_sizing_method
        if copy_private_ip is not None:
            input["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input["copy_tags"] = copy_tags
        if licensing is not None:
            input["licensing"] = licensing
        if export_bucket_arn is not None:
            input["export_bucket_arn"] = export_bucket_arn
        if post_launch_enabled is not None:
            input["post_launch_enabled"] = post_launch_enabled
        if launch_into_source_instance is not None:
            input["launch_into_source_instance"] = launch_into_source_instance

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, launch_configuration_template_id: "aws_sdk_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID", *, config_overrides: Optional[AsyncdrsClientConfig] = None, launch_disposition: Optional["aws_sdk_drs.types.launch_disposition.LaunchDisposition"] = None, target_instance_type_right_sizing_method: Optional["aws_sdk_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"] = None, copy_private_ip: Optional[bool] = None, copy_tags: Optional[bool] = None, licensing: Optional["aws_sdk_drs.types.licensing.Licensing"] = None, export_bucket_arn: Optional["aws_sdk_drs.types.arn.ARN"] = None, post_launch_enabled: Optional[bool] = None, launch_into_source_instance: Optional[bool] = None) -> "aws_sdk_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse":
        """<p>Updates an existing Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>Launch Configuration Template ID.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private IP.</p>
            copy_tags: <p>Copy tags.</p>
            licensing: <p>Licensing.</p>
            export_bucket_arn: <p>S3 bucket ARN to export Source Network templates.</p>
            post_launch_enabled: <p>Whether we want to activate post-launch actions.</p>
            launch_into_source_instance: <p>DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_drs.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest]') -> AsyncOperationResponse["aws_sdk_drs.types.update_launch_configuration_template_response.UpdateLaunchConfigurationTemplateResponse"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.update_launch_configuration_template
            output, http_response = await aws_sdk_drs._operations.elastic_disaster_recovery_service.update_launch_configuration_template.async_update_launch_configuration_template(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_drs.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input["launch_configuration_template_id"] = launch_configuration_template_id
        if launch_disposition is not None:
            input["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input["target_instance_type_right_sizing_method"] = target_instance_type_right_sizing_method
        if copy_private_ip is not None:
            input["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input["copy_tags"] = copy_tags
        if licensing is not None:
            input["licensing"] = licensing
        if export_bucket_arn is not None:
            input["export_bucket_arn"] = export_bucket_arn
        if post_launch_enabled is not None:
            input["post_launch_enabled"] = post_launch_enabled
        if launch_into_source_instance is not None:
            input["launch_into_source_instance"] = launch_into_source_instance

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, launch_configuration_template_id: "aws_sdk_drs.types.launch_configuration_template_id.LaunchConfigurationTemplateID", *, config_overrides: Optional[AsyncdrsClientConfig] = None) -> "aws_sdk_drs.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse":
        """<p>Deletes a single Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>The ID of the Launch Configuration Template to be deleted.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_drs.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest]') -> AsyncOperationResponse["aws_sdk_drs.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_launch_configuration_template
            output, http_response = await aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_launch_configuration_template.async_delete_launch_configuration_template(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_drs.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input["launch_configuration_template_id"] = launch_configuration_template_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncdrsClientConfig] = None, launch_configuration_template_i_ds: Optional["aws_sdk_drs.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"] = None, max_results: Optional["aws_sdk_drs.types.max_results_type.MaxResultsType"] = None, next_token: Optional["aws_sdk_drs.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse":
        """<p>Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs</p>

        Args:
            launch_configuration_template_i_ds: <p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>
            max_results: <p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>
            next_token: <p>The token of the next Launch Configuration Template to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_drs.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest]') -> AsyncOperationResponse["aws_sdk_drs.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_launch_configuration_templates
            output, http_response = await aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_launch_configuration_templates.async_describe_launch_configuration_templates(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_drs.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest = {}  # type: ignore[typeddict-item]
        if launch_configuration_template_i_ds is not None:
            input["launch_configuration_template_i_ds"] = launch_configuration_template_i_ds
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output