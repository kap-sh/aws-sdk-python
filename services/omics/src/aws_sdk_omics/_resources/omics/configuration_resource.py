from typing import TYPE_CHECKING, Optional

import aws_sdk_omics._auth._signers
import aws_sdk_omics._auth._sigv4
from aws_sdk_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_omics.types.configuration_description
    import aws_sdk_omics.types.configuration_list_item
    import aws_sdk_omics.types.configuration_list_token
    import aws_sdk_omics.types.configuration_name
    import aws_sdk_omics.types.configuration_request_id
    import aws_sdk_omics.types.create_configuration_request
    import aws_sdk_omics.types.create_configuration_response
    import aws_sdk_omics.types.delete_configuration_request
    import aws_sdk_omics.types.get_configuration_request
    import aws_sdk_omics.types.get_configuration_response
    import aws_sdk_omics.types.list_configurations_request
    import aws_sdk_omics.types.list_configurations_response
    import aws_sdk_omics.types.run_configurations
    import aws_sdk_omics.types.tag_map
    from aws_sdk_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from aws_sdk_omics._services.omics import OmicsClient, OmicsClientConfig


class ConfigurationResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def put(
        self,
        name: "aws_sdk_omics.types.configuration_name.ConfigurationName",
        run_configurations: "aws_sdk_omics.types.run_configurations.RunConfigurations",
        request_id: "aws_sdk_omics.types.configuration_request_id.ConfigurationRequestId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional[
            "aws_sdk_omics.types.configuration_description.ConfigurationDescription"
        ] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
    ) -> (
        "aws_sdk_omics.types.create_configuration_response.CreateConfigurationResponse"
    ):
        """<p>Create a new configuration.</p>

        Args:
            name: <p>User-friendly name for the configuration.</p>
            description: <p>Optional description for the configuration.</p>
            run_configurations: <p>Required run-specific configurations.</p>
            tags: <p>Optional tags for the configuration.</p>
            request_id: <p>Optional request idempotency token. If not specified, a universally unique identifier (UUID) will be automatically generated for the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.create_configuration_request.CreateConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.create_configuration_response.CreateConfigurationResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_configuration

            output, http_response = (
                aws_sdk_omics._operations.omics.create_configuration.create_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.create_configuration_request.CreateConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["run_configurations"] = run_configurations
        if tags is not None:
            input["tags"] = tags
        input["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        name: "aws_sdk_omics.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_configuration_response.GetConfigurationResponse":
        """<p>Retrieve configuration details for specified name.</p>

        Args:
            name: <p>Configuration name to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.get_configuration_request.GetConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.get_configuration_response.GetConfigurationResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_configuration

            output, http_response = (
                aws_sdk_omics._operations.omics.get_configuration.get_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.get_configuration_request.GetConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        name: "aws_sdk_omics.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> None:
        """<p>Delete an existing configuration.</p>

        Args:
            name: <p>Configuration name to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.delete_configuration_request.DeleteConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_omics._operations.omics.delete_configuration

            output, http_response = (
                aws_sdk_omics._operations.omics.delete_configuration.delete_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.delete_configuration_request.DeleteConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        starting_token: Optional[
            "aws_sdk_omics.types.configuration_list_token.ConfigurationListToken"
        ] = None,
    ) -> "aws_sdk_omics.types.list_configurations_response.ListConfigurationsResponse":
        """<p>List all configurations for the account.</p>

        Args:
            max_results: <p>Maximum number of results to return.</p>
            starting_token: <p>Pagination token for retrieving next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.list_configurations_request.ListConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.list_configurations_response.ListConfigurationsResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_configurations

            output, http_response = (
                aws_sdk_omics._operations.omics.list_configurations.list_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.list_configurations_request.ListConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if starting_token is not None:
            input["starting_token"] = starting_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncConfigurationResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def put(
        self,
        name: "aws_sdk_omics.types.configuration_name.ConfigurationName",
        run_configurations: "aws_sdk_omics.types.run_configurations.RunConfigurations",
        request_id: "aws_sdk_omics.types.configuration_request_id.ConfigurationRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional[
            "aws_sdk_omics.types.configuration_description.ConfigurationDescription"
        ] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
    ) -> (
        "aws_sdk_omics.types.create_configuration_response.CreateConfigurationResponse"
    ):
        """<p>Create a new configuration.</p>

        Args:
            name: <p>User-friendly name for the configuration.</p>
            description: <p>Optional description for the configuration.</p>
            run_configurations: <p>Required run-specific configurations.</p>
            tags: <p>Optional tags for the configuration.</p>
            request_id: <p>Optional request idempotency token. If not specified, a universally unique identifier (UUID) will be automatically generated for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.create_configuration_request.CreateConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.create_configuration_response.CreateConfigurationResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.create_configuration.async_create_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.create_configuration_request.CreateConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["run_configurations"] = run_configurations
        if tags is not None:
            input["tags"] = tags
        input["request_id"] = request_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        name: "aws_sdk_omics.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_configuration_response.GetConfigurationResponse":
        """<p>Retrieve configuration details for specified name.</p>

        Args:
            name: <p>Configuration name to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.get_configuration_request.GetConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.get_configuration_response.GetConfigurationResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.get_configuration.async_get_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.get_configuration_request.GetConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        name: "aws_sdk_omics.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Delete an existing configuration.</p>

        Args:
            name: <p>Configuration name to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.delete_configuration_request.DeleteConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_omics._operations.omics.delete_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.delete_configuration.async_delete_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.delete_configuration_request.DeleteConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        starting_token: Optional[
            "aws_sdk_omics.types.configuration_list_token.ConfigurationListToken"
        ] = None,
    ) -> "aws_sdk_omics.types.list_configurations_response.ListConfigurationsResponse":
        """<p>List all configurations for the account.</p>

        Args:
            max_results: <p>Maximum number of results to return.</p>
            starting_token: <p>Pagination token for retrieving next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.list_configurations_request.ListConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.list_configurations_response.ListConfigurationsResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.list_configurations.async_list_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_omics.types.list_configurations_request.ListConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if starting_token is not None:
            input["starting_token"] = starting_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
