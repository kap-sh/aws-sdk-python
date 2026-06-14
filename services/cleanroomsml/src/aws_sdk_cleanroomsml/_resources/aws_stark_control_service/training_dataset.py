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
    import aws_sdk_cleanroomsml.types.create_training_dataset_request
    import aws_sdk_cleanroomsml.types.create_training_dataset_response
    import aws_sdk_cleanroomsml.types.dataset_list
    import aws_sdk_cleanroomsml.types.delete_training_dataset_request
    import aws_sdk_cleanroomsml.types.get_training_dataset_request
    import aws_sdk_cleanroomsml.types.get_training_dataset_response
    import aws_sdk_cleanroomsml.types.iam_role_arn
    import aws_sdk_cleanroomsml.types.list_training_datasets_request
    import aws_sdk_cleanroomsml.types.list_training_datasets_response
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.training_dataset_arn
    import aws_sdk_cleanroomsml.types.training_dataset_summary
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class TrainingDataset:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        role_arn: "aws_sdk_cleanroomsml.types.iam_role_arn.IamRoleArn",
        training_data: "aws_sdk_cleanroomsml.types.dataset_list.DatasetList",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.create_training_dataset_response.CreateTrainingDatasetResponse":
        """<p>Defines the information necessary to create a training dataset. In Clean Rooms ML, the <code>TrainingDataset</code> is metadata that points to a Glue table, which is read only during <code>AudienceModel</code> creation.</p>

        Args:
            name: <p>The name of the training dataset. This name must be unique in your account and region.</p>
            role_arn: <p>The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the <code>dataSource</code> field of each dataset.</p> <p>Passing a role across AWS accounts is not allowed. If you pass a role that isn't in your account, you get an <code>AccessDeniedException</code> error.</p>
            training_data: <p>An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema. You must provide a role that has read access to these tables.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            description: <p>The description of the training dataset.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.create_training_dataset_request.CreateTrainingDatasetRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.create_training_dataset_response.CreateTrainingDatasetResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_training_dataset

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_training_dataset.create_training_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.create_training_dataset_request.CreateTrainingDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["role_arn"] = role_arn
        input_["training_data"] = training_data
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
        training_dataset_arn: "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_training_dataset_response.GetTrainingDatasetResponse":
        """<p>Returns information about a training dataset.</p>

        Args:
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset that you are interested in.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.get_training_dataset_request.GetTrainingDatasetRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.get_training_dataset_response.GetTrainingDatasetResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_training_dataset

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_training_dataset.get_training_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_training_dataset_request.GetTrainingDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["training_dataset_arn"] = training_dataset_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        training_dataset_arn: "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Specifies a training dataset that you want to delete. You can't delete a training dataset if there are any audience models that depend on the training dataset. In Clean Rooms ML, the <code>TrainingDataset</code> is metadata that points to a Glue table, which is read only during <code>AudienceModel</code> creation. This action deletes the metadata.</p>

        Args:
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.delete_training_dataset_request.DeleteTrainingDatasetRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_training_dataset

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_training_dataset.delete_training_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.delete_training_dataset_request.DeleteTrainingDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["training_dataset_arn"] = training_dataset_arn

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
    ) -> "aws_sdk_cleanroomsml.types.list_training_datasets_response.ListTrainingDatasetsResponse":
        """<p>Returns a list of training datasets.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.list_training_datasets_request.ListTrainingDatasetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.list_training_datasets_response.ListTrainingDatasetsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_training_datasets

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_training_datasets.list_training_datasets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_training_datasets_request.ListTrainingDatasetsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncTrainingDataset:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        role_arn: "aws_sdk_cleanroomsml.types.iam_role_arn.IamRoleArn",
        training_data: "aws_sdk_cleanroomsml.types.dataset_list.DatasetList",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.create_training_dataset_response.CreateTrainingDatasetResponse":
        """<p>Defines the information necessary to create a training dataset. In Clean Rooms ML, the <code>TrainingDataset</code> is metadata that points to a Glue table, which is read only during <code>AudienceModel</code> creation.</p>

        Args:
            name: <p>The name of the training dataset. This name must be unique in your account and region.</p>
            role_arn: <p>The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the <code>dataSource</code> field of each dataset.</p> <p>Passing a role across AWS accounts is not allowed. If you pass a role that isn't in your account, you get an <code>AccessDeniedException</code> error.</p>
            training_data: <p>An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema. You must provide a role that has read access to these tables.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            description: <p>The description of the training dataset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.create_training_dataset_request.CreateTrainingDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.create_training_dataset_response.CreateTrainingDatasetResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_training_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_training_dataset.async_create_training_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.create_training_dataset_request.CreateTrainingDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["role_arn"] = role_arn
        input_["training_data"] = training_data
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
        training_dataset_arn: "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_training_dataset_response.GetTrainingDatasetResponse":
        """<p>Returns information about a training dataset.</p>

        Args:
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset that you are interested in.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_training_dataset_request.GetTrainingDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.get_training_dataset_response.GetTrainingDatasetResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_training_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_training_dataset.async_get_training_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_training_dataset_request.GetTrainingDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["training_dataset_arn"] = training_dataset_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        training_dataset_arn: "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Specifies a training dataset that you want to delete. You can't delete a training dataset if there are any audience models that depend on the training dataset. In Clean Rooms ML, the <code>TrainingDataset</code> is metadata that points to a Glue table, which is read only during <code>AudienceModel</code> creation. This action deletes the metadata.</p>

        Args:
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.delete_training_dataset_request.DeleteTrainingDatasetRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_training_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_training_dataset.async_delete_training_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.delete_training_dataset_request.DeleteTrainingDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["training_dataset_arn"] = training_dataset_arn

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
    ) -> "aws_sdk_cleanroomsml.types.list_training_datasets_response.ListTrainingDatasetsResponse":
        """<p>Returns a list of training datasets.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_training_datasets_request.ListTrainingDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_training_datasets_response.ListTrainingDatasetsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_training_datasets

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_training_datasets.async_list_training_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_training_datasets_request.ListTrainingDatasetsRequest = {}  # type: ignore[typeddict-item]
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
