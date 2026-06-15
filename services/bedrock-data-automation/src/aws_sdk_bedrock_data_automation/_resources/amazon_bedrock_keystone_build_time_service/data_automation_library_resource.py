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
    import aws_sdk_bedrock_data_automation.types.client_token
    import aws_sdk_bedrock_data_automation.types.create_data_automation_library_request
    import aws_sdk_bedrock_data_automation.types.create_data_automation_library_response
    import aws_sdk_bedrock_data_automation.types.data_automation_library_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_library_description
    import aws_sdk_bedrock_data_automation.types.data_automation_library_name
    import aws_sdk_bedrock_data_automation.types.data_automation_library_summary
    import aws_sdk_bedrock_data_automation.types.data_automation_project_filter
    import aws_sdk_bedrock_data_automation.types.delete_data_automation_library_request
    import aws_sdk_bedrock_data_automation.types.delete_data_automation_library_response
    import aws_sdk_bedrock_data_automation.types.encryption_configuration
    import aws_sdk_bedrock_data_automation.types.get_data_automation_library_request
    import aws_sdk_bedrock_data_automation.types.get_data_automation_library_response
    import aws_sdk_bedrock_data_automation.types.list_data_automation_libraries_request
    import aws_sdk_bedrock_data_automation.types.list_data_automation_libraries_response
    import aws_sdk_bedrock_data_automation.types.max_results
    import aws_sdk_bedrock_data_automation.types.next_token
    import aws_sdk_bedrock_data_automation.types.tag_list
    import aws_sdk_bedrock_data_automation.types.update_data_automation_library_request
    import aws_sdk_bedrock_data_automation.types.update_data_automation_library_response
    from aws_sdk_bedrock_data_automation._services.async_bedrock_data_automation import (
        AsyncBedrockDataAutomationClient,
        AsyncBedrockDataAutomationClientConfig,
    )
    from aws_sdk_bedrock_data_automation._services.bedrock_data_automation import (
        BedrockDataAutomationClient,
        BedrockDataAutomationClientConfig,
    )


class DataAutomationLibraryResource:
    def __init__(self, service: BedrockDataAutomationClient) -> None:
        self._service = service

    def create(
        self,
        library_name: "aws_sdk_bedrock_data_automation.types.data_automation_library_name.DataAutomationLibraryName",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        library_description: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["aws_sdk_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.create_data_automation_library_response.CreateDataAutomationLibraryResponse":
        """Creates an Amazon Bedrock Data Automation Library"""

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.create_data_automation_library_response.CreateDataAutomationLibraryResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_library

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_library.create_data_automation_library(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
        input_["library_name"] = library_name
        if library_description is not None:
            input_["library_description"] = library_description
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
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse":
        """Gets an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.get_data_automation_library_request.GetDataAutomationLibraryRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library.get_data_automation_library(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.get_data_automation_library_request.GetDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        library_description: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.update_data_automation_library_response.UpdateDataAutomationLibraryResponse":
        """Updates an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.update_data_automation_library_response.UpdateDataAutomationLibraryResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_library

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_library.update_data_automation_library(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn
        if library_description is not None:
            input_["library_description"] = library_description
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.delete_data_automation_library_response.DeleteDataAutomationLibraryResponse":
        """Deletes an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.delete_data_automation_library_request.DeleteDataAutomationLibraryRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.delete_data_automation_library_response.DeleteDataAutomationLibraryResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_library

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_library.delete_data_automation_library(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.delete_data_automation_library_request.DeleteDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn

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
        project_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse":
        """Lists all existing Amazon Bedrock Data Automation Libraries"""

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.list_data_automation_libraries_request.ListDataAutomationLibrariesRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_libraries

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_libraries.list_data_automation_libraries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.list_data_automation_libraries_request.ListDataAutomationLibrariesRequest = {}  # type: ignore[typeddict-item]
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


class AsyncDataAutomationLibraryResource:
    def __init__(self, service: AsyncBedrockDataAutomationClient) -> None:
        self._service = service

    async def create(
        self,
        library_name: "aws_sdk_bedrock_data_automation.types.data_automation_library_name.DataAutomationLibraryName",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        library_description: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["aws_sdk_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.create_data_automation_library_response.CreateDataAutomationLibraryResponse":
        """Creates an Amazon Bedrock Data Automation Library"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.create_data_automation_library_response.CreateDataAutomationLibraryResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_library

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.create_data_automation_library.async_create_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.create_data_automation_library_request.CreateDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
        input_["library_name"] = library_name
        if library_description is not None:
            input_["library_description"] = library_description
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
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse":
        """Gets an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.get_data_automation_library_request.GetDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.get_data_automation_library_response.GetDataAutomationLibraryResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library.async_get_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.get_data_automation_library_request.GetDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        library_description: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.update_data_automation_library_response.UpdateDataAutomationLibraryResponse":
        """Updates an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.update_data_automation_library_response.UpdateDataAutomationLibraryResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_library

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.update_data_automation_library.async_update_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.update_data_automation_library_request.UpdateDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn
        if library_description is not None:
            input_["library_description"] = library_description
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.delete_data_automation_library_response.DeleteDataAutomationLibraryResponse":
        """Deletes an existing Amazon Bedrock Data Automation Library

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.delete_data_automation_library_request.DeleteDataAutomationLibraryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.delete_data_automation_library_response.DeleteDataAutomationLibraryResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_library

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.delete_data_automation_library.async_delete_data_automation_library(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.delete_data_automation_library_request.DeleteDataAutomationLibraryRequest = {}  # type: ignore[typeddict-item]
        input_["library_arn"] = library_arn

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
        project_filter: Optional[
            "aws_sdk_bedrock_data_automation.types.data_automation_project_filter.DataAutomationProjectFilter"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse":
        """Lists all existing Amazon Bedrock Data Automation Libraries"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.list_data_automation_libraries_request.ListDataAutomationLibrariesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.list_data_automation_libraries_response.ListDataAutomationLibrariesResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_libraries

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_libraries.async_list_data_automation_libraries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.list_data_automation_libraries_request.ListDataAutomationLibrariesRequest = {}  # type: ignore[typeddict-item]
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
