from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock._services.async_bedrock import ensure_async_iterator
from aws_sdk_bedrock._services.bedrock import ensure_sync_iterator
from aws_sdk_bedrock._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)
import aws_sdk_bedrock._auth._signers
import aws_sdk_bedrock._auth._sigv4

if TYPE_CHECKING:
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    import aws_sdk_bedrock.types.commitment_duration
    import aws_sdk_bedrock.types.create_provisioned_model_throughput_request
    import aws_sdk_bedrock.types.create_provisioned_model_throughput_response
    import aws_sdk_bedrock.types.delete_provisioned_model_throughput_request
    import aws_sdk_bedrock.types.delete_provisioned_model_throughput_response
    import aws_sdk_bedrock.types.get_provisioned_model_throughput_request
    import aws_sdk_bedrock.types.get_provisioned_model_throughput_response
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.list_provisioned_model_throughputs_request
    import aws_sdk_bedrock.types.list_provisioned_model_throughputs_response
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.model_arn
    import aws_sdk_bedrock.types.model_identifier
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.positive_integer
    import aws_sdk_bedrock.types.provisioned_model_id
    import aws_sdk_bedrock.types.provisioned_model_name
    import aws_sdk_bedrock.types.provisioned_model_status
    import aws_sdk_bedrock.types.provisioned_model_summary
    import aws_sdk_bedrock.types.sort_by_provisioned_models
    import aws_sdk_bedrock.types.sort_order
    import aws_sdk_bedrock.types.tag_list
    import aws_sdk_bedrock.types.timestamp
    import aws_sdk_bedrock.types.update_provisioned_model_throughput_request
    import aws_sdk_bedrock.types.update_provisioned_model_throughput_response


class ProvisionedModelThroughputResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_provisioned_model_throughput(
        self,
        model_units: "aws_sdk_bedrock.types.positive_integer.PositiveInteger",
        provisioned_model_name: "aws_sdk_bedrock.types.provisioned_model_name.ProvisionedModelName",
        model_id: "aws_sdk_bedrock.types.model_identifier.ModelIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        commitment_duration: Optional[
            "aws_sdk_bedrock.types.commitment_duration.CommitmentDuration"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock.types.create_provisioned_model_throughput_response.CreateProvisionedModelThroughputResponse":
        """<p>Creates dedicated throughput for a base or custom model with the model units and for the duration that you specify. For pricing details, see <a href=\"http://aws.amazon.com/bedrock/pricing/\">Amazon Bedrock Pricing</a>. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the Amazon S3 User Guide.</p>
            model_units: <p>Number of model units to allocate. A model unit delivers a specific throughput level for the specified model. The throughput level of a model unit specifies the total number of input and output tokens that it can process and generate within a span of one minute. By default, your account has no model units for purchasing Provisioned Throughputs with commitment. You must first visit the <a href=\"https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase\">Amazon Web Services support center</a> to request MUs.</p> <p>For model unit quotas, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html#prov-thru-quotas\">Provisioned Throughput quotas</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p> <p>For more information about what an MU specifies, contact your Amazon Web Services account manager.</p>
            provisioned_model_name: <p>The name for this Provisioned Throughput.</p>
            model_id: <p>The Amazon Resource Name (ARN) or name of the model to associate with this Provisioned Throughput. For a list of models for which you can purchase Provisioned Throughput, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#prov-throughput-models\">Amazon Bedrock model IDs for purchasing Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>
            commitment_duration: <p>The commitment duration requested for the Provisioned Throughput. Billing occurs hourly and is discounted for longer commitment terms. To request a no-commit Provisioned Throughput, omit this field.</p> <p>Custom models support all levels of commitment. To see which base models support no commitment, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/pt-supported.html\">Supported regions and models for Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a> </p>
            tags: <p>Tags to associate with this Provisioned Throughput.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.create_provisioned_model_throughput_request.CreateProvisionedModelThroughputRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.create_provisioned_model_throughput_response.CreateProvisionedModelThroughputResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_provisioned_model_throughput

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_provisioned_model_throughput.create_provisioned_model_throughput(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_provisioned_model_throughput_request.CreateProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        input["model_units"] = model_units
        input["provisioned_model_name"] = provisioned_model_name
        input["model_id"] = model_id
        if commitment_duration is not None:
            input["commitment_duration"] = commitment_duration
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_provisioned_model_throughput(
        self,
        provisioned_model_id: "aws_sdk_bedrock.types.provisioned_model_id.ProvisionedModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_provisioned_model_throughput_response.DeleteProvisionedModelThroughputResponse":
        """<p>Deletes a Provisioned Throughput. You can't delete a Provisioned Throughput before the commitment term is over. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            provisioned_model_id: <p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.delete_provisioned_model_throughput_request.DeleteProvisionedModelThroughputRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.delete_provisioned_model_throughput_response.DeleteProvisionedModelThroughputResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_provisioned_model_throughput

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_provisioned_model_throughput.delete_provisioned_model_throughput(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_provisioned_model_throughput_request.DeleteProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
        input["provisioned_model_id"] = provisioned_model_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_provisioned_model_throughput(
        self,
        provisioned_model_id: "aws_sdk_bedrock.types.provisioned_model_id.ProvisionedModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_provisioned_model_throughput_response.GetProvisionedModelThroughputResponse":
        """<p>Returns details for a Provisioned Throughput. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            provisioned_model_id: <p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_provisioned_model_throughput_request.GetProvisionedModelThroughputRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_provisioned_model_throughput_response.GetProvisionedModelThroughputResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_provisioned_model_throughput

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_provisioned_model_throughput.get_provisioned_model_throughput(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_provisioned_model_throughput_request.GetProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
        input["provisioned_model_id"] = provisioned_model_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_provisioned_model_throughputs(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        creation_time_after: Optional[
            "aws_sdk_bedrock.types.timestamp.Timestamp"
        ] = None,
        creation_time_before: Optional[
            "aws_sdk_bedrock.types.timestamp.Timestamp"
        ] = None,
        status_equals: Optional[
            "aws_sdk_bedrock.types.provisioned_model_status.ProvisionedModelStatus"
        ] = None,
        model_arn_equals: Optional["aws_sdk_bedrock.types.model_arn.ModelArn"] = None,
        name_contains: Optional[
            "aws_sdk_bedrock.types.provisioned_model_name.ProvisionedModelName"
        ] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "aws_sdk_bedrock.types.sort_by_provisioned_models.SortByProvisionedModels"
        ] = None,
        sort_order: Optional["aws_sdk_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_bedrock.types.list_provisioned_model_throughputs_response.ListProvisionedModelThroughputsResponse":
        """<p>Lists the Provisioned Throughputs in the account. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>A filter that returns Provisioned Throughputs created after the specified time. </p>
            creation_time_before: <p>A filter that returns Provisioned Throughputs created before the specified time. </p>
            status_equals: <p>A filter that returns Provisioned Throughputs if their statuses matches the value that you specify.</p>
            model_arn_equals: <p>A filter that returns Provisioned Throughputs whose model Amazon Resource Name (ARN) is equal to the value that you specify.</p>
            name_contains: <p>A filter that returns Provisioned Throughputs if their name contains the expression that you specify.</p>
            max_results: <p>THe maximum number of results to return in the response. If there are more results than the number you specified, the response returns a <code>nextToken</code> value. To see the next batch of results, send the <code>nextToken</code> value in another list request.</p>
            next_token: <p>If there are more results than the number you specified in the <code>maxResults</code> field, the response returns a <code>nextToken</code> value. To see the next batch of results, specify the <code>nextToken</code> value in this field.</p>
            sort_by: <p>The field by which to sort the returned list of Provisioned Throughputs.</p>
            sort_order: <p>The sort order of the results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_provisioned_model_throughputs_request.ListProvisionedModelThroughputsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_provisioned_model_throughputs_response.ListProvisionedModelThroughputsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_provisioned_model_throughputs

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_provisioned_model_throughputs.list_provisioned_model_throughputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_provisioned_model_throughputs_request.ListProvisionedModelThroughputsRequest = {}  # type: ignore[typeddict-item]
        if creation_time_after is not None:
            input["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input["status_equals"] = status_equals
        if model_arn_equals is not None:
            input["model_arn_equals"] = model_arn_equals
        if name_contains is not None:
            input["name_contains"] = name_contains
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort_by is not None:
            input["sort_by"] = sort_by
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_provisioned_model_throughput(
        self,
        provisioned_model_id: "aws_sdk_bedrock.types.provisioned_model_id.ProvisionedModelId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        desired_provisioned_model_name: Optional[
            "aws_sdk_bedrock.types.provisioned_model_name.ProvisionedModelName"
        ] = None,
        desired_model_id: Optional[
            "aws_sdk_bedrock.types.model_identifier.ModelIdentifier"
        ] = None,
    ) -> "aws_sdk_bedrock.types.update_provisioned_model_throughput_response.UpdateProvisionedModelThroughputResponse":
        """<p>Updates the name or associated model for a Provisioned Throughput. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            provisioned_model_id: <p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput to update.</p>
            desired_provisioned_model_name: <p>The new name for this Provisioned Throughput.</p>
            desired_model_id: <p>The Amazon Resource Name (ARN) of the new model to associate with this Provisioned Throughput. You can't specify this field if this Provisioned Throughput is associated with a base model.</p> <p>If this Provisioned Throughput is associated with a custom model, you can specify one of the following options:</p> <ul> <li> <p>The base model from which the custom model was customized.</p> </li> <li> <p>Another custom model that was customized from the same base model as the custom model.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.update_provisioned_model_throughput_request.UpdateProvisionedModelThroughputRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.update_provisioned_model_throughput_response.UpdateProvisionedModelThroughputResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.update_provisioned_model_throughput

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.update_provisioned_model_throughput.update_provisioned_model_throughput(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.update_provisioned_model_throughput_request.UpdateProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
        input["provisioned_model_id"] = provisioned_model_id
        if desired_provisioned_model_name is not None:
            input["desired_provisioned_model_name"] = desired_provisioned_model_name
        if desired_model_id is not None:
            input["desired_model_id"] = desired_model_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncProvisionedModelThroughputResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_provisioned_model_throughput(
        self,
        model_units: "aws_sdk_bedrock.types.positive_integer.PositiveInteger",
        provisioned_model_name: "aws_sdk_bedrock.types.provisioned_model_name.ProvisionedModelName",
        model_id: "aws_sdk_bedrock.types.model_identifier.ModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        commitment_duration: Optional[
            "aws_sdk_bedrock.types.commitment_duration.CommitmentDuration"
        ] = None,
        tags: Optional["aws_sdk_bedrock.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock.types.create_provisioned_model_throughput_response.CreateProvisionedModelThroughputResponse":
        """<p>Creates dedicated throughput for a base or custom model with the model units and for the duration that you specify. For pricing details, see <a href=\"http://aws.amazon.com/bedrock/pricing/\">Amazon Bedrock Pricing</a>. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the Amazon S3 User Guide.</p>
            model_units: <p>Number of model units to allocate. A model unit delivers a specific throughput level for the specified model. The throughput level of a model unit specifies the total number of input and output tokens that it can process and generate within a span of one minute. By default, your account has no model units for purchasing Provisioned Throughputs with commitment. You must first visit the <a href=\"https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase\">Amazon Web Services support center</a> to request MUs.</p> <p>For model unit quotas, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html#prov-thru-quotas\">Provisioned Throughput quotas</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p> <p>For more information about what an MU specifies, contact your Amazon Web Services account manager.</p>
            provisioned_model_name: <p>The name for this Provisioned Throughput.</p>
            model_id: <p>The Amazon Resource Name (ARN) or name of the model to associate with this Provisioned Throughput. For a list of models for which you can purchase Provisioned Throughput, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#prov-throughput-models\">Amazon Bedrock model IDs for purchasing Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>
            commitment_duration: <p>The commitment duration requested for the Provisioned Throughput. Billing occurs hourly and is discounted for longer commitment terms. To request a no-commit Provisioned Throughput, omit this field.</p> <p>Custom models support all levels of commitment. To see which base models support no commitment, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/pt-supported.html\">Supported regions and models for Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a> </p>
            tags: <p>Tags to associate with this Provisioned Throughput.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.create_provisioned_model_throughput_request.CreateProvisionedModelThroughputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.create_provisioned_model_throughput_response.CreateProvisionedModelThroughputResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_provisioned_model_throughput

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.create_provisioned_model_throughput.async_create_provisioned_model_throughput(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.create_provisioned_model_throughput_request.CreateProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        input["model_units"] = model_units
        input["provisioned_model_name"] = provisioned_model_name
        input["model_id"] = model_id
        if commitment_duration is not None:
            input["commitment_duration"] = commitment_duration
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_provisioned_model_throughput(
        self,
        provisioned_model_id: "aws_sdk_bedrock.types.provisioned_model_id.ProvisionedModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_provisioned_model_throughput_response.DeleteProvisionedModelThroughputResponse":
        """<p>Deletes a Provisioned Throughput. You can't delete a Provisioned Throughput before the commitment term is over. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            provisioned_model_id: <p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.delete_provisioned_model_throughput_request.DeleteProvisionedModelThroughputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.delete_provisioned_model_throughput_response.DeleteProvisionedModelThroughputResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_provisioned_model_throughput

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_provisioned_model_throughput.async_delete_provisioned_model_throughput(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_provisioned_model_throughput_request.DeleteProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
        input["provisioned_model_id"] = provisioned_model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_provisioned_model_throughput(
        self,
        provisioned_model_id: "aws_sdk_bedrock.types.provisioned_model_id.ProvisionedModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_provisioned_model_throughput_response.GetProvisionedModelThroughputResponse":
        """<p>Returns details for a Provisioned Throughput. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            provisioned_model_id: <p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_provisioned_model_throughput_request.GetProvisionedModelThroughputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_provisioned_model_throughput_response.GetProvisionedModelThroughputResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_provisioned_model_throughput

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_provisioned_model_throughput.async_get_provisioned_model_throughput(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_provisioned_model_throughput_request.GetProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
        input["provisioned_model_id"] = provisioned_model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_provisioned_model_throughputs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional[
            "aws_sdk_bedrock.types.timestamp.Timestamp"
        ] = None,
        creation_time_before: Optional[
            "aws_sdk_bedrock.types.timestamp.Timestamp"
        ] = None,
        status_equals: Optional[
            "aws_sdk_bedrock.types.provisioned_model_status.ProvisionedModelStatus"
        ] = None,
        model_arn_equals: Optional["aws_sdk_bedrock.types.model_arn.ModelArn"] = None,
        name_contains: Optional[
            "aws_sdk_bedrock.types.provisioned_model_name.ProvisionedModelName"
        ] = None,
        max_results: Optional["aws_sdk_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "aws_sdk_bedrock.types.sort_by_provisioned_models.SortByProvisionedModels"
        ] = None,
        sort_order: Optional["aws_sdk_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_bedrock.types.list_provisioned_model_throughputs_response.ListProvisionedModelThroughputsResponse":
        """<p>Lists the Provisioned Throughputs in the account. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>A filter that returns Provisioned Throughputs created after the specified time. </p>
            creation_time_before: <p>A filter that returns Provisioned Throughputs created before the specified time. </p>
            status_equals: <p>A filter that returns Provisioned Throughputs if their statuses matches the value that you specify.</p>
            model_arn_equals: <p>A filter that returns Provisioned Throughputs whose model Amazon Resource Name (ARN) is equal to the value that you specify.</p>
            name_contains: <p>A filter that returns Provisioned Throughputs if their name contains the expression that you specify.</p>
            max_results: <p>THe maximum number of results to return in the response. If there are more results than the number you specified, the response returns a <code>nextToken</code> value. To see the next batch of results, send the <code>nextToken</code> value in another list request.</p>
            next_token: <p>If there are more results than the number you specified in the <code>maxResults</code> field, the response returns a <code>nextToken</code> value. To see the next batch of results, specify the <code>nextToken</code> value in this field.</p>
            sort_by: <p>The field by which to sort the returned list of Provisioned Throughputs.</p>
            sort_order: <p>The sort order of the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_provisioned_model_throughputs_request.ListProvisionedModelThroughputsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_provisioned_model_throughputs_response.ListProvisionedModelThroughputsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_provisioned_model_throughputs

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_provisioned_model_throughputs.async_list_provisioned_model_throughputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_provisioned_model_throughputs_request.ListProvisionedModelThroughputsRequest = {}  # type: ignore[typeddict-item]
        if creation_time_after is not None:
            input["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input["status_equals"] = status_equals
        if model_arn_equals is not None:
            input["model_arn_equals"] = model_arn_equals
        if name_contains is not None:
            input["name_contains"] = name_contains
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort_by is not None:
            input["sort_by"] = sort_by
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_provisioned_model_throughput(
        self,
        provisioned_model_id: "aws_sdk_bedrock.types.provisioned_model_id.ProvisionedModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        desired_provisioned_model_name: Optional[
            "aws_sdk_bedrock.types.provisioned_model_name.ProvisionedModelName"
        ] = None,
        desired_model_id: Optional[
            "aws_sdk_bedrock.types.model_identifier.ModelIdentifier"
        ] = None,
    ) -> "aws_sdk_bedrock.types.update_provisioned_model_throughput_response.UpdateProvisionedModelThroughputResponse":
        """<p>Updates the name or associated model for a Provisioned Throughput. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            provisioned_model_id: <p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput to update.</p>
            desired_provisioned_model_name: <p>The new name for this Provisioned Throughput.</p>
            desired_model_id: <p>The Amazon Resource Name (ARN) of the new model to associate with this Provisioned Throughput. You can't specify this field if this Provisioned Throughput is associated with a base model.</p> <p>If this Provisioned Throughput is associated with a custom model, you can specify one of the following options:</p> <ul> <li> <p>The base model from which the custom model was customized.</p> </li> <li> <p>Another custom model that was customized from the same base model as the custom model.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.update_provisioned_model_throughput_request.UpdateProvisionedModelThroughputRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.update_provisioned_model_throughput_response.UpdateProvisionedModelThroughputResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.update_provisioned_model_throughput

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.update_provisioned_model_throughput.async_update_provisioned_model_throughput(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.update_provisioned_model_throughput_request.UpdateProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
        input["provisioned_model_id"] = provisioned_model_id
        if desired_provisioned_model_name is not None:
            input["desired_provisioned_model_name"] = desired_provisioned_model_name
        if desired_model_id is not None:
            input["desired_model_id"] = desired_model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
