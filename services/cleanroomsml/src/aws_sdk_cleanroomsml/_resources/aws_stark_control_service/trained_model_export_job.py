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
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.start_trained_model_export_job_request
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.trained_model_export_output_configuration
    import aws_sdk_cleanroomsml.types.uuid
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class TrainedModelExportJob:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        output_configuration: "aws_sdk_cleanroomsml.types.trained_model_export_output_configuration.TrainedModelExportOutputConfiguration",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        trained_model_version_identifier: Optional[
            "aws_sdk_cleanroomsml.types.uuid.UUID"
        ] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> None:
        """<p>Provides the information necessary to start a trained model export job.</p>

        Args:
            name: <p>The name of the trained model export job.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you want to export.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to export. This specifies which version of the trained model should be exported to the specified destination.</p>
            membership_identifier: <p>The membership ID of the member that is receiving the exported trained model artifacts.</p>
            output_configuration: <p>The output configuration information for the trained model export job.</p>
            description: <p>The description of the trained model export job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.start_trained_model_export_job_request.StartTrainedModelExportJobRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_trained_model_export_job

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_trained_model_export_job.start_trained_model_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.start_trained_model_export_job_request.StartTrainedModelExportJobRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["trained_model_arn"] = trained_model_arn
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )
        input_["membership_identifier"] = membership_identifier
        input_["output_configuration"] = output_configuration
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTrainedModelExportJob:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        output_configuration: "aws_sdk_cleanroomsml.types.trained_model_export_output_configuration.TrainedModelExportOutputConfiguration",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        trained_model_version_identifier: Optional[
            "aws_sdk_cleanroomsml.types.uuid.UUID"
        ] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> None:
        """<p>Provides the information necessary to start a trained model export job.</p>

        Args:
            name: <p>The name of the trained model export job.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you want to export.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to export. This specifies which version of the trained model should be exported to the specified destination.</p>
            membership_identifier: <p>The membership ID of the member that is receiving the exported trained model artifacts.</p>
            output_configuration: <p>The output configuration information for the trained model export job.</p>
            description: <p>The description of the trained model export job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.start_trained_model_export_job_request.StartTrainedModelExportJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_trained_model_export_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_trained_model_export_job.async_start_trained_model_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.start_trained_model_export_job_request.StartTrainedModelExportJobRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["trained_model_arn"] = trained_model_arn
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )
        input_["membership_identifier"] = membership_identifier
        input_["output_configuration"] = output_configuration
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
