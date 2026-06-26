from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_securityagent._auth._signers
import aws_sdk_securityagent._auth._sigv4
from aws_sdk_securityagent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.batch_get_target_domains_input
    import aws_sdk_securityagent.types.batch_get_target_domains_output
    import aws_sdk_securityagent.types.create_target_domain_input
    import aws_sdk_securityagent.types.create_target_domain_output
    import aws_sdk_securityagent.types.delete_target_domain_input
    import aws_sdk_securityagent.types.delete_target_domain_output
    import aws_sdk_securityagent.types.domain_verification_method
    import aws_sdk_securityagent.types.list_target_domains_input
    import aws_sdk_securityagent.types.list_target_domains_output
    import aws_sdk_securityagent.types.max_results
    import aws_sdk_securityagent.types.next_token
    import aws_sdk_securityagent.types.tag_map
    import aws_sdk_securityagent.types.target_domain_id
    import aws_sdk_securityagent.types.target_domain_id_list
    import aws_sdk_securityagent.types.target_domain_summary
    import aws_sdk_securityagent.types.update_target_domain_input
    import aws_sdk_securityagent.types.update_target_domain_output
    from aws_sdk_securityagent._services.async_security_agent import (
        AsyncSecurityAgentClient,
        AsyncSecurityAgentClientConfig,
    )
    from aws_sdk_securityagent._services.security_agent import (
        SecurityAgentClient,
        SecurityAgentClientConfig,
    )


class TargetDomainResource:
    def __init__(self, service: SecurityAgentClient) -> None:
        self._service = service

    def create(
        self,
        target_domain_name: str,
        verification_method: "aws_sdk_securityagent.types.domain_verification_method.DomainVerificationMethod",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        tags: Optional["aws_sdk_securityagent.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_securityagent.types.create_target_domain_output.CreateTargetDomainOutput":
        """<p>Creates a new target domain for penetration testing. A target domain is a web domain that must be registered and verified before it can be tested.</p>

        Args:
            target_domain_name: <p>The domain name to register as a target domain.</p>
            verification_method: <p>The method to use for verifying domain ownership. Valid values are DNS_TXT, HTTP_ROUTE, and PRIVATE_VPC.</p>
            tags: <p>The tags to associate with the target domain.</p>

        Raises:
            aws_sdk_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.create_target_domain_input.CreateTargetDomainInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.create_target_domain_output.CreateTargetDomainOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.create_target_domain

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.create_target_domain.create_target_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.create_target_domain_input.CreateTargetDomainInput = {}  # type: ignore[typeddict-item]
        input_["target_domain_name"] = target_domain_name
        input_["verification_method"] = verification_method
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        target_domain_id: "aws_sdk_securityagent.types.target_domain_id.TargetDomainId",
        verification_method: "aws_sdk_securityagent.types.domain_verification_method.DomainVerificationMethod",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.update_target_domain_output.UpdateTargetDomainOutput":
        """<p>Updates the verification method for a target domain.</p>

        Args:
            target_domain_id: <p>The unique identifier of the target domain to update.</p>
            verification_method: <p>The updated verification method for the target domain.</p>

        Raises:
            aws_sdk_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.update_target_domain_input.UpdateTargetDomainInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.update_target_domain_output.UpdateTargetDomainOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.update_target_domain

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.update_target_domain.update_target_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.update_target_domain_input.UpdateTargetDomainInput = {}  # type: ignore[typeddict-item]
        input_["target_domain_id"] = target_domain_id
        input_["verification_method"] = verification_method

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        target_domain_id: "aws_sdk_securityagent.types.target_domain_id.TargetDomainId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.delete_target_domain_output.DeleteTargetDomainOutput":
        """<p>Deletes a target domain registration. After deletion, the domain can no longer be used for penetration testing.</p>

        Args:
            target_domain_id: <p>The unique identifier of the target domain to delete.</p>

        Raises:
            aws_sdk_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.delete_target_domain_input.DeleteTargetDomainInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.delete_target_domain_output.DeleteTargetDomainOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.delete_target_domain

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.delete_target_domain.delete_target_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.delete_target_domain_input.DeleteTargetDomainInput = {}  # type: ignore[typeddict-item]
        input_["target_domain_id"] = target_domain_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "aws_sdk_securityagent.types.list_target_domains_output.ListTargetDomainsOutput"
    ):
        """<p>Returns a paginated list of target domain summaries in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            aws_sdk_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.list_target_domains_input.ListTargetDomainsInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.list_target_domains_output.ListTargetDomainsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_target_domains

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.list_target_domains.list_target_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_target_domains_input.ListTargetDomainsInput = {}  # type: ignore[typeddict-item]
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

    def batch_get_target_domains(
        self,
        target_domain_ids: "aws_sdk_securityagent.types.target_domain_id_list.TargetDomainIdList",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_target_domains_output.BatchGetTargetDomainsOutput":
        """<p>Retrieves information about one or more target domains.</p>

        Args:
            target_domain_ids: <p>The list of target domain identifiers to retrieve.</p>

        Raises:
            aws_sdk_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.batch_get_target_domains_input.BatchGetTargetDomainsInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.batch_get_target_domains_output.BatchGetTargetDomainsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_target_domains

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.batch_get_target_domains.batch_get_target_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_target_domains_input.BatchGetTargetDomainsInput = {}  # type: ignore[typeddict-item]
        input_["target_domain_ids"] = target_domain_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTargetDomainResource:
    def __init__(self, service: AsyncSecurityAgentClient) -> None:
        self._service = service

    async def create(
        self,
        target_domain_name: str,
        verification_method: "aws_sdk_securityagent.types.domain_verification_method.DomainVerificationMethod",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        tags: Optional["aws_sdk_securityagent.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_securityagent.types.create_target_domain_output.CreateTargetDomainOutput":
        """<p>Creates a new target domain for penetration testing. A target domain is a web domain that must be registered and verified before it can be tested.</p>

        Args:
            target_domain_name: <p>The domain name to register as a target domain.</p>
            verification_method: <p>The method to use for verifying domain ownership. Valid values are DNS_TXT, HTTP_ROUTE, and PRIVATE_VPC.</p>
            tags: <p>The tags to associate with the target domain.</p>

        Raises:
            aws_sdk_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.create_target_domain_input.CreateTargetDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.create_target_domain_output.CreateTargetDomainOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.create_target_domain

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.create_target_domain.async_create_target_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.create_target_domain_input.CreateTargetDomainInput = {}  # type: ignore[typeddict-item]
        input_["target_domain_name"] = target_domain_name
        input_["verification_method"] = verification_method
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        target_domain_id: "aws_sdk_securityagent.types.target_domain_id.TargetDomainId",
        verification_method: "aws_sdk_securityagent.types.domain_verification_method.DomainVerificationMethod",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.update_target_domain_output.UpdateTargetDomainOutput":
        """<p>Updates the verification method for a target domain.</p>

        Args:
            target_domain_id: <p>The unique identifier of the target domain to update.</p>
            verification_method: <p>The updated verification method for the target domain.</p>

        Raises:
            aws_sdk_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.update_target_domain_input.UpdateTargetDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.update_target_domain_output.UpdateTargetDomainOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.update_target_domain

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.update_target_domain.async_update_target_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.update_target_domain_input.UpdateTargetDomainInput = {}  # type: ignore[typeddict-item]
        input_["target_domain_id"] = target_domain_id
        input_["verification_method"] = verification_method

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        target_domain_id: "aws_sdk_securityagent.types.target_domain_id.TargetDomainId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.delete_target_domain_output.DeleteTargetDomainOutput":
        """<p>Deletes a target domain registration. After deletion, the domain can no longer be used for penetration testing.</p>

        Args:
            target_domain_id: <p>The unique identifier of the target domain to delete.</p>

        Raises:
            aws_sdk_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.delete_target_domain_input.DeleteTargetDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.delete_target_domain_output.DeleteTargetDomainOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.delete_target_domain

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.delete_target_domain.async_delete_target_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.delete_target_domain_input.DeleteTargetDomainInput = {}  # type: ignore[typeddict-item]
        input_["target_domain_id"] = target_domain_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "aws_sdk_securityagent.types.list_target_domains_output.ListTargetDomainsOutput"
    ):
        """<p>Returns a paginated list of target domain summaries in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            aws_sdk_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_target_domains_input.ListTargetDomainsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_target_domains_output.ListTargetDomainsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_target_domains

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_target_domains.async_list_target_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_target_domains_input.ListTargetDomainsInput = {}  # type: ignore[typeddict-item]
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

    async def batch_get_target_domains(
        self,
        target_domain_ids: "aws_sdk_securityagent.types.target_domain_id_list.TargetDomainIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_target_domains_output.BatchGetTargetDomainsOutput":
        """<p>Retrieves information about one or more target domains.</p>

        Args:
            target_domain_ids: <p>The list of target domain identifiers to retrieve.</p>

        Raises:
            aws_sdk_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_get_target_domains_input.BatchGetTargetDomainsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_get_target_domains_output.BatchGetTargetDomainsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_target_domains

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_get_target_domains.async_batch_get_target_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_target_domains_input.BatchGetTargetDomainsInput = {}  # type: ignore[typeddict-item]
        input_["target_domain_ids"] = target_domain_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
