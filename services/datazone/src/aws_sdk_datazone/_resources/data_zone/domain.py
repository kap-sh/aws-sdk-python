from typing import TYPE_CHECKING, Optional

import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4
from aws_sdk_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_datazone.types.create_domain_input
    import aws_sdk_datazone.types.create_domain_output
    import aws_sdk_datazone.types.delete_domain_input
    import aws_sdk_datazone.types.delete_domain_output
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_status
    import aws_sdk_datazone.types.domain_summary
    import aws_sdk_datazone.types.domain_version
    import aws_sdk_datazone.types.get_domain_input
    import aws_sdk_datazone.types.get_domain_output
    import aws_sdk_datazone.types.kms_key_arn
    import aws_sdk_datazone.types.list_domains_input
    import aws_sdk_datazone.types.list_domains_output
    import aws_sdk_datazone.types.max_results_for_list_domains
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.role_arn
    import aws_sdk_datazone.types.single_sign_on
    import aws_sdk_datazone.types.tags
    import aws_sdk_datazone.types.update_domain_input
    import aws_sdk_datazone.types.update_domain_output
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )


class Domain:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional[str] = None,
        single_sign_on: Optional[
            "aws_sdk_datazone.types.single_sign_on.SingleSignOn"
        ] = None,
        domain_execution_role: Optional[
            "aws_sdk_datazone.types.role_arn.RoleArn"
        ] = None,
        kms_key_identifier: Optional[
            "aws_sdk_datazone.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_datazone.types.tags.Tags"] = None,
        domain_version: Optional[
            "aws_sdk_datazone.types.domain_version.DomainVersion"
        ] = None,
        service_role: Optional["aws_sdk_datazone.types.role_arn.RoleArn"] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.create_domain_output.CreateDomainOutput":
        """<p>Creates an Amazon DataZone domain.</p>

        Args:
            name: <p>The name of the Amazon DataZone domain.</p>
            description: <p>The description of the Amazon DataZone domain.</p>
            single_sign_on: <p>The single-sign on configuration of the Amazon DataZone domain.</p>
            domain_execution_role: <p>The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the Amazon Web Services account that houses the Amazon DataZone domain.</p>
            kms_key_identifier: <p>The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data. </p>
            tags: <p>The tags specified for the Amazon DataZone domain.</p>
            domain_version: <p>The version of the domain that is created.</p>
            service_role: <p>The service role of the domain that is created.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.create_domain_input.CreateDomainInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.create_domain_output.CreateDomainOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_domain

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.create_domain.create_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_domain_input.CreateDomainInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if single_sign_on is not None:
            input_["single_sign_on"] = single_sign_on
        if domain_execution_role is not None:
            input_["domain_execution_role"] = domain_execution_role
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if tags is not None:
            input_["tags"] = tags
        if domain_version is not None:
            input_["domain_version"] = domain_version
        if service_role is not None:
            input_["service_role"] = service_role
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_domain_output.GetDomainOutput":
        """<p>Gets an Amazon DataZone domain.</p>

        Args:
            identifier: <p>The identifier of the specified Amazon DataZone domain.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_domain_input.GetDomainInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_domain_output.GetDomainOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_domain

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_domain.get_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_domain_input.GetDomainInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional[str] = None,
        single_sign_on: Optional[
            "aws_sdk_datazone.types.single_sign_on.SingleSignOn"
        ] = None,
        domain_execution_role: Optional[
            "aws_sdk_datazone.types.role_arn.RoleArn"
        ] = None,
        service_role: Optional["aws_sdk_datazone.types.role_arn.RoleArn"] = None,
        name: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.update_domain_output.UpdateDomainOutput":
        """<p>Updates a Amazon DataZone domain.</p>

        Args:
            identifier: <p>The ID of the Amazon Web Services domain that is to be updated.</p>
            description: <p>The description to be updated as part of the <code>UpdateDomain</code> action.</p>
            single_sign_on: <p>The single sign-on option to be updated as part of the <code>UpdateDomain</code> action.</p>
            domain_execution_role: <p>The domain execution role to be updated as part of the <code>UpdateDomain</code> action.</p>
            service_role: <p>The service role of the domain.</p>
            name: <p>The name to be updated as part of the <code>UpdateDomain</code> action.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.update_domain_input.UpdateDomainInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.update_domain_output.UpdateDomainOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_domain

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.update_domain.update_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_domain_input.UpdateDomainInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if description is not None:
            input_["description"] = description
        if single_sign_on is not None:
            input_["single_sign_on"] = single_sign_on
        if domain_execution_role is not None:
            input_["domain_execution_role"] = domain_execution_role
        if service_role is not None:
            input_["service_role"] = service_role
        if name is not None:
            input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        client_token: Optional[str] = None,
        skip_deletion_check: Optional[bool] = None,
    ) -> "aws_sdk_datazone.types.delete_domain_output.DeleteDomainOutput":
        """<p>Deletes a Amazon DataZone domain.</p>

        Args:
            identifier: <p>The identifier of the Amazon Web Services domain that is to be deleted.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            skip_deletion_check: <p>Specifies the optional flag to delete all child entities within the domain.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.delete_domain_input.DeleteDomainInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.delete_domain_output.DeleteDomainOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_domain

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.delete_domain.delete_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_domain_input.DeleteDomainInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if client_token is not None:
            input_["client_token"] = client_token
        if skip_deletion_check is not None:
            input_["skip_deletion_check"] = skip_deletion_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        status: Optional["aws_sdk_datazone.types.domain_status.DomainStatus"] = None,
        max_results: Optional[
            "aws_sdk_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_domains_output.ListDomainsOutput":
        """<p>Lists Amazon DataZone domains.</p>

        Args:
            status: <p>The status of the data source.</p>
            max_results: <p>The maximum number of domains to return in a single call to <code>ListDomains</code>. When the number of domains to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>
            next_token: <p>When the number of domains is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of domains, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.list_domains_input.ListDomainsInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.list_domains_output.ListDomainsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_domains

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_domains_input.ListDomainsInput = {}  # type: ignore[typeddict-item]
        if status is not None:
            input_["status"] = status
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


class AsyncDomain:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
        single_sign_on: Optional[
            "aws_sdk_datazone.types.single_sign_on.SingleSignOn"
        ] = None,
        domain_execution_role: Optional[
            "aws_sdk_datazone.types.role_arn.RoleArn"
        ] = None,
        kms_key_identifier: Optional[
            "aws_sdk_datazone.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_datazone.types.tags.Tags"] = None,
        domain_version: Optional[
            "aws_sdk_datazone.types.domain_version.DomainVersion"
        ] = None,
        service_role: Optional["aws_sdk_datazone.types.role_arn.RoleArn"] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.create_domain_output.CreateDomainOutput":
        """<p>Creates an Amazon DataZone domain.</p>

        Args:
            name: <p>The name of the Amazon DataZone domain.</p>
            description: <p>The description of the Amazon DataZone domain.</p>
            single_sign_on: <p>The single-sign on configuration of the Amazon DataZone domain.</p>
            domain_execution_role: <p>The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the Amazon Web Services account that houses the Amazon DataZone domain.</p>
            kms_key_identifier: <p>The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data. </p>
            tags: <p>The tags specified for the Amazon DataZone domain.</p>
            domain_version: <p>The version of the domain that is created.</p>
            service_role: <p>The service role of the domain that is created.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_domain_input.CreateDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_domain_output.CreateDomainOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_domain

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_domain_input.CreateDomainInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if single_sign_on is not None:
            input_["single_sign_on"] = single_sign_on
        if domain_execution_role is not None:
            input_["domain_execution_role"] = domain_execution_role
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if tags is not None:
            input_["tags"] = tags
        if domain_version is not None:
            input_["domain_version"] = domain_version
        if service_role is not None:
            input_["service_role"] = service_role
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_domain_output.GetDomainOutput":
        """<p>Gets an Amazon DataZone domain.</p>

        Args:
            identifier: <p>The identifier of the specified Amazon DataZone domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_domain_input.GetDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_domain_output.GetDomainOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_domain

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_domain.async_get_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_domain_input.GetDomainInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
        single_sign_on: Optional[
            "aws_sdk_datazone.types.single_sign_on.SingleSignOn"
        ] = None,
        domain_execution_role: Optional[
            "aws_sdk_datazone.types.role_arn.RoleArn"
        ] = None,
        service_role: Optional["aws_sdk_datazone.types.role_arn.RoleArn"] = None,
        name: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_datazone.types.update_domain_output.UpdateDomainOutput":
        """<p>Updates a Amazon DataZone domain.</p>

        Args:
            identifier: <p>The ID of the Amazon Web Services domain that is to be updated.</p>
            description: <p>The description to be updated as part of the <code>UpdateDomain</code> action.</p>
            single_sign_on: <p>The single sign-on option to be updated as part of the <code>UpdateDomain</code> action.</p>
            domain_execution_role: <p>The domain execution role to be updated as part of the <code>UpdateDomain</code> action.</p>
            service_role: <p>The service role of the domain.</p>
            name: <p>The name to be updated as part of the <code>UpdateDomain</code> action.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_domain_input.UpdateDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_domain_output.UpdateDomainOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_domain

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_domain.async_update_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_domain_input.UpdateDomainInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if description is not None:
            input_["description"] = description
        if single_sign_on is not None:
            input_["single_sign_on"] = single_sign_on
        if domain_execution_role is not None:
            input_["domain_execution_role"] = domain_execution_role
        if service_role is not None:
            input_["service_role"] = service_role
        if name is not None:
            input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[str] = None,
        skip_deletion_check: Optional[bool] = None,
    ) -> "aws_sdk_datazone.types.delete_domain_output.DeleteDomainOutput":
        """<p>Deletes a Amazon DataZone domain.</p>

        Args:
            identifier: <p>The identifier of the Amazon Web Services domain that is to be deleted.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            skip_deletion_check: <p>Specifies the optional flag to delete all child entities within the domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_domain_input.DeleteDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_domain_output.DeleteDomainOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_domain

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_domain_input.DeleteDomainInput = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if client_token is not None:
            input_["client_token"] = client_token
        if skip_deletion_check is not None:
            input_["skip_deletion_check"] = skip_deletion_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["aws_sdk_datazone.types.domain_status.DomainStatus"] = None,
        max_results: Optional[
            "aws_sdk_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_domains_output.ListDomainsOutput":
        """<p>Lists Amazon DataZone domains.</p>

        Args:
            status: <p>The status of the data source.</p>
            max_results: <p>The maximum number of domains to return in a single call to <code>ListDomains</code>. When the number of domains to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>
            next_token: <p>When the number of domains is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of domains, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_domains_input.ListDomainsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_domains_output.ListDomainsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_domains

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_domains_input.ListDomainsInput = {}  # type: ignore[typeddict-item]
        if status is not None:
            input_["status"] = status
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
