from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Optional

import aws_sdk_cleanroomsml._auth._signers
import aws_sdk_cleanroomsml._auth._sigv4
from aws_sdk_cleanroomsml._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_model_arn
    import aws_sdk_cleanroomsml.types.audience_model_summary
    import aws_sdk_cleanroomsml.types.create_audience_model_request
    import aws_sdk_cleanroomsml.types.create_audience_model_response
    import aws_sdk_cleanroomsml.types.delete_audience_model_request
    import aws_sdk_cleanroomsml.types.get_audience_model_request
    import aws_sdk_cleanroomsml.types.get_audience_model_response
    import aws_sdk_cleanroomsml.types.kms_key_arn
    import aws_sdk_cleanroomsml.types.list_audience_models_request
    import aws_sdk_cleanroomsml.types.list_audience_models_response
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.training_dataset_arn
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class AudienceModel:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        training_dataset_arn: "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        training_data_start_time: Optional[datetime.datetime] = None,
        training_data_end_time: Optional[datetime.datetime] = None,
        kms_key_arn: Optional[
            "aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.create_audience_model_response.CreateAudienceModelResponse":
        """<p>Defines the information necessary to create an audience model. An audience model is a machine learning model that Clean Rooms ML trains to measure similarity between users. Clean Rooms ML manages training and storing the audience model. The audience model can be used in multiple calls to the <a>StartAudienceGenerationJob</a> API.</p>

        Args:
            training_data_start_time: <p>The start date and time of the training window.</p>
            training_data_end_time: <p>The end date and time of the training window.</p>
            name: <p>The name of the audience model resource.</p>
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset for this audience model.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            description: <p>The description of the audience model.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.create_audience_model_request.CreateAudienceModelRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.create_audience_model_response.CreateAudienceModelResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_audience_model

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_audience_model.create_audience_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.create_audience_model_request.CreateAudienceModelRequest = {}  # type: ignore[typeddict-item]
        if training_data_start_time is not None:
            input_["training_data_start_time"] = training_data_start_time
        if training_data_end_time is not None:
            input_["training_data_end_time"] = training_data_end_time
        input_["name"] = name
        input_["training_dataset_arn"] = training_dataset_arn
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        audience_model_arn: "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_audience_model_response.GetAudienceModelResponse":
        """<p>Returns information about an audience model</p>

        Args:
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model that you are interested in.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.get_audience_model_request.GetAudienceModelRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.get_audience_model_response.GetAudienceModelResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_audience_model

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_audience_model.get_audience_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_audience_model_request.GetAudienceModelRequest = {}  # type: ignore[typeddict-item]
        input_["audience_model_arn"] = audience_model_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        audience_model_arn: "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Specifies an audience model that you want to delete. You can't delete an audience model if there are any configured audience models that depend on the audience model.</p>

        Args:
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.delete_audience_model_request.DeleteAudienceModelRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_audience_model

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_audience_model.delete_audience_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.delete_audience_model_request.DeleteAudienceModelRequest = {}  # type: ignore[typeddict-item]
        input_["audience_model_arn"] = audience_model_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_audience_models_response.ListAudienceModelsResponse":
        """<p>Returns a list of audience models.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.list_audience_models_request.ListAudienceModelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.list_audience_models_response.ListAudienceModelsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_models

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_models.list_audience_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_audience_models_request.ListAudienceModelsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncAudienceModel:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        training_dataset_arn: "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        training_data_start_time: Optional[datetime.datetime] = None,
        training_data_end_time: Optional[datetime.datetime] = None,
        kms_key_arn: Optional[
            "aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.create_audience_model_response.CreateAudienceModelResponse":
        """<p>Defines the information necessary to create an audience model. An audience model is a machine learning model that Clean Rooms ML trains to measure similarity between users. Clean Rooms ML manages training and storing the audience model. The audience model can be used in multiple calls to the <a>StartAudienceGenerationJob</a> API.</p>

        Args:
            training_data_start_time: <p>The start date and time of the training window.</p>
            training_data_end_time: <p>The end date and time of the training window.</p>
            name: <p>The name of the audience model resource.</p>
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset for this audience model.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            description: <p>The description of the audience model.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.create_audience_model_request.CreateAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.create_audience_model_response.CreateAudienceModelResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_audience_model

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_audience_model.async_create_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.create_audience_model_request.CreateAudienceModelRequest = {}  # type: ignore[typeddict-item]
        if training_data_start_time is not None:
            input_["training_data_start_time"] = training_data_start_time
        if training_data_end_time is not None:
            input_["training_data_end_time"] = training_data_end_time
        input_["name"] = name
        input_["training_dataset_arn"] = training_dataset_arn
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        audience_model_arn: "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_audience_model_response.GetAudienceModelResponse":
        """<p>Returns information about an audience model</p>

        Args:
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model that you are interested in.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_audience_model_request.GetAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.get_audience_model_response.GetAudienceModelResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_audience_model

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_audience_model.async_get_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_audience_model_request.GetAudienceModelRequest = {}  # type: ignore[typeddict-item]
        input_["audience_model_arn"] = audience_model_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        audience_model_arn: "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Specifies an audience model that you want to delete. You can't delete an audience model if there are any configured audience models that depend on the audience model.</p>

        Args:
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.delete_audience_model_request.DeleteAudienceModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_audience_model

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_audience_model.async_delete_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.delete_audience_model_request.DeleteAudienceModelRequest = {}  # type: ignore[typeddict-item]
        input_["audience_model_arn"] = audience_model_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_audience_models_response.ListAudienceModelsResponse":
        """<p>Returns a list of audience models.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_audience_models_request.ListAudienceModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_audience_models_response.ListAudienceModelsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_models

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_models.async_list_audience_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_audience_models_request.ListAudienceModelsRequest = {}  # type: ignore[typeddict-item]
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
