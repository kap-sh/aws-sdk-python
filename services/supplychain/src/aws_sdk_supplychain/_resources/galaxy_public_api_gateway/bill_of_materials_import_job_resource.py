from typing import TYPE_CHECKING, Optional

import aws_sdk_supplychain._auth._signers
import aws_sdk_supplychain._auth._sigv4
from aws_sdk_supplychain._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.client_token
    import aws_sdk_supplychain.types.configuration_s3_uri
    import aws_sdk_supplychain.types.create_bill_of_materials_import_job_request
    import aws_sdk_supplychain.types.create_bill_of_materials_import_job_response
    import aws_sdk_supplychain.types.get_bill_of_materials_import_job_request
    import aws_sdk_supplychain.types.get_bill_of_materials_import_job_response
    import aws_sdk_supplychain.types.uuid
    from aws_sdk_supplychain._services.async_supply_chain import (
        AsyncSupplyChainClient,
        AsyncSupplyChainClientConfig,
    )
    from aws_sdk_supplychain._services.supply_chain import (
        SupplyChainClient,
        SupplyChainClientConfig,
    )


class BillOfMaterialsImportJobResource:
    def __init__(self, service: SupplyChainClient) -> None:
        self._service = service

    def create(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        s3uri: "aws_sdk_supplychain.types.configuration_s3_uri.ConfigurationS3Uri",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        client_token: Optional[
            "aws_sdk_supplychain.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_supplychain.types.create_bill_of_materials_import_job_response.CreateBillOfMaterialsImportJobResponse":
        """<p>CreateBillOfMaterialsImportJob creates an import job for the Product Bill Of Materials (BOM) entity. For information on the product_bom entity, see the AWS Supply Chain User Guide.</p> <p>The CSV file must be located in an Amazon S3 location accessible to AWS Supply Chain. It is recommended to use the same Amazon S3 bucket created during your AWS Supply Chain instance creation.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            s3uri: <p>The S3 URI of the CSV file to be imported. The bucket must grant permissions for AWS Supply Chain to read the file.</p>
            client_token: <p>An idempotency token ensures the API request is only completed no more than once. This way, retrying the request will not trigger the operation multiple times. A client token is a unique, case-sensitive string of 33 to 128 ASCII characters. To make an idempotent API request, specify a client token in the request. You should not reuse the same client token for other requests. If you retry a successful request with the same client token, the request will succeed with no further actions being taken, and you will receive the same API response as the original successful request.</p>

        Examples:
            Invoke CreateBillOfMaterialsImportJob

            >>> client.create(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', s3uri='s3://mybucketname/pathelemene/file.csv', client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.create_bill_of_materials_import_job_request.CreateBillOfMaterialsImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.create_bill_of_materials_import_job_response.CreateBillOfMaterialsImportJobResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_bill_of_materials_import_job

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_bill_of_materials_import_job.create_bill_of_materials_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.create_bill_of_materials_import_job_request.CreateBillOfMaterialsImportJobRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["s3uri"] = s3uri
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        job_id: "aws_sdk_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.get_bill_of_materials_import_job_response.GetBillOfMaterialsImportJobResponse":
        """<p>Get status and details of a BillOfMaterialsImportJob.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            job_id: <p>The BillOfMaterialsImportJob identifier.</p>

        Examples:
            Invoke GetBillOfMaterialsImportJob for a successful job

            >>> client.read(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', job_id='f79b359b-1515-4436-a3bf-bae7b33e47b4')
            Invoke GetBillOfMaterialsImportJob for an in-progress job

            >>> client.read(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', job_id='f79b359b-1515-4436-a3bf-bae7b33e47b4')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.get_bill_of_materials_import_job_request.GetBillOfMaterialsImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.get_bill_of_materials_import_job_response.GetBillOfMaterialsImportJobResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_bill_of_materials_import_job

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_bill_of_materials_import_job.get_bill_of_materials_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.get_bill_of_materials_import_job_request.GetBillOfMaterialsImportJobRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncBillOfMaterialsImportJobResource:
    def __init__(self, service: AsyncSupplyChainClient) -> None:
        self._service = service

    async def create(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        s3uri: "aws_sdk_supplychain.types.configuration_s3_uri.ConfigurationS3Uri",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        client_token: Optional[
            "aws_sdk_supplychain.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_supplychain.types.create_bill_of_materials_import_job_response.CreateBillOfMaterialsImportJobResponse":
        """<p>CreateBillOfMaterialsImportJob creates an import job for the Product Bill Of Materials (BOM) entity. For information on the product_bom entity, see the AWS Supply Chain User Guide.</p> <p>The CSV file must be located in an Amazon S3 location accessible to AWS Supply Chain. It is recommended to use the same Amazon S3 bucket created during your AWS Supply Chain instance creation.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            s3uri: <p>The S3 URI of the CSV file to be imported. The bucket must grant permissions for AWS Supply Chain to read the file.</p>
            client_token: <p>An idempotency token ensures the API request is only completed no more than once. This way, retrying the request will not trigger the operation multiple times. A client token is a unique, case-sensitive string of 33 to 128 ASCII characters. To make an idempotent API request, specify a client token in the request. You should not reuse the same client token for other requests. If you retry a successful request with the same client token, the request will succeed with no further actions being taken, and you will receive the same API response as the original successful request.</p>

        Examples:
            Invoke CreateBillOfMaterialsImportJob

            >>> await client.create(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', s3uri='s3://mybucketname/pathelemene/file.csv', client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.create_bill_of_materials_import_job_request.CreateBillOfMaterialsImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.create_bill_of_materials_import_job_response.CreateBillOfMaterialsImportJobResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_bill_of_materials_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_bill_of_materials_import_job.async_create_bill_of_materials_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.create_bill_of_materials_import_job_request.CreateBillOfMaterialsImportJobRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["s3uri"] = s3uri
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        job_id: "aws_sdk_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.get_bill_of_materials_import_job_response.GetBillOfMaterialsImportJobResponse":
        """<p>Get status and details of a BillOfMaterialsImportJob.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            job_id: <p>The BillOfMaterialsImportJob identifier.</p>

        Examples:
            Invoke GetBillOfMaterialsImportJob for a successful job

            >>> await client.read(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', job_id='f79b359b-1515-4436-a3bf-bae7b33e47b4')
            Invoke GetBillOfMaterialsImportJob for an in-progress job

            >>> await client.read(instance_id='60f82bbd-71f7-4fcd-a941-472f574c5243', job_id='f79b359b-1515-4436-a3bf-bae7b33e47b4')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.get_bill_of_materials_import_job_request.GetBillOfMaterialsImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.get_bill_of_materials_import_job_response.GetBillOfMaterialsImportJobResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_bill_of_materials_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_bill_of_materials_import_job.async_get_bill_of_materials_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_supplychain.types.get_bill_of_materials_import_job_request.GetBillOfMaterialsImportJobRequest = {}  # type: ignore[typeddict-item]
        input["instance_id"] = instance_id
        input["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
