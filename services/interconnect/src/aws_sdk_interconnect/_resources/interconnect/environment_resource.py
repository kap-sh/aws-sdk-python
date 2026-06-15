from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from aws_sdk_interconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.environment
    import aws_sdk_interconnect.types.environment_id
    import aws_sdk_interconnect.types.get_environment_request
    import aws_sdk_interconnect.types.get_environment_response
    import aws_sdk_interconnect.types.list_environments_request
    import aws_sdk_interconnect.types.list_environments_response
    import aws_sdk_interconnect.types.location
    import aws_sdk_interconnect.types.max_results
    import aws_sdk_interconnect.types.next_token
    import aws_sdk_interconnect.types.provider
    from aws_sdk_interconnect._services.async_interconnect import (
        AsyncInterconnectClient,
        AsyncInterconnectClientConfig,
    )
    from aws_sdk_interconnect._services.interconnect import (
        InterconnectClient,
        InterconnectClientConfig,
    )


class EnvironmentResource:
    def __init__(self, service: InterconnectClient) -> None:
        self._service = service

    def read(
        self,
        id: "aws_sdk_interconnect.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
    ) -> "aws_sdk_interconnect.types.get_environment_response.GetEnvironmentResponse":
        """<p>Describes a specific <a>Environment</a> </p>

        Args:
            id: <p>The identifier of the specific <a>Environment</a> to describe.</p>

        Examples:
            Get a specific environment

            >>> client.read(id='mce-aws-acme-1')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_interconnect.types.get_environment_request.GetEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_interconnect.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import aws_sdk_interconnect._operations.interconnect.get_environment

            output, http_response = (
                aws_sdk_interconnect._operations.interconnect.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_interconnect.types.get_environment_request.GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_interconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_interconnect.types.next_token.NextToken"] = None,
        provider: Optional["aws_sdk_interconnect.types.provider.Provider"] = None,
        location: Optional["aws_sdk_interconnect.types.location.Location"] = None,
    ) -> (
        "aws_sdk_interconnect.types.list_environments_response.ListEnvironmentsResponse"
    ):
        """<p>Lists all of the environments that can produce connections that will land in the called AWS region.</p>

        Args:
            max_results: <p>The max number of list results in a single paginated response.</p>
            next_token: <p>A pagination token from a previous paginated response indicating you wish to get the next page of results.</p>
            provider: <p>Filter results to only include <a>Environment</a> objects that connect to the <a>Provider</a>.</p>
            location: <p>Filter results to only include <a>Environment</a> objects that connect to a given location distiguisher.</p>

        Examples:
            List All Environments

            >>> client.list()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_interconnect.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_interconnect.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import aws_sdk_interconnect._operations.interconnect.list_environments

            output, http_response = (
                aws_sdk_interconnect._operations.interconnect.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_interconnect.types.list_environments_request.ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if provider is not None:
            input_["provider"] = provider
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEnvironmentResource:
    def __init__(self, service: AsyncInterconnectClient) -> None:
        self._service = service

    async def read(
        self,
        id: "aws_sdk_interconnect.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
    ) -> "aws_sdk_interconnect.types.get_environment_response.GetEnvironmentResponse":
        """<p>Describes a specific <a>Environment</a> </p>

        Args:
            id: <p>The identifier of the specific <a>Environment</a> to describe.</p>

        Examples:
            Get a specific environment

            >>> await client.read(id='mce-aws-acme-1')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_interconnect.types.get_environment_request.GetEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_interconnect.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import aws_sdk_interconnect._operations.interconnect.get_environment

            (
                output,
                http_response,
            ) = await aws_sdk_interconnect._operations.interconnect.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_interconnect.types.get_environment_request.GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_interconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_interconnect.types.next_token.NextToken"] = None,
        provider: Optional["aws_sdk_interconnect.types.provider.Provider"] = None,
        location: Optional["aws_sdk_interconnect.types.location.Location"] = None,
    ) -> (
        "aws_sdk_interconnect.types.list_environments_response.ListEnvironmentsResponse"
    ):
        """<p>Lists all of the environments that can produce connections that will land in the called AWS region.</p>

        Args:
            max_results: <p>The max number of list results in a single paginated response.</p>
            next_token: <p>A pagination token from a previous paginated response indicating you wish to get the next page of results.</p>
            provider: <p>Filter results to only include <a>Environment</a> objects that connect to the <a>Provider</a>.</p>
            location: <p>Filter results to only include <a>Environment</a> objects that connect to a given location distiguisher.</p>

        Examples:
            List All Environments

            >>> await client.list()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_interconnect.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_interconnect.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import aws_sdk_interconnect._operations.interconnect.list_environments

            (
                output,
                http_response,
            ) = await aws_sdk_interconnect._operations.interconnect.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_interconnect.types.list_environments_request.ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if provider is not None:
            input_["provider"] = provider
        if location is not None:
            input_["location"] = location

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
