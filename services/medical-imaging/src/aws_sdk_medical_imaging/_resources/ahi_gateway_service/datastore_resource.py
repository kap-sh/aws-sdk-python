from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_medical_imaging._auth._signers
import aws_sdk_medical_imaging._auth._sigv4
from aws_sdk_medical_imaging._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.client_token
    import aws_sdk_medical_imaging.types.create_datastore_request
    import aws_sdk_medical_imaging.types.create_datastore_response
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.datastore_name
    import aws_sdk_medical_imaging.types.datastore_status
    import aws_sdk_medical_imaging.types.datastore_summary
    import aws_sdk_medical_imaging.types.delete_datastore_request
    import aws_sdk_medical_imaging.types.delete_datastore_response
    import aws_sdk_medical_imaging.types.get_datastore_request
    import aws_sdk_medical_imaging.types.get_datastore_response
    import aws_sdk_medical_imaging.types.kms_key_arn
    import aws_sdk_medical_imaging.types.lambda_arn
    import aws_sdk_medical_imaging.types.list_datastores_request
    import aws_sdk_medical_imaging.types.list_datastores_response
    import aws_sdk_medical_imaging.types.lossless_storage_format
    import aws_sdk_medical_imaging.types.next_token
    import aws_sdk_medical_imaging.types.tag_map
    from aws_sdk_medical_imaging._services.async_medical_imaging import (
        AsyncMedicalImagingClient,
        AsyncMedicalImagingClientConfig,
    )
    from aws_sdk_medical_imaging._services.medical_imaging import (
        MedicalImagingClient,
        MedicalImagingClientConfig,
    )


class DatastoreResource:
    def __init__(self, service: MedicalImagingClient) -> None:
        self._service = service

    def create(
        self,
        client_token: "aws_sdk_medical_imaging.types.client_token.ClientToken",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        datastore_name: Optional[
            "aws_sdk_medical_imaging.types.datastore_name.DatastoreName"
        ] = None,
        tags: Optional["aws_sdk_medical_imaging.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional[
            "aws_sdk_medical_imaging.types.kms_key_arn.KmsKeyArn"
        ] = None,
        lambda_authorizer_arn: Optional[
            "aws_sdk_medical_imaging.types.lambda_arn.LambdaArn"
        ] = None,
        lossless_storage_format: Optional[
            "aws_sdk_medical_imaging.types.lossless_storage_format.LosslessStorageFormat"
        ] = None,
    ) -> "aws_sdk_medical_imaging.types.create_datastore_response.CreateDatastoreResponse":
        """<p>Create a data store.</p>

        Args:
            datastore_name: <p>The data store name.</p>
            client_token: <p>A unique identifier for API idempotency.</p>
            tags: <p>The tags provided when creating a data store.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.</p>
            lambda_authorizer_arn: <p>The ARN of the authorizer's Lambda function.</p>
            lossless_storage_format: <p>The lossless storage format for the datastore.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.create_datastore_request.CreateDatastoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.create_datastore_response.CreateDatastoreResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.create_datastore

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.create_datastore.create_datastore(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.create_datastore_request.CreateDatastoreRequest = {}  # type: ignore[typeddict-item]
        if datastore_name is not None:
            input_["datastore_name"] = datastore_name
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if lambda_authorizer_arn is not None:
            input_["lambda_authorizer_arn"] = lambda_authorizer_arn
        if lossless_storage_format is not None:
            input_["lossless_storage_format"] = lossless_storage_format

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.get_datastore_response.GetDatastoreResponse":
        """<p>Get data store properties.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.get_datastore_request.GetDatastoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.get_datastore_response.GetDatastoreResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.get_datastore

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.get_datastore.get_datastore(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.get_datastore_request.GetDatastoreRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.delete_datastore_response.DeleteDatastoreResponse":
        """<p>Delete a data store.</p> <note> <p>Before a data store can be deleted, you must first delete all image sets within it.</p> </note>

        Args:
            datastore_id: <p>The data store identifier.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.delete_datastore_request.DeleteDatastoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.delete_datastore_response.DeleteDatastoreResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.delete_datastore

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.delete_datastore.delete_datastore(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.delete_datastore_request.DeleteDatastoreRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        datastore_status: Optional[
            "aws_sdk_medical_imaging.types.datastore_status.DatastoreStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> (
        "aws_sdk_medical_imaging.types.list_datastores_response.ListDatastoresResponse"
    ):
        """<p>List data stores.</p>

        Args:
            datastore_status: <p>The data store status.</p>
            next_token: <p>The pagination token used to request the list of data stores on the next page.</p>
            max_results: <p>Valid Range: Minimum value of 1. Maximum value of 50.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.list_datastores_request.ListDatastoresRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.list_datastores_response.ListDatastoresResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.list_datastores

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.list_datastores.list_datastores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.list_datastores_request.ListDatastoresRequest = {}  # type: ignore[typeddict-item]
        if datastore_status is not None:
            input_["datastore_status"] = datastore_status
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


class AsyncDatastoreResource:
    def __init__(self, service: AsyncMedicalImagingClient) -> None:
        self._service = service

    async def create(
        self,
        client_token: "aws_sdk_medical_imaging.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
        datastore_name: Optional[
            "aws_sdk_medical_imaging.types.datastore_name.DatastoreName"
        ] = None,
        tags: Optional["aws_sdk_medical_imaging.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional[
            "aws_sdk_medical_imaging.types.kms_key_arn.KmsKeyArn"
        ] = None,
        lambda_authorizer_arn: Optional[
            "aws_sdk_medical_imaging.types.lambda_arn.LambdaArn"
        ] = None,
        lossless_storage_format: Optional[
            "aws_sdk_medical_imaging.types.lossless_storage_format.LosslessStorageFormat"
        ] = None,
    ) -> "aws_sdk_medical_imaging.types.create_datastore_response.CreateDatastoreResponse":
        """<p>Create a data store.</p>

        Args:
            datastore_name: <p>The data store name.</p>
            client_token: <p>A unique identifier for API idempotency.</p>
            tags: <p>The tags provided when creating a data store.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.</p>
            lambda_authorizer_arn: <p>The ARN of the authorizer's Lambda function.</p>
            lossless_storage_format: <p>The lossless storage format for the datastore.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.create_datastore_request.CreateDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.create_datastore_response.CreateDatastoreResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.create_datastore

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.create_datastore.async_create_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.create_datastore_request.CreateDatastoreRequest = {}  # type: ignore[typeddict-item]
        if datastore_name is not None:
            input_["datastore_name"] = datastore_name
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if lambda_authorizer_arn is not None:
            input_["lambda_authorizer_arn"] = lambda_authorizer_arn
        if lossless_storage_format is not None:
            input_["lossless_storage_format"] = lossless_storage_format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.get_datastore_response.GetDatastoreResponse":
        """<p>Get data store properties.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.get_datastore_request.GetDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.get_datastore_response.GetDatastoreResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.get_datastore

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.get_datastore.async_get_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.get_datastore_request.GetDatastoreRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.delete_datastore_response.DeleteDatastoreResponse":
        """<p>Delete a data store.</p> <note> <p>Before a data store can be deleted, you must first delete all image sets within it.</p> </note>

        Args:
            datastore_id: <p>The data store identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.delete_datastore_request.DeleteDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.delete_datastore_response.DeleteDatastoreResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.delete_datastore

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.delete_datastore.async_delete_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.delete_datastore_request.DeleteDatastoreRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
        datastore_status: Optional[
            "aws_sdk_medical_imaging.types.datastore_status.DatastoreStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> (
        "aws_sdk_medical_imaging.types.list_datastores_response.ListDatastoresResponse"
    ):
        """<p>List data stores.</p>

        Args:
            datastore_status: <p>The data store status.</p>
            next_token: <p>The pagination token used to request the list of data stores on the next page.</p>
            max_results: <p>Valid Range: Minimum value of 1. Maximum value of 50.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.list_datastores_request.ListDatastoresRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.list_datastores_response.ListDatastoresResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.list_datastores

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.list_datastores.async_list_datastores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.list_datastores_request.ListDatastoresRequest = {}  # type: ignore[typeddict-item]
        if datastore_status is not None:
            input_["datastore_status"] = datastore_status
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
