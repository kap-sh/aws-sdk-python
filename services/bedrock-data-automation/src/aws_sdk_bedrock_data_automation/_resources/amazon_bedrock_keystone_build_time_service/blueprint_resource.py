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
    import aws_sdk_bedrock_data_automation.types.blueprint_arn
    import aws_sdk_bedrock_data_automation.types.blueprint_name
    import aws_sdk_bedrock_data_automation.types.blueprint_schema
    import aws_sdk_bedrock_data_automation.types.blueprint_stage
    import aws_sdk_bedrock_data_automation.types.blueprint_stage_filter
    import aws_sdk_bedrock_data_automation.types.blueprint_summary
    import aws_sdk_bedrock_data_automation.types.blueprint_version
    import aws_sdk_bedrock_data_automation.types.client_token
    import aws_sdk_bedrock_data_automation.types.create_blueprint_request
    import aws_sdk_bedrock_data_automation.types.create_blueprint_response
    import aws_sdk_bedrock_data_automation.types.data_automation_project_filter
    import aws_sdk_bedrock_data_automation.types.delete_blueprint_request
    import aws_sdk_bedrock_data_automation.types.delete_blueprint_response
    import aws_sdk_bedrock_data_automation.types.encryption_configuration
    import aws_sdk_bedrock_data_automation.types.get_blueprint_request
    import aws_sdk_bedrock_data_automation.types.get_blueprint_response
    import aws_sdk_bedrock_data_automation.types.list_blueprints_request
    import aws_sdk_bedrock_data_automation.types.list_blueprints_response
    import aws_sdk_bedrock_data_automation.types.max_results
    import aws_sdk_bedrock_data_automation.types.next_token
    import aws_sdk_bedrock_data_automation.types.resource_owner
    import aws_sdk_bedrock_data_automation.types.tag_list
    import aws_sdk_bedrock_data_automation.types.type
    import aws_sdk_bedrock_data_automation.types.update_blueprint_request
    import aws_sdk_bedrock_data_automation.types.update_blueprint_response
    from aws_sdk_bedrock_data_automation._services.async_bedrock_data_automation import (
        AsyncBedrockDataAutomationClient,
        AsyncBedrockDataAutomationClientConfig,
    )
    from aws_sdk_bedrock_data_automation._services.bedrock_data_automation import (
        BedrockDataAutomationClient,
        BedrockDataAutomationClientConfig,
    )


class BlueprintResource:
    def __init__(self, service: BedrockDataAutomationClient) -> None:
        self._service = service

    def create(
        self,
        blueprint_name: "aws_sdk_bedrock_data_automation.types.blueprint_name.BlueprintName",
        type: "aws_sdk_bedrock_data_automation.types.type.Type",
        schema: "aws_sdk_bedrock_data_automation.types.blueprint_schema.BlueprintSchema",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        blueprint_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["aws_sdk_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse":
        """Creates an Amazon Bedrock Data Automation Blueprint

        Raises:
            aws_sdk_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            aws_sdk_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            aws_sdk_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            aws_sdk_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            aws_sdk_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            aws_sdk_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            aws_sdk_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint.create_blueprint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_name"] = blueprint_name
        input_["type"] = type
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage
        input_["schema"] = schema
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
        blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        blueprint_version: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
        ] = None,
        blueprint_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse":
        """Gets an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created
            blueprint_version: Optional field to get a specific Blueprint version
            blueprint_stage: Optional field to get a specific Blueprint stage

        Raises:
            aws_sdk_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            aws_sdk_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            aws_sdk_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            aws_sdk_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            aws_sdk_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            aws_sdk_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.get_blueprint_request.GetBlueprintRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint.get_blueprint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.get_blueprint_request.GetBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_arn"] = blueprint_arn
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        schema: "aws_sdk_bedrock_data_automation.types.blueprint_schema.BlueprintSchema",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        blueprint_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse":
        """Updates an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created

        Raises:
            aws_sdk_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            aws_sdk_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            aws_sdk_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            aws_sdk_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            aws_sdk_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            aws_sdk_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            aws_sdk_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_blueprint

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_blueprint.update_blueprint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_arn"] = blueprint_arn
        input_["schema"] = schema
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage
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
        blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        blueprint_version: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.delete_blueprint_response.DeleteBlueprintResponse":
        """Deletes an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created
            blueprint_version: Optional field to delete a specific Blueprint version

        Raises:
            aws_sdk_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            aws_sdk_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            aws_sdk_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            aws_sdk_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            aws_sdk_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            aws_sdk_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.delete_blueprint_request.DeleteBlueprintRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.delete_blueprint_response.DeleteBlueprintResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_blueprint

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_blueprint.delete_blueprint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.delete_blueprint_request.DeleteBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_arn"] = blueprint_arn
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version

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
        blueprint_arn: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
        ] = None,
        resource_owner: Optional[
            "aws_sdk_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        blueprint_stage_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_stage_filter.BlueprintStageFilter"
        ] = None,
        max_results: Optional[
            "aws_sdk_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse":
        """Lists all existing Amazon Bedrock Data Automation Blueprints

        Raises:
            aws_sdk_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            aws_sdk_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            aws_sdk_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            aws_sdk_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            aws_sdk_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            aws_sdk_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.list_blueprints_request.ListBlueprintsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_blueprints

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_blueprints.list_blueprints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.list_blueprints_request.ListBlueprintsRequest = {}  # type: ignore[typeddict-item]
        if blueprint_arn is not None:
            input_["blueprint_arn"] = blueprint_arn
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if blueprint_stage_filter is not None:
            input_["blueprint_stage_filter"] = blueprint_stage_filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_filter is not None:
            input_["project_filter"] = project_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncBlueprintResource:
    def __init__(self, service: AsyncBedrockDataAutomationClient) -> None:
        self._service = service

    async def create(
        self,
        blueprint_name: "aws_sdk_bedrock_data_automation.types.blueprint_name.BlueprintName",
        type: "aws_sdk_bedrock_data_automation.types.type.Type",
        schema: "aws_sdk_bedrock_data_automation.types.blueprint_schema.BlueprintSchema",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["aws_sdk_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse":
        """Creates an Amazon Bedrock Data Automation Blueprint

        Raises:
            aws_sdk_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            aws_sdk_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            aws_sdk_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            aws_sdk_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            aws_sdk_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            aws_sdk_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            aws_sdk_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.create_blueprint_response.CreateBlueprintResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_blueprint.async_create_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.create_blueprint_request.CreateBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_name"] = blueprint_name
        input_["type"] = type
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage
        input_["schema"] = schema
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
        blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_version: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
        ] = None,
        blueprint_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse":
        """Gets an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created
            blueprint_version: Optional field to get a specific Blueprint version
            blueprint_stage: Optional field to get a specific Blueprint stage

        Raises:
            aws_sdk_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            aws_sdk_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            aws_sdk_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            aws_sdk_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            aws_sdk_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            aws_sdk_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.get_blueprint_request.GetBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.get_blueprint_response.GetBlueprintResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint.async_get_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.get_blueprint_request.GetBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_arn"] = blueprint_arn
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        schema: "aws_sdk_bedrock_data_automation.types.blueprint_schema.BlueprintSchema",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_stage: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse":
        """Updates an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created

        Raises:
            aws_sdk_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            aws_sdk_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            aws_sdk_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            aws_sdk_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            aws_sdk_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            aws_sdk_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            aws_sdk_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.update_blueprint_response.UpdateBlueprintResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_blueprint.async_update_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.update_blueprint_request.UpdateBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_arn"] = blueprint_arn
        input_["schema"] = schema
        if blueprint_stage is not None:
            input_["blueprint_stage"] = blueprint_stage
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
        blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        blueprint_version: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.delete_blueprint_response.DeleteBlueprintResponse":
        """Deletes an existing Amazon Bedrock Data Automation Blueprint

        Args:
            blueprint_arn: ARN generated at the server side when a Blueprint is created
            blueprint_version: Optional field to delete a specific Blueprint version

        Raises:
            aws_sdk_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            aws_sdk_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            aws_sdk_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            aws_sdk_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            aws_sdk_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            aws_sdk_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.delete_blueprint_request.DeleteBlueprintRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.delete_blueprint_response.DeleteBlueprintResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_blueprint

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_blueprint.async_delete_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.delete_blueprint_request.DeleteBlueprintRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint_arn"] = blueprint_arn
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version

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
        blueprint_arn: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
        ] = None,
        resource_owner: Optional[
            "aws_sdk_bedrock_data_automation.types.resource_owner.ResourceOwner"
        ] = None,
        blueprint_stage_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.blueprint_stage_filter.BlueprintStageFilter"
        ] = None,
        max_results: Optional[
            "aws_sdk_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
        project_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse":
        """Lists all existing Amazon Bedrock Data Automation Blueprints

        Raises:
            aws_sdk_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            aws_sdk_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            aws_sdk_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            aws_sdk_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            aws_sdk_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            aws_sdk_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.list_blueprints_request.ListBlueprintsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.list_blueprints_response.ListBlueprintsResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_blueprints

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_blueprints.async_list_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.list_blueprints_request.ListBlueprintsRequest = {}  # type: ignore[typeddict-item]
        if blueprint_arn is not None:
            input_["blueprint_arn"] = blueprint_arn
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner
        if blueprint_stage_filter is not None:
            input_["blueprint_stage_filter"] = blueprint_stage_filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_filter is not None:
            input_["project_filter"] = project_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
