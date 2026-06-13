from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock._auth._signers
import aws_sdk_bedrock._auth._sigv4
from aws_sdk_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.bedrock_model_id
    import aws_sdk_bedrock.types.create_foundation_model_agreement_request
    import aws_sdk_bedrock.types.create_foundation_model_agreement_response
    import aws_sdk_bedrock.types.delete_foundation_model_agreement_request
    import aws_sdk_bedrock.types.delete_foundation_model_agreement_response
    import aws_sdk_bedrock.types.get_foundation_model_availability_request
    import aws_sdk_bedrock.types.get_foundation_model_availability_response
    import aws_sdk_bedrock.types.list_foundation_model_agreement_offers_request
    import aws_sdk_bedrock.types.list_foundation_model_agreement_offers_response
    import aws_sdk_bedrock.types.offer_token
    import aws_sdk_bedrock.types.offer_type
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class SubscriptionResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_foundation_model_agreement(
        self,
        offer_token: "aws_sdk_bedrock.types.offer_token.OfferToken",
        model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.create_foundation_model_agreement_response.CreateFoundationModelAgreementResponse":
        """<p>Request a model access agreement for the specified model.</p>

        Args:
            offer_token: <p>An offer token encapsulates the information for an offer.</p>
            model_id: <p>Model Id of the model for the access request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.create_foundation_model_agreement_request.CreateFoundationModelAgreementRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.create_foundation_model_agreement_response.CreateFoundationModelAgreementResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_foundation_model_agreement

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_foundation_model_agreement.create_foundation_model_agreement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_foundation_model_agreement_request.CreateFoundationModelAgreementRequest = {}  # type: ignore[typeddict-item]
        input["offer_token"] = offer_token
        input["model_id"] = model_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_foundation_model_agreement(
        self,
        model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_foundation_model_agreement_response.DeleteFoundationModelAgreementResponse":
        """<p>Delete the model access agreement for the specified model.</p>

        Args:
            model_id: <p>Model Id of the model access to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.delete_foundation_model_agreement_request.DeleteFoundationModelAgreementRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.delete_foundation_model_agreement_response.DeleteFoundationModelAgreementResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_foundation_model_agreement

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_foundation_model_agreement.delete_foundation_model_agreement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_foundation_model_agreement_request.DeleteFoundationModelAgreementRequest = {}  # type: ignore[typeddict-item]
        input["model_id"] = model_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_foundation_model_availability(
        self,
        model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_foundation_model_availability_response.GetFoundationModelAvailabilityResponse":
        """<p>Get information about the Foundation model availability.</p>

        Args:
            model_id: <p>The model Id of the foundation model.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_foundation_model_availability_request.GetFoundationModelAvailabilityRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_foundation_model_availability_response.GetFoundationModelAvailabilityResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model_availability

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model_availability.get_foundation_model_availability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_foundation_model_availability_request.GetFoundationModelAvailabilityRequest = {}  # type: ignore[typeddict-item]
        input["model_id"] = model_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_foundation_model_agreement_offers(
        self,
        model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        offer_type: Optional["aws_sdk_bedrock.types.offer_type.OfferType"] = None,
    ) -> "aws_sdk_bedrock.types.list_foundation_model_agreement_offers_response.ListFoundationModelAgreementOffersResponse":
        """<p>Get the offers associated with the specified model.</p>

        Args:
            model_id: <p>Model Id of the foundation model.</p>
            offer_type: <p>Type of offer associated with the model.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_foundation_model_agreement_offers_request.ListFoundationModelAgreementOffersRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_foundation_model_agreement_offers_response.ListFoundationModelAgreementOffersResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_model_agreement_offers

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_model_agreement_offers.list_foundation_model_agreement_offers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_foundation_model_agreement_offers_request.ListFoundationModelAgreementOffersRequest = {}  # type: ignore[typeddict-item]
        input["model_id"] = model_id
        if offer_type is not None:
            input["offer_type"] = offer_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSubscriptionResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_foundation_model_agreement(
        self,
        offer_token: "aws_sdk_bedrock.types.offer_token.OfferToken",
        model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.create_foundation_model_agreement_response.CreateFoundationModelAgreementResponse":
        """<p>Request a model access agreement for the specified model.</p>

        Args:
            offer_token: <p>An offer token encapsulates the information for an offer.</p>
            model_id: <p>Model Id of the model for the access request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.create_foundation_model_agreement_request.CreateFoundationModelAgreementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.create_foundation_model_agreement_response.CreateFoundationModelAgreementResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_foundation_model_agreement

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_foundation_model_agreement.async_create_foundation_model_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_foundation_model_agreement_request.CreateFoundationModelAgreementRequest = {}  # type: ignore[typeddict-item]
        input["offer_token"] = offer_token
        input["model_id"] = model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_foundation_model_agreement(
        self,
        model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_foundation_model_agreement_response.DeleteFoundationModelAgreementResponse":
        """<p>Delete the model access agreement for the specified model.</p>

        Args:
            model_id: <p>Model Id of the model access to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.delete_foundation_model_agreement_request.DeleteFoundationModelAgreementRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.delete_foundation_model_agreement_response.DeleteFoundationModelAgreementResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_foundation_model_agreement

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_foundation_model_agreement.async_delete_foundation_model_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_foundation_model_agreement_request.DeleteFoundationModelAgreementRequest = {}  # type: ignore[typeddict-item]
        input["model_id"] = model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_foundation_model_availability(
        self,
        model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_foundation_model_availability_response.GetFoundationModelAvailabilityResponse":
        """<p>Get information about the Foundation model availability.</p>

        Args:
            model_id: <p>The model Id of the foundation model.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_foundation_model_availability_request.GetFoundationModelAvailabilityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_foundation_model_availability_response.GetFoundationModelAvailabilityResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model_availability

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model_availability.async_get_foundation_model_availability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_foundation_model_availability_request.GetFoundationModelAvailabilityRequest = {}  # type: ignore[typeddict-item]
        input["model_id"] = model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_foundation_model_agreement_offers(
        self,
        model_id: "aws_sdk_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        offer_type: Optional["aws_sdk_bedrock.types.offer_type.OfferType"] = None,
    ) -> "aws_sdk_bedrock.types.list_foundation_model_agreement_offers_response.ListFoundationModelAgreementOffersResponse":
        """<p>Get the offers associated with the specified model.</p>

        Args:
            model_id: <p>Model Id of the foundation model.</p>
            offer_type: <p>Type of offer associated with the model.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_foundation_model_agreement_offers_request.ListFoundationModelAgreementOffersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_foundation_model_agreement_offers_response.ListFoundationModelAgreementOffersResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_model_agreement_offers

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_model_agreement_offers.async_list_foundation_model_agreement_offers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_foundation_model_agreement_offers_request.ListFoundationModelAgreementOffersRequest = {}  # type: ignore[typeddict-item]
        input["model_id"] = model_id
        if offer_type is not None:
            input["offer_type"] = offer_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
