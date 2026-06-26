from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_drs._auth._signers
import aws_sdk_drs._auth._sigv4
from aws_sdk_drs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_drs.types.account_id
    import aws_sdk_drs.types.associate_source_network_stack_request
    import aws_sdk_drs.types.associate_source_network_stack_response
    import aws_sdk_drs.types.aws_region
    import aws_sdk_drs.types.cfn_stack_name
    import aws_sdk_drs.types.create_source_network_request
    import aws_sdk_drs.types.create_source_network_response
    import aws_sdk_drs.types.delete_source_network_request
    import aws_sdk_drs.types.delete_source_network_response
    import aws_sdk_drs.types.describe_source_networks_request
    import aws_sdk_drs.types.describe_source_networks_request_filters
    import aws_sdk_drs.types.describe_source_networks_response
    import aws_sdk_drs.types.export_source_network_cfn_template_request
    import aws_sdk_drs.types.export_source_network_cfn_template_response
    import aws_sdk_drs.types.pagination_token
    import aws_sdk_drs.types.source_network
    import aws_sdk_drs.types.source_network_id
    import aws_sdk_drs.types.start_source_network_recovery_request
    import aws_sdk_drs.types.start_source_network_recovery_request_network_entries
    import aws_sdk_drs.types.start_source_network_recovery_response
    import aws_sdk_drs.types.start_source_network_replication_request
    import aws_sdk_drs.types.start_source_network_replication_response
    import aws_sdk_drs.types.stop_source_network_replication_request
    import aws_sdk_drs.types.stop_source_network_replication_response
    import aws_sdk_drs.types.strictly_positive_integer
    import aws_sdk_drs.types.tags_map
    import aws_sdk_drs.types.vpc_id
    from aws_sdk_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from aws_sdk_drs._services.drs import drsClient, drsClientConfig


class SourceNetworkResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def create(
        self,
        vpc_id: "aws_sdk_drs.types.vpc_id.VpcID",
        origin_account_id: "aws_sdk_drs.types.account_id.AccountID",
        origin_region: "aws_sdk_drs.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_drs.types.create_source_network_response.CreateSourceNetworkResponse":
        """<p>Create a new Source Network resource for a provided VPC ID.</p>

        Args:
            vpc_id: <p>Which VPC ID to protect.</p>
            origin_account_id: <p>Account containing the VPC to protect.</p>
            origin_region: <p>Region containing the VPC to protect.</p>
            tags: <p>A set of tags to be associated with the Source Network resource.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.create_source_network_request.CreateSourceNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.create_source_network_response.CreateSourceNetworkResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.create_source_network

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.create_source_network.create_source_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.create_source_network_request.CreateSourceNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_id"] = vpc_id
        input_["origin_account_id"] = origin_account_id
        input_["origin_region"] = origin_region
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.delete_source_network_response.DeleteSourceNetworkResponse":
        """<p>Delete Source Network resource.</p>

        Args:
            source_network_id: <p>ID of the Source Network to delete.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.delete_source_network_request.DeleteSourceNetworkRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.delete_source_network_response.DeleteSourceNetworkResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_source_network

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_source_network.delete_source_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.delete_source_network_request.DeleteSourceNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["source_network_id"] = source_network_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[drsClientConfig] = None,
        filters: Optional[
            "aws_sdk_drs.types.describe_source_networks_request_filters.DescribeSourceNetworksRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse":
        """<p>Lists all Source Networks or multiple Source Networks filtered by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Source Networks.</p>
            max_results: <p>Maximum number of Source Networks to retrieve.</p>
            next_token: <p>The token of the next Source Networks to retrieve.</p>

        Raises:
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.describe_source_networks_request.DescribeSourceNetworksRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_source_networks

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_source_networks.describe_source_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_source_networks_request.DescribeSourceNetworksRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_source_network_stack(
        self,
        source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID",
        cfn_stack_name: "aws_sdk_drs.types.cfn_stack_name.CfnStackName",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse":
        """<p>Associate a Source Network to an existing CloudFormation Stack and modify launch templates to use this network. Can be used for reverting to previously deployed CloudFormation stacks.</p>

        Args:
            source_network_id: <p>The Source Network ID to associate with CloudFormation template.</p>
            cfn_stack_name: <p>CloudFormation template to associate with a Source Network.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.associate_source_network_stack

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.associate_source_network_stack.associate_source_network_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest = {}  # type: ignore[typeddict-item]
        input_["source_network_id"] = source_network_id
        input_["cfn_stack_name"] = cfn_stack_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def export_source_network_cfn_template(
        self,
        source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.export_source_network_cfn_template_response.ExportSourceNetworkCfnTemplateResponse":
        """<p>Export the Source Network CloudFormation template to an S3 bucket.</p>

        Args:
            source_network_id: <p>The Source Network ID to export its CloudFormation template to an S3 bucket.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.export_source_network_cfn_template_request.ExportSourceNetworkCfnTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.export_source_network_cfn_template_response.ExportSourceNetworkCfnTemplateResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.export_source_network_cfn_template

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.export_source_network_cfn_template.export_source_network_cfn_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.export_source_network_cfn_template_request.ExportSourceNetworkCfnTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["source_network_id"] = source_network_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_source_network_replication(
        self,
        source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse":
        """<p>Starts replication for a Source Network. This action would make the Source Network protected.</p>

        Args:
            source_network_id: <p>ID of the Source Network to replicate.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.start_source_network_replication_request.StartSourceNetworkReplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.start_source_network_replication

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.start_source_network_replication.start_source_network_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.start_source_network_replication_request.StartSourceNetworkReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["source_network_id"] = source_network_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_source_network_replication(
        self,
        source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse":
        """<p>Stops replication for a Source Network. This action would make the Source Network unprotected.</p>

        Args:
            source_network_id: <p>ID of the Source Network to stop replication.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.stop_source_network_replication_request.StopSourceNetworkReplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.stop_source_network_replication

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.stop_source_network_replication.stop_source_network_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.stop_source_network_replication_request.StopSourceNetworkReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["source_network_id"] = source_network_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_source_network_recovery(
        self,
        source_networks: "aws_sdk_drs.types.start_source_network_recovery_request_network_entries.StartSourceNetworkRecoveryRequestNetworkEntries",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        deploy_as_new: Optional[bool] = None,
        tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse":
        """<p>Deploy VPC for the specified Source Network and modify launch templates to use this network. The VPC will be deployed using a dedicated CloudFormation stack.</p>

        Args:
            source_networks: <p>The Source Networks that we want to start a Recovery Job for.</p>
            deploy_as_new: <p>Don't update existing CloudFormation Stack, recover the network using a new stack.</p>
            tags: <p>The tags to be associated with the Source Network recovery Job.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.start_source_network_recovery

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.start_source_network_recovery.start_source_network_recovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest = {}  # type: ignore[typeddict-item]
        input_["source_networks"] = source_networks
        if deploy_as_new is not None:
            input_["deploy_as_new"] = deploy_as_new
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSourceNetworkResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def create(
        self,
        vpc_id: "aws_sdk_drs.types.vpc_id.VpcID",
        origin_account_id: "aws_sdk_drs.types.account_id.AccountID",
        origin_region: "aws_sdk_drs.types.aws_region.AwsRegion",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_drs.types.create_source_network_response.CreateSourceNetworkResponse":
        """<p>Create a new Source Network resource for a provided VPC ID.</p>

        Args:
            vpc_id: <p>Which VPC ID to protect.</p>
            origin_account_id: <p>Account containing the VPC to protect.</p>
            origin_region: <p>Region containing the VPC to protect.</p>
            tags: <p>A set of tags to be associated with the Source Network resource.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.create_source_network_request.CreateSourceNetworkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.create_source_network_response.CreateSourceNetworkResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.create_source_network

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.create_source_network.async_create_source_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.create_source_network_request.CreateSourceNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_id"] = vpc_id
        input_["origin_account_id"] = origin_account_id
        input_["origin_region"] = origin_region
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.delete_source_network_response.DeleteSourceNetworkResponse":
        """<p>Delete Source Network resource.</p>

        Args:
            source_network_id: <p>ID of the Source Network to delete.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.delete_source_network_request.DeleteSourceNetworkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.delete_source_network_response.DeleteSourceNetworkResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_source_network

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_source_network.async_delete_source_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.delete_source_network_request.DeleteSourceNetworkRequest = {}  # type: ignore[typeddict-item]
        input_["source_network_id"] = source_network_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "aws_sdk_drs.types.describe_source_networks_request_filters.DescribeSourceNetworksRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse":
        """<p>Lists all Source Networks or multiple Source Networks filtered by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Source Networks.</p>
            max_results: <p>Maximum number of Source Networks to retrieve.</p>
            next_token: <p>The token of the next Source Networks to retrieve.</p>

        Raises:
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.describe_source_networks_request.DescribeSourceNetworksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.describe_source_networks_response.DescribeSourceNetworksResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_source_networks

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_source_networks.async_describe_source_networks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_source_networks_request.DescribeSourceNetworksRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_source_network_stack(
        self,
        source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID",
        cfn_stack_name: "aws_sdk_drs.types.cfn_stack_name.CfnStackName",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse":
        """<p>Associate a Source Network to an existing CloudFormation Stack and modify launch templates to use this network. Can be used for reverting to previously deployed CloudFormation stacks.</p>

        Args:
            source_network_id: <p>The Source Network ID to associate with CloudFormation template.</p>
            cfn_stack_name: <p>CloudFormation template to associate with a Source Network.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.associate_source_network_stack_response.AssociateSourceNetworkStackResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.associate_source_network_stack

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.associate_source_network_stack.async_associate_source_network_stack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.associate_source_network_stack_request.AssociateSourceNetworkStackRequest = {}  # type: ignore[typeddict-item]
        input_["source_network_id"] = source_network_id
        input_["cfn_stack_name"] = cfn_stack_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def export_source_network_cfn_template(
        self,
        source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.export_source_network_cfn_template_response.ExportSourceNetworkCfnTemplateResponse":
        """<p>Export the Source Network CloudFormation template to an S3 bucket.</p>

        Args:
            source_network_id: <p>The Source Network ID to export its CloudFormation template to an S3 bucket.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.export_source_network_cfn_template_request.ExportSourceNetworkCfnTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.export_source_network_cfn_template_response.ExportSourceNetworkCfnTemplateResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.export_source_network_cfn_template

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.export_source_network_cfn_template.async_export_source_network_cfn_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.export_source_network_cfn_template_request.ExportSourceNetworkCfnTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["source_network_id"] = source_network_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_source_network_replication(
        self,
        source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse":
        """<p>Starts replication for a Source Network. This action would make the Source Network protected.</p>

        Args:
            source_network_id: <p>ID of the Source Network to replicate.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.start_source_network_replication_request.StartSourceNetworkReplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.start_source_network_replication_response.StartSourceNetworkReplicationResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.start_source_network_replication

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.start_source_network_replication.async_start_source_network_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.start_source_network_replication_request.StartSourceNetworkReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["source_network_id"] = source_network_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_source_network_replication(
        self,
        source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse":
        """<p>Stops replication for a Source Network. This action would make the Source Network unprotected.</p>

        Args:
            source_network_id: <p>ID of the Source Network to stop replication.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.stop_source_network_replication_request.StopSourceNetworkReplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.stop_source_network_replication_response.StopSourceNetworkReplicationResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.stop_source_network_replication

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.stop_source_network_replication.async_stop_source_network_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.stop_source_network_replication_request.StopSourceNetworkReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["source_network_id"] = source_network_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_source_network_recovery(
        self,
        source_networks: "aws_sdk_drs.types.start_source_network_recovery_request_network_entries.StartSourceNetworkRecoveryRequestNetworkEntries",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        deploy_as_new: Optional[bool] = None,
        tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse":
        """<p>Deploy VPC for the specified Source Network and modify launch templates to use this network. The VPC will be deployed using a dedicated CloudFormation stack.</p>

        Args:
            source_networks: <p>The Source Networks that we want to start a Recovery Job for.</p>
            deploy_as_new: <p>Don't update existing CloudFormation Stack, recover the network using a new stack.</p>
            tags: <p>The tags to be associated with the Source Network recovery Job.</p>

        Raises:
            aws_sdk_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_drs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            aws_sdk_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            aws_sdk_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            aws_sdk_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.start_source_network_recovery_response.StartSourceNetworkRecoveryResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.start_source_network_recovery

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.start_source_network_recovery.async_start_source_network_recovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.start_source_network_recovery_request.StartSourceNetworkRecoveryRequest = {}  # type: ignore[typeddict-item]
        input_["source_networks"] = source_networks
        if deploy_as_new is not None:
            input_["deploy_as_new"] = deploy_as_new
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
