from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from aws_sdk_voice_id._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.client_token_string
    import aws_sdk_voice_id.types.create_domain_request
    import aws_sdk_voice_id.types.create_domain_response
    import aws_sdk_voice_id.types.delete_domain_request
    import aws_sdk_voice_id.types.describe_domain_request
    import aws_sdk_voice_id.types.describe_domain_response
    import aws_sdk_voice_id.types.description
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.domain_name
    import aws_sdk_voice_id.types.domain_summary
    import aws_sdk_voice_id.types.list_domains_request
    import aws_sdk_voice_id.types.list_domains_response
    import aws_sdk_voice_id.types.max_results_for_list_domain_fe
    import aws_sdk_voice_id.types.next_token
    import aws_sdk_voice_id.types.server_side_encryption_configuration
    import aws_sdk_voice_id.types.tag_list
    import aws_sdk_voice_id.types.update_domain_request
    import aws_sdk_voice_id.types.update_domain_response
    from aws_sdk_voice_id._services.async_voice_id import (
        AsyncVoiceIDClient,
        AsyncVoiceIDClientConfig,
    )
    from aws_sdk_voice_id._services.voice_id import VoiceIDClient, VoiceIDClientConfig


class DomainResource:
    def __init__(self, service: VoiceIDClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_voice_id.types.domain_name.DomainName",
        server_side_encryption_configuration: "aws_sdk_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        description: Optional["aws_sdk_voice_id.types.description.Description"] = None,
        client_token: Optional[
            "aws_sdk_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional["aws_sdk_voice_id.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_voice_id.types.create_domain_response.CreateDomainResponse":
        r"""<p>Creates a domain that contains all Amazon Connect Voice ID data, such as speakers, fraudsters, customer audio, and voiceprints. Every domain is created with a default watchlist that fraudsters can be a part of.</p>

        Args:
            name: <p>The name of the domain.</p>
            description: <p>A brief description of this domain.</p>
            server_side_encryption_configuration: <p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Refer to <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/encryption-at-rest.html#encryption-at-rest-voiceid\"> Amazon Connect Voice ID encryption at rest</a> for more details on how the KMS key is used. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A list of tags you want added to the domain.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_voice_id.types.create_domain_request.CreateDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_voice_id.types.create_domain_response.CreateDomainResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.create_domain

            output, http_response = (
                aws_sdk_voice_id._operations.voice_id.create_domain.create_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.create_domain_request.CreateDomainRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["server_side_encryption_configuration"] = (
            server_side_encryption_configuration
        )
        if client_token is not None:
            input_["client_token"] = client_token
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
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.describe_domain_response.DescribeDomainResponse":
        """<p>Describes the specified domain.</p>

        Args:
            domain_id: <p>The identifier of the domain that you are describing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_voice_id.types.describe_domain_request.DescribeDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_voice_id.types.describe_domain_response.DescribeDomainResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.describe_domain

            output, http_response = (
                aws_sdk_voice_id._operations.voice_id.describe_domain.describe_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.describe_domain_request.DescribeDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        name: "aws_sdk_voice_id.types.domain_name.DomainName",
        server_side_encryption_configuration: "aws_sdk_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        description: Optional["aws_sdk_voice_id.types.description.Description"] = None,
    ) -> "aws_sdk_voice_id.types.update_domain_response.UpdateDomainResponse":
        """<p>Updates the specified domain. This API has clobber behavior, and clears and replaces all attributes. If an optional field, such as 'Description' is not provided, it is removed from the domain.</p>

        Args:
            domain_id: <p>The identifier of the domain to be updated.</p>
            name: <p>The name of the domain.</p>
            description: <p>A brief description about this domain.</p>
            server_side_encryption_configuration: <p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Changing the domain's associated KMS key immediately triggers an asynchronous process to remove dependency on the old KMS key, such that the domain's data can only be accessed using the new KMS key. The domain's <code>ServerSideEncryptionUpdateDetails</code> contains the details for this process.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_voice_id.types.update_domain_request.UpdateDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_voice_id.types.update_domain_response.UpdateDomainResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.update_domain

            output, http_response = (
                aws_sdk_voice_id._operations.voice_id.update_domain.update_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.update_domain_request.UpdateDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["server_side_encryption_configuration"] = (
            server_side_encryption_configuration
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified domain from Voice ID.</p>

        Args:
            domain_id: <p>The identifier of the domain you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_voice_id.types.delete_domain_request.DeleteDomainRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_voice_id._operations.voice_id.delete_domain

            output, http_response = (
                aws_sdk_voice_id._operations.voice_id.delete_domain.delete_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.delete_domain_request.DeleteDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[VoiceIDClientConfig] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list_domain_fe.MaxResultsForListDomainFe"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_voice_id.types.list_domains_response.ListDomainsResponse":
        """<p>Lists all the domains in the Amazon Web Services account. </p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100.</p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_voice_id.types.list_domains_request.ListDomainsRequest]",
        ) -> OperationResponse[
            "aws_sdk_voice_id.types.list_domains_response.ListDomainsResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.list_domains

            output, http_response = (
                aws_sdk_voice_id._operations.voice_id.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.list_domains_request.ListDomainsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncDomainResource:
    def __init__(self, service: AsyncVoiceIDClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_voice_id.types.domain_name.DomainName",
        server_side_encryption_configuration: "aws_sdk_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        description: Optional["aws_sdk_voice_id.types.description.Description"] = None,
        client_token: Optional[
            "aws_sdk_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional["aws_sdk_voice_id.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_voice_id.types.create_domain_response.CreateDomainResponse":
        r"""<p>Creates a domain that contains all Amazon Connect Voice ID data, such as speakers, fraudsters, customer audio, and voiceprints. Every domain is created with a default watchlist that fraudsters can be a part of.</p>

        Args:
            name: <p>The name of the domain.</p>
            description: <p>A brief description of this domain.</p>
            server_side_encryption_configuration: <p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Refer to <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/encryption-at-rest.html#encryption-at-rest-voiceid\"> Amazon Connect Voice ID encryption at rest</a> for more details on how the KMS key is used. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A list of tags you want added to the domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.create_domain_request.CreateDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.create_domain_response.CreateDomainResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.create_domain

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.create_domain_request.CreateDomainRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["server_side_encryption_configuration"] = (
            server_side_encryption_configuration
        )
        if client_token is not None:
            input_["client_token"] = client_token
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
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.describe_domain_response.DescribeDomainResponse":
        """<p>Describes the specified domain.</p>

        Args:
            domain_id: <p>The identifier of the domain that you are describing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.describe_domain_request.DescribeDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.describe_domain_response.DescribeDomainResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.describe_domain

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.describe_domain.async_describe_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.describe_domain_request.DescribeDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        name: "aws_sdk_voice_id.types.domain_name.DomainName",
        server_side_encryption_configuration: "aws_sdk_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        description: Optional["aws_sdk_voice_id.types.description.Description"] = None,
    ) -> "aws_sdk_voice_id.types.update_domain_response.UpdateDomainResponse":
        """<p>Updates the specified domain. This API has clobber behavior, and clears and replaces all attributes. If an optional field, such as 'Description' is not provided, it is removed from the domain.</p>

        Args:
            domain_id: <p>The identifier of the domain to be updated.</p>
            name: <p>The name of the domain.</p>
            description: <p>A brief description about this domain.</p>
            server_side_encryption_configuration: <p>The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Changing the domain's associated KMS key immediately triggers an asynchronous process to remove dependency on the old KMS key, such that the domain's data can only be accessed using the new KMS key. The domain's <code>ServerSideEncryptionUpdateDetails</code> contains the details for this process.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.update_domain_request.UpdateDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.update_domain_response.UpdateDomainResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.update_domain

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.update_domain.async_update_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.update_domain_request.UpdateDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["server_side_encryption_configuration"] = (
            server_side_encryption_configuration
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified domain from Voice ID.</p>

        Args:
            domain_id: <p>The identifier of the domain you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.delete_domain_request.DeleteDomainRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_voice_id._operations.voice_id.delete_domain

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.delete_domain_request.DeleteDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list_domain_fe.MaxResultsForListDomainFe"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_voice_id.types.list_domains_response.ListDomainsResponse":
        """<p>Lists all the domains in the Amazon Web Services account. </p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100.</p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.list_domains_request.ListDomainsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.list_domains_response.ListDomainsResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.list_domains

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.list_domains_request.ListDomainsRequest = {}  # type: ignore[typeddict-item]
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
