from typing import TYPE_CHECKING, Optional

from aws_sdk_redshift_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.create_endpoint_access_request
    import aws_sdk_redshift_serverless.types.create_endpoint_access_response
    import aws_sdk_redshift_serverless.types.delete_endpoint_access_request
    import aws_sdk_redshift_serverless.types.delete_endpoint_access_response
    import aws_sdk_redshift_serverless.types.endpoint_access
    import aws_sdk_redshift_serverless.types.get_endpoint_access_request
    import aws_sdk_redshift_serverless.types.get_endpoint_access_response
    import aws_sdk_redshift_serverless.types.list_endpoint_access_request
    import aws_sdk_redshift_serverless.types.list_endpoint_access_response
    import aws_sdk_redshift_serverless.types.owner_account
    import aws_sdk_redshift_serverless.types.subnet_id_list
    import aws_sdk_redshift_serverless.types.update_endpoint_access_request
    import aws_sdk_redshift_serverless.types.update_endpoint_access_response
    import aws_sdk_redshift_serverless.types.vpc_security_group_id_list
    from aws_sdk_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from aws_sdk_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class CrossVpcEndpointResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def create_endpoint_access(
        self,
        endpoint_name: str,
        subnet_ids: "aws_sdk_redshift_serverless.types.subnet_id_list.SubnetIdList",
        workgroup_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        vpc_security_group_ids: Optional[
            "aws_sdk_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        owner_account: Optional[
            "aws_sdk_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_endpoint_access_response.CreateEndpointAccessResponse":
        """<p>Creates an Amazon Redshift Serverless managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint. An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can't contain two consecutive hyphens or end with a hyphen.</p>
            subnet_ids: <p>The unique identifers of subnets from which Amazon Redshift Serverless chooses one to deploy a VPC endpoint.</p>
            workgroup_name: <p>The name of the workgroup to associate with the VPC endpoint.</p>
            vpc_security_group_ids: <p>The unique identifiers of the security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.create_endpoint_access_request.CreateEndpointAccessRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.create_endpoint_access_response.CreateEndpointAccessResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_endpoint_access

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.create_endpoint_access.create_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_endpoint_access_request.CreateEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name
        input_["subnet_ids"] = subnet_ids
        input_["workgroup_name"] = workgroup_name
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_endpoint_access_response.DeleteEndpointAccessResponse":
        """<p>Deletes an Amazon Redshift Serverless managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.delete_endpoint_access_request.DeleteEndpointAccessRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.delete_endpoint_access_response.DeleteEndpointAccessResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_endpoint_access

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.delete_endpoint_access.delete_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_endpoint_access_request.DeleteEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_endpoint_access_response.GetEndpointAccessResponse":
        """<p>Returns information, such as the name, about a VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to return information for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.get_endpoint_access_request.GetEndpointAccessRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.get_endpoint_access_response.GetEndpointAccessResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_endpoint_access

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.get_endpoint_access.get_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_endpoint_access_request.GetEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_endpoint_access(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        workgroup_name: Optional[str] = None,
        vpc_id: Optional[str] = None,
        owner_account: Optional[
            "aws_sdk_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_endpoint_access_response.ListEndpointAccessResponse":
        """<p>Returns an array of <code>EndpointAccess</code> objects and relevant information.</p>

        Args:
            next_token: <p>If your initial <code>ListEndpointAccess</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListEndpointAccess</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            workgroup_name: <p>The name of the workgroup associated with the VPC endpoint to return.</p>
            vpc_id: <p>The unique identifier of the virtual private cloud with access to Amazon Redshift Serverless.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.list_endpoint_access_request.ListEndpointAccessRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.list_endpoint_access_response.ListEndpointAccessResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_endpoint_access

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.list_endpoint_access.list_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_endpoint_access_request.ListEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        vpc_security_group_ids: Optional[
            "aws_sdk_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_endpoint_access_response.UpdateEndpointAccessResponse":
        """<p>Updates an Amazon Redshift Serverless managed endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to update.</p>
            vpc_security_group_ids: <p>The list of VPC security groups associated with the endpoint after the endpoint is modified.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.update_endpoint_access_request.UpdateEndpointAccessRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.update_endpoint_access_response.UpdateEndpointAccessResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_endpoint_access

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.update_endpoint_access.update_endpoint_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_endpoint_access_request.UpdateEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCrossVpcEndpointResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def create_endpoint_access(
        self,
        endpoint_name: str,
        subnet_ids: "aws_sdk_redshift_serverless.types.subnet_id_list.SubnetIdList",
        workgroup_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        vpc_security_group_ids: Optional[
            "aws_sdk_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        owner_account: Optional[
            "aws_sdk_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_endpoint_access_response.CreateEndpointAccessResponse":
        """<p>Creates an Amazon Redshift Serverless managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint. An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can't contain two consecutive hyphens or end with a hyphen.</p>
            subnet_ids: <p>The unique identifers of subnets from which Amazon Redshift Serverless chooses one to deploy a VPC endpoint.</p>
            workgroup_name: <p>The name of the workgroup to associate with the VPC endpoint.</p>
            vpc_security_group_ids: <p>The unique identifiers of the security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.create_endpoint_access_request.CreateEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.create_endpoint_access_response.CreateEndpointAccessResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.create_endpoint_access.async_create_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_endpoint_access_request.CreateEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name
        input_["subnet_ids"] = subnet_ids
        input_["workgroup_name"] = workgroup_name
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_endpoint_access_response.DeleteEndpointAccessResponse":
        """<p>Deletes an Amazon Redshift Serverless managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.delete_endpoint_access_request.DeleteEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.delete_endpoint_access_response.DeleteEndpointAccessResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.delete_endpoint_access.async_delete_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_endpoint_access_request.DeleteEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_endpoint_access_response.GetEndpointAccessResponse":
        """<p>Returns information, such as the name, about a VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to return information for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.get_endpoint_access_request.GetEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.get_endpoint_access_response.GetEndpointAccessResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.get_endpoint_access.async_get_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_endpoint_access_request.GetEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        workgroup_name: Optional[str] = None,
        vpc_id: Optional[str] = None,
        owner_account: Optional[
            "aws_sdk_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_endpoint_access_response.ListEndpointAccessResponse":
        """<p>Returns an array of <code>EndpointAccess</code> objects and relevant information.</p>

        Args:
            next_token: <p>If your initial <code>ListEndpointAccess</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListEndpointAccess</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            workgroup_name: <p>The name of the workgroup associated with the VPC endpoint to return.</p>
            vpc_id: <p>The unique identifier of the virtual private cloud with access to Amazon Redshift Serverless.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.list_endpoint_access_request.ListEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.list_endpoint_access_response.ListEndpointAccessResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.list_endpoint_access.async_list_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_endpoint_access_request.ListEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        vpc_security_group_ids: Optional[
            "aws_sdk_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_endpoint_access_response.UpdateEndpointAccessResponse":
        """<p>Updates an Amazon Redshift Serverless managed endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to update.</p>
            vpc_security_group_ids: <p>The list of VPC security groups associated with the endpoint after the endpoint is modified.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.update_endpoint_access_request.UpdateEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.update_endpoint_access_response.UpdateEndpointAccessResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.update_endpoint_access.async_update_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_endpoint_access_request.UpdateEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_name"] = endpoint_name
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
