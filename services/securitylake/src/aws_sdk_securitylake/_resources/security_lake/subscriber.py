from typing import TYPE_CHECKING, Optional

import aws_sdk_securitylake._auth._signers
import aws_sdk_securitylake._auth._sigv4
from aws_sdk_securitylake._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.access_type_list
    import aws_sdk_securitylake.types.aws_identity
    import aws_sdk_securitylake.types.create_subscriber_notification_request
    import aws_sdk_securitylake.types.create_subscriber_notification_response
    import aws_sdk_securitylake.types.create_subscriber_request
    import aws_sdk_securitylake.types.create_subscriber_response
    import aws_sdk_securitylake.types.delete_subscriber_notification_request
    import aws_sdk_securitylake.types.delete_subscriber_notification_response
    import aws_sdk_securitylake.types.delete_subscriber_request
    import aws_sdk_securitylake.types.delete_subscriber_response
    import aws_sdk_securitylake.types.description_string
    import aws_sdk_securitylake.types.get_subscriber_request
    import aws_sdk_securitylake.types.get_subscriber_response
    import aws_sdk_securitylake.types.list_subscribers_request
    import aws_sdk_securitylake.types.list_subscribers_response
    import aws_sdk_securitylake.types.log_source_resource_list
    import aws_sdk_securitylake.types.max_results
    import aws_sdk_securitylake.types.next_token
    import aws_sdk_securitylake.types.notification_configuration
    import aws_sdk_securitylake.types.safe_string
    import aws_sdk_securitylake.types.subscriber_resource
    import aws_sdk_securitylake.types.tag_list
    import aws_sdk_securitylake.types.update_subscriber_notification_request
    import aws_sdk_securitylake.types.update_subscriber_notification_response
    import aws_sdk_securitylake.types.update_subscriber_request
    import aws_sdk_securitylake.types.update_subscriber_response
    import aws_sdk_securitylake.types.uuid
    from aws_sdk_securitylake._services.async_security_lake import (
        AsyncSecurityLakeClient,
        AsyncSecurityLakeClientConfig,
    )
    from aws_sdk_securitylake._services.security_lake import (
        SecurityLakeClient,
        SecurityLakeClientConfig,
    )


class Subscriber:
    def __init__(self, service: SecurityLakeClient) -> None:
        self._service = service

    def create(
        self,
        subscriber_identity: "aws_sdk_securitylake.types.aws_identity.AwsIdentity",
        subscriber_name: str,
        sources: "aws_sdk_securitylake.types.log_source_resource_list.LogSourceResourceList",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        subscriber_description: Optional[
            "aws_sdk_securitylake.types.description_string.DescriptionString"
        ] = None,
        access_types: Optional[
            "aws_sdk_securitylake.types.access_type_list.AccessTypeList"
        ] = None,
        tags: Optional["aws_sdk_securitylake.types.tag_list.TagList"] = None,
    ) -> (
        "aws_sdk_securitylake.types.create_subscriber_response.CreateSubscriberResponse"
    ):
        """<p>Creates a subscriber for accounts that are already enabled in Amazon Security Lake. You can create a subscriber with access to data in the current Amazon Web Services Region.</p>

        Args:
            subscriber_identity: <p>The Amazon Web Services identity used to access your data.</p>
            subscriber_name: <p>The name of your Security Lake subscriber account.</p>
            subscriber_description: <p>The description for your subscriber account in Security Lake.</p>
            sources: <p>The supported Amazon Web Services services from which logs and events are collected. Security Lake supports log and event collection for natively supported Amazon Web Services services.</p>
            access_types: <p>The Amazon S3 or Lake Formation access type.</p>
            tags: <p>An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securitylake.types.create_subscriber_request.CreateSubscriberRequest]",
        ) -> OperationResponse[
            "aws_sdk_securitylake.types.create_subscriber_response.CreateSubscriberResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.create_subscriber

            output, http_response = (
                aws_sdk_securitylake._operations.security_lake.create_subscriber.create_subscriber(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.create_subscriber_request.CreateSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_identity"] = subscriber_identity
        input_["subscriber_name"] = subscriber_name
        if subscriber_description is not None:
            input_["subscriber_description"] = subscriber_description
        input_["sources"] = sources
        if access_types is not None:
            input_["access_types"] = access_types
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
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.get_subscriber_response.GetSubscriberResponse":
        """<p>Retrieves the subscription information for the specified subscription ID. You can get information about a specific subscriber.</p>

        Args:
            subscriber_id: <p>A value created by Amazon Security Lake that uniquely identifies your <code>GetSubscriber</code> API request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securitylake.types.get_subscriber_request.GetSubscriberRequest]",
        ) -> OperationResponse[
            "aws_sdk_securitylake.types.get_subscriber_response.GetSubscriberResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.get_subscriber

            output, http_response = (
                aws_sdk_securitylake._operations.security_lake.get_subscriber.get_subscriber(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.get_subscriber_request.GetSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        subscriber_identity: Optional[
            "aws_sdk_securitylake.types.aws_identity.AwsIdentity"
        ] = None,
        subscriber_name: Optional[
            "aws_sdk_securitylake.types.safe_string.SafeString"
        ] = None,
        subscriber_description: Optional[
            "aws_sdk_securitylake.types.description_string.DescriptionString"
        ] = None,
        sources: Optional[
            "aws_sdk_securitylake.types.log_source_resource_list.LogSourceResourceList"
        ] = None,
    ) -> (
        "aws_sdk_securitylake.types.update_subscriber_response.UpdateSubscriberResponse"
    ):
        """<p>Updates an existing subscription for the given Amazon Security Lake account ID. You can update a subscriber by changing the sources that the subscriber consumes data from.</p>

        Args:
            subscriber_id: <p>A value created by Security Lake that uniquely identifies your subscription.</p>
            subscriber_identity: <p>The Amazon Web Services identity used to access your data.</p>
            subscriber_name: <p>The name of the Security Lake account subscriber.</p>
            subscriber_description: <p>The description of the Security Lake account subscriber.</p>
            sources: <p>The supported Amazon Web Services services from which logs and events are collected. For the list of supported Amazon Web Services services, see the <a href=\"https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html\">Amazon Security Lake User Guide</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securitylake.types.update_subscriber_request.UpdateSubscriberRequest]",
        ) -> OperationResponse[
            "aws_sdk_securitylake.types.update_subscriber_response.UpdateSubscriberResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.update_subscriber

            output, http_response = (
                aws_sdk_securitylake._operations.security_lake.update_subscriber.update_subscriber(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.update_subscriber_request.UpdateSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id
        if subscriber_identity is not None:
            input_["subscriber_identity"] = subscriber_identity
        if subscriber_name is not None:
            input_["subscriber_name"] = subscriber_name
        if subscriber_description is not None:
            input_["subscriber_description"] = subscriber_description
        if sources is not None:
            input_["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> (
        "aws_sdk_securitylake.types.delete_subscriber_response.DeleteSubscriberResponse"
    ):
        """<p>Deletes the subscription permission and all notification settings for accounts that are already enabled in Amazon Security Lake. When you run <code>DeleteSubscriber</code>, the subscriber will no longer consume data from Security Lake and the subscriber is removed. This operation deletes the subscriber and removes access to data in the current Amazon Web Services Region.</p>

        Args:
            subscriber_id: <p>A value created by Security Lake that uniquely identifies your <code>DeleteSubscriber</code> API request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securitylake.types.delete_subscriber_request.DeleteSubscriberRequest]",
        ) -> OperationResponse[
            "aws_sdk_securitylake.types.delete_subscriber_response.DeleteSubscriberResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.delete_subscriber

            output, http_response = (
                aws_sdk_securitylake._operations.security_lake.delete_subscriber.delete_subscriber(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.delete_subscriber_request.DeleteSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        next_token: Optional["aws_sdk_securitylake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securitylake.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securitylake.types.list_subscribers_response.ListSubscribersResponse":
        """<p>Lists all subscribers for the specific Amazon Security Lake account ID. You can retrieve a list of subscriptions associated with a specific organization or Amazon Web Services account.</p>

        Args:
            next_token: <p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>
            max_results: <p>The maximum number of accounts for which the configuration is displayed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securitylake.types.list_subscribers_request.ListSubscribersRequest]",
        ) -> OperationResponse[
            "aws_sdk_securitylake.types.list_subscribers_response.ListSubscribersResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.list_subscribers

            output, http_response = (
                aws_sdk_securitylake._operations.security_lake.list_subscribers.list_subscribers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.list_subscribers_request.ListSubscribersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_subscriber_notification(
        self,
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        configuration: "aws_sdk_securitylake.types.notification_configuration.NotificationConfiguration",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.create_subscriber_notification_response.CreateSubscriberNotificationResponse":
        """<p>Notifies the subscriber when new data is written to the data lake for the sources that the subscriber consumes in Security Lake. You can create only one subscriber notification per subscriber.</p>

        Args:
            subscriber_id: <p>The subscriber ID for the notification subscription.</p>
            configuration: <p>Specify the configuration using which you want to create the subscriber notification.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securitylake.types.create_subscriber_notification_request.CreateSubscriberNotificationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securitylake.types.create_subscriber_notification_response.CreateSubscriberNotificationResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.create_subscriber_notification

            output, http_response = (
                aws_sdk_securitylake._operations.security_lake.create_subscriber_notification.create_subscriber_notification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.create_subscriber_notification_request.CreateSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id
        input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_subscriber_notification(
        self,
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.delete_subscriber_notification_response.DeleteSubscriberNotificationResponse":
        """<p>Deletes the specified subscription notification in Amazon Security Lake for the organization you specify.</p>

        Args:
            subscriber_id: <p>The ID of the Security Lake subscriber account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securitylake.types.delete_subscriber_notification_request.DeleteSubscriberNotificationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securitylake.types.delete_subscriber_notification_response.DeleteSubscriberNotificationResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.delete_subscriber_notification

            output, http_response = (
                aws_sdk_securitylake._operations.security_lake.delete_subscriber_notification.delete_subscriber_notification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.delete_subscriber_notification_request.DeleteSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_subscriber_notification(
        self,
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        configuration: "aws_sdk_securitylake.types.notification_configuration.NotificationConfiguration",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.update_subscriber_notification_response.UpdateSubscriberNotificationResponse":
        """<p>Updates an existing notification method for the subscription (SQS or HTTPs endpoint) or switches the notification subscription endpoint for a subscriber.</p>

        Args:
            subscriber_id: <p>The subscription ID for which the subscription notification is specified.</p>
            configuration: <p>The configuration for subscriber notification.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securitylake.types.update_subscriber_notification_request.UpdateSubscriberNotificationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securitylake.types.update_subscriber_notification_response.UpdateSubscriberNotificationResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.update_subscriber_notification

            output, http_response = (
                aws_sdk_securitylake._operations.security_lake.update_subscriber_notification.update_subscriber_notification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.update_subscriber_notification_request.UpdateSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id
        input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSubscriber:
    def __init__(self, service: AsyncSecurityLakeClient) -> None:
        self._service = service

    async def create(
        self,
        subscriber_identity: "aws_sdk_securitylake.types.aws_identity.AwsIdentity",
        subscriber_name: str,
        sources: "aws_sdk_securitylake.types.log_source_resource_list.LogSourceResourceList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        subscriber_description: Optional[
            "aws_sdk_securitylake.types.description_string.DescriptionString"
        ] = None,
        access_types: Optional[
            "aws_sdk_securitylake.types.access_type_list.AccessTypeList"
        ] = None,
        tags: Optional["aws_sdk_securitylake.types.tag_list.TagList"] = None,
    ) -> (
        "aws_sdk_securitylake.types.create_subscriber_response.CreateSubscriberResponse"
    ):
        """<p>Creates a subscriber for accounts that are already enabled in Amazon Security Lake. You can create a subscriber with access to data in the current Amazon Web Services Region.</p>

        Args:
            subscriber_identity: <p>The Amazon Web Services identity used to access your data.</p>
            subscriber_name: <p>The name of your Security Lake subscriber account.</p>
            subscriber_description: <p>The description for your subscriber account in Security Lake.</p>
            sources: <p>The supported Amazon Web Services services from which logs and events are collected. Security Lake supports log and event collection for natively supported Amazon Web Services services.</p>
            access_types: <p>The Amazon S3 or Lake Formation access type.</p>
            tags: <p>An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.create_subscriber_request.CreateSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.create_subscriber_response.CreateSubscriberResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.create_subscriber

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.create_subscriber.async_create_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.create_subscriber_request.CreateSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_identity"] = subscriber_identity
        input_["subscriber_name"] = subscriber_name
        if subscriber_description is not None:
            input_["subscriber_description"] = subscriber_description
        input_["sources"] = sources
        if access_types is not None:
            input_["access_types"] = access_types
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
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.get_subscriber_response.GetSubscriberResponse":
        """<p>Retrieves the subscription information for the specified subscription ID. You can get information about a specific subscriber.</p>

        Args:
            subscriber_id: <p>A value created by Amazon Security Lake that uniquely identifies your <code>GetSubscriber</code> API request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.get_subscriber_request.GetSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.get_subscriber_response.GetSubscriberResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.get_subscriber

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.get_subscriber.async_get_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.get_subscriber_request.GetSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        subscriber_identity: Optional[
            "aws_sdk_securitylake.types.aws_identity.AwsIdentity"
        ] = None,
        subscriber_name: Optional[
            "aws_sdk_securitylake.types.safe_string.SafeString"
        ] = None,
        subscriber_description: Optional[
            "aws_sdk_securitylake.types.description_string.DescriptionString"
        ] = None,
        sources: Optional[
            "aws_sdk_securitylake.types.log_source_resource_list.LogSourceResourceList"
        ] = None,
    ) -> (
        "aws_sdk_securitylake.types.update_subscriber_response.UpdateSubscriberResponse"
    ):
        """<p>Updates an existing subscription for the given Amazon Security Lake account ID. You can update a subscriber by changing the sources that the subscriber consumes data from.</p>

        Args:
            subscriber_id: <p>A value created by Security Lake that uniquely identifies your subscription.</p>
            subscriber_identity: <p>The Amazon Web Services identity used to access your data.</p>
            subscriber_name: <p>The name of the Security Lake account subscriber.</p>
            subscriber_description: <p>The description of the Security Lake account subscriber.</p>
            sources: <p>The supported Amazon Web Services services from which logs and events are collected. For the list of supported Amazon Web Services services, see the <a href=\"https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html\">Amazon Security Lake User Guide</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.update_subscriber_request.UpdateSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.update_subscriber_response.UpdateSubscriberResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.update_subscriber

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.update_subscriber.async_update_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.update_subscriber_request.UpdateSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id
        if subscriber_identity is not None:
            input_["subscriber_identity"] = subscriber_identity
        if subscriber_name is not None:
            input_["subscriber_name"] = subscriber_name
        if subscriber_description is not None:
            input_["subscriber_description"] = subscriber_description
        if sources is not None:
            input_["sources"] = sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> (
        "aws_sdk_securitylake.types.delete_subscriber_response.DeleteSubscriberResponse"
    ):
        """<p>Deletes the subscription permission and all notification settings for accounts that are already enabled in Amazon Security Lake. When you run <code>DeleteSubscriber</code>, the subscriber will no longer consume data from Security Lake and the subscriber is removed. This operation deletes the subscriber and removes access to data in the current Amazon Web Services Region.</p>

        Args:
            subscriber_id: <p>A value created by Security Lake that uniquely identifies your <code>DeleteSubscriber</code> API request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.delete_subscriber_request.DeleteSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.delete_subscriber_response.DeleteSubscriberResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.delete_subscriber

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.delete_subscriber.async_delete_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.delete_subscriber_request.DeleteSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        next_token: Optional["aws_sdk_securitylake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securitylake.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securitylake.types.list_subscribers_response.ListSubscribersResponse":
        """<p>Lists all subscribers for the specific Amazon Security Lake account ID. You can retrieve a list of subscriptions associated with a specific organization or Amazon Web Services account.</p>

        Args:
            next_token: <p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>
            max_results: <p>The maximum number of accounts for which the configuration is displayed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.list_subscribers_request.ListSubscribersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.list_subscribers_response.ListSubscribersResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.list_subscribers

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.list_subscribers.async_list_subscribers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.list_subscribers_request.ListSubscribersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_subscriber_notification(
        self,
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        configuration: "aws_sdk_securitylake.types.notification_configuration.NotificationConfiguration",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.create_subscriber_notification_response.CreateSubscriberNotificationResponse":
        """<p>Notifies the subscriber when new data is written to the data lake for the sources that the subscriber consumes in Security Lake. You can create only one subscriber notification per subscriber.</p>

        Args:
            subscriber_id: <p>The subscriber ID for the notification subscription.</p>
            configuration: <p>Specify the configuration using which you want to create the subscriber notification.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.create_subscriber_notification_request.CreateSubscriberNotificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.create_subscriber_notification_response.CreateSubscriberNotificationResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.create_subscriber_notification

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.create_subscriber_notification.async_create_subscriber_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.create_subscriber_notification_request.CreateSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id
        input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_subscriber_notification(
        self,
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.delete_subscriber_notification_response.DeleteSubscriberNotificationResponse":
        """<p>Deletes the specified subscription notification in Amazon Security Lake for the organization you specify.</p>

        Args:
            subscriber_id: <p>The ID of the Security Lake subscriber account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.delete_subscriber_notification_request.DeleteSubscriberNotificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.delete_subscriber_notification_response.DeleteSubscriberNotificationResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.delete_subscriber_notification

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.delete_subscriber_notification.async_delete_subscriber_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.delete_subscriber_notification_request.DeleteSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_subscriber_notification(
        self,
        subscriber_id: "aws_sdk_securitylake.types.uuid.UUID",
        configuration: "aws_sdk_securitylake.types.notification_configuration.NotificationConfiguration",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.update_subscriber_notification_response.UpdateSubscriberNotificationResponse":
        """<p>Updates an existing notification method for the subscription (SQS or HTTPs endpoint) or switches the notification subscription endpoint for a subscriber.</p>

        Args:
            subscriber_id: <p>The subscription ID for which the subscription notification is specified.</p>
            configuration: <p>The configuration for subscriber notification.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.update_subscriber_notification_request.UpdateSubscriberNotificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.update_subscriber_notification_response.UpdateSubscriberNotificationResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.update_subscriber_notification

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.update_subscriber_notification.async_update_subscriber_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.update_subscriber_notification_request.UpdateSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
        input_["subscriber_id"] = subscriber_id
        input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
