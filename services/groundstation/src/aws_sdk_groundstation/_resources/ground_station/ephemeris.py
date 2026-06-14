import datetime
from typing import TYPE_CHECKING, Optional

import aws_sdk_groundstation._auth._signers
import aws_sdk_groundstation._auth._sigv4
from aws_sdk_groundstation._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.create_ephemeris_request
    import aws_sdk_groundstation.types.customer_ephemeris_priority
    import aws_sdk_groundstation.types.delete_ephemeris_request
    import aws_sdk_groundstation.types.describe_ephemeris_request
    import aws_sdk_groundstation.types.describe_ephemeris_response
    import aws_sdk_groundstation.types.ephemeris_data
    import aws_sdk_groundstation.types.ephemeris_id_response
    import aws_sdk_groundstation.types.ephemeris_item
    import aws_sdk_groundstation.types.ephemeris_priority
    import aws_sdk_groundstation.types.ephemeris_status_list
    import aws_sdk_groundstation.types.ephemeris_type
    import aws_sdk_groundstation.types.key_arn
    import aws_sdk_groundstation.types.list_ephemerides_request
    import aws_sdk_groundstation.types.list_ephemerides_response
    import aws_sdk_groundstation.types.pagination_max_results
    import aws_sdk_groundstation.types.pagination_token
    import aws_sdk_groundstation.types.safe_name
    import aws_sdk_groundstation.types.tags_map
    import aws_sdk_groundstation.types.update_ephemeris_request
    import aws_sdk_groundstation.types.uuid
    from aws_sdk_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from aws_sdk_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class Ephemeris:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_groundstation.types.safe_name.SafeName",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        satellite_id: Optional["aws_sdk_groundstation.types.uuid.Uuid"] = None,
        enabled: Optional[bool] = None,
        priority: Optional[
            "aws_sdk_groundstation.types.customer_ephemeris_priority.CustomerEphemerisPriority"
        ] = None,
        expiration_time: Optional[datetime.datetime] = None,
        kms_key_arn: Optional["aws_sdk_groundstation.types.key_arn.KeyArn"] = None,
        ephemeris: Optional[
            "aws_sdk_groundstation.types.ephemeris_data.EphemerisData"
        ] = None,
        tags: Optional["aws_sdk_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse":
        """<p>Create an ephemeris with your specified <a>EphemerisData</a>.</p>

        Args:
            satellite_id: <p>The satellite ID that associates this ephemeris with a satellite in AWS Ground Station.</p>
            enabled: <p>Set to <code>true</code> to enable the ephemeris after validation. Set to <code>false</code> to keep it disabled.</p>
            priority: <p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>
            expiration_time: <p>An overall expiration time for the ephemeris in UTC, after which it will become <code>EXPIRED</code>.</p>
            name: <p>A name that you can use to identify the ephemeris.</p>
            kms_key_arn: <p>The ARN of the KMS key to use for encrypting the ephemeris.</p>
            ephemeris: <p>Ephemeris data.</p>
            tags: <p>Tags assigned to an ephemeris.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.create_ephemeris_request.CreateEphemerisRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.create_ephemeris

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.create_ephemeris.create_ephemeris(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.create_ephemeris_request.CreateEphemerisRequest = {}  # type: ignore[typeddict-item]
        if satellite_id is not None:
            input_["satellite_id"] = satellite_id
        if enabled is not None:
            input_["enabled"] = enabled
        if priority is not None:
            input_["priority"] = priority
        if expiration_time is not None:
            input_["expiration_time"] = expiration_time
        input_["name"] = name
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if ephemeris is not None:
            input_["ephemeris"] = ephemeris
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
        ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.describe_ephemeris_response.DescribeEphemerisResponse":
        """<p>Retrieve information about an existing ephemeris.</p>

        Args:
            ephemeris_id: <p>The AWS Ground Station ephemeris ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.describe_ephemeris_request.DescribeEphemerisRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.describe_ephemeris_response.DescribeEphemerisResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.describe_ephemeris

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.describe_ephemeris.describe_ephemeris(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.describe_ephemeris_request.DescribeEphemerisRequest = {}  # type: ignore[typeddict-item]
        input_["ephemeris_id"] = ephemeris_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid",
        enabled: bool,
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        name: Optional["aws_sdk_groundstation.types.safe_name.SafeName"] = None,
        priority: Optional[
            "aws_sdk_groundstation.types.ephemeris_priority.EphemerisPriority"
        ] = None,
    ) -> "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse":
        """<p>Update an existing ephemeris.</p>

        Args:
            ephemeris_id: <p>The AWS Ground Station ephemeris ID.</p>
            enabled: <p>Enable or disable the ephemeris. Changing this value doesn't require re-validation.</p>
            name: <p>A name that you can use to identify the ephemeris.</p>
            priority: <p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.update_ephemeris_request.UpdateEphemerisRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.update_ephemeris

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.update_ephemeris.update_ephemeris(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.update_ephemeris_request.UpdateEphemerisRequest = {}  # type: ignore[typeddict-item]
        input_["ephemeris_id"] = ephemeris_id
        input_["enabled"] = enabled
        if name is not None:
            input_["name"] = name
        if priority is not None:
            input_["priority"] = priority

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse":
        """<p>Delete an ephemeris.</p>

        Args:
            ephemeris_id: <p>The AWS Ground Station ephemeris ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.delete_ephemeris_request.DeleteEphemerisRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.delete_ephemeris

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.delete_ephemeris.delete_ephemeris(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.delete_ephemeris_request.DeleteEphemerisRequest = {}  # type: ignore[typeddict-item]
        input_["ephemeris_id"] = ephemeris_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        satellite_id: Optional["aws_sdk_groundstation.types.uuid.Uuid"] = None,
        ephemeris_type: Optional[
            "aws_sdk_groundstation.types.ephemeris_type.EphemerisType"
        ] = None,
        status_list: Optional[
            "aws_sdk_groundstation.types.ephemeris_status_list.EphemerisStatusList"
        ] = None,
        max_results: Optional[
            "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "aws_sdk_groundstation.types.list_ephemerides_response.ListEphemeridesResponse"
    ):
        """<p>List your existing ephemerides.</p>

        Args:
            satellite_id: <p>The AWS Ground Station satellite ID to list ephemeris for.</p>
            ephemeris_type: <p>Filter ephemerides by type. If not specified, all ephemeris types will be returned.</p>
            start_time: <p>The start time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.</p>
            end_time: <p>The end time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.</p>
            status_list: <p>The list of ephemeris status to return.</p>
            max_results: <p>Maximum number of ephemerides to return.</p>
            next_token: <p>Pagination token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.list_ephemerides_request.ListEphemeridesRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.list_ephemerides_response.ListEphemeridesResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_ephemerides

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.list_ephemerides.list_ephemerides(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_ephemerides_request.ListEphemeridesRequest = {}  # type: ignore[typeddict-item]
        if satellite_id is not None:
            input_["satellite_id"] = satellite_id
        if ephemeris_type is not None:
            input_["ephemeris_type"] = ephemeris_type
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        if status_list is not None:
            input_["status_list"] = status_list
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


class AsyncEphemeris:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_groundstation.types.safe_name.SafeName",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_id: Optional["aws_sdk_groundstation.types.uuid.Uuid"] = None,
        enabled: Optional[bool] = None,
        priority: Optional[
            "aws_sdk_groundstation.types.customer_ephemeris_priority.CustomerEphemerisPriority"
        ] = None,
        expiration_time: Optional[datetime.datetime] = None,
        kms_key_arn: Optional["aws_sdk_groundstation.types.key_arn.KeyArn"] = None,
        ephemeris: Optional[
            "aws_sdk_groundstation.types.ephemeris_data.EphemerisData"
        ] = None,
        tags: Optional["aws_sdk_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse":
        """<p>Create an ephemeris with your specified <a>EphemerisData</a>.</p>

        Args:
            satellite_id: <p>The satellite ID that associates this ephemeris with a satellite in AWS Ground Station.</p>
            enabled: <p>Set to <code>true</code> to enable the ephemeris after validation. Set to <code>false</code> to keep it disabled.</p>
            priority: <p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>
            expiration_time: <p>An overall expiration time for the ephemeris in UTC, after which it will become <code>EXPIRED</code>.</p>
            name: <p>A name that you can use to identify the ephemeris.</p>
            kms_key_arn: <p>The ARN of the KMS key to use for encrypting the ephemeris.</p>
            ephemeris: <p>Ephemeris data.</p>
            tags: <p>Tags assigned to an ephemeris.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.create_ephemeris_request.CreateEphemerisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.create_ephemeris

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.create_ephemeris.async_create_ephemeris(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.create_ephemeris_request.CreateEphemerisRequest = {}  # type: ignore[typeddict-item]
        if satellite_id is not None:
            input_["satellite_id"] = satellite_id
        if enabled is not None:
            input_["enabled"] = enabled
        if priority is not None:
            input_["priority"] = priority
        if expiration_time is not None:
            input_["expiration_time"] = expiration_time
        input_["name"] = name
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if ephemeris is not None:
            input_["ephemeris"] = ephemeris
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
        ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.describe_ephemeris_response.DescribeEphemerisResponse":
        """<p>Retrieve information about an existing ephemeris.</p>

        Args:
            ephemeris_id: <p>The AWS Ground Station ephemeris ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.describe_ephemeris_request.DescribeEphemerisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.describe_ephemeris_response.DescribeEphemerisResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.describe_ephemeris

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.describe_ephemeris.async_describe_ephemeris(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.describe_ephemeris_request.DescribeEphemerisRequest = {}  # type: ignore[typeddict-item]
        input_["ephemeris_id"] = ephemeris_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid",
        enabled: bool,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        name: Optional["aws_sdk_groundstation.types.safe_name.SafeName"] = None,
        priority: Optional[
            "aws_sdk_groundstation.types.ephemeris_priority.EphemerisPriority"
        ] = None,
    ) -> "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse":
        """<p>Update an existing ephemeris.</p>

        Args:
            ephemeris_id: <p>The AWS Ground Station ephemeris ID.</p>
            enabled: <p>Enable or disable the ephemeris. Changing this value doesn't require re-validation.</p>
            name: <p>A name that you can use to identify the ephemeris.</p>
            priority: <p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.update_ephemeris_request.UpdateEphemerisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.update_ephemeris

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.update_ephemeris.async_update_ephemeris(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.update_ephemeris_request.UpdateEphemerisRequest = {}  # type: ignore[typeddict-item]
        input_["ephemeris_id"] = ephemeris_id
        input_["enabled"] = enabled
        if name is not None:
            input_["name"] = name
        if priority is not None:
            input_["priority"] = priority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse":
        """<p>Delete an ephemeris.</p>

        Args:
            ephemeris_id: <p>The AWS Ground Station ephemeris ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.delete_ephemeris_request.DeleteEphemerisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.ephemeris_id_response.EphemerisIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.delete_ephemeris

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.delete_ephemeris.async_delete_ephemeris(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.delete_ephemeris_request.DeleteEphemerisRequest = {}  # type: ignore[typeddict-item]
        input_["ephemeris_id"] = ephemeris_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_id: Optional["aws_sdk_groundstation.types.uuid.Uuid"] = None,
        ephemeris_type: Optional[
            "aws_sdk_groundstation.types.ephemeris_type.EphemerisType"
        ] = None,
        status_list: Optional[
            "aws_sdk_groundstation.types.ephemeris_status_list.EphemerisStatusList"
        ] = None,
        max_results: Optional[
            "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "aws_sdk_groundstation.types.list_ephemerides_response.ListEphemeridesResponse"
    ):
        """<p>List your existing ephemerides.</p>

        Args:
            satellite_id: <p>The AWS Ground Station satellite ID to list ephemeris for.</p>
            ephemeris_type: <p>Filter ephemerides by type. If not specified, all ephemeris types will be returned.</p>
            start_time: <p>The start time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.</p>
            end_time: <p>The end time for the list operation in UTC. Returns ephemerides with expiration times within your specified time range.</p>
            status_list: <p>The list of ephemeris status to return.</p>
            max_results: <p>Maximum number of ephemerides to return.</p>
            next_token: <p>Pagination token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.list_ephemerides_request.ListEphemeridesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.list_ephemerides_response.ListEphemeridesResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_ephemerides

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.list_ephemerides.async_list_ephemerides(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_ephemerides_request.ListEphemeridesRequest = {}  # type: ignore[typeddict-item]
        if satellite_id is not None:
            input_["satellite_id"] = satellite_id
        if ephemeris_type is not None:
            input_["ephemeris_type"] = ephemeris_type
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        if status_list is not None:
            input_["status_list"] = status_list
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
