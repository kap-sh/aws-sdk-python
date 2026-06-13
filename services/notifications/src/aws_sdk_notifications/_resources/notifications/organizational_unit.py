from typing import TYPE_CHECKING, Optional

import aws_sdk_notifications._auth._signers
import aws_sdk_notifications._auth._sigv4
from aws_sdk_notifications._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_notifications.types.associate_organizational_unit_request
    import aws_sdk_notifications.types.associate_organizational_unit_response
    import aws_sdk_notifications.types.disassociate_organizational_unit_request
    import aws_sdk_notifications.types.disassociate_organizational_unit_response
    import aws_sdk_notifications.types.list_organizational_units_request
    import aws_sdk_notifications.types.list_organizational_units_response
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.organizational_unit_id
    from aws_sdk_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from aws_sdk_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class OrganizationalUnit:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def put(
        self,
        organizational_unit_id: "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId",
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.associate_organizational_unit_response.AssociateOrganizationalUnitResponse":
        """<p>Associates an organizational unit with a notification configuration.</p>

        Args:
            organizational_unit_id: <p>The unique identifier of the organizational unit to associate.</p>
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration to associate with the organizational unit.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.associate_organizational_unit_request.AssociateOrganizationalUnitRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.associate_organizational_unit_response.AssociateOrganizationalUnitResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.associate_organizational_unit

            output, http_response = (
                aws_sdk_notifications._operations.notifications.associate_organizational_unit.associate_organizational_unit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.associate_organizational_unit_request.AssociateOrganizationalUnitRequest = {}  # type: ignore[typeddict-item]
        input["organizational_unit_id"] = organizational_unit_id
        input["notification_configuration_arn"] = notification_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        organizational_unit_id: "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId",
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.disassociate_organizational_unit_response.DisassociateOrganizationalUnitResponse":
        """<p>Removes the association between an organizational unit and a notification configuration.</p>

        Args:
            organizational_unit_id: <p>The unique identifier of the organizational unit to disassociate.</p>
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration to disassociate from the organizational unit.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.disassociate_organizational_unit_request.DisassociateOrganizationalUnitRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.disassociate_organizational_unit_response.DisassociateOrganizationalUnitResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.disassociate_organizational_unit

            output, http_response = (
                aws_sdk_notifications._operations.notifications.disassociate_organizational_unit.disassociate_organizational_unit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.disassociate_organizational_unit_request.DisassociateOrganizationalUnitRequest = {}  # type: ignore[typeddict-item]
        input["organizational_unit_id"] = organizational_unit_id
        input["notification_configuration_arn"] = notification_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_organizational_units_response.ListOrganizationalUnitsResponse":
        """<p>Returns a list of organizational units associated with a notification configuration.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration used to filter the organizational units.</p>
            max_results: <p>The maximum number of organizational units to return in a single call. Valid values are 1-100.</p>
            next_token: <p>The token for the next page of results. Use the value returned in the previous response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.list_organizational_units_request.ListOrganizationalUnitsRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.list_organizational_units_response.ListOrganizationalUnitsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_organizational_units

            output, http_response = (
                aws_sdk_notifications._operations.notifications.list_organizational_units.list_organizational_units(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.list_organizational_units_request.ListOrganizationalUnitsRequest = {}  # type: ignore[typeddict-item]
        input["notification_configuration_arn"] = notification_configuration_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncOrganizationalUnit:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def put(
        self,
        organizational_unit_id: "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId",
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.associate_organizational_unit_response.AssociateOrganizationalUnitResponse":
        """<p>Associates an organizational unit with a notification configuration.</p>

        Args:
            organizational_unit_id: <p>The unique identifier of the organizational unit to associate.</p>
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration to associate with the organizational unit.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.associate_organizational_unit_request.AssociateOrganizationalUnitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.associate_organizational_unit_response.AssociateOrganizationalUnitResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.associate_organizational_unit

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.associate_organizational_unit.async_associate_organizational_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.associate_organizational_unit_request.AssociateOrganizationalUnitRequest = {}  # type: ignore[typeddict-item]
        input["organizational_unit_id"] = organizational_unit_id
        input["notification_configuration_arn"] = notification_configuration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        organizational_unit_id: "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId",
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.disassociate_organizational_unit_response.DisassociateOrganizationalUnitResponse":
        """<p>Removes the association between an organizational unit and a notification configuration.</p>

        Args:
            organizational_unit_id: <p>The unique identifier of the organizational unit to disassociate.</p>
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration to disassociate from the organizational unit.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.disassociate_organizational_unit_request.DisassociateOrganizationalUnitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.disassociate_organizational_unit_response.DisassociateOrganizationalUnitResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.disassociate_organizational_unit

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.disassociate_organizational_unit.async_disassociate_organizational_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.disassociate_organizational_unit_request.DisassociateOrganizationalUnitRequest = {}  # type: ignore[typeddict-item]
        input["organizational_unit_id"] = organizational_unit_id
        input["notification_configuration_arn"] = notification_configuration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_organizational_units_response.ListOrganizationalUnitsResponse":
        """<p>Returns a list of organizational units associated with a notification configuration.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration used to filter the organizational units.</p>
            max_results: <p>The maximum number of organizational units to return in a single call. Valid values are 1-100.</p>
            next_token: <p>The token for the next page of results. Use the value returned in the previous response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.list_organizational_units_request.ListOrganizationalUnitsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.list_organizational_units_response.ListOrganizationalUnitsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_organizational_units

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.list_organizational_units.async_list_organizational_units(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.list_organizational_units_request.ListOrganizationalUnitsRequest = {}  # type: ignore[typeddict-item]
        input["notification_configuration_arn"] = notification_configuration_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
