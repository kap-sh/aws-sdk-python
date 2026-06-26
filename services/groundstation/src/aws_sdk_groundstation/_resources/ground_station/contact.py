from __future__ import annotations

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
    import aws_sdk_groundstation.types.cancel_contact_request
    import aws_sdk_groundstation.types.client_token
    import aws_sdk_groundstation.types.contact_data
    import aws_sdk_groundstation.types.contact_id_response
    import aws_sdk_groundstation.types.contact_version
    import aws_sdk_groundstation.types.describe_contact_request
    import aws_sdk_groundstation.types.describe_contact_response
    import aws_sdk_groundstation.types.describe_contact_version_request
    import aws_sdk_groundstation.types.describe_contact_version_response
    import aws_sdk_groundstation.types.ephemeris_filter
    import aws_sdk_groundstation.types.ground_station_name
    import aws_sdk_groundstation.types.list_contact_versions_request
    import aws_sdk_groundstation.types.list_contact_versions_response
    import aws_sdk_groundstation.types.list_contacts_request
    import aws_sdk_groundstation.types.list_contacts_response
    import aws_sdk_groundstation.types.mission_profile_arn
    import aws_sdk_groundstation.types.pagination_max_results
    import aws_sdk_groundstation.types.pagination_token
    import aws_sdk_groundstation.types.reserve_contact_request
    import aws_sdk_groundstation.types.satellite_arn
    import aws_sdk_groundstation.types.status_list
    import aws_sdk_groundstation.types.tags_map
    import aws_sdk_groundstation.types.tracking_overrides
    import aws_sdk_groundstation.types.update_contact_request
    import aws_sdk_groundstation.types.update_contact_response
    import aws_sdk_groundstation.types.uuid
    import aws_sdk_groundstation.types.version_id
    from aws_sdk_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from aws_sdk_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class Contact:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def create(
        self,
        mission_profile_arn: "aws_sdk_groundstation.types.mission_profile_arn.MissionProfileArn",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        ground_station: "aws_sdk_groundstation.types.ground_station_name.GroundStationName",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        satellite_arn: Optional[
            "aws_sdk_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        tags: Optional["aws_sdk_groundstation.types.tags_map.TagsMap"] = None,
        tracking_overrides: Optional[
            "aws_sdk_groundstation.types.tracking_overrides.TrackingOverrides"
        ] = None,
    ) -> "aws_sdk_groundstation.types.contact_id_response.ContactIdResponse":
        """<p>Reserves a contact using specified parameters.</p>

        Args:
            mission_profile_arn: <p>ARN of a mission profile.</p>
            satellite_arn: <p>ARN of a satellite</p>
            start_time: <p>Start time of a contact in UTC.</p>
            end_time: <p>End time of a contact in UTC.</p>
            ground_station: <p>Name of a ground station.</p>
            tags: <p>Tags assigned to a contact.</p>
            tracking_overrides: <p>Tracking configuration overrides for the contact.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.reserve_contact_request.ReserveContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.contact_id_response.ContactIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.reserve_contact

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.reserve_contact.reserve_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.reserve_contact_request.ReserveContactRequest = {}  # type: ignore[typeddict-item]
        input_["mission_profile_arn"] = mission_profile_arn
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        input_["ground_station"] = ground_station
        if tags is not None:
            input_["tags"] = tags
        if tracking_overrides is not None:
            input_["tracking_overrides"] = tracking_overrides

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        contact_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> (
        "aws_sdk_groundstation.types.describe_contact_response.DescribeContactResponse"
    ):
        """<p>Describes an existing contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.describe_contact_request.DescribeContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.describe_contact_response.DescribeContactResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.describe_contact

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.describe_contact.describe_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.describe_contact_request.DescribeContactRequest = {}  # type: ignore[typeddict-item]
        input_["contact_id"] = contact_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        contact_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_groundstation.types.client_token.ClientToken"
        ] = None,
        tracking_overrides: Optional[
            "aws_sdk_groundstation.types.tracking_overrides.TrackingOverrides"
        ] = None,
        satellite_arn: Optional[
            "aws_sdk_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
    ) -> "aws_sdk_groundstation.types.update_contact_response.UpdateContactResponse":
        """<p>Updates a specific contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            client_token: <p>A client token is a unique, case-sensitive string of up to 64 ASCII characters. It is generated by the client to ensure idempotent operations, allowing safe retries without unintended side effects.</p>
            satellite_arn: <p>ARN of a satellite.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.update_contact_request.UpdateContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.update_contact_response.UpdateContactResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.update_contact

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.update_contact.update_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.update_contact_request.UpdateContactRequest = {}  # type: ignore[typeddict-item]
        input_["contact_id"] = contact_id
        if client_token is not None:
            input_["client_token"] = client_token
        if tracking_overrides is not None:
            input_["tracking_overrides"] = tracking_overrides
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        contact_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.contact_id_response.ContactIdResponse":
        r"""<p>Cancels or stops a contact with a specified contact ID based on its position in the <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/contacts.lifecycle.html\">contact lifecycle</a>.</p> <p>For contacts that:</p> <ul> <li> <p>Have yet to start, the contact will be cancelled.</p> </li> <li> <p>Have started but have yet to finish, the contact will be stopped.</p> </li> </ul>

        Args:
            contact_id: <p>UUID of a contact.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.cancel_contact_request.CancelContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.contact_id_response.ContactIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.cancel_contact

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.cancel_contact.cancel_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.cancel_contact_request.CancelContactRequest = {}  # type: ignore[typeddict-item]
        input_["contact_id"] = contact_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        status_list: "aws_sdk_groundstation.types.status_list.StatusList",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        max_results: Optional[
            "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_groundstation.types.pagination_token.PaginationToken"
        ] = None,
        ground_station: Optional[
            "aws_sdk_groundstation.types.ground_station_name.GroundStationName"
        ] = None,
        satellite_arn: Optional[
            "aws_sdk_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        mission_profile_arn: Optional[
            "aws_sdk_groundstation.types.mission_profile_arn.MissionProfileArn"
        ] = None,
        ephemeris: Optional[
            "aws_sdk_groundstation.types.ephemeris_filter.EphemerisFilter"
        ] = None,
    ) -> "aws_sdk_groundstation.types.list_contacts_response.ListContactsResponse":
        r"""<p>Returns a list of contacts.</p> <p>If <code>statusList</code> contains AVAILABLE, the request must include <code> groundStation</code>, <code>missionprofileArn</code>, and <code>satelliteArn</code>. </p>

        Args:
            max_results: <p>Maximum number of contacts returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListContacts</code> call. Used to get the next page of results.</p>
            status_list: <p>Status of a contact reservation.</p>
            start_time: <p>Start time of a contact in UTC.</p>
            end_time: <p>End time of a contact in UTC.</p>
            ground_station: <p>Name of a ground station.</p>
            satellite_arn: <p>ARN of a satellite.</p>
            mission_profile_arn: <p>ARN of a mission profile.</p>
            ephemeris: <p>Filter for selecting contacts that use a specific ephemeris\".</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.list_contacts_request.ListContactsRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.list_contacts_response.ListContactsResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_contacts

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.list_contacts.list_contacts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_contacts_request.ListContactsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["status_list"] = status_list
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        if ground_station is not None:
            input_["ground_station"] = ground_station
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn
        if mission_profile_arn is not None:
            input_["mission_profile_arn"] = mission_profile_arn
        if ephemeris is not None:
            input_["ephemeris"] = ephemeris

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_contact_version(
        self,
        contact_id: "aws_sdk_groundstation.types.uuid.Uuid",
        version_id: "aws_sdk_groundstation.types.version_id.VersionId",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse":
        """<p>Describes a specific version of a contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            version_id: <p>Version ID of a contact.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.describe_contact_version

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.describe_contact_version.describe_contact_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest = {}  # type: ignore[typeddict-item]
        input_["contact_id"] = contact_id
        input_["version_id"] = version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_contact_versions(
        self,
        contact_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        max_results: Optional[
            "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_groundstation.types.list_contact_versions_response.ListContactVersionsResponse":
        """<p>Returns a list of versions for a specified contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            max_results: <p>Maximum number of contact versions returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListContactVersions</code> call. Used to get the next page of results.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.list_contact_versions_request.ListContactVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.list_contact_versions_response.ListContactVersionsResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_contact_versions

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.list_contact_versions.list_contact_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_contact_versions_request.ListContactVersionsRequest = {}  # type: ignore[typeddict-item]
        input_["contact_id"] = contact_id
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


class AsyncContact:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def create(
        self,
        mission_profile_arn: "aws_sdk_groundstation.types.mission_profile_arn.MissionProfileArn",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        ground_station: "aws_sdk_groundstation.types.ground_station_name.GroundStationName",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_arn: Optional[
            "aws_sdk_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        tags: Optional["aws_sdk_groundstation.types.tags_map.TagsMap"] = None,
        tracking_overrides: Optional[
            "aws_sdk_groundstation.types.tracking_overrides.TrackingOverrides"
        ] = None,
    ) -> "aws_sdk_groundstation.types.contact_id_response.ContactIdResponse":
        """<p>Reserves a contact using specified parameters.</p>

        Args:
            mission_profile_arn: <p>ARN of a mission profile.</p>
            satellite_arn: <p>ARN of a satellite</p>
            start_time: <p>Start time of a contact in UTC.</p>
            end_time: <p>End time of a contact in UTC.</p>
            ground_station: <p>Name of a ground station.</p>
            tags: <p>Tags assigned to a contact.</p>
            tracking_overrides: <p>Tracking configuration overrides for the contact.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.reserve_contact_request.ReserveContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.contact_id_response.ContactIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.reserve_contact

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.reserve_contact.async_reserve_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.reserve_contact_request.ReserveContactRequest = {}  # type: ignore[typeddict-item]
        input_["mission_profile_arn"] = mission_profile_arn
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        input_["ground_station"] = ground_station
        if tags is not None:
            input_["tags"] = tags
        if tracking_overrides is not None:
            input_["tracking_overrides"] = tracking_overrides

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        contact_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> (
        "aws_sdk_groundstation.types.describe_contact_response.DescribeContactResponse"
    ):
        """<p>Describes an existing contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.describe_contact_request.DescribeContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.describe_contact_response.DescribeContactResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.describe_contact

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.describe_contact.async_describe_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.describe_contact_request.DescribeContactRequest = {}  # type: ignore[typeddict-item]
        input_["contact_id"] = contact_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        contact_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_groundstation.types.client_token.ClientToken"
        ] = None,
        tracking_overrides: Optional[
            "aws_sdk_groundstation.types.tracking_overrides.TrackingOverrides"
        ] = None,
        satellite_arn: Optional[
            "aws_sdk_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
    ) -> "aws_sdk_groundstation.types.update_contact_response.UpdateContactResponse":
        """<p>Updates a specific contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            client_token: <p>A client token is a unique, case-sensitive string of up to 64 ASCII characters. It is generated by the client to ensure idempotent operations, allowing safe retries without unintended side effects.</p>
            satellite_arn: <p>ARN of a satellite.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.update_contact_request.UpdateContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.update_contact_response.UpdateContactResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.update_contact

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.update_contact.async_update_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.update_contact_request.UpdateContactRequest = {}  # type: ignore[typeddict-item]
        input_["contact_id"] = contact_id
        if client_token is not None:
            input_["client_token"] = client_token
        if tracking_overrides is not None:
            input_["tracking_overrides"] = tracking_overrides
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        contact_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.contact_id_response.ContactIdResponse":
        r"""<p>Cancels or stops a contact with a specified contact ID based on its position in the <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/contacts.lifecycle.html\">contact lifecycle</a>.</p> <p>For contacts that:</p> <ul> <li> <p>Have yet to start, the contact will be cancelled.</p> </li> <li> <p>Have started but have yet to finish, the contact will be stopped.</p> </li> </ul>

        Args:
            contact_id: <p>UUID of a contact.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.cancel_contact_request.CancelContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.contact_id_response.ContactIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.cancel_contact

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.cancel_contact.async_cancel_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.cancel_contact_request.CancelContactRequest = {}  # type: ignore[typeddict-item]
        input_["contact_id"] = contact_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        status_list: "aws_sdk_groundstation.types.status_list.StatusList",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_groundstation.types.pagination_token.PaginationToken"
        ] = None,
        ground_station: Optional[
            "aws_sdk_groundstation.types.ground_station_name.GroundStationName"
        ] = None,
        satellite_arn: Optional[
            "aws_sdk_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        mission_profile_arn: Optional[
            "aws_sdk_groundstation.types.mission_profile_arn.MissionProfileArn"
        ] = None,
        ephemeris: Optional[
            "aws_sdk_groundstation.types.ephemeris_filter.EphemerisFilter"
        ] = None,
    ) -> "aws_sdk_groundstation.types.list_contacts_response.ListContactsResponse":
        r"""<p>Returns a list of contacts.</p> <p>If <code>statusList</code> contains AVAILABLE, the request must include <code> groundStation</code>, <code>missionprofileArn</code>, and <code>satelliteArn</code>. </p>

        Args:
            max_results: <p>Maximum number of contacts returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListContacts</code> call. Used to get the next page of results.</p>
            status_list: <p>Status of a contact reservation.</p>
            start_time: <p>Start time of a contact in UTC.</p>
            end_time: <p>End time of a contact in UTC.</p>
            ground_station: <p>Name of a ground station.</p>
            satellite_arn: <p>ARN of a satellite.</p>
            mission_profile_arn: <p>ARN of a mission profile.</p>
            ephemeris: <p>Filter for selecting contacts that use a specific ephemeris\".</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.list_contacts_request.ListContactsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.list_contacts_response.ListContactsResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_contacts

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.list_contacts.async_list_contacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_contacts_request.ListContactsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["status_list"] = status_list
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        if ground_station is not None:
            input_["ground_station"] = ground_station
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn
        if mission_profile_arn is not None:
            input_["mission_profile_arn"] = mission_profile_arn
        if ephemeris is not None:
            input_["ephemeris"] = ephemeris

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_contact_version(
        self,
        contact_id: "aws_sdk_groundstation.types.uuid.Uuid",
        version_id: "aws_sdk_groundstation.types.version_id.VersionId",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse":
        """<p>Describes a specific version of a contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            version_id: <p>Version ID of a contact.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.describe_contact_version

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.describe_contact_version.async_describe_contact_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest = {}  # type: ignore[typeddict-item]
        input_["contact_id"] = contact_id
        input_["version_id"] = version_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_contact_versions(
        self,
        contact_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_groundstation.types.list_contact_versions_response.ListContactVersionsResponse":
        """<p>Returns a list of versions for a specified contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            max_results: <p>Maximum number of contact versions returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListContactVersions</code> call. Used to get the next page of results.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.list_contact_versions_request.ListContactVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.list_contact_versions_response.ListContactVersionsResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_contact_versions

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.list_contact_versions.async_list_contact_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_contact_versions_request.ListContactVersionsRequest = {}  # type: ignore[typeddict-item]
        input_["contact_id"] = contact_id
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
