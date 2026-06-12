from typing import TYPE_CHECKING, Optional

import aws_sdk_artifact._auth._signers
import aws_sdk_artifact._auth._sigv4
from aws_sdk_artifact._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_artifact.types.customer_agreement_summary
    import aws_sdk_artifact.types.list_customer_agreements_request
    import aws_sdk_artifact.types.list_customer_agreements_response
    import aws_sdk_artifact.types.max_results_attribute
    import aws_sdk_artifact.types.next_token_attribute
    from aws_sdk_artifact._services.artifact import ArtifactClient, ArtifactClientConfig
    from aws_sdk_artifact._services.async_artifact import (
        AsyncArtifactClient,
        AsyncArtifactClientConfig,
    )


class CustomerAgreementResource:
    def __init__(self, service: ArtifactClient) -> None:
        self._service = service

    def list_customer_agreements(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "aws_sdk_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "aws_sdk_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "aws_sdk_artifact.types.list_customer_agreements_response.ListCustomerAgreementsResponse":
        """<p>List active customer-agreements applicable to calling identity.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Examples:
            Invoke ListCustomerAgreements operation
            The ListCustomerAgreements operation returns a collection of customer-agreement resources in the ACTIVE state for the calling credential.

            >>> client.list_customer_agreements()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_artifact.types.list_customer_agreements_request.ListCustomerAgreementsRequest]",
        ) -> OperationResponse[
            "aws_sdk_artifact.types.list_customer_agreements_response.ListCustomerAgreementsResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.list_customer_agreements

            output, http_response = (
                aws_sdk_artifact._operations.artifact.list_customer_agreements.list_customer_agreements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.list_customer_agreements_request.ListCustomerAgreementsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncCustomerAgreementResource:
    def __init__(self, service: AsyncArtifactClient) -> None:
        self._service = service

    async def list_customer_agreements(
        self,
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        max_results: Optional[
            "aws_sdk_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "aws_sdk_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "aws_sdk_artifact.types.list_customer_agreements_response.ListCustomerAgreementsResponse":
        """<p>List active customer-agreements applicable to calling identity.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Examples:
            Invoke ListCustomerAgreements operation
            The ListCustomerAgreements operation returns a collection of customer-agreement resources in the ACTIVE state for the calling credential.

            >>> await client.list_customer_agreements()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_artifact.types.list_customer_agreements_request.ListCustomerAgreementsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_artifact.types.list_customer_agreements_response.ListCustomerAgreementsResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.list_customer_agreements

            (
                output,
                http_response,
            ) = await aws_sdk_artifact._operations.artifact.list_customer_agreements.async_list_customer_agreements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.list_customer_agreements_request.ListCustomerAgreementsRequest = {}  # type: ignore[typeddict-item]
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
