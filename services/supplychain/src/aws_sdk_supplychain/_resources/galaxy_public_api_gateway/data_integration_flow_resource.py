from __future__ import annotations

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
    import aws_sdk_supplychain.types.create_data_integration_flow_request
    import aws_sdk_supplychain.types.create_data_integration_flow_response
    import aws_sdk_supplychain.types.data_integration_flow
    import aws_sdk_supplychain.types.data_integration_flow_max_results
    import aws_sdk_supplychain.types.data_integration_flow_name
    import aws_sdk_supplychain.types.data_integration_flow_next_token
    import aws_sdk_supplychain.types.data_integration_flow_source_list
    import aws_sdk_supplychain.types.data_integration_flow_target
    import aws_sdk_supplychain.types.data_integration_flow_transformation
    import aws_sdk_supplychain.types.delete_data_integration_flow_request
    import aws_sdk_supplychain.types.delete_data_integration_flow_response
    import aws_sdk_supplychain.types.get_data_integration_flow_request
    import aws_sdk_supplychain.types.get_data_integration_flow_response
    import aws_sdk_supplychain.types.list_data_integration_flows_request
    import aws_sdk_supplychain.types.list_data_integration_flows_response
    import aws_sdk_supplychain.types.tag_map
    import aws_sdk_supplychain.types.update_data_integration_flow_request
    import aws_sdk_supplychain.types.update_data_integration_flow_response
    import aws_sdk_supplychain.types.uuid
    from aws_sdk_supplychain._services.async_supply_chain import (
        AsyncSupplyChainClient,
        AsyncSupplyChainClientConfig,
    )
    from aws_sdk_supplychain._services.supply_chain import (
        SupplyChainClient,
        SupplyChainClientConfig,
    )


class DataIntegrationFlowResource:
    def __init__(self, service: SupplyChainClient) -> None:
        self._service = service

    def put(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        sources: "aws_sdk_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList",
        transformation: "aws_sdk_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation",
        target: "aws_sdk_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        tags: Optional["aws_sdk_supplychain.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_supplychain.types.create_data_integration_flow_response.CreateDataIntegrationFlowResponse":
        """<p>Enables you to programmatically create a data pipeline to ingest data from source systems such as Amazon S3 buckets, to a predefined Amazon Web Services Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>Name of the DataIntegrationFlow.</p>
            sources: <p>The source configurations for DataIntegrationFlow.</p>
            transformation: <p>The transformation configurations for DataIntegrationFlow.</p>
            target: <p>The target configurations for DataIntegrationFlow.</p>
            tags: <p>The tags of the DataIntegrationFlow to be created</p>

        Examples:
            Successful CreateDataIntegrationFlow for s3 to dataset flow

            >>> client.put(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow', sources=[{'sourceType': 'S3', 'sourceName': 'testSourceName', 's3Source': {'bucketName': 'aws-supply-chain-data-b8c7bb28-a576-4334-b481-6d6e8e47371f', 'prefix': 'example-prefix'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT * FROM testSourceName'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset'}}, tags={'tagKey1': 'tagValue1'})
            Successful CreateDataIntegrationFlow for dataset to dataset flow

            >>> client.put(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='trading-partner', sources=[{'sourceType': 'DATASET', 'sourceName': 'testSourceName1', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset1'}}, {'sourceType': 'DATASET', 'sourceName': 'testSourceName2', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset2'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT S1.id AS id, S1.poc_org_unit_description AS description, S1.company_id AS company_id, S1.tpartner_type AS tpartner_type, S1.geo_id AS geo_id, S1.eff_start_date AS eff_start_date, S1.eff_end_date AS eff_end_date FROM testSourceName1 AS S1 LEFT JOIN testSourceName2 as S2 ON S1.id=S2.id'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/asc/datasets/trading_partner', 'options': {'loadType': 'REPLACE', 'dedupeRecords': True, 'dedupeStrategy': {'type': 'FIELD_PRIORITY', 'fieldPriority': {'fields': [{'name': 'eff_start_date', 'sortOrder': 'DESC'}]}}}}}, tags={'tagKey1': 'tagValue1'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.create_data_integration_flow_response.CreateDataIntegrationFlowResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_integration_flow

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_integration_flow.create_data_integration_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["name"] = name
        input_["sources"] = sources
        input_["transformation"] = transformation
        input_["target"] = target
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse":
        """<p>Enables you to programmatically view a specific data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow created.</p>

        Examples:
            Successful GetDataIntegrationFlow

            >>> client.read(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.get_data_integration_flow_request.GetDataIntegrationFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow.get_data_integration_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_supplychain.types.get_data_integration_flow_request.GetDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        sources: Optional[
            "aws_sdk_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
        ] = None,
        transformation: Optional[
            "aws_sdk_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
        ] = None,
        target: Optional[
            "aws_sdk_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
        ] = None,
    ) -> "aws_sdk_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse":
        """<p>Enables you to programmatically update an existing data pipeline to ingest data from the source systems such as, Amazon S3 buckets, to a predefined Amazon Web Services Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow to be updated.</p>
            sources: <p>The new source configurations for the DataIntegrationFlow.</p>
            transformation: <p>The new transformation configurations for the DataIntegrationFlow.</p>
            target: <p>The new target configurations for the DataIntegrationFlow.</p>

        Examples:
            Successful UpdateDataIntegrationFlow for s3 to dataset flow to update SQL transformation

            >>> client.update(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow', sources=[{'sourceType': 'S3', 'sourceName': 'testSourceName', 's3Source': {'bucketName': 'aws-supply-chain-data-b8c7bb28-a576-4334-b481-6d6e8e47371f', 'prefix': 'example-prefix'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': "SELECT connection_id, bukrs AS id, txtmd AS description FROM testSourceName WHERE langu = 'E'"}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset'}})
            Successful UpdateDataIntegrationFlow for dataset to dataset flow to update sources

            >>> client.update(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='trading-partner', sources=[{'sourceType': 'DATASET', 'sourceName': 'testSourceName1', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset1'}}, {'sourceType': 'DATASET', 'sourceName': 'testSourceName2', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset2_updated'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT S1.id AS id, S1.poc_org_unit_description AS description, S1.company_id AS company_id, S1.tpartner_type AS tpartner_type, S1.geo_id AS geo_id, S1.eff_start_date AS eff_start_date, S1.eff_end_date AS eff_end_date FROM testSourceName1 AS S1 LEFT JOIN testSourceName2 as S2 ON S1.id=S2.id'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/asc/datasets/trading_partner', 'options': {'loadType': 'REPLACE', 'dedupeRecords': True, 'dedupeStrategy': {'type': 'FIELD_PRIORITY', 'fieldPriority': {'fields': [{'name': 'eff_start_date', 'sortOrder': 'ASC'}]}}}}})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_integration_flow

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_integration_flow.update_data_integration_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["name"] = name
        if sources is not None:
            input_["sources"] = sources
        if transformation is not None:
            input_["transformation"] = transformation
        if target is not None:
            input_["target"] = target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.delete_data_integration_flow_response.DeleteDataIntegrationFlowResponse":
        """<p>Enable you to programmatically delete an existing data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow to be deleted.</p>

        Examples:
            Successful DeleteDataIntegrationFlow

            >>> client.delete(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.delete_data_integration_flow_request.DeleteDataIntegrationFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.delete_data_integration_flow_response.DeleteDataIntegrationFlowResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_integration_flow

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_integration_flow.delete_data_integration_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_supplychain.types.delete_data_integration_flow_request.DeleteDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        next_token: Optional[
            "aws_sdk_supplychain.types.data_integration_flow_next_token.DataIntegrationFlowNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_supplychain.types.data_integration_flow_max_results.DataIntegrationFlowMaxResults"
        ] = None,
    ) -> "aws_sdk_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse":
        """<p>Enables you to programmatically list all data pipelines for the provided Amazon Web Services Supply Chain instance.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            next_token: <p>The pagination token to fetch the next page of the DataIntegrationFlows.</p>
            max_results: <p>Specify the maximum number of DataIntegrationFlows to fetch in one paginated request.</p>

        Examples:
            Successful ListDataIntegrationFlow

            >>> client.list(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_supplychain.types.list_data_integration_flows_request.ListDataIntegrationFlowsRequest]",
        ) -> OperationResponse[
            "aws_sdk_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flows

            output, http_response = (
                aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flows.list_data_integration_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_supplychain.types.list_data_integration_flows_request.ListDataIntegrationFlowsRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
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


class AsyncDataIntegrationFlowResource:
    def __init__(self, service: AsyncSupplyChainClient) -> None:
        self._service = service

    async def put(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        sources: "aws_sdk_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList",
        transformation: "aws_sdk_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation",
        target: "aws_sdk_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        tags: Optional["aws_sdk_supplychain.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_supplychain.types.create_data_integration_flow_response.CreateDataIntegrationFlowResponse":
        """<p>Enables you to programmatically create a data pipeline to ingest data from source systems such as Amazon S3 buckets, to a predefined Amazon Web Services Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>Name of the DataIntegrationFlow.</p>
            sources: <p>The source configurations for DataIntegrationFlow.</p>
            transformation: <p>The transformation configurations for DataIntegrationFlow.</p>
            target: <p>The target configurations for DataIntegrationFlow.</p>
            tags: <p>The tags of the DataIntegrationFlow to be created</p>

        Examples:
            Successful CreateDataIntegrationFlow for s3 to dataset flow

            >>> await client.put(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow', sources=[{'sourceType': 'S3', 'sourceName': 'testSourceName', 's3Source': {'bucketName': 'aws-supply-chain-data-b8c7bb28-a576-4334-b481-6d6e8e47371f', 'prefix': 'example-prefix'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT * FROM testSourceName'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset'}}, tags={'tagKey1': 'tagValue1'})
            Successful CreateDataIntegrationFlow for dataset to dataset flow

            >>> await client.put(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='trading-partner', sources=[{'sourceType': 'DATASET', 'sourceName': 'testSourceName1', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset1'}}, {'sourceType': 'DATASET', 'sourceName': 'testSourceName2', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset2'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT S1.id AS id, S1.poc_org_unit_description AS description, S1.company_id AS company_id, S1.tpartner_type AS tpartner_type, S1.geo_id AS geo_id, S1.eff_start_date AS eff_start_date, S1.eff_end_date AS eff_end_date FROM testSourceName1 AS S1 LEFT JOIN testSourceName2 as S2 ON S1.id=S2.id'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/asc/datasets/trading_partner', 'options': {'loadType': 'REPLACE', 'dedupeRecords': True, 'dedupeStrategy': {'type': 'FIELD_PRIORITY', 'fieldPriority': {'fields': [{'name': 'eff_start_date', 'sortOrder': 'DESC'}]}}}}}, tags={'tagKey1': 'tagValue1'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.create_data_integration_flow_response.CreateDataIntegrationFlowResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_integration_flow

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.create_data_integration_flow.async_create_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_supplychain.types.create_data_integration_flow_request.CreateDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["name"] = name
        input_["sources"] = sources
        input_["transformation"] = transformation
        input_["target"] = target
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse":
        """<p>Enables you to programmatically view a specific data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow created.</p>

        Examples:
            Successful GetDataIntegrationFlow

            >>> await client.read(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.get_data_integration_flow_request.GetDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.get_data_integration_flow_response.GetDataIntegrationFlowResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow.async_get_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_supplychain.types.get_data_integration_flow_request.GetDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        sources: Optional[
            "aws_sdk_supplychain.types.data_integration_flow_source_list.DataIntegrationFlowSourceList"
        ] = None,
        transformation: Optional[
            "aws_sdk_supplychain.types.data_integration_flow_transformation.DataIntegrationFlowTransformation"
        ] = None,
        target: Optional[
            "aws_sdk_supplychain.types.data_integration_flow_target.DataIntegrationFlowTarget"
        ] = None,
    ) -> "aws_sdk_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse":
        """<p>Enables you to programmatically update an existing data pipeline to ingest data from the source systems such as, Amazon S3 buckets, to a predefined Amazon Web Services Supply Chain dataset (product, inbound_order) or a temporary dataset along with the data transformation query provided with the API.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow to be updated.</p>
            sources: <p>The new source configurations for the DataIntegrationFlow.</p>
            transformation: <p>The new transformation configurations for the DataIntegrationFlow.</p>
            target: <p>The new target configurations for the DataIntegrationFlow.</p>

        Examples:
            Successful UpdateDataIntegrationFlow for s3 to dataset flow to update SQL transformation

            >>> await client.update(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow', sources=[{'sourceType': 'S3', 'sourceName': 'testSourceName', 's3Source': {'bucketName': 'aws-supply-chain-data-b8c7bb28-a576-4334-b481-6d6e8e47371f', 'prefix': 'example-prefix'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': "SELECT connection_id, bukrs AS id, txtmd AS description FROM testSourceName WHERE langu = 'E'"}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset'}})
            Successful UpdateDataIntegrationFlow for dataset to dataset flow to update sources

            >>> await client.update(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='trading-partner', sources=[{'sourceType': 'DATASET', 'sourceName': 'testSourceName1', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset1'}}, {'sourceType': 'DATASET', 'sourceName': 'testSourceName2', 'datasetSource': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/default/datasets/my_staging_dataset2_updated'}}], transformation={'transformationType': 'SQL', 'sqlTransformation': {'query': 'SELECT S1.id AS id, S1.poc_org_unit_description AS description, S1.company_id AS company_id, S1.tpartner_type AS tpartner_type, S1.geo_id AS geo_id, S1.eff_start_date AS eff_start_date, S1.eff_end_date AS eff_end_date FROM testSourceName1 AS S1 LEFT JOIN testSourceName2 as S2 ON S1.id=S2.id'}}, target={'targetType': 'DATASET', 'datasetTarget': {'datasetIdentifier': 'arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/namespaces/asc/datasets/trading_partner', 'options': {'loadType': 'REPLACE', 'dedupeRecords': True, 'dedupeStrategy': {'type': 'FIELD_PRIORITY', 'fieldPriority': {'fields': [{'name': 'eff_start_date', 'sortOrder': 'ASC'}]}}}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.update_data_integration_flow_response.UpdateDataIntegrationFlowResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_integration_flow

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.update_data_integration_flow.async_update_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_supplychain.types.update_data_integration_flow_request.UpdateDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["name"] = name
        if sources is not None:
            input_["sources"] = sources
        if transformation is not None:
            input_["transformation"] = transformation
        if target is not None:
            input_["target"] = target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        name: "aws_sdk_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
    ) -> "aws_sdk_supplychain.types.delete_data_integration_flow_response.DeleteDataIntegrationFlowResponse":
        """<p>Enable you to programmatically delete an existing data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            name: <p>The name of the DataIntegrationFlow to be deleted.</p>

        Examples:
            Successful DeleteDataIntegrationFlow

            >>> await client.delete(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d', name='testStagingFlow')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.delete_data_integration_flow_request.DeleteDataIntegrationFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.delete_data_integration_flow_response.DeleteDataIntegrationFlowResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_integration_flow

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.delete_data_integration_flow.async_delete_data_integration_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_supplychain.types.delete_data_integration_flow_request.DeleteDataIntegrationFlowRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        instance_id: "aws_sdk_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSupplyChainClientConfig] = None,
        next_token: Optional[
            "aws_sdk_supplychain.types.data_integration_flow_next_token.DataIntegrationFlowNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_supplychain.types.data_integration_flow_max_results.DataIntegrationFlowMaxResults"
        ] = None,
    ) -> "aws_sdk_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse":
        """<p>Enables you to programmatically list all data pipelines for the provided Amazon Web Services Supply Chain instance.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            next_token: <p>The pagination token to fetch the next page of the DataIntegrationFlows.</p>
            max_results: <p>Specify the maximum number of DataIntegrationFlows to fetch in one paginated request.</p>

        Examples:
            Successful ListDataIntegrationFlow

            >>> await client.list(instance_id='8850c54e-e187-4fa7-89d4-6370f165174d')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_supplychain.types.list_data_integration_flows_request.ListDataIntegrationFlowsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_supplychain.types.list_data_integration_flows_response.ListDataIntegrationFlowsResponse"
        ]:
            import aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flows

            (
                output,
                http_response,
            ) = await aws_sdk_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flows.async_list_data_integration_flows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_supplychain.types.list_data_integration_flows_request.ListDataIntegrationFlowsRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
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
