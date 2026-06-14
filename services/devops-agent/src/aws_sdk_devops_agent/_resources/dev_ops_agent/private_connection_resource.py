from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_devops_agent._auth._signers
import aws_sdk_devops_agent._auth._sigv4
from aws_sdk_devops_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.certificate_string
    import aws_sdk_devops_agent.types.create_private_connection_input
    import aws_sdk_devops_agent.types.create_private_connection_output
    import aws_sdk_devops_agent.types.delete_private_connection_input
    import aws_sdk_devops_agent.types.delete_private_connection_output
    import aws_sdk_devops_agent.types.describe_private_connection_input
    import aws_sdk_devops_agent.types.describe_private_connection_output
    import aws_sdk_devops_agent.types.list_private_connections_input
    import aws_sdk_devops_agent.types.list_private_connections_output
    import aws_sdk_devops_agent.types.private_connection_mode
    import aws_sdk_devops_agent.types.private_connection_name
    import aws_sdk_devops_agent.types.tags
    import aws_sdk_devops_agent.types.update_private_connection_certificate_input
    import aws_sdk_devops_agent.types.update_private_connection_certificate_output
    from aws_sdk_devops_agent._services.async_dev_ops_agent import (
        AsyncDevOpsAgentClient,
        AsyncDevOpsAgentClientConfig,
    )
    from aws_sdk_devops_agent._services.dev_ops_agent import (
        DevOpsAgentClient,
        DevOpsAgentClientConfig,
    )


class PrivateConnectionResource:
    def __init__(self, service: DevOpsAgentClient) -> None:
        self._service = service

    def put(
        self,
        name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName",
        mode: "aws_sdk_devops_agent.types.private_connection_mode.PrivateConnectionMode",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        tags: Optional["aws_sdk_devops_agent.types.tags.Tags"] = None,
    ) -> "aws_sdk_devops_agent.types.create_private_connection_output.CreatePrivateConnectionOutput":
        """<p>Creates a Private Connection to a target resource.</p>

        Args:
            name: <p>Unique name for this Private Connection within the account.</p>
            mode: <p>Private Connection mode configuration.</p>
            tags: <p>Tags to add to the Private Connection at creation time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.create_private_connection_input.CreatePrivateConnectionInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.create_private_connection_output.CreatePrivateConnectionOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.create_private_connection

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.create_private_connection.create_private_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.create_private_connection_input.CreatePrivateConnectionInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["mode"] = mode
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
        name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.describe_private_connection_output.DescribePrivateConnectionOutput":
        """<p>Retrieves details of an existing Private Connection.</p>

        Args:
            name: <p>The name of the Private Connection.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.describe_private_connection_input.DescribePrivateConnectionInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.describe_private_connection_output.DescribePrivateConnectionOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.describe_private_connection

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.describe_private_connection.describe_private_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.describe_private_connection_input.DescribePrivateConnectionInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.delete_private_connection_output.DeletePrivateConnectionOutput":
        """<p>Deletes a Private Connection. The deletion is asynchronous and returns DELETE_IN_PROGRESS status.</p>

        Args:
            name: <p>The name of the Private Connection.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.delete_private_connection_input.DeletePrivateConnectionInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.delete_private_connection_output.DeletePrivateConnectionOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.delete_private_connection

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.delete_private_connection.delete_private_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.delete_private_connection_input.DeletePrivateConnectionInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self, *, config_overrides: Optional[DevOpsAgentClientConfig] = None
    ) -> "aws_sdk_devops_agent.types.list_private_connections_output.ListPrivateConnectionsOutput":
        """<p>Lists all Private Connections in the caller's account.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.list_private_connections_input.ListPrivateConnectionsInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.list_private_connections_output.ListPrivateConnectionsOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_private_connections

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.list_private_connections.list_private_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_private_connections_input.ListPrivateConnectionsInput = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_private_connection_certificate(
        self,
        name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName",
        certificate: "aws_sdk_devops_agent.types.certificate_string.CertificateString",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput":
        """<p>Updates the certificate associated with a Private Connection.</p>

        Args:
            name: <p>The name of the Private Connection.</p>
            certificate: <p>The new certificate for the Private Connection.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_agent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput]",
        ) -> OperationResponse[
            "aws_sdk_devops_agent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_private_connection_certificate

            output, http_response = (
                aws_sdk_devops_agent._operations.dev_ops_agent.update_private_connection_certificate.update_private_connection_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["certificate"] = certificate

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncPrivateConnectionResource:
    def __init__(self, service: AsyncDevOpsAgentClient) -> None:
        self._service = service

    async def put(
        self,
        name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName",
        mode: "aws_sdk_devops_agent.types.private_connection_mode.PrivateConnectionMode",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        tags: Optional["aws_sdk_devops_agent.types.tags.Tags"] = None,
    ) -> "aws_sdk_devops_agent.types.create_private_connection_output.CreatePrivateConnectionOutput":
        """<p>Creates a Private Connection to a target resource.</p>

        Args:
            name: <p>Unique name for this Private Connection within the account.</p>
            mode: <p>Private Connection mode configuration.</p>
            tags: <p>Tags to add to the Private Connection at creation time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.create_private_connection_input.CreatePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.create_private_connection_output.CreatePrivateConnectionOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.create_private_connection

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.create_private_connection.async_create_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.create_private_connection_input.CreatePrivateConnectionInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["mode"] = mode
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
        name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.describe_private_connection_output.DescribePrivateConnectionOutput":
        """<p>Retrieves details of an existing Private Connection.</p>

        Args:
            name: <p>The name of the Private Connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.describe_private_connection_input.DescribePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.describe_private_connection_output.DescribePrivateConnectionOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.describe_private_connection

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.describe_private_connection.async_describe_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.describe_private_connection_input.DescribePrivateConnectionInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.delete_private_connection_output.DeletePrivateConnectionOutput":
        """<p>Deletes a Private Connection. The deletion is asynchronous and returns DELETE_IN_PROGRESS status.</p>

        Args:
            name: <p>The name of the Private Connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.delete_private_connection_input.DeletePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.delete_private_connection_output.DeletePrivateConnectionOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.delete_private_connection

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.delete_private_connection.async_delete_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.delete_private_connection_input.DeletePrivateConnectionInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self, *, config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None
    ) -> "aws_sdk_devops_agent.types.list_private_connections_output.ListPrivateConnectionsOutput":
        """<p>Lists all Private Connections in the caller's account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_private_connections_input.ListPrivateConnectionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_private_connections_output.ListPrivateConnectionsOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_private_connections

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_private_connections.async_list_private_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_private_connections_input.ListPrivateConnectionsInput = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_private_connection_certificate(
        self,
        name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName",
        certificate: "aws_sdk_devops_agent.types.certificate_string.CertificateString",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput":
        """<p>Updates the certificate associated with a Private Connection.</p>

        Args:
            name: <p>The name of the Private Connection.</p>
            certificate: <p>The new certificate for the Private Connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_private_connection_certificate

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.update_private_connection_certificate.async_update_private_connection_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["certificate"] = certificate

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
