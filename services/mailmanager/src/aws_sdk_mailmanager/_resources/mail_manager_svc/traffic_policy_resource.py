from typing import TYPE_CHECKING, Optional

from aws_sdk_mailmanager._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.accept_action
    import aws_sdk_mailmanager.types.create_traffic_policy_request
    import aws_sdk_mailmanager.types.create_traffic_policy_response
    import aws_sdk_mailmanager.types.delete_traffic_policy_request
    import aws_sdk_mailmanager.types.delete_traffic_policy_response
    import aws_sdk_mailmanager.types.get_traffic_policy_request
    import aws_sdk_mailmanager.types.get_traffic_policy_response
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.list_traffic_policies_request
    import aws_sdk_mailmanager.types.list_traffic_policies_response
    import aws_sdk_mailmanager.types.max_message_size_bytes
    import aws_sdk_mailmanager.types.page_size
    import aws_sdk_mailmanager.types.pagination_token
    import aws_sdk_mailmanager.types.policy_statement_list
    import aws_sdk_mailmanager.types.tag_list
    import aws_sdk_mailmanager.types.traffic_policy
    import aws_sdk_mailmanager.types.traffic_policy_id
    import aws_sdk_mailmanager.types.traffic_policy_name
    import aws_sdk_mailmanager.types.update_traffic_policy_request
    import aws_sdk_mailmanager.types.update_traffic_policy_response
    from aws_sdk_mailmanager._services.async_mail_manager import (
        AsyncMailManagerClient,
        AsyncMailManagerClientConfig,
    )
    from aws_sdk_mailmanager._services.mail_manager import (
        MailManagerClient,
        MailManagerClientConfig,
    )


class TrafficPolicyResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        traffic_policy_name: "aws_sdk_mailmanager.types.traffic_policy_name.TrafficPolicyName",
        policy_statements: "aws_sdk_mailmanager.types.policy_statement_list.PolicyStatementList",
        default_action: "aws_sdk_mailmanager.types.accept_action.AcceptAction",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        max_message_size_bytes: Optional[
            "aws_sdk_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
        ] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_traffic_policy_response.CreateTrafficPolicyResponse":
        """<p>Provision a new traffic policy resource.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            traffic_policy_name: <p>A user-friendly name for the traffic policy resource.</p>
            policy_statements: <p>Conditional statements for filtering email traffic.</p>
            default_action: <p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>
            max_message_size_bytes: <p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>

        Examples:
            Create TrafficPolicy

            >>> client.create(traffic_policy_name='trafficPolicyName', policy_statements=[{'Conditions': [{'IpExpression': {'Evaluate': {'Attribute': 'SENDER_IP'}, 'Operator': 'CIDR_MATCHES', 'Values': ['0.0.0.0/12']}}], 'Action': 'ALLOW'}], default_action='DENY')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.create_traffic_policy_request.CreateTrafficPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.create_traffic_policy_response.CreateTrafficPolicyResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_traffic_policy

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.create_traffic_policy.create_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mailmanager.types.create_traffic_policy_request.CreateTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["traffic_policy_name"] = traffic_policy_name
        input["policy_statements"] = policy_statements
        input["default_action"] = default_action
        if max_message_size_bytes is not None:
            input["max_message_size_bytes"] = max_message_size_bytes
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        traffic_policy_id: "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> (
        "aws_sdk_mailmanager.types.get_traffic_policy_response.GetTrafficPolicyResponse"
    ):
        """<p>Fetch attributes of a traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy resource.</p>

        Examples:
            Get TrafficPolicy

            >>> client.read(traffic_policy_id='tp-12345')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_traffic_policy_request.GetTrafficPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_traffic_policy_response.GetTrafficPolicyResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_traffic_policy

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_traffic_policy.get_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mailmanager.types.get_traffic_policy_request.GetTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
        input["traffic_policy_id"] = traffic_policy_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        traffic_policy_id: "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        traffic_policy_name: Optional[
            "aws_sdk_mailmanager.types.traffic_policy_name.TrafficPolicyName"
        ] = None,
        policy_statements: Optional[
            "aws_sdk_mailmanager.types.policy_statement_list.PolicyStatementList"
        ] = None,
        default_action: Optional[
            "aws_sdk_mailmanager.types.accept_action.AcceptAction"
        ] = None,
        max_message_size_bytes: Optional[
            "aws_sdk_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.update_traffic_policy_response.UpdateTrafficPolicyResponse":
        """<p>Update attributes of an already provisioned traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy that you want to update.</p>
            traffic_policy_name: <p>A user-friendly name for the traffic policy resource.</p>
            policy_statements: <p>The list of conditions to be updated for filtering email traffic.</p>
            default_action: <p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>
            max_message_size_bytes: <p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>

        Examples:
            Update TrafficPolicy with new Name

            >>> client.update(traffic_policy_id='tp-12345', traffic_policy_name='trafficPolicyNewName')
            Update TrafficPolicy with new PolicyStatements

            >>> client.update(traffic_policy_id='tp-12345', policy_statements=[{'Conditions': [{'StringExpression': {'Evaluate': {'Attribute': 'RECIPIENT'}, 'Operator': 'EQUALS', 'Values': ['example@amazon.com', 'example@gmail.com']}}], 'Action': 'ALLOW'}])
            Update TrafficPolicy with new DefaultAction

            >>> client.update(traffic_policy_id='tp-12345', default_action='ALLOW')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.update_traffic_policy_request.UpdateTrafficPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.update_traffic_policy_response.UpdateTrafficPolicyResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.update_traffic_policy

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.update_traffic_policy.update_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mailmanager.types.update_traffic_policy_request.UpdateTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
        input["traffic_policy_id"] = traffic_policy_id
        if traffic_policy_name is not None:
            input["traffic_policy_name"] = traffic_policy_name
        if policy_statements is not None:
            input["policy_statements"] = policy_statements
        if default_action is not None:
            input["default_action"] = default_action
        if max_message_size_bytes is not None:
            input["max_message_size_bytes"] = max_message_size_bytes

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        traffic_policy_id: "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse":
        """<p>Delete a traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy that you want to delete.</p>

        Examples:
            Delete TrafficPolicy

            >>> client.delete(traffic_policy_id='tp-12345')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_traffic_policy

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.delete_traffic_policy.delete_traffic_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mailmanager.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
        input["traffic_policy_id"] = traffic_policy_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.list_traffic_policies_response.ListTrafficPoliciesResponse":
        """<p>List traffic policy resources.</p>

        Args:
            page_size: <p>The maximum number of traffic policy resources that are returned per call. You can use NextToken to obtain further traffic policies.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Examples:
            List TrafficPolicies

            >>> client.list()
            List TrafficPolicies with PageSize

            >>> client.list(page_size=10)
            List TrafficPolicies with NextToken

            >>> client.list(next_token='nextToken')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_traffic_policies_request.ListTrafficPoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_traffic_policies_response.ListTrafficPoliciesResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_traffic_policies

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_traffic_policies.list_traffic_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mailmanager.types.list_traffic_policies_request.ListTrafficPoliciesRequest = {}  # type: ignore[typeddict-item]
        if page_size is not None:
            input["page_size"] = page_size
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTrafficPolicyResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        traffic_policy_name: "aws_sdk_mailmanager.types.traffic_policy_name.TrafficPolicyName",
        policy_statements: "aws_sdk_mailmanager.types.policy_statement_list.PolicyStatementList",
        default_action: "aws_sdk_mailmanager.types.accept_action.AcceptAction",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        max_message_size_bytes: Optional[
            "aws_sdk_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
        ] = None,
        tags: Optional["aws_sdk_mailmanager.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mailmanager.types.create_traffic_policy_response.CreateTrafficPolicyResponse":
        """<p>Provision a new traffic policy resource.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            traffic_policy_name: <p>A user-friendly name for the traffic policy resource.</p>
            policy_statements: <p>Conditional statements for filtering email traffic.</p>
            default_action: <p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>
            max_message_size_bytes: <p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>

        Examples:
            Create TrafficPolicy

            >>> await client.create(traffic_policy_name='trafficPolicyName', policy_statements=[{'Conditions': [{'IpExpression': {'Evaluate': {'Attribute': 'SENDER_IP'}, 'Operator': 'CIDR_MATCHES', 'Values': ['0.0.0.0/12']}}], 'Action': 'ALLOW'}], default_action='DENY')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.create_traffic_policy_request.CreateTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.create_traffic_policy_response.CreateTrafficPolicyResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_traffic_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.create_traffic_policy.async_create_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mailmanager.types.create_traffic_policy_request.CreateTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["traffic_policy_name"] = traffic_policy_name
        input["policy_statements"] = policy_statements
        input["default_action"] = default_action
        if max_message_size_bytes is not None:
            input["max_message_size_bytes"] = max_message_size_bytes
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        traffic_policy_id: "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> (
        "aws_sdk_mailmanager.types.get_traffic_policy_response.GetTrafficPolicyResponse"
    ):
        """<p>Fetch attributes of a traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy resource.</p>

        Examples:
            Get TrafficPolicy

            >>> await client.read(traffic_policy_id='tp-12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.get_traffic_policy_request.GetTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.get_traffic_policy_response.GetTrafficPolicyResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_traffic_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.get_traffic_policy.async_get_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mailmanager.types.get_traffic_policy_request.GetTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
        input["traffic_policy_id"] = traffic_policy_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        traffic_policy_id: "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        traffic_policy_name: Optional[
            "aws_sdk_mailmanager.types.traffic_policy_name.TrafficPolicyName"
        ] = None,
        policy_statements: Optional[
            "aws_sdk_mailmanager.types.policy_statement_list.PolicyStatementList"
        ] = None,
        default_action: Optional[
            "aws_sdk_mailmanager.types.accept_action.AcceptAction"
        ] = None,
        max_message_size_bytes: Optional[
            "aws_sdk_mailmanager.types.max_message_size_bytes.MaxMessageSizeBytes"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.update_traffic_policy_response.UpdateTrafficPolicyResponse":
        """<p>Update attributes of an already provisioned traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy that you want to update.</p>
            traffic_policy_name: <p>A user-friendly name for the traffic policy resource.</p>
            policy_statements: <p>The list of conditions to be updated for filtering email traffic.</p>
            default_action: <p>Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements</p>
            max_message_size_bytes: <p>The maximum message size in bytes of email which is allowed in by this traffic policy—anything larger will be blocked.</p>

        Examples:
            Update TrafficPolicy with new Name

            >>> await client.update(traffic_policy_id='tp-12345', traffic_policy_name='trafficPolicyNewName')
            Update TrafficPolicy with new PolicyStatements

            >>> await client.update(traffic_policy_id='tp-12345', policy_statements=[{'Conditions': [{'StringExpression': {'Evaluate': {'Attribute': 'RECIPIENT'}, 'Operator': 'EQUALS', 'Values': ['example@amazon.com', 'example@gmail.com']}}], 'Action': 'ALLOW'}])
            Update TrafficPolicy with new DefaultAction

            >>> await client.update(traffic_policy_id='tp-12345', default_action='ALLOW')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.update_traffic_policy_request.UpdateTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.update_traffic_policy_response.UpdateTrafficPolicyResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.update_traffic_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.update_traffic_policy.async_update_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mailmanager.types.update_traffic_policy_request.UpdateTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
        input["traffic_policy_id"] = traffic_policy_id
        if traffic_policy_name is not None:
            input["traffic_policy_name"] = traffic_policy_name
        if policy_statements is not None:
            input["policy_statements"] = policy_statements
        if default_action is not None:
            input["default_action"] = default_action
        if max_message_size_bytes is not None:
            input["max_message_size_bytes"] = max_message_size_bytes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        traffic_policy_id: "aws_sdk_mailmanager.types.traffic_policy_id.TrafficPolicyId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse":
        """<p>Delete a traffic policy resource.</p>

        Args:
            traffic_policy_id: <p>The identifier of the traffic policy that you want to delete.</p>

        Examples:
            Delete TrafficPolicy

            >>> await client.delete(traffic_policy_id='tp-12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.delete_traffic_policy_response.DeleteTrafficPolicyResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.delete_traffic_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.delete_traffic_policy.async_delete_traffic_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mailmanager.types.delete_traffic_policy_request.DeleteTrafficPolicyRequest = {}  # type: ignore[typeddict-item]
        input["traffic_policy_id"] = traffic_policy_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.list_traffic_policies_response.ListTrafficPoliciesResponse":
        """<p>List traffic policy resources.</p>

        Args:
            page_size: <p>The maximum number of traffic policy resources that are returned per call. You can use NextToken to obtain further traffic policies.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Examples:
            List TrafficPolicies

            >>> await client.list()
            List TrafficPolicies with PageSize

            >>> await client.list(page_size=10)
            List TrafficPolicies with NextToken

            >>> await client.list(next_token='nextToken')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mailmanager.types.list_traffic_policies_request.ListTrafficPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mailmanager.types.list_traffic_policies_response.ListTrafficPoliciesResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_traffic_policies

            (
                output,
                http_response,
            ) = await aws_sdk_mailmanager._operations.mail_manager_svc.list_traffic_policies.async_list_traffic_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mailmanager.types.list_traffic_policies_request.ListTrafficPoliciesRequest = {}  # type: ignore[typeddict-item]
        if page_size is not None:
            input["page_size"] = page_size
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
