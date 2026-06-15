from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_data_automation._auth._signers
import aws_sdk_bedrock_data_automation._auth._sigv4
from aws_sdk_bedrock_data_automation._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_filter
    import aws_sdk_bedrock_data_automation.types.client_token
    import aws_sdk_bedrock_data_automation.types.create_data_automation_project_request
    import aws_sdk_bedrock_data_automation.types.create_data_automation_project_response
    import aws_sdk_bedrock_data_automation.types.custom_output_configuration
    import aws_sdk_bedrock_data_automation.types.data_automation_library_configuration
    import aws_sdk_bedrock_data_automation.types.data_automation_library_filter
    import aws_sdk_bedrock_data_automation.types.data_automation_project_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_project_description
    import aws_sdk_bedrock_data_automation.types.data_automation_project_name
    import aws_sdk_bedrock_data_automation.types.data_automation_project_stage
    import aws_sdk_bedrock_data_automation.types.data_automation_project_stage_filter
    import aws_sdk_bedrock_data_automation.types.data_automation_project_summary
    import aws_sdk_bedrock_data_automation.types.data_automation_project_type
    import aws_sdk_bedrock_data_automation.types.delete_data_automation_project_request
    import aws_sdk_bedrock_data_automation.types.delete_data_automation_project_response
    import aws_sdk_bedrock_data_automation.types.encryption_configuration
    import aws_sdk_bedrock_data_automation.types.get_data_automation_project_request
    import aws_sdk_bedrock_data_automation.types.get_data_automation_project_response
    import aws_sdk_bedrock_data_automation.types.list_data_automation_projects_request
    import aws_sdk_bedrock_data_automation.types.list_data_automation_projects_response
    import aws_sdk_bedrock_data_automation.types.max_results
    import aws_sdk_bedrock_data_automation.types.next_token
    import aws_sdk_bedrock_data_automation.types.override_configuration
    import aws_sdk_bedrock_data_automation.types.resource_owner
    import aws_sdk_bedrock_data_automation.types.standard_output_configuration
    import aws_sdk_bedrock_data_automation.types.tag_list
    import aws_sdk_bedrock_data_automation.types.update_data_automation_project_request
    import aws_sdk_bedrock_data_automation.types.update_data_automation_project_response
    from aws_sdk_bedrock_data_automation._services.async_bedrock_data_automation import (
        AsyncBedrockDataAutomationClient,
        AsyncBedrockDataAutomationClientConfig,
    )
    from aws_sdk_bedrock_data_automation._services.bedrock_data_automation import (
        BedrockDataAutomationClient,
        BedrockDataAutomationClientConfig,
    )


class DataAutomationProjectResource:
    def __init__(self, service: BedrockDataAutomationClient) -> None:
        self._service = service

    def create(
        self,
        project_name: "aws_sdk_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName",
        standard_output_configuration: "aws_sdk_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        project_description: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
        ] = None,
        project_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
        project_type: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
        ] = None,
        custom_output_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        override_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
        ] = None,
        data_automation_library_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["aws_sdk_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.create_data_automation_project_response.CreateDataAutomationProjectResponse":
        """Creates an Amazon Bedrock Data Automation Project"""

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.create_data_automation_project_response.CreateDataAutomationProjectResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_project

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_project.create_data_automation_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_name"] = project_name
        if project_description is not None:
            input_["project_description"] = project_description
        if project_stage is not None:
            input_["project_stage"] = project_stage
        if project_type is not None:
            input_["project_type"] = project_type
        input_["standard_output_configuration"] = standard_output_configuration
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if override_configuration is not None:
            input_["override_configuration"] = override_configuration
        if data_automation_library_configuration is not None:
            input_["data_automation_library_configuration"] = (
                data_automation_library_configuration
            )
        if client_token is not None:
            input_["client_token"] = client_token
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
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
        project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        project_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse":
        """Gets an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created
            project_stage: Optional field to delete a specific DataAutomationProject stage
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.get_data_automation_project_request.GetDataAutomationProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_project

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_project.get_data_automation_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.get_data_automation_project_request.GetDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        if project_stage is not None:
            input_["project_stage"] = project_stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        standard_output_configuration: "aws_sdk_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        project_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
        project_description: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
        ] = None,
        custom_output_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        override_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
        ] = None,
        data_automation_library_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.update_data_automation_project_response.UpdateDataAutomationProjectResponse":
        """Updates an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.update_data_automation_project_response.UpdateDataAutomationProjectResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_project

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_project.update_data_automation_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        if project_stage is not None:
            input_["project_stage"] = project_stage
        if project_description is not None:
            input_["project_description"] = project_description
        input_["standard_output_configuration"] = standard_output_configuration
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if override_configuration is not None:
            input_["override_configuration"] = override_configuration
        if data_automation_library_configuration is not None:
            input_["data_automation_library_configuration"] = (
                data_automation_library_configuration
            )
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.delete_data_automation_project_response.DeleteDataAutomationProjectResponse":
        """Deletes an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.delete_data_automation_project_request.DeleteDataAutomationProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.delete_data_automation_project_response.DeleteDataAutomationProjectResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_project

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_project.delete_data_automation_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.delete_data_automation_project_request.DeleteDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_stage_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_stage_filter.DataAutomationProjectStageFilter"
        ] = None,
        blueprint_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_filter.BlueprintFilter"
        ] = None,
        resource_owner: Optional[
            "aws_sdk_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        library_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_library_filter.DataAutomationLibraryFilter"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse":
        """Lists all existing Amazon Bedrock Data Automation Projects"""

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.list_data_automation_projects_request.ListDataAutomationProjectsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_projects

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_projects.list_data_automation_projects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.list_data_automation_projects_request.ListDataAutomationProjectsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_stage_filter is not None:
            input_["project_stage_filter"] = project_stage_filter
        if blueprint_filter is not None:
            input_["blueprint_filter"] = blueprint_filter
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if library_filter is not None:
            input_["library_filter"] = library_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDataAutomationProjectResource:
    def __init__(self, service: AsyncBedrockDataAutomationClient) -> None:
        self._service = service

    async def create(
        self,
        project_name: "aws_sdk_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName",
        standard_output_configuration: "aws_sdk_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        project_description: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
        ] = None,
        project_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
        project_type: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
        ] = None,
        custom_output_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        override_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
        ] = None,
        data_automation_library_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["aws_sdk_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.create_data_automation_project_response.CreateDataAutomationProjectResponse":
        """Creates an Amazon Bedrock Data Automation Project"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.create_data_automation_project_response.CreateDataAutomationProjectResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_project

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_project.async_create_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.create_data_automation_project_request.CreateDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_name"] = project_name
        if project_description is not None:
            input_["project_description"] = project_description
        if project_stage is not None:
            input_["project_stage"] = project_stage
        if project_type is not None:
            input_["project_type"] = project_type
        input_["standard_output_configuration"] = standard_output_configuration
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if override_configuration is not None:
            input_["override_configuration"] = override_configuration
        if data_automation_library_configuration is not None:
            input_["data_automation_library_configuration"] = (
                data_automation_library_configuration
            )
        if client_token is not None:
            input_["client_token"] = client_token
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
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
        project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        project_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse":
        """Gets an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created
            project_stage: Optional field to delete a specific DataAutomationProject stage
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.get_data_automation_project_request.GetDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.get_data_automation_project_response.GetDataAutomationProjectResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_project

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_project.async_get_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.get_data_automation_project_request.GetDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        if project_stage is not None:
            input_["project_stage"] = project_stage

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        standard_output_configuration: "aws_sdk_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        project_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
        ] = None,
        project_description: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
        ] = None,
        custom_output_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        override_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
        ] = None,
        data_automation_library_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.update_data_automation_project_response.UpdateDataAutomationProjectResponse":
        """Updates an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.update_data_automation_project_response.UpdateDataAutomationProjectResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_project

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_project.async_update_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.update_data_automation_project_request.UpdateDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        if project_stage is not None:
            input_["project_stage"] = project_stage
        if project_description is not None:
            input_["project_description"] = project_description
        input_["standard_output_configuration"] = standard_output_configuration
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if override_configuration is not None:
            input_["override_configuration"] = override_configuration
        if data_automation_library_configuration is not None:
            input_["data_automation_library_configuration"] = (
                data_automation_library_configuration
            )
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.delete_data_automation_project_response.DeleteDataAutomationProjectResponse":
        """Deletes an existing Amazon Bedrock Data Automation Project

        Args:
            project_arn: ARN generated at the server side when a DataAutomationProject is created
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.delete_data_automation_project_request.DeleteDataAutomationProjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.delete_data_automation_project_response.DeleteDataAutomationProjectResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_project

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_project.async_delete_data_automation_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.delete_data_automation_project_request.DeleteDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_stage_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_stage_filter.DataAutomationProjectStageFilter"
        ] = None,
        blueprint_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_filter.BlueprintFilter"
        ] = None,
        resource_owner: Optional[
            "aws_sdk_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        library_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_library_filter.DataAutomationLibraryFilter"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse":
        """Lists all existing Amazon Bedrock Data Automation Projects"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.list_data_automation_projects_request.ListDataAutomationProjectsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.list_data_automation_projects_response.ListDataAutomationProjectsResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_projects

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_projects.async_list_data_automation_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.list_data_automation_projects_request.ListDataAutomationProjectsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_stage_filter is not None:
            input_["project_stage_filter"] = project_stage_filter
        if blueprint_filter is not None:
            input_["blueprint_filter"] = blueprint_filter
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if library_filter is not None:
            input_["library_filter"] = library_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
