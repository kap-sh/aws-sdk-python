from typing import Optional, TYPE_CHECKING
from aws_sdk_proton._services.async_proton import ensure_async_iterator
from aws_sdk_proton._services.proton import ensure_sync_iterator
from aws_sdk_proton._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
if TYPE_CHECKING:
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig
    from aws_sdk_proton._services.async_proton import AsyncProtonClient, AsyncProtonClientConfig
    import aws_sdk_proton.types.accept_environment_account_connection_input
    import aws_sdk_proton.types.accept_environment_account_connection_output
    import aws_sdk_proton.types.aws_account_id
    import aws_sdk_proton.types.client_token
    import aws_sdk_proton.types.create_environment_account_connection_input
    import aws_sdk_proton.types.create_environment_account_connection_output
    import aws_sdk_proton.types.delete_environment_account_connection_input
    import aws_sdk_proton.types.delete_environment_account_connection_output
    import aws_sdk_proton.types.environment_account_connection_id
    import aws_sdk_proton.types.environment_account_connection_requester_account_type
    import aws_sdk_proton.types.environment_account_connection_status_list
    import aws_sdk_proton.types.environment_account_connection_summary
    import aws_sdk_proton.types.get_environment_account_connection_input
    import aws_sdk_proton.types.get_environment_account_connection_output
    import aws_sdk_proton.types.list_environment_account_connections_input
    import aws_sdk_proton.types.list_environment_account_connections_output
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.reject_environment_account_connection_input
    import aws_sdk_proton.types.reject_environment_account_connection_output
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.role_arn
    import aws_sdk_proton.types.tag_list
    import aws_sdk_proton.types.update_environment_account_connection_input
    import aws_sdk_proton.types.update_environment_account_connection_output

class EnvironmentAccountConnectionResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service
    def create(self, management_account_id: "aws_sdk_proton.types.aws_account_id.AwsAccountId", environment_name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[ProtonClientConfig] = None, client_token: Optional["aws_sdk_proton.types.client_token.ClientToken"] = None, role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None, tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None, component_role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None, codebuild_role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None) -> "aws_sdk_proton.types.create_environment_account_connection_output.CreateEnvironmentAccountConnectionOutput":
        """<p>Create an environment account connection in an environment account so that environment infrastructure resources can be provisioned in the environment account from a management account.</p> <p>An environment account connection is a secure bi-directional connection between a <i>management account</i> and an <i>environment account</i> that maintains authorization and permissions. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the environment account connection that the first request created.</p>
            management_account_id: <p>The ID of the management account that accepts or rejects the environment account connection. You create and manage the Proton environment in this account. If the management account accepts the environment account connection, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. Proton uses this role to provision infrastructure resources in the associated environment account.</p>
            environment_name: <p>The name of the Proton environment that's created in the associated management account.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment account connection. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>You must specify <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in this account.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.create_environment_account_connection_input.CreateEnvironmentAccountConnectionInput]') -> OperationResponse["aws_sdk_proton.types.create_environment_account_connection_output.CreateEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.create_environment_account_connection
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.create_environment_account_connection.create_environment_account_connection(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_environment_account_connection_input.CreateEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["management_account_id"] = management_account_id
        if role_arn is not None:
            input["role_arn"] = role_arn
        input["environment_name"] = environment_name
        if tags is not None:
            input["tags"] = tags
        if component_role_arn is not None:
            input["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input["codebuild_role_arn"] = codebuild_role_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.get_environment_account_connection_output.GetEnvironmentAccountConnectionOutput":
        """<p>In an environment account, get the detailed data for an environment account connection.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection that you want to get the detailed data for.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.get_environment_account_connection_input.GetEnvironmentAccountConnectionInput]') -> OperationResponse["aws_sdk_proton.types.get_environment_account_connection_output.GetEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.get_environment_account_connection
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.get_environment_account_connection.get_environment_account_connection(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_environment_account_connection_input.GetEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId", *, config_overrides: Optional[ProtonClientConfig] = None, role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None, component_role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None, codebuild_role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None) -> "aws_sdk_proton.types.update_environment_account_connection_output.UpdateEnvironmentAccountConnectionOutput":
        """<p>In an environment account, update an environment account connection to use a new IAM role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to update.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that's associated with the environment account connection to update.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>The environment account connection must have a <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in the account.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.update_environment_account_connection_input.UpdateEnvironmentAccountConnectionInput]') -> OperationResponse["aws_sdk_proton.types.update_environment_account_connection_output.UpdateEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.update_environment_account_connection
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.update_environment_account_connection.update_environment_account_connection(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_environment_account_connection_input.UpdateEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if role_arn is not None:
            input["role_arn"] = role_arn
        if component_role_arn is not None:
            input["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input["codebuild_role_arn"] = codebuild_role_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.delete_environment_account_connection_output.DeleteEnvironmentAccountConnectionOutput":
        """<p>In an environment account, delete an environment account connection.</p> <p>After you delete an environment account connection that’s in use by an Proton environment, Proton <i>can’t</i> manage the environment infrastructure resources until a new environment account connection is accepted for the environment account and associated environment. You're responsible for cleaning up provisioned resources that remain without an environment connection.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.delete_environment_account_connection_input.DeleteEnvironmentAccountConnectionInput]') -> OperationResponse["aws_sdk_proton.types.delete_environment_account_connection_output.DeleteEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_environment_account_connection
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.delete_environment_account_connection.delete_environment_account_connection(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.delete_environment_account_connection_input.DeleteEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, requested_by: "aws_sdk_proton.types.environment_account_connection_requester_account_type.EnvironmentAccountConnectionRequesterAccountType", *, config_overrides: Optional[ProtonClientConfig] = None, environment_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, statuses: Optional["aws_sdk_proton.types.environment_account_connection_status_list.EnvironmentAccountConnectionStatusList"] = None, next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_proton.types.max_page_results.MaxPageResults"] = None) -> "aws_sdk_proton.types.list_environment_account_connections_output.ListEnvironmentAccountConnectionsOutput":
        """<p>View a list of environment account connections.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            requested_by: <p>The type of account making the <code>ListEnvironmentAccountConnections</code> request.</p>
            environment_name: <p>The environment name that's associated with each listed environment account connection.</p>
            statuses: <p>The status details for each listed environment account connection.</p>
            next_token: <p>A token that indicates the location of the next environment account connection in the array of environment account connections, after the list of environment account connections that was previously requested.</p>
            max_results: <p>The maximum number of environment account connections to list.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.list_environment_account_connections_input.ListEnvironmentAccountConnectionsInput]') -> OperationResponse["aws_sdk_proton.types.list_environment_account_connections_output.ListEnvironmentAccountConnectionsOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.list_environment_account_connections
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.list_environment_account_connections.list_environment_account_connections(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.list_environment_account_connections_input.ListEnvironmentAccountConnectionsInput = {}  # type: ignore[typeddict-item]
        input["requested_by"] = requested_by
        if environment_name is not None:
            input["environment_name"] = environment_name
        if statuses is not None:
            input["statuses"] = statuses
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def accept_environment_account_connection(self, id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.accept_environment_account_connection_output.AcceptEnvironmentAccountConnectionOutput":
        """<p>In a management account, an environment account connection request is accepted. When the environment account connection request is accepted, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.accept_environment_account_connection_input.AcceptEnvironmentAccountConnectionInput]') -> OperationResponse["aws_sdk_proton.types.accept_environment_account_connection_output.AcceptEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.accept_environment_account_connection
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.accept_environment_account_connection.accept_environment_account_connection(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.accept_environment_account_connection_input.AcceptEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def reject_environment_account_connection(self, id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId", *, config_overrides: Optional[ProtonClientConfig] = None) -> "aws_sdk_proton.types.reject_environment_account_connection_output.RejectEnvironmentAccountConnectionOutput":
        """<p>In a management account, reject an environment account connection from another environment account.</p> <p>After you reject an environment account connection request, you <i>can't</i> accept or use the rejected environment account connection.</p> <p>You <i>can’t</i> reject an environment account connection that's connected to an environment.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to reject.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_proton.types.reject_environment_account_connection_input.RejectEnvironmentAccountConnectionInput]') -> OperationResponse["aws_sdk_proton.types.reject_environment_account_connection_output.RejectEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.reject_environment_account_connection
            output, http_response = aws_sdk_proton._operations.aws_proton20200720.reject_environment_account_connection.reject_environment_account_connection(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.reject_environment_account_connection_input.RejectEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncEnvironmentAccountConnectionResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service
    async def create(self, management_account_id: "aws_sdk_proton.types.aws_account_id.AwsAccountId", environment_name: "aws_sdk_proton.types.resource_name.ResourceName", *, config_overrides: Optional[AsyncProtonClientConfig] = None, client_token: Optional["aws_sdk_proton.types.client_token.ClientToken"] = None, role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None, tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None, component_role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None, codebuild_role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None) -> "aws_sdk_proton.types.create_environment_account_connection_output.CreateEnvironmentAccountConnectionOutput":
        """<p>Create an environment account connection in an environment account so that environment infrastructure resources can be provisioned in the environment account from a management account.</p> <p>An environment account connection is a secure bi-directional connection between a <i>management account</i> and an <i>environment account</i> that maintains authorization and permissions. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the environment account connection that the first request created.</p>
            management_account_id: <p>The ID of the management account that accepts or rejects the environment account connection. You create and manage the Proton environment in this account. If the management account accepts the environment account connection, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. Proton uses this role to provision infrastructure resources in the associated environment account.</p>
            environment_name: <p>The name of the Proton environment that's created in the associated management account.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment account connection. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>You must specify <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in this account.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.create_environment_account_connection_input.CreateEnvironmentAccountConnectionInput]') -> AsyncOperationResponse["aws_sdk_proton.types.create_environment_account_connection_output.CreateEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.create_environment_account_connection
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.create_environment_account_connection.async_create_environment_account_connection(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.create_environment_account_connection_input.CreateEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["management_account_id"] = management_account_id
        if role_arn is not None:
            input["role_arn"] = role_arn
        input["environment_name"] = environment_name
        if tags is not None:
            input["tags"] = tags
        if component_role_arn is not None:
            input["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input["codebuild_role_arn"] = codebuild_role_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.get_environment_account_connection_output.GetEnvironmentAccountConnectionOutput":
        """<p>In an environment account, get the detailed data for an environment account connection.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection that you want to get the detailed data for.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.get_environment_account_connection_input.GetEnvironmentAccountConnectionInput]') -> AsyncOperationResponse["aws_sdk_proton.types.get_environment_account_connection_output.GetEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.get_environment_account_connection
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.get_environment_account_connection.async_get_environment_account_connection(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.get_environment_account_connection_input.GetEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId", *, config_overrides: Optional[AsyncProtonClientConfig] = None, role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None, component_role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None, codebuild_role_arn: Optional["aws_sdk_proton.types.role_arn.RoleArn"] = None) -> "aws_sdk_proton.types.update_environment_account_connection_output.UpdateEnvironmentAccountConnectionOutput":
        """<p>In an environment account, update an environment account connection to use a new IAM role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to update.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that's associated with the environment account connection to update.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>The environment account connection must have a <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in the account.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.update_environment_account_connection_input.UpdateEnvironmentAccountConnectionInput]') -> AsyncOperationResponse["aws_sdk_proton.types.update_environment_account_connection_output.UpdateEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.update_environment_account_connection
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.update_environment_account_connection.async_update_environment_account_connection(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_environment_account_connection_input.UpdateEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if role_arn is not None:
            input["role_arn"] = role_arn
        if component_role_arn is not None:
            input["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input["codebuild_role_arn"] = codebuild_role_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.delete_environment_account_connection_output.DeleteEnvironmentAccountConnectionOutput":
        """<p>In an environment account, delete an environment account connection.</p> <p>After you delete an environment account connection that’s in use by an Proton environment, Proton <i>can’t</i> manage the environment infrastructure resources until a new environment account connection is accepted for the environment account and associated environment. You're responsible for cleaning up provisioned resources that remain without an environment connection.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.delete_environment_account_connection_input.DeleteEnvironmentAccountConnectionInput]') -> AsyncOperationResponse["aws_sdk_proton.types.delete_environment_account_connection_output.DeleteEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_environment_account_connection
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.delete_environment_account_connection.async_delete_environment_account_connection(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.delete_environment_account_connection_input.DeleteEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, requested_by: "aws_sdk_proton.types.environment_account_connection_requester_account_type.EnvironmentAccountConnectionRequesterAccountType", *, config_overrides: Optional[AsyncProtonClientConfig] = None, environment_name: Optional["aws_sdk_proton.types.resource_name.ResourceName"] = None, statuses: Optional["aws_sdk_proton.types.environment_account_connection_status_list.EnvironmentAccountConnectionStatusList"] = None, next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_proton.types.max_page_results.MaxPageResults"] = None) -> "aws_sdk_proton.types.list_environment_account_connections_output.ListEnvironmentAccountConnectionsOutput":
        """<p>View a list of environment account connections.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            requested_by: <p>The type of account making the <code>ListEnvironmentAccountConnections</code> request.</p>
            environment_name: <p>The environment name that's associated with each listed environment account connection.</p>
            statuses: <p>The status details for each listed environment account connection.</p>
            next_token: <p>A token that indicates the location of the next environment account connection in the array of environment account connections, after the list of environment account connections that was previously requested.</p>
            max_results: <p>The maximum number of environment account connections to list.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.list_environment_account_connections_input.ListEnvironmentAccountConnectionsInput]') -> AsyncOperationResponse["aws_sdk_proton.types.list_environment_account_connections_output.ListEnvironmentAccountConnectionsOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.list_environment_account_connections
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.list_environment_account_connections.async_list_environment_account_connections(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.list_environment_account_connections_input.ListEnvironmentAccountConnectionsInput = {}  # type: ignore[typeddict-item]
        input["requested_by"] = requested_by
        if environment_name is not None:
            input["environment_name"] = environment_name
        if statuses is not None:
            input["statuses"] = statuses
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def accept_environment_account_connection(self, id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.accept_environment_account_connection_output.AcceptEnvironmentAccountConnectionOutput":
        """<p>In a management account, an environment account connection request is accepted. When the environment account connection request is accepted, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.accept_environment_account_connection_input.AcceptEnvironmentAccountConnectionInput]') -> AsyncOperationResponse["aws_sdk_proton.types.accept_environment_account_connection_output.AcceptEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.accept_environment_account_connection
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.accept_environment_account_connection.async_accept_environment_account_connection(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.accept_environment_account_connection_input.AcceptEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def reject_environment_account_connection(self, id: "aws_sdk_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId", *, config_overrides: Optional[AsyncProtonClientConfig] = None) -> "aws_sdk_proton.types.reject_environment_account_connection_output.RejectEnvironmentAccountConnectionOutput":
        """<p>In a management account, reject an environment account connection from another environment account.</p> <p>After you reject an environment account connection request, you <i>can't</i> accept or use the rejected environment account connection.</p> <p>You <i>can’t</i> reject an environment account connection that's connected to an environment.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html\">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to reject.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_proton.types.reject_environment_account_connection_input.RejectEnvironmentAccountConnectionInput]') -> AsyncOperationResponse["aws_sdk_proton.types.reject_environment_account_connection_output.RejectEnvironmentAccountConnectionOutput"]:
            import aws_sdk_proton._operations.aws_proton20200720.reject_environment_account_connection
            output, http_response = await aws_sdk_proton._operations.aws_proton20200720.reject_environment_account_connection.async_reject_environment_account_connection(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.reject_environment_account_connection_input.RejectEnvironmentAccountConnectionInput = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output