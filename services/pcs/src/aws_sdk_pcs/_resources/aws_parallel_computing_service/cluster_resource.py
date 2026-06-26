from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from aws_sdk_pcs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_pcs.types.bootstrap_id
    import aws_sdk_pcs.types.cluster_identifier
    import aws_sdk_pcs.types.cluster_name
    import aws_sdk_pcs.types.cluster_slurm_configuration_request
    import aws_sdk_pcs.types.cluster_summary
    import aws_sdk_pcs.types.create_cluster_request
    import aws_sdk_pcs.types.create_cluster_response
    import aws_sdk_pcs.types.delete_cluster_request
    import aws_sdk_pcs.types.delete_cluster_response
    import aws_sdk_pcs.types.get_cluster_request
    import aws_sdk_pcs.types.get_cluster_response
    import aws_sdk_pcs.types.list_clusters_request
    import aws_sdk_pcs.types.list_clusters_response
    import aws_sdk_pcs.types.max_results
    import aws_sdk_pcs.types.networking_request
    import aws_sdk_pcs.types.register_compute_node_group_instance_request
    import aws_sdk_pcs.types.register_compute_node_group_instance_response
    import aws_sdk_pcs.types.request_tag_map
    import aws_sdk_pcs.types.sb_client_token
    import aws_sdk_pcs.types.scheduler_request
    import aws_sdk_pcs.types.size
    import aws_sdk_pcs.types.update_cluster_request
    import aws_sdk_pcs.types.update_cluster_response
    import aws_sdk_pcs.types.update_cluster_slurm_configuration_request
    from aws_sdk_pcs._services.async_pcs import AsyncPCSClient, AsyncPCSClientConfig
    from aws_sdk_pcs._services.pcs import PCSClient, PCSClientConfig


class ClusterResource:
    def __init__(self, service: PCSClient) -> None:
        self._service = service

    def create(
        self,
        cluster_name: "aws_sdk_pcs.types.cluster_name.ClusterName",
        scheduler: "aws_sdk_pcs.types.scheduler_request.SchedulerRequest",
        size: "aws_sdk_pcs.types.size.Size",
        networking: "aws_sdk_pcs.types.networking_request.NetworkingRequest",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        slurm_configuration: Optional[
            "aws_sdk_pcs.types.cluster_slurm_configuration_request.ClusterSlurmConfigurationRequest"
        ] = None,
        client_token: Optional[
            "aws_sdk_pcs.types.sb_client_token.SBClientToken"
        ] = None,
        tags: Optional["aws_sdk_pcs.types.request_tag_map.RequestTagMap"] = None,
    ) -> "aws_sdk_pcs.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a cluster in your account. PCS creates the cluster controller in a service-owned account. The cluster controller communicates with the cluster resources in your account. The subnets and security groups for the cluster must already exist before you use this API action.</p> <note> <p>It takes time for PCS to create the cluster. The cluster is in a <code>Creating</code> state until it is ready to use. There can only be 1 cluster in a <code>Creating</code> state per Amazon Web Services Region per Amazon Web Services account. <code>CreateCluster</code> fails with a <code>ServiceQuotaExceededException</code> if there is already a cluster in a <code>Creating</code> state.</p> </note>

        Args:
            cluster_name: <p>A name to identify the cluster. Example: <code>MyCluster</code> </p>
            scheduler: <p>The cluster management and job scheduling software associated with the cluster.</p>
            size: <p>A value that determines the maximum number of compute nodes in the cluster and the maximum number of jobs (active and queued).</p> <ul> <li> <p> <code>SMALL</code>: 32 compute nodes and 256 jobs</p> </li> <li> <p> <code>MEDIUM</code>: 512 compute nodes and 8192 jobs</p> </li> <li> <p> <code>LARGE</code>: 2048 compute nodes and 16,384 jobs</p> </li> </ul>
            networking: <p>The networking configuration used to set up the cluster's control plane.</p>
            slurm_configuration: <p>Additional options related to the Slurm scheduler.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>
            tags: <p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. To learn how to increase your service quota, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i> </p> <p> <u>Examples</u> </p> <ul> <li> <p>The max number of clusters or queues has been reached for the account.</p> </li> <li> <p>The max number of compute node groups has been reached for the associated cluster.</p> </li> <li> <p>The total of <code>maxInstances</code> across all compute node groups has been reached for associated cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            aws_sdk_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pcs.types.create_cluster_request.CreateClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_pcs.types.create_cluster_response.CreateClusterResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.create_cluster

            output, http_response = (
                aws_sdk_pcs._operations.aws_parallel_computing_service.create_cluster.create_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.create_cluster_request.CreateClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_name"] = cluster_name
        input_["scheduler"] = scheduler
        input_["size"] = size
        input_["networking"] = networking
        if slurm_configuration is not None:
            input_["slurm_configuration"] = slurm_configuration
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pcs.types.sb_client_token.SBClientToken"
        ] = None,
        slurm_configuration: Optional[
            "aws_sdk_pcs.types.update_cluster_slurm_configuration_request.UpdateClusterSlurmConfigurationRequest"
        ] = None,
    ) -> "aws_sdk_pcs.types.update_cluster_response.UpdateClusterResponse":
        """<p>Updates a cluster configuration. You can modify Slurm scheduler settings, accounting configuration, and security groups for an existing cluster. </p> <note> <p>You can only update clusters that are in <code>ACTIVE</code>, <code>UPDATE_FAILED</code>, or <code>SUSPENDED</code> state. All associated resources (queues and compute node groups) must be in <code>ACTIVE</code> state before you can update the cluster.</p> </note>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to update.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>
            slurm_configuration: <p>Additional options related to the Slurm scheduler.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            aws_sdk_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            aws_sdk_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pcs.types.update_cluster_request.UpdateClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_pcs.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.update_cluster

            output, http_response = (
                aws_sdk_pcs._operations.aws_parallel_computing_service.update_cluster.update_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.update_cluster_request.UpdateClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_identifier"] = cluster_identifier
        if client_token is not None:
            input_["client_token"] = client_token
        if slurm_configuration is not None:
            input_["slurm_configuration"] = slurm_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_cluster(
        self,
        cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pcs.types.sb_client_token.SBClientToken"
        ] = None,
    ) -> "aws_sdk_pcs.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes a cluster and all its linked resources. You must delete all queues and compute node groups associated with the cluster before you can delete the cluster.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            aws_sdk_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            aws_sdk_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pcs.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_pcs.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.delete_cluster

            output, http_response = (
                aws_sdk_pcs._operations.aws_parallel_computing_service.delete_cluster.delete_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.delete_cluster_request.DeleteClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_identifier"] = cluster_identifier
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cluster(
        self,
        cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "aws_sdk_pcs.types.get_cluster_response.GetClusterResponse":
        """<p>Returns detailed information about a running cluster in your account. This API action provides networking information, endpoint information for communication with the scheduler, and provisioning status.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            aws_sdk_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            aws_sdk_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pcs.types.get_cluster_request.GetClusterRequest]",
        ) -> OperationResponse[
            "aws_sdk_pcs.types.get_cluster_response.GetClusterResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.get_cluster

            output, http_response = (
                aws_sdk_pcs._operations.aws_parallel_computing_service.get_cluster.get_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.get_cluster_request.GetClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_identifier"] = cluster_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_compute_node_group_instance(
        self,
        cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier",
        bootstrap_id: "aws_sdk_pcs.types.bootstrap_id.BootstrapId",
        *,
        config_overrides: Optional[PCSClientConfig] = None,
    ) -> "aws_sdk_pcs.types.register_compute_node_group_instance_response.RegisterComputeNodeGroupInstanceResponse":
        """<important> <p>This API action isn't intended for you to use.</p> </important> <p>PCS uses this API action to register the compute nodes it launches in your account.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to register the compute node group instance in.</p>
            bootstrap_id: <p>The client-generated token to allow for retries.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pcs.types.register_compute_node_group_instance_request.RegisterComputeNodeGroupInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_pcs.types.register_compute_node_group_instance_response.RegisterComputeNodeGroupInstanceResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.register_compute_node_group_instance

            output, http_response = (
                aws_sdk_pcs._operations.aws_parallel_computing_service.register_compute_node_group_instance.register_compute_node_group_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.register_compute_node_group_instance_request.RegisterComputeNodeGroupInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_identifier"] = cluster_identifier
        input_["bootstrap_id"] = bootstrap_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_clusters(
        self,
        *,
        config_overrides: Optional[PCSClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional["aws_sdk_pcs.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_pcs.types.list_clusters_response.ListClustersResponse":
        """<p>Returns a list of running clusters in your account.</p>

        Args:
            next_token: <p>The value of <code>nextToken</code> is a unique pagination token for each page of results returned. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an <code>HTTP 400 InvalidToken</code> error.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 10 results, and the maximum allowed page size is 100 results. A value of 0 uses the default.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            aws_sdk_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            aws_sdk_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pcs.types.list_clusters_request.ListClustersRequest]",
        ) -> OperationResponse[
            "aws_sdk_pcs.types.list_clusters_response.ListClustersResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.list_clusters

            output, http_response = (
                aws_sdk_pcs._operations.aws_parallel_computing_service.list_clusters.list_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.list_clusters_request.ListClustersRequest = {}  # type: ignore[typeddict-item]
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


class AsyncClusterResource:
    def __init__(self, service: AsyncPCSClient) -> None:
        self._service = service

    async def create(
        self,
        cluster_name: "aws_sdk_pcs.types.cluster_name.ClusterName",
        scheduler: "aws_sdk_pcs.types.scheduler_request.SchedulerRequest",
        size: "aws_sdk_pcs.types.size.Size",
        networking: "aws_sdk_pcs.types.networking_request.NetworkingRequest",
        *,
        config_overrides: Optional[AsyncPCSClientConfig] = None,
        slurm_configuration: Optional[
            "aws_sdk_pcs.types.cluster_slurm_configuration_request.ClusterSlurmConfigurationRequest"
        ] = None,
        client_token: Optional[
            "aws_sdk_pcs.types.sb_client_token.SBClientToken"
        ] = None,
        tags: Optional["aws_sdk_pcs.types.request_tag_map.RequestTagMap"] = None,
    ) -> "aws_sdk_pcs.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a cluster in your account. PCS creates the cluster controller in a service-owned account. The cluster controller communicates with the cluster resources in your account. The subnets and security groups for the cluster must already exist before you use this API action.</p> <note> <p>It takes time for PCS to create the cluster. The cluster is in a <code>Creating</code> state until it is ready to use. There can only be 1 cluster in a <code>Creating</code> state per Amazon Web Services Region per Amazon Web Services account. <code>CreateCluster</code> fails with a <code>ServiceQuotaExceededException</code> if there is already a cluster in a <code>Creating</code> state.</p> </note>

        Args:
            cluster_name: <p>A name to identify the cluster. Example: <code>MyCluster</code> </p>
            scheduler: <p>The cluster management and job scheduling software associated with the cluster.</p>
            size: <p>A value that determines the maximum number of compute nodes in the cluster and the maximum number of jobs (active and queued).</p> <ul> <li> <p> <code>SMALL</code>: 32 compute nodes and 256 jobs</p> </li> <li> <p> <code>MEDIUM</code>: 512 compute nodes and 8192 jobs</p> </li> <li> <p> <code>LARGE</code>: 2048 compute nodes and 16,384 jobs</p> </li> </ul>
            networking: <p>The networking configuration used to set up the cluster's control plane.</p>
            slurm_configuration: <p>Additional options related to the Slurm scheduler.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>
            tags: <p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. To learn how to increase your service quota, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i> </p> <p> <u>Examples</u> </p> <ul> <li> <p>The max number of clusters or queues has been reached for the account.</p> </li> <li> <p>The max number of compute node groups has been reached for the associated cluster.</p> </li> <li> <p>The total of <code>maxInstances</code> across all compute node groups has been reached for associated cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            aws_sdk_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pcs.types.create_cluster_request.CreateClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pcs.types.create_cluster_response.CreateClusterResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.create_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_pcs._operations.aws_parallel_computing_service.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.create_cluster_request.CreateClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_name"] = cluster_name
        input_["scheduler"] = scheduler
        input_["size"] = size
        input_["networking"] = networking
        if slurm_configuration is not None:
            input_["slurm_configuration"] = slurm_configuration
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[AsyncPCSClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pcs.types.sb_client_token.SBClientToken"
        ] = None,
        slurm_configuration: Optional[
            "aws_sdk_pcs.types.update_cluster_slurm_configuration_request.UpdateClusterSlurmConfigurationRequest"
        ] = None,
    ) -> "aws_sdk_pcs.types.update_cluster_response.UpdateClusterResponse":
        """<p>Updates a cluster configuration. You can modify Slurm scheduler settings, accounting configuration, and security groups for an existing cluster. </p> <note> <p>You can only update clusters that are in <code>ACTIVE</code>, <code>UPDATE_FAILED</code>, or <code>SUSPENDED</code> state. All associated resources (queues and compute node groups) must be in <code>ACTIVE</code> state before you can update the cluster.</p> </note>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to update.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>
            slurm_configuration: <p>Additional options related to the Slurm scheduler.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            aws_sdk_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            aws_sdk_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pcs.types.update_cluster_request.UpdateClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pcs.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.update_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_pcs._operations.aws_parallel_computing_service.update_cluster.async_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.update_cluster_request.UpdateClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_identifier"] = cluster_identifier
        if client_token is not None:
            input_["client_token"] = client_token
        if slurm_configuration is not None:
            input_["slurm_configuration"] = slurm_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_cluster(
        self,
        cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[AsyncPCSClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pcs.types.sb_client_token.SBClientToken"
        ] = None,
    ) -> "aws_sdk_pcs.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes a cluster and all its linked resources. You must delete all queues and compute node groups associated with the cluster before you can delete the cluster.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            aws_sdk_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            aws_sdk_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pcs.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pcs.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.delete_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_pcs._operations.aws_parallel_computing_service.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.delete_cluster_request.DeleteClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_identifier"] = cluster_identifier
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_cluster(
        self,
        cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier",
        *,
        config_overrides: Optional[AsyncPCSClientConfig] = None,
    ) -> "aws_sdk_pcs.types.get_cluster_response.GetClusterResponse":
        """<p>Returns detailed information about a running cluster in your account. This API action provides networking information, endpoint information for communication with the scheduler, and provisioning status.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            aws_sdk_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            aws_sdk_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pcs.types.get_cluster_request.GetClusterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pcs.types.get_cluster_response.GetClusterResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.get_cluster

            (
                output,
                http_response,
            ) = await aws_sdk_pcs._operations.aws_parallel_computing_service.get_cluster.async_get_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.get_cluster_request.GetClusterRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_identifier"] = cluster_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def register_compute_node_group_instance(
        self,
        cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier",
        bootstrap_id: "aws_sdk_pcs.types.bootstrap_id.BootstrapId",
        *,
        config_overrides: Optional[AsyncPCSClientConfig] = None,
    ) -> "aws_sdk_pcs.types.register_compute_node_group_instance_response.RegisterComputeNodeGroupInstanceResponse":
        """<important> <p>This API action isn't intended for you to use.</p> </important> <p>PCS uses this API action to register the compute nodes it launches in your account.</p>

        Args:
            cluster_identifier: <p>The name or ID of the cluster to register the compute node group instance in.</p>
            bootstrap_id: <p>The client-generated token to allow for retries.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pcs.types.register_compute_node_group_instance_request.RegisterComputeNodeGroupInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pcs.types.register_compute_node_group_instance_response.RegisterComputeNodeGroupInstanceResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.register_compute_node_group_instance

            (
                output,
                http_response,
            ) = await aws_sdk_pcs._operations.aws_parallel_computing_service.register_compute_node_group_instance.async_register_compute_node_group_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.register_compute_node_group_instance_request.RegisterComputeNodeGroupInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["cluster_identifier"] = cluster_identifier
        input_["bootstrap_id"] = bootstrap_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_clusters(
        self,
        *,
        config_overrides: Optional[AsyncPCSClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional["aws_sdk_pcs.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_pcs.types.list_clusters_response.ListClustersResponse":
        """<p>Returns a list of running clusters in your account.</p>

        Args:
            next_token: <p>The value of <code>nextToken</code> is a unique pagination token for each page of results returned. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an <code>HTTP 400 InvalidToken</code> error.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 10 results, and the maximum allowed page size is 100 results. A value of 0 uses the default.</p>

        Raises:
            aws_sdk_pcs.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p> <p> <u>Examples</u> </p> <ul> <li> <p>The launch template instance profile doesn't pass <code>iam:PassRole</code> verification.</p> </li> <li> <p>There is a mismatch between the account ID and cluster ID.</p> </li> <li> <p>The cluster ID doesn't exist.</p> </li> <li> <p>The EC2 instance isn't present.</p> </li> </ul>
            aws_sdk_pcs.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.</p> <p> <u>Examples</u> </p> <ul> <li> <p>A cluster with the same name already exists.</p> </li> <li> <p>A cluster isn't in <code>ACTIVE</code> status.</p> </li> <li> <p>A cluster to delete is in an unstable state. For example, because it still has <code>ACTIVE</code> node groups or queues.</p> </li> <li> <p>A queue already exists in a cluster.</p> </li> </ul>
            aws_sdk_pcs.errors.internal_server_exception.InternalServerException: <p>PCS can't process your request right now. Try again later.</p>
            aws_sdk_pcs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.</p> <p> <u>Examples</u> </p>
            aws_sdk_pcs.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota. Check the resource's request rate quota and try again.</p>
            aws_sdk_pcs.errors.validation_exception.ValidationException: <p>The request isn't valid.</p> <p> <u>Examples</u> </p> <ul> <li> <p>Your request contains malformed JSON or unsupported characters.</p> </li> <li> <p>The scheduler version isn't supported.</p> </li> <li> <p>There are networking related errors, such as network validation failure.</p> </li> <li> <p>AMI type is <code>CUSTOM</code> and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.</p> </li> </ul>
            aws_sdk_pcs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pcs.types.list_clusters_request.ListClustersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pcs.types.list_clusters_response.ListClustersResponse"
        ]:
            import aws_sdk_pcs._operations.aws_parallel_computing_service.list_clusters

            (
                output,
                http_response,
            ) = await aws_sdk_pcs._operations.aws_parallel_computing_service.list_clusters.async_list_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pcs.types.list_clusters_request.ListClustersRequest = {}  # type: ignore[typeddict-item]
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
