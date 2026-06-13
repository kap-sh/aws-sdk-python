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
    import aws_sdk_bedrock.types.create_inference_profile_request
    import aws_sdk_bedrock.types.create_inference_profile_response
    import aws_sdk_bedrock.types.delete_inference_profile_request
    import aws_sdk_bedrock.types.delete_inference_profile_response
    import aws_sdk_bedrock.types.get_inference_profile_request
    import aws_sdk_bedrock.types.get_inference_profile_response
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.inference_profile_description
    import aws_sdk_bedrock.types.inference_profile_identifier
    import aws_sdk_bedrock.types.inference_profile_model_source
    import aws_sdk_bedrock.types.inference_profile_name
    import aws_sdk_bedrock.types.inference_profile_summary
    import aws_sdk_bedrock.types.inference_profile_type
    import aws_sdk_bedrock.types.list_inference_profiles_request
    import aws_sdk_bedrock.types.list_inference_profiles_response
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.tag_list
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class InferenceProfileResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create(
        self,
        inference_profile_name: "aws_sdk_bedrock.types.inference_profile_name.InferenceProfileName",
        model_source: "aws_sdk_bedrock.types.inference_profile_model_source.InferenceProfileModelSource",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock.types.inference_profile_description.InferenceProfileDescription"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock.types.create_inference_profile_response.CreateInferenceProfileResponse":
        """<p>Creates an application inference profile to track metrics and costs when invoking a model. To create an application inference profile for a foundation model in one region, specify the ARN of the model in that region. To create an application inference profile for a foundation model across multiple regions, specify the ARN of the system-defined inference profile that contains the regions that you want to route requests to. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            inference_profile_name: <p>A name for the inference profile.</p>
            description: <p>A description for the inference profile.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            model_source: <p>The foundation model or system-defined inference profile that the inference profile will track metrics and costs for.</p>
            tags: <p>An array of objects, each of which contains a tag and its value. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Tagging resources</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.create_inference_profile_request.CreateInferenceProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.create_inference_profile_response.CreateInferenceProfileResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_inference_profile

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_inference_profile.create_inference_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_inference_profile_request.CreateInferenceProfileRequest = {}  # type: ignore[typeddict-item]
        input["inference_profile_name"] = inference_profile_name
        if description is not None:
            input["description"] = description
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        input["model_source"] = model_source
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
        inference_profile_identifier: "aws_sdk_bedrock.types.inference_profile_identifier.InferenceProfileIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_inference_profile_response.GetInferenceProfileResponse":
        """<p>Gets information about an inference profile. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            inference_profile_identifier: <p>The ID or Amazon Resource Name (ARN) of the inference profile.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_inference_profile_request.GetInferenceProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_inference_profile_response.GetInferenceProfileResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_inference_profile

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_inference_profile.get_inference_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_inference_profile_request.GetInferenceProfileRequest = {}  # type: ignore[typeddict-item]
        input["inference_profile_identifier"] = inference_profile_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        inference_profile_identifier: "aws_sdk_bedrock.types.inference_profile_identifier.InferenceProfileIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_inference_profile_response.DeleteInferenceProfileResponse":
        """<p>Deletes an application inference profile. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            inference_profile_identifier: <p>The Amazon Resource Name (ARN) or ID of the application inference profile to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.delete_inference_profile_request.DeleteInferenceProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.delete_inference_profile_response.DeleteInferenceProfileResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_inference_profile

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_inference_profile.delete_inference_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_inference_profile_request.DeleteInferenceProfileRequest = {}  # type: ignore[typeddict-item]
        input["inference_profile_identifier"] = inference_profile_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        type_equals: Optional[
            "aws_sdk_bedrock.types.inference_profile_type.InferenceProfileType"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_inference_profiles_response.ListInferenceProfilesResponse":
        """<p>Returns a list of inference profiles that you can use. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            type_equals: <p>Filters for inference profiles that match the type you specify.</p> <ul> <li> <p> <code>SYSTEM_DEFINED</code> – The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles.</p> </li> <li> <p> <code>APPLICATION</code> – The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_inference_profiles_request.ListInferenceProfilesRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_inference_profiles_response.ListInferenceProfilesResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_inference_profiles

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_inference_profiles.list_inference_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_inference_profiles_request.ListInferenceProfilesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if type_equals is not None:
            input["type_equals"] = type_equals

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncInferenceProfileResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create(
        self,
        inference_profile_name: "aws_sdk_bedrock.types.inference_profile_name.InferenceProfileName",
        model_source: "aws_sdk_bedrock.types.inference_profile_model_source.InferenceProfileModelSource",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock.types.inference_profile_description.InferenceProfileDescription"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock.types.create_inference_profile_response.CreateInferenceProfileResponse":
        """<p>Creates an application inference profile to track metrics and costs when invoking a model. To create an application inference profile for a foundation model in one region, specify the ARN of the model in that region. To create an application inference profile for a foundation model across multiple regions, specify the ARN of the system-defined inference profile that contains the regions that you want to route requests to. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            inference_profile_name: <p>A name for the inference profile.</p>
            description: <p>A description for the inference profile.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            model_source: <p>The foundation model or system-defined inference profile that the inference profile will track metrics and costs for.</p>
            tags: <p>An array of objects, each of which contains a tag and its value. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Tagging resources</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.create_inference_profile_request.CreateInferenceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.create_inference_profile_response.CreateInferenceProfileResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_inference_profile

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_inference_profile.async_create_inference_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_inference_profile_request.CreateInferenceProfileRequest = {}  # type: ignore[typeddict-item]
        input["inference_profile_name"] = inference_profile_name
        if description is not None:
            input["description"] = description
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        input["model_source"] = model_source
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
        inference_profile_identifier: "aws_sdk_bedrock.types.inference_profile_identifier.InferenceProfileIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_inference_profile_response.GetInferenceProfileResponse":
        """<p>Gets information about an inference profile. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            inference_profile_identifier: <p>The ID or Amazon Resource Name (ARN) of the inference profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_inference_profile_request.GetInferenceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_inference_profile_response.GetInferenceProfileResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_inference_profile

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_inference_profile.async_get_inference_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_inference_profile_request.GetInferenceProfileRequest = {}  # type: ignore[typeddict-item]
        input["inference_profile_identifier"] = inference_profile_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        inference_profile_identifier: "aws_sdk_bedrock.types.inference_profile_identifier.InferenceProfileIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_inference_profile_response.DeleteInferenceProfileResponse":
        """<p>Deletes an application inference profile. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            inference_profile_identifier: <p>The Amazon Resource Name (ARN) or ID of the application inference profile to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.delete_inference_profile_request.DeleteInferenceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.delete_inference_profile_response.DeleteInferenceProfileResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_inference_profile

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_inference_profile.async_delete_inference_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_inference_profile_request.DeleteInferenceProfileRequest = {}  # type: ignore[typeddict-item]
        input["inference_profile_identifier"] = inference_profile_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        type_equals: Optional[
            "aws_sdk_bedrock.types.inference_profile_type.InferenceProfileType"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_inference_profiles_response.ListInferenceProfilesResponse":
        """<p>Returns a list of inference profiles that you can use. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html\">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            type_equals: <p>Filters for inference profiles that match the type you specify.</p> <ul> <li> <p> <code>SYSTEM_DEFINED</code> – The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles.</p> </li> <li> <p> <code>APPLICATION</code> – The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_inference_profiles_request.ListInferenceProfilesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_inference_profiles_response.ListInferenceProfilesResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_inference_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_inference_profiles.async_list_inference_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_inference_profiles_request.ListInferenceProfilesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if type_equals is not None:
            input["type_equals"] = type_equals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
